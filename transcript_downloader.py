#!/usr/bin/env python3
"""
Pipeline LOCAL de transcripciones — Windows.
SOLO descarga transcripciones. El VPS hace el resto.
Ejecutar via Windows Task Scheduler diariamente.
"""
import subprocess, time, sys
from datetime import datetime
from pathlib import Path

BASE = Path("C:/trading-knowledge-base")
COOKIES = BASE / "cookies/youtube.txt"
PROCESSED = BASE / "processed_videos.txt"
STREAMERS = ["ArgenTrader", "ZCoinTV", "ScottFDX", "NovaTrader", "MambaFx"]

def log(msg):
    print(f"[{datetime.now():%H:%M:%S}] {msg}")

def git_run(*args):
    """Ejecuta comando git en el repo."""
    r = subprocess.run(["git"] + list(args), capture_output=True, text=True,
                       timeout=30, cwd=BASE)
    if r.returncode != 0:
        log(f"⚠ git {' '.join(args)}: {r.stderr[:100].strip()}")
    return r

def main():
    log("=" * 45)
    log("INICIANDO PIPELINE DE TRANSCRIPCIONES")
    log("=" * 45)

    # Paso 1: Traer cambios del VPS (processed_videos.txt actualizado)
    log("\n[1/4] git pull desde GitHub...")
    git_run("pull")

    if not PROCESSED.exists():
        log("❌ No existe processed_videos.txt. Saliendo.")
        return

    # Paso 2: Identificar videos sin transcripción
    log("\n[2/4] Buscando videos sin transcripción...")
    pendientes = []
    with open(PROCESSED, encoding="utf-8", errors="replace") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) < 3:
                continue
            vid = parts[0].strip()
            titulo = parts[1].strip() if len(parts) >= 3 else parts[0].strip()

            # Verificar si ya tiene transcripción en algún streamer
            ya_tiene = False
            for s in STREAMERS:
                carpeta = BASE / "streamers" / s / "transcripciones"
                if list(carpeta.glob(f"{vid}_transcript.txt")):
                    ya_tiene = True
                    break
            # También verificar en temp
            if (BASE / "temp" / f"{vid}_transcript.txt").exists():
                ya_tiene = True

            if not ya_tiene:
                streamer = parts[3].strip() if len(parts) >= 4 else ""
                pendientes.append((vid, titulo, streamer))

    log(f"   → {len(pendientes)} video(s) pendiente(s)")

    if not pendientes:
        log("✓ Todo al día. Saliendo.")
        return

    # Paso 3: Descargar transcripciones una por una
    log("\n[3/4] Descargando transcripciones...")
    descargados = 0
    for i, (vid, titulo, streamer) in enumerate(pendientes, 1):
        url = f"https://www.youtube.com/watch?v={vid}"
        output = str(BASE / "temp" / vid)

        log(f"   [{i}/{len(pendientes)}] {titulo[:60]}...")

        # Construir comando yt-dlp
        cmd = [
            "yt-dlp",
            "--write-auto-subs",
            "--sub-lang", "es,en",
            "--skip-download",
            "--output", output,
            "--quiet",
        ]

        # Agregar cookies si existen
        if COOKIES.exists():
            cmd = ["yt-dlp", "--cookies", str(COOKIES)] + cmd[1:]

        cmd.append(url)

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)

        if result.returncode == 0:
            # Buscar archivo de subtítulos descargado
            subs_dir = BASE / "temp"
            for ext in [".vtt", ".srt"]:
                files = list(subs_dir.glob(f"{vid}*{ext}"))
                if files:
                    vtt_file = files[0]
                    # Convertir a TXT limpio
                    content = vtt_file.read_text(encoding="utf-8", errors="replace")
                    lines = [
                        l.strip() for l in content.split("\n")
                        if l.strip()
                        and "-->" not in l
                        and "WEBVTT" not in l
                        and not l.strip().isdigit()
                    ]
                    texto_limpio = " ".join(lines)

                    # Guardar en carpeta temporal
                    txt_path = subs_dir / f"{vid}_transcript.txt"
                    txt_path.write_text(texto_limpio, encoding="utf-8")

                    # Limpiar VTT
                    vtt_file.unlink(missing_ok=True)
                    log(f"   ✅ Transcripción descargada ({len(texto_limpio)} chars)")
                    descargados += 1
                    break
            else:
                log(f"   ⚠ Sin archivo de sub encontrado")
        else:
            log(f"   ❌ Error: {result.stderr[:80].strip()}")

        # Pequeña pausa entre descargas
        time.sleep(3)

    if descargados == 0:
        log("\n⚠ No se descargó ninguna transcripción nueva")
        return

    # Paso 4: Mover transcripciones y hacer commit
    log(f"\n[4/4] Subiendo {descargados} transcripción(es) a GitHub...")

    # Mover archivos de temp a sus carpetas de streamer
    with open(PROCESSED, encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) >= 4:
                vid = parts[0].strip()
                streamer = parts[3].strip()
                txt_file = BASE / "temp" / f"{vid}_transcript.txt"
                if txt_file.exists():
                    destino = BASE / "streamers" / streamer / "transcripciones" / f"{vid}_transcript.txt"
                    destino.parent.mkdir(parents=True, exist_ok=True)
                    txt_file.rename(destino)
                    log(f"   → {streamer}/transcripciones/{vid}_transcript.txt")

    git_run("add", "-A")
    r = git_run("diff", "--cached", "--quiet")
    if r.returncode != 0:
        fecha = datetime.now().strftime("%Y-%m-%d")
        git_run("commit", "-m", f"[transcripciones] {fecha}")
        git_run("push")
        log("✅ Push exitoso — VPS ya puede procesarlas")
    else:
        log("📭 Sin cambios para commit")

    log("\n" + "=" * 45)
    log("PIPELINE COMPLETADO")
    log("=" * 45)

if __name__ == "__main__":
    main()
