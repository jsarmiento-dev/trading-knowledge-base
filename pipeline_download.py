#!/usr/bin/env python3
"""
Pipeline CONSOLIDADO completo.
FASE 1 (paralelo): Descubrir videos nuevos en todos los streamers.
FASE 2 (secuencial): Descargar transcripciones de videos nuevos.
FASE 3: Git commit + push.
"""
import os, sys, json, time, subprocess, re
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# ─── Config ─────────────────────────────────────────────────────
YT_DLP = "/home/ubuntu/.yt-dlp-venv/bin/yt-dlp"
BASE_DIR = Path.home() / "proyects/trading"
STREAMERS_DIR = BASE_DIR / "streamers"
PROCESSED_FILE = BASE_DIR / "processed_videos.txt"
RESULTS_FILE = BASE_DIR / "pipeline_results.json"
COOKIES_FILE = Path.home() / "proyects/trading/cookies/youtube.txt"
MAX_PER_STREAMER = 50     # videos a revisar por canal
MAX_DOWNLOAD = 3           # transcripciones a descargar por streamer
CURL_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"

# Streamers prioritarios — incluso con subtítulos, descargar audio para Whisper
PRIORITY_STREAMERS = {"PuntoDeEntrada"}
AUDIOS_DIR = BASE_DIR / "audios_pendientes"

STREAMERS = [
    {'name': 'ArgenTrader', 'channel': 'https://www.youtube.com/@ArgenTraderr', 'dir': 'ArgenTrader', 'extra': []},
    {'name': 'ZCoinTV',     'channel': 'https://www.youtube.com/@ZCoinTV',     'dir': 'ZCoinTV',     'extra': []},
    {'name': 'ScottFDX',    'channel': 'https://www.youtube.com/@ScottFDX',     'dir': 'ScottFDX',    'extra': []},
    {'name': 'NovaTrader',  'channel': 'https://www.youtube.com/@nova-trader',  'dir': 'NovaTrader',
     'extra': ['https://www.youtube.com/@nova-trader/streams', 'https://www.youtube.com/@nova-trader/shorts']},
    {'name': 'MambaFx',     'channel': 'https://www.youtube.com/@mambafx',      'dir': 'MambaFx',
     'extra': ['https://www.youtube.com/@mambafx/streams']},
    # ⭐ FAVORITO: Nuevo canal de trading — pendiente de su crecimiento
    {'name': 'PuntoDeEntrada', 'channel': 'https://www.youtube.com/@PuntoDeEntradaYT', 'dir': 'PuntoDeEntrada', 'extra': []},
]

# ─── Logging ────────────────────────────────────────────────────

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)

# ─── Procesados ─────────────────────────────────────────────────

def load_processed():
    s = set()
    if PROCESSED_FILE.exists():
        for line in open(PROCESSED_FILE):
            if '|' in line:
                s.add(line.split('|')[0].strip())
    return s

def save_processed(vid, title, streamer_name=""):
    with open(PROCESSED_FILE, 'a') as f:
        f.write(f"{vid}|{datetime.now().strftime('%Y-%m-%d')}|{title}|{streamer_name}\n")

# ─── Listado de canales ─────────────────────────────────────────

def list_channel(url):
    """Lista videos de un canal vía yt-dlp (fallback a curl)."""
    cmd = [YT_DLP, '--flat-playlist', '--playlist-end', str(MAX_PER_STREAMER),
           '--print', '%(id)s|%(title)s', url]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if r.returncode != 0:
            log(f"  ⚠ yt-dlp falló {url}: {r.stderr[:80]}")
            curl_cmd = ['curl', '-s', '--max-time', '10',
                       '-H', f'User-Agent: {CURL_UA}', url]
            cr = subprocess.run(curl_cmd, capture_output=True, text=True, timeout=15)
            ids = re.findall(r'"videoId":"([^"]+)"', cr.stdout)
            return [{'id': vid, 'title': vid, 'url': f'https://www.youtube.com/watch?v={vid}'} for vid in dict.fromkeys(ids)]
        videos = []
        for line in r.stdout.strip().split('\n'):
            if '|' in line:
                parts = line.split('|', 1)
                vid = parts[0].strip()
                title = parts[1].strip() if len(parts) > 1 else vid
                videos.append({'id': vid, 'title': title, 'url': f'https://www.youtube.com/watch?v={vid}'})
        return videos
    except Exception as e:
        log(f"  ✗ Error {url}: {e}")
        return []

