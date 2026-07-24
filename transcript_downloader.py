#!/usr/bin/env python3
"""
Pipeline LOCAL de transcripciones — Windows.
SOLO descarga transcripciones de videos nuevos.
Usa processed_videos.txt (formato: id|fecha|titulo|streamer)
Ejecutar via Windows Task Scheduler diariamente.
"""
import random, subprocess, time
from datetime import datetime
from pathlib import Path

YT_DLP = r"C:\Users\USER\AppData\Local\Programs\Python\Python313\Scripts\yt-dlp.exe"
BASE = Path("C:/trading-knowledge-base")
COOKIES = BASE / "cookies/youtube.txt"
PROCESSED = BASE / "processed_videos.txt"
STREAMERS = ["ZCoinTV", "ScottFDX", "MambaFx", "PuntoDeEntrada"]  # ArgenTrader + NovaTrader → PuntoDeEntrada
AUDIOS_DIR = BASE / "audios_pendientes"
PRIORITY_STREAMERS = {"PuntoDeEntrada"}

def log(msg):
    print(f"[{datetime.now():%H:%M:%S}] {msg}")

def git(*args):
    r = subprocess.run(["git"] + list(args), capture_output=True, text=True,
                       timeout=30, cwd=BASE)
    if r.returncode != 0:
        log(f"⚠ git {' '.join(args)}: {r.stderr[:100].strip()}")
    return r

def _download_audio(video_id, streamer, titulo=""):
    """Descarga el audio de un video que no tiene subtítulos."""
    AUDIOS_DIR.mkdir(parents=True, exist_ok=True)
    output_template = str(AUDIOS_DIR / f"{video_id}.%(ext)s")

    cmd = [
        YT_DLP,
        "-f", "bestaudio[ext=m4a]/bestaudio",
        "--output", output_template,
        "--quiet",
        "--no-embed-thumbnail",
        "--no-playlist",
        "--js-runtimes", "node",
        "--impersonate", "chrome",
        f"https://www.youtube.com/watch?v={video_id}"
    ]
    if COOKIES.exists():
        cmd = [YT_DLP, "--cookies", str(COOKIES)] + cmd[1:]

    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        if r.returncode == 0:
            for f in AUDIOS_DIR.glob(f"{video_id}.*"):
                if f.suffix in [".m4a", ".webm", ".opus", ".mp3"]:
                    log(f"   ✅ Audio descargado: {f.name}")
                    meta_file = AUDIOS_DIR / f"{video_id}.meta"
                    meta_file.write_text(f"{streamer}|{titulo}", encoding="utf-8")
                    return
            log(f"   ⚠ Audio descargado pero no se encontró el archivo")
        elif "HTTP Error 429" in r.stderr:
            log(f"   ⚠ Rate limited (429) en audio, esperando 30s...")
            time.sleep(30)
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
            if r.returncode == 0:
                for f in AUDIOS_DIR.glob(f"{video_id}.*"):
                    if f.suffix in [".m4a", ".webm", ".opus", ".mp3"]:
                        log(f"   ✅ Audio descargado: {f.name}")
                        meta_file = AUDIOS_DIR / f"{video_id}.meta"
                        meta_file.write_text(f"{streamer}|{titulo}", encoding="utf-8")
                        return
            log(f"   ❌ Error audio (reintento): {r.stderr[:80].strip()}")
        else:
            log(f"   ❌ Error descargando audio: {r.stderr[:80].strip()}")
    except subprocess.TimeoutExpired:
        log(f"   ❌ Timeout descargando audio ({video_id})")
    except Exception as e:
        log(f"   ❌ Excepción audio: {e}")

