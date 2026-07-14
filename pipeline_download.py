#!/usr/bin/env python3
"""
Pipeline de DESCARGA v2 — Rápido.
FASE 1 (rápida): Listar videos nuevos de todos los streamers (paralelo).
FASE 2 (lenta): Descargar transcripciones solo si hay videos nuevos.
"""
import os, sys, json, time, subprocess, re
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

YT_DLP = "/home/ubuntu/.yt-dlp-venv/bin/yt-dlp"
BASE_DIR = Path.home() / "proyects/trading"
PROCESSED_FILE = BASE_DIR / "processed_videos.txt"
RESULTS_FILE = BASE_DIR / "pipeline_results.json"
MAX_PER_STREAMER = 50
MAX_DOWNLOAD = 3

STREAMERS = [
    {'name': 'ArgenTrader', 'channel': 'https://www.youtube.com/@ArgenTraderr', 'dir': 'ArgenTrader', 'extra': []},
    {'name': 'ZCoinTV',     'channel': 'https://www.youtube.com/@ZCoinTV',     'dir': 'ZCoinTV',     'extra': []},
    {'name': 'ScottFDX',    'channel': 'https://www.youtube.com/@ScottFDX',     'dir': 'ScottFDX',    'extra': []},
    {'name': 'NovaTrader',  'channel': 'https://www.youtube.com/@nova-trader',  'dir': 'NovaTrader',
     'extra': ['https://www.youtube.com/@nova-trader/streams', 'https://www.youtube.com/@nova-trader/shorts']},
    {'name': 'MambaFx',     'channel': 'https://www.youtube.com/@mambafx',     'dir': 'MambaFx',
     'extra': ['https://www.youtube.com/@mambafx/streams']},
]

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)

def load_processed():
    s = set()
    if PROCESSED_FILE.exists():
        for line in open(PROCESSED_FILE):
            if '|' in line:
                s.add(line.split('|')[0].strip())
    return s

def save_processed(vid, title):
    with open(PROCESSED_FILE, 'a') as f:
        f.write(f"{vid}|{datetime.now().strftime('%Y-%m-%d')}|{title}\n")

def list_channel(url):
    """Lista videos de un canal (rápido, solo IDs)."""
    cmd = [YT_DLP, '--flat-playlist', '--playlist-end', str(MAX_PER_STREAMER),
           '--print', '%(id)s|%(title)s', url]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if r.returncode != 0:
            log(f"  ⚠ yt-dlp falló {url}: {r.stderr[:80]}")
            # Fallback: curl
            curl_cmd = ['curl', '-s', '--max-time', '10',
                       '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                       url]
            cr = subprocess.run(curl_cmd, capture_output=True, text=True, timeout=15)
            ids = re.findall(r'"videoId":"([^"]+)"', cr.stdout)
            return [{'id': vid, 'title': vid} for vid in dict.fromkeys(ids)]
        
        videos = []
        for line in r.stdout.strip().split('\n'):
            if '|' in line:
                parts = line.split('|', 1)
                videos.append({'id': parts[0].strip(), 'title': parts[1].strip() if len(parts) > 1 else parts[0]})
        return videos
    except Exception as e:
        log(f"  ✗ Error {url}: {e}")
        return []

def git_auto_commit(total_new):
    """Hace git add, commit y push si hay cambios en el repo.
    total_new: número de videos nuevos encontrados en esta ejecución.
    """
    repo = BASE_DIR
    try:
        # git add
        r = subprocess.run(['git', 'add', '-A'], capture_output=True, text=True, timeout=15, cwd=repo)
        if r.returncode != 0:
            log(f"git add falló: {r.stderr[:100]}")
            return
        
        # Verificar si hay algo que commitear
        r = subprocess.run(['git', 'diff', '--cached', '--quiet'], capture_output=True, text=True, timeout=10, cwd=repo)
        if r.returncode == 0:
            log("Sin cambios nuevos para commitear")
            return
        
        today = datetime.now().strftime("%Y-%m-%d")
        r = subprocess.run(
            ['git', 'commit', '-m', f'[auto] Pipeline {today} — {total_new} videos nuevos detectados'],
            capture_output=True, text=True, timeout=15, cwd=repo
        )
        if r.returncode != 0:
            log(f"git commit falló: {r.stderr[:100]}")
            return
        log(f"Commit creado: {r.stdout[:80]}")
        
        # Push
        r = subprocess.run(['git', 'push'], capture_output=True, text=True, timeout=30, cwd=repo)
        if r.returncode != 0:
            log(f"git push falló: {r.stderr[:100]}")
            return
        log("Push exitoso")
    except Exception as e:
        log(f"Error en git_auto_commit: {e}")


def main():
    log("=== PIPELINE v2 ===")
    
    # FASE 1: Listar todos los streamers EN PARALELO
    log("FASE 1: Escaneando canales...")
    processed = load_processed()
    
    all_urls = []
    for s in STREAMERS:
        all_urls.append((s['name'], s['channel']))
        for ex in s.get('extra', []):
            all_urls.append((s['name'], ex))
    
    results = {s['name']: {'streamer': s['name'], 'new_videos': 0, 'processed': []} for s in STREAMERS}
    
    with ThreadPoolExecutor(max_workers=4) as pool:
        fut_map = {pool.submit(list_channel, url): (name, url) for name, url in all_urls}
        for fut in as_completed(fut_map):
            name, url = fut_map[fut]
            videos = fut.result()
            new = [v for v in videos if v['id'] not in processed]
            log(f"  {name}: {len(new)} nuevos de {len(videos)} en {url.split('/')[-1]}")
            if new:
                results[name]['new_videos'] += len(new)
                results[name]['processed'].extend(new[:MAX_DOWNLOAD])
    
    # FASE 2: Marcar como procesados
    total_new = sum(r['new_videos'] for r in results.values())
    log(f"\nTotal videos nuevos: {total_new}")
    
    for r in results.values():
        for p in r['processed'][:MAX_DOWNLOAD]:
            save_processed(p['id'], p['title'])
    
    # Guardar resultados
    with open(RESULTS_FILE, 'w') as f:
        json.dump(list(results.values()), f, indent=2, ensure_ascii=False)
    
    log(f"Resultados guardados en {RESULTS_FILE}")
    
    # FASE 3: Commit y push automático si hay cambios
    git_auto_commit(total_new)
    
    return 0 if total_new > 0 else 1

if __name__ == "__main__":
    sys.exit(main())