# ─── Transcripciones ────────────────────────────────────────────

def download_transcript(video_url, video_id, output_dir):
    """Descarga transcripción de un video. Retorna path o None."""
    output_dir.mkdir(parents=True, exist_ok=True)
    base_cmd = [YT_DLP]
    if COOKIES_FILE.exists():
        base_cmd += ['--cookies', str(COOKIES_FILE)]

    for lang in ['es', 'en', 'es-MX']:
        cmd = base_cmd + ['--write-auto-subs', '--sub-lang', lang,
                          '--skip-download', '--output', str(output_dir / video_id), video_url]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
        if r.returncode == 0:
            for ext in ['.vtt', '.srt']:
                files = list(output_dir.glob(f"{video_id}*{ext}"))
                if files:
                    log(f"  → Transcripción {lang}: {files[0].name}")
                    return files[0]
    return None

def vtt_to_text(vtt_file):
    """Convierte VTT/SRT a texto plano."""
    try:
        content = vtt_file.read_text(encoding='utf-8', errors='replace')
        lines = content.split('\n')
        text = []
        for line in lines:
            line = line.strip()
            if not line or 'WEBVTT' in line or '-->' in line or line.isdigit():
                continue
            if line.startswith('Kind:') or line.startswith('Language:') or line.startswith('<'):
                continue
            text.append(line)
        unique = []
        for l in text:
            if not unique or l != unique[-1]:
                unique.append(l)
        return ' '.join(unique)
    except Exception as e:
        log(f"  → Error VTT: {e}")
        return ""

# ─── Audio para Whisper ─────────────────────────────────────────
def download_audio(video_id, streamer_name, titulo=""):
    """Descarga audio para transcripción con Whisper (streamers prioritarios)."""
    AUDIOS_DIR.mkdir(parents=True, exist_ok=True)
    output_template = str(AUDIOS_DIR / f"{video_id}.%(ext)s")

    cmd = [YT_DLP, "-f", "bestaudio[ext=m4a]/bestaudio",
           "--output", output_template, "--quiet",
           "--no-embed-thumbnail", "--no-playlist",
           "--js-runtimes", "node", "--impersonate", "chrome",
           f"https://www.youtube.com/watch?v={video_id}"]
    if COOKIES_FILE.exists():
        cmd = [YT_DLP, "--cookies", str(COOKIES_FILE)] + cmd[1:]

    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        if r.returncode == 0:
            for f in AUDIOS_DIR.glob(f"{video_id}.*"):
                if f.suffix in [".m4a", ".webm", ".opus", ".mp3"]:
                    log(f"  🎧 Audio descargado p/Whisper: {f.name}")
                    meta_file = AUDIOS_DIR / f"{video_id}.meta"
                    meta_file.write_text(f"{streamer_name}|{titulo}", encoding="utf-8")
                    return True
        log(f"  ⚠ Error descargando audio: {r.stderr[:80].strip()}")
    except Exception as e:
        log(f"  ⚠ Excepción audio: {e}")
    return False

# ─── Procesar streamer ──────────────────────────────────────────