def main():
    log("=" * 45)
    log("INICIANDO PIPELINE DE TRANSCRIPCIONES")
    log("=" * 45)

    # 1. Traer cambios del VPS
    log("\n[1/4] git pull...")
    git("pull")

    if not PROCESSED.exists():
        log("❌ No existe processed_videos.txt")
        return

    # 2. Identificar videos sin transcripción
    log("\n[2/4] Buscando videos sin transcripción...")
    pendientes = []
    with open(PROCESSED, encoding="utf-8", errors="replace") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) < 4:
                continue
            vid = parts[0].strip()
            fecha = parts[1].strip()
            streamer = parts[-1].strip()
            titulo = "|".join(parts[2:-1]).strip()

            if streamer not in STREAMERS:
                continue

            carpeta = BASE / "streamers" / streamer / "transcripciones"
            tiene = bool(list(carpeta.glob(f"{vid}_transcript.md")))

            if not tiene:
                pendientes.append({"vid": vid, "titulo": titulo, "fecha": fecha, "streamer": streamer})

    log(f"   → {len(pendientes)} video(s) pendiente(s)")
    if not pendientes:
        log("✓ Todo al día. Saliendo.")
        return

    # 3. Descargar transcripciones
    log("\n[3/4] Descargando transcripciones...")
    descargados = 0
    for i, p in enumerate(pendientes, 1):
        url = f"https://www.youtube.com/watch?v={p['vid']}"
        destino = BASE / "streamers" / p["streamer"] / "transcripciones"
        destino.mkdir(parents=True, exist_ok=True)
        output = str(destino / p["vid"])

        log(f"   [{i}/{len(pendientes)}] {p['streamer']}: {p['titulo'][:40]}...")

        cmd = [
            YT_DLP, "--write-auto-subs",
            "--sub-lang", "en.*,es.*",
            "--sub-format", "vtt",
            "--js-runtimes", "node",
            "--impersonate", "chrome",
            "--skip-download",
            "--output", output,
            "--quiet",
            url
        ]
        if COOKIES.exists():
            cmd = [YT_DLP, "--cookies", str(COOKIES)] + cmd[1:]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)

        if "HTTP Error 429" in result.stderr:
            log(f"   ⚠ Rate limited (429), esperando 30s antes de reintentar...")
            time.sleep(30)
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)

        if result.returncode == 0:
            encontrado = False
            for ext in [".vtt", ".srt", ".json"]:
                files = list(destino.glob(f"{p['vid']}*{ext}"))
                if files:
                    sub_file = files[0]
                    content = sub_file.read_text(encoding="utf-8", errors="replace")
                    lines = [
                        l.strip() for l in content.split("\n")
                        if l.strip()
                        and "-->" not in l
                        and "WEBVTT" not in l
                        and not l.strip().isdigit()
                        and not l.startswith("Kind:")
                        and not l.startswith("Language:")
                    ]
                    clean = []
                    for l in lines:
                        if not clean or l != clean[-1]:
                            clean.append(l)

                    texto = " ".join(clean)
                    txt_file = destino / f"{p['vid']}_transcript.md"
                    header = f"# {p['fecha']} | {p['titulo']} | {p['streamer']}\n"
                    txt_file.write_text(header + texto, encoding="utf-8")
                    sub_file.unlink(missing_ok=True)
                    log(f"   ✅ {len(texto)} chars")
                    descargados += 1
                    encontrado = True
                    break
            # Streamers prioritarios: también descargar audio para Whisper
            if encontrado and p['streamer'] in PRIORITY_STREAMERS:
                log(f"   ⚡ Streamer prioritario — también descargando audio para Whisper...")
                _download_audio(p['vid'], p['streamer'], p['titulo'])
            if not encontrado:
                log(f"   ⚠ Sin subtítulos — descargando audio para Whisper...")
                _download_audio(p['vid'], p['streamer'], p['titulo'])
        else:
            log(f"   ⚠ yt-dlp falló ({result.stderr[:60].strip()}) — descargando audio para Whisper...")
            _download_audio(p['vid'], p['streamer'], p['titulo'])

        time.sleep(random.uniform(10, 18))

    # Check if there are audios to commit even if no transcripts downloaded
    nuevos_audios = len(list(AUDIOS_DIR.glob("*.m4a"))) + len(list(AUDIOS_DIR.glob("*.webm"))) + len(list(AUDIOS_DIR.glob("*.opus")))

    if descargados == 0 and nuevos_audios == 0:
        log("\n⚠ No se descargó nada nuevo")
        return

    # 4. Commit y push
    if nuevos_audios:
        log(f"\n[4/4] Subiendo {descargados} transcripción(es) y {nuevos_audios} audio(s)...")
    else:
        log(f"\n[4/4] Subiendo {descargados} transcripción(es)...")
    git("add", "-A")
    r = git("diff", "--cached", "--quiet")
    if r.returncode != 0:
        fecha = datetime.now().strftime("%Y-%m-%d")
        msg = f"[transcripciones] {fecha} - {descargados} transcripciones"
        if nuevos_audios:
            msg += f", {nuevos_audios} audios p/Whisper"
        git("commit", "-m", msg)
        git("push")
        log(f"✅ Push exitoso — {descargados} transcripciones, {nuevos_audios} audios")
    else:
        log("📭 Sin cambios para commit")

    log("\n" + "=" * 45)
    log("PIPELINE COMPLETADO")
    log("=" * 45)

if __name__ == "__main__":
    main()
