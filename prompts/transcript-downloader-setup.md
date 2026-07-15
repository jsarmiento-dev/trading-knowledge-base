# 📋 Prompt para Agente Local — Transcript Downloader

> Copia y pega esto COMPLETO a tu agente local (Cursor, Claude Code, Codex, etc.)
> El agente local leerá esto y configurará el pipeline automáticamente.

---

## Objetivo

Configurar un script en Windows que descargue automáticamente las transcripciones
de YouTube para 5 canales de trading, usando el archivo `processed_videos.txt`
como fuente de verdad. El VPS descubre los videos, tu PC solo baja transcripciones.

---

## Setup

### 1. Clonar el repo
```powershell
cd C:\
git clone git@github.com:jsarmiento-dev/trading-knowledge-base.git
cd trading-knowledge-base
```

### 2. Instalar Python 3.11+
- Descargar desde python.org
- Marcar "Add to PATH" durante instalación

### 3. Instalar yt-dlp
```powershell
pip install yt-dlp
yt-dlp --version
```

### 4. Exportar cookies de YouTube
- Abrir Chrome loggeado con cuenta de Gmail
- Extensión: **Get cookies.txt LOCALLY**
- Ir a https://www.youtube.com
- Click en extensión → Export
- Guardar como: `C:\trading-knowledge-base\cookies\youtube.txt`
- Crear carpeta cookies si no existe

---

## Crear el Script

Crear archivo: `C:\trading-knowledge-base\transcript_downloader.py`

```python
#!/usr/bin/env python3
"""
Pipeline LOCAL de transcripciones — Windows
SOLO descarga transcripciones. El VPS descubre los videos.
Formato esperado de processed_videos.txt: id|fecha|titulo|streamer
"""
import subprocess, time
from datetime import datetime
from pathlib import Path

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
        log(f"\u26a0 git {' '.join(args)}: {r.stderr[:100].strip()}")
    return r


def main():
    log("=" * 45)
    log("INICIANDO PIPELINE DE TRANSCRIPCIONES")
    log("=" * 45)

    # 1. Traer cambios del VPS
    log("\n[1/4] git pull...")
    git("pull")

    if not PROCESSED.exists():
        log("\u274c No existe processed_videos.txt")
        return

    # 2. Identificar videos sin transcripci\u00f3n
    log("\n[2/4] Buscando videos sin transcripci\u00f3n...")
    pendientes = []
    with open(PROCESSED, encoding="utf-8", errors="replace") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) < 4:
                continue
            vid = parts[0].strip()
            streamer = parts[3].strip()

            if streamer not in STREAMERS:
                continue

            # Verificar si ya tiene transcripci\u00f3n
            carpeta = BASE / "streamers" / streamer / "transcripciones"
            tiene = bool(list(carpeta.glob(f"{vid}_transcript.txt")))

            if not tiene:
                pendientes.append({"vid": vid, "streamer": streamer})

    log(f"   \u2192 {len(pendientes)} video(s) pendiente(s)")
    if not pendientes:
        log("\u2713 Todo al d\u00eda. Saliendo.")
        return

    # 3. Descargar transcripciones
    log("\n[3/4] Descargando transcripciones...")
    descargados = 0
    for i, p in enumerate(pendientes, 1):
        url = f"https://www.youtube.com/watch?v={p[\"vid\"]}"
        destino = BASE / "streamers" / p["streamer"] / "transcripciones"
        destino.mkdir(parents=True, exist_ok=True)
        output = str(destino / p["vid"])

        log(f"   [{i}/{len(pendientes)}] {p[\"streamer\"]}...")

        cmd = [
            "yt-dlp", "--write-auto-subs",
            "--sub-lang", "es,en",
            "--skip-download",
            "--output", output,
            "--quiet",
            url
        ]
        if COOKIES.exists():
            cmd = ["yt-dlp", "--cookies", str(COOKIES)] + cmd[1:]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)

        if result.returncode == 0:
            for ext in [".vtt", ".srt", ".json"]:
                files = list(destino.glob(f"{p[\"vid\"]}*{ext}"))
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
                    txt_file = destino / f"{p[\"vid\"]}_transcript.txt"
                    txt_file.write_text(texto, encoding="utf-8")
                    sub_file.unlink(missing_ok=True)
                    descargados += 1
                    break

        time.sleep(3)

    if descargados == 0:
        log("\n\u26a0 No se descarg\u00f3 nada nuevo")
        return

    # 4. Commit y push
    log(f"\n[4/4] Subiendo {descargados} transcripci\u00f3n(es)...")
    git("add", "-A")
    r = git("diff", "--cached", "--quiet")
    if r.returncode != 0:
        fecha = datetime.now().strftime("%Y-%m-%d")
        git("commit", "-m", f"[transcripciones] {fecha} - {descargados} videos")
        git("push")
        log(f"\u2705 Push exitoso \u2014 {descargados} transcripciones nuevas")
    else:
        log("\U0001f4ed Sin cambios para commit")

    log("\n" + "=" * 45)
    log("PIPELINE COMPLETADO")
    log("=" * 45)


if __name__ == "__main__":
    main()
```

---

## Programar en Windows Task Scheduler

1. Abrir **Task Scheduler** como Administrador
2. **Create Task**:
   - General: Name = `Trading Transcript Downloader`
   - Security: **Run whether user is logged on or not**
   - Check: **Run with highest privileges**
3. **Triggers -> New**:
   - Daily
   - Start: 2:50 AM
   - Enable
4. **Actions -> New**:
   - Program: `C:\Users\[TU_USUARIO]\AppData\Local\Programs\Python\Python311\python.exe`
   - Arguments: `C:\trading-knowledge-base\transcript_downloader.py`
   - Start in: `C:\trading-knowledge-base`
5. **Conditions**:
   - Uncheck: "Stop if running for X days"
6. **Settings**:
   - Check: "Run task as soon as possible after a scheduled start is missed"

---

## Verificaci\u00f3n

```powershell
cd C:\trading-knowledge-base
python transcript_downloader.py
```

Deben crearse archivos en:
```
streamers/ArgenTrader/transcripciones/VIDEOID_transcript.txt
streamers/ZCoinTV/transcripciones/VIDEOID_transcript.txt
streamers/ScottFDX/transcripciones/VIDEOID_transcript.txt
streamers/NovaTrader/transcripciones/VIDEOID_transcript.txt
streamers/MambaFx/transcripciones/VIDEOID_transcript.txt
```

---

## Notas

- Las cookies de YouTube expiran cada 2-3 meses. Reexportar cuando deje de funcionar.
- El script descarga SOLO videos que no tengan `_transcript.txt` en la carpeta del streamer.
- Si un video no tiene subt\u00edtulos, se salta sin fallar.
- No modificar `processed_videos.txt` manualmente.
- Task Scheduler corre aunque la PC est\u00e9 bloqueada.