def process_streamer(streamer):
    """Procesa un streamer: descubre videos, descarga transcripciones."""
    log(f"\n{'='*60}")
    log(f"PROCESANDO: {streamer['name']}")
    log(f"{'='*60}")

    processed_set = load_processed()

    # Listar canales
    all_videos = list_channel(streamer['channel'])
    for extra in streamer.get('extra', []):
        all_videos.extend(list_channel(extra))

    if not all_videos:
        return {'streamer': streamer['name'], 'new_videos': 0, 'processed': [], 'error': 'Sin videos'}

    new_videos = [v for v in all_videos if v['id'] not in processed_set]
    log(f"Nuevos: {len(new_videos)} de {len(all_videos)} totales")

    if not new_videos:
        return {'streamer': streamer['name'], 'new_videos': 0, 'processed': [], 'error': None}

    # Crear directorio del streamer
    base_dir = STREAMERS_DIR / streamer['dir']
    base_dir.mkdir(parents=True, exist_ok=True)
    transcripciones_dir = base_dir / "transcripciones"
    transcripciones_dir.mkdir(exist_ok=True)

    # Descargar transcripciones
    processed = []
    for video in new_videos[:MAX_DOWNLOAD]:
        log(f"\n  → {video['title'][:60]} ({video['id']})")

        vtt = download_transcript(video['url'], video['id'], transcripciones_dir)

        transcript_len = 0
        if vtt and vtt.exists():
            text = vtt_to_text(vtt)
            if text:
                txt_file = transcripciones_dir / f"{video['id']}_transcript.txt"
                txt_file.write_text(text, encoding='utf-8')
                transcript_len = len(text)
                log(f"  → Guardado: {txt_file.name} ({transcript_len} chars)")
                try:
                    vtt.unlink(missing_ok=True)
                except:
                    pass

        # Streamers prioritarios: también descargar audio para Whisper
        streamer_name = streamer['name']
        if streamer_name in PRIORITY_STREAMERS:
            download_audio(video['id'], streamer_name, video['title'])

        processed.append({
            'video_id': video['id'],
            'title': video['title'],
            'url': video['url'],
            'transcript_length': transcript_len
        })
        save_processed(video['id'], video['title'], streamer_name)
        time.sleep(3)

    return {'streamer': streamer['name'], 'new_videos': len(processed), 'processed': processed, 'error': None}

# ─── Git auto-commit ────────────────────────────────────────────

def git_auto_commit(total_new):
    """Git add, commit, push si hay cambios."""
    try:
        r = subprocess.run(['git', 'add', '-A'], capture_output=True, text=True, timeout=15, cwd=BASE_DIR)
        if r.returncode != 0:
            log(f"git add falló: {r.stderr[:100]}")
            return
        r = subprocess.run(['git', 'diff', '--cached', '--quiet'], capture_output=True, text=True, timeout=10, cwd=BASE_DIR)
        if r.returncode == 0:
            log("Sin cambios nuevos")
            return
        today = datetime.now().strftime("%Y-%m-%d")
        r = subprocess.run(
            ['git', 'commit', '-m', f'[auto] Pipeline {today} — {total_new} videos nuevos'],
            capture_output=True, text=True, timeout=15, cwd=BASE_DIR
        )
        if r.returncode != 0:
            log(f"commit falló: {r.stderr[:100]}")
            return
        log(f"Commit: {r.stdout[:80].strip()}")
        r = subprocess.run(['git', 'push'], capture_output=True, text=True, timeout=30, cwd=BASE_DIR)
        log("Push OK" if r.returncode == 0 else f"push falló: {r.stderr[:100]}")
    except Exception as e:
        log(f"Git error: {e}")

# ─── Main ───────────────────────────────────────────────────────

def main():
    log("="*60)
    log("PIPELINE CONSOLIDADO COMPLETO")
    log(f"yt-dlp: {YT_DLP}")
    log(f"Streamers: {len(STREAMERS)}")
    log(f"MAX_DOWNLOAD: {MAX_DOWNLOAD}")
    log("="*60)

    results = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        fut_map = {pool.submit(process_streamer, s): s['name'] for s in STREAMERS}
        for fut in as_completed(fut_map):
            name = fut_map[fut]
            try:
                results.append(fut.result())
            except Exception as e:
                log(f"ERROR {name}: {e}")
                results.append({'streamer': name, 'new_videos': 0, 'processed': [], 'error': str(e)})

    total_new = sum(r.get('new_videos', 0) for r in results)
    log(f"\n{'='*60}")
    log(f"TOTAL: {total_new} videos nuevos")
    for r in results:
        status = '✅' if r.get('new_videos', 0) > 0 else ('⚠️' if r.get('error') else '○')
        log(f"  {status} {r['streamer']}: {r.get('new_videos', 0)} nuevos")

    with open(RESULTS_FILE, 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    log(f"Resultados: {RESULTS_FILE}")

    git_auto_commit(total_new)
    return 0 if total_new > 0 else 1

if __name__ == "__main__":
    sys.exit(main())
