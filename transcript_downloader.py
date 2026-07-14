#!/usr/bin/env python3
"""
Pipeline LOCAL de transcripciones — Windows.
SOLO descarga transcripciones de videos nuevos.
Usa processed_videos.txt (formato: id|fecha|titulo|streamer)
Ejecutar via Windows Task Scheduler diariamente.
"""
import subprocess, time
from datetime import datetime
from pathlib import Path

YT_DLP = r"C:\Users\USER\AppData\Local\Programs\Python\Python313\Scripts\yt-dlp.exe"
BASE = Path("C:/trading-knowledge-base")
COOKIES = BASE / "cookies/youtube.txt"
PROCESSED = BASE / "processed_videos.txt"
STREAMERS = ["ArgenTrader", "ZCoinTV", "ScottFDX", "NovaTrader", "MambaFx"]

def log(msg):
    print(f"[{datetime.now():%H:%M:%S}] {msg}")

def git(*args):
    r = subprocess.run(["git"] + list(args), capture_output=True, text=True,
                       timeout=30, cwd=BASE)
    if r.returncode != 0:
        log(f"⚠ git {' '.join(args)}: {r.stderr[:100].strip()}")
    return r

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
            titulo = parts[1].strip()
            streamer = parts[3].strip()

            if streamer not in STREAMERS:
                continue

            carpeta = BASE / "streamers" / streamer / "transcripciones"
            tiene = bool(list(carpeta.glob(f"{vid}_transcript.txt")))

            if not tiene:
                pendientes.append({"vid": vid, "titulo": titulo, "streamer": streamer})

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
            "--skip-download",
            "--output", output,
            "--quiet",
            url
        ]
        if COOKIES.exists():
            cmd = [YT_DLP, "--cookies", str(COOKIES)] + cmd[1:]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)

        if result.returncode == 0:
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
                    txt_file = destino / f"{p['vid']}_transcript.txt"
                    txt_file.write_text(texto, encoding="utf-8")
                    sub_file.unlink(missing_ok=True)
                    log(f"   ✅ {len(texto)} chars")
                    descargados += 1
                    break
            else:
                log(f"   ⚠ Sin archivo de subtítulos")
        else:
            log(f"   ❌ Error: {result.stderr[:80].strip()}")

        time.sleep(3)

    if descargados == 0:
        log("\n⚠ No se descargó nada nuevo")
        return

    # 4. Commit y push
    log(f"\n[4/4] Subiendo {descargados} transcripción(es)...")
    git("add", "-A")
    r = git("diff", "--cached", "--quiet")
    if r.returncode != 0:
        fecha = datetime.now().strftime("%Y-%m-%d")
        git("commit", "-m", f"[transcripciones] {fecha} - {descargados} videos")
        git("push")
        log(f"✅ Push exitoso — {descargados} transcripciones nuevas")
    else:
        log("📭 Sin cambios para commit")

    log("\n" + "=" * 45)
    log("PIPELINE COMPLETADO")
    log("=" * 45)

if __name__ == "__main__":
    main()
