#!/usr/bin/env python3
"""
Pipeline Whisper — Procesa audios sin transcripción (subidos desde PC local).

Flujo:
  1. Escanea audios_pendientes/ buscando .m4a/.webm/.opus
  2. Lee .meta (streamer|título)
  3. Transcribe con faster-whisper (modelo: base)
  4. Guarda transcripción en streamers/{streamer}/transcripciones/{video_id}_transcript.md
  5. Elimina .m4a y .meta procesados
  6. Git commit + push

Ejecución: python3 pipeline_whisper.py
Cron sugerido: 0 3 * * * (1 hora después del pipeline de descarga)
"""

import os
import sys
import time
import json
import subprocess
from pathlib import Path
from datetime import datetime
from faster_whisper import WhisperModel

# ─── Config ─────────────────────────────────────────────────────
BASE_DIR = Path.home() / "proyects/trading"
AUDIOS_DIR = BASE_DIR / "audios_pendientes"
STREAMERS_DIR = BASE_DIR / "streamers"
PROCESSED_FILE = BASE_DIR / "processed_videos.txt"
RESULTS_FILE = BASE_DIR / "pipeline_results.json"
RESULTS_KEY = "whisper"  # clave dentro de pipeline_results.json

WHISPER_MODEL = "tiny"       # tiny | base | small | medium | large-v3
WHISPER_DEVICE = "cpu"       # cpu | cuda
WHISPER_THREADS = 4
WHISPER_BEAM = 1             # 1 = greedy (rápido), 5 = beam search (mejor calidad)
WHISPER_COMPUTE = "int8"     # int8 (rápido), float16, float32

TRANSCRIPT_HEADER = (
    "# Transcripción generada por Whisper (IA) — video sin subtítulos automáticos\n"
    "# Fuente: audio descargado desde PC local\n"
    "# Modelo: faster-whisper/{model} | fecha: {date}\n"
    "---\n\n"
)

# Extensiones de audio válidas
AUDIO_EXTENSIONS = {".m4a", ".webm", ".opus", ".mp3"}


# ─── Logging ────────────────────────────────────────────────────
def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


# ─── Meta ────────────────────────────────────────────────────────
def parse_meta(meta_path):
    """Lee .meta y devuelve (streamer, titulo)."""
    content = meta_path.read_text(encoding="utf-8").strip()
    if "|" in content:
        parts = content.split("|", 1)
        return parts[0].strip(), parts[1].strip()
    return "desconocido", content


def save_processed(vid, title, streamer_name):
    """Registra audio como procesado en processed_videos.txt."""
    with open(PROCESSED_FILE, "a", encoding="utf-8") as f:
        f.write(f"{vid}|{datetime.now().strftime('%Y-%m-%d')}|{title}|{streamer_name}|whisper\n")


# ─── Transcripción ──────────────────────────────────────────────
def transcribe_audio(audio_path, model):
    """Transcribe un archivo de audio. Retorna (texto, info_idioma)."""
    log(f"  Transcribiendo {audio_path.name}...")
    t0 = time.time()

    segments, info = model.transcribe(
        str(audio_path),
        beam_size=WHISPER_BEAM,
        language="es",          # forzar español (la mayoría del contenido)
    )

    text_parts = []
    for seg in segments:
        text_parts.append(seg.text.strip())

    full_text = " ".join(text_parts)
    elapsed = time.time() - t0
    log(f"  ✅ Transcripción completada — {elapsed:.1f}s, {len(full_text)} chars")
    return full_text, info


def save_transcript(video_id, streamer, titulo, text, model_name):
    """Guarda la transcripción como markdown en el directorio del streamer."""
    transc_dir = STREAMERS_DIR / streamer / "transcripciones"
    transc_dir.mkdir(parents=True, exist_ok=True)

    output_path = transc_dir / f"{video_id}_transcript.md"

    header = TRANSCRIPT_HEADER.format(
        model=model_name,
        date=datetime.now().strftime("%Y-%m-%d %H:%M"),
    )
    content = f"{header}# {titulo}\n\n{text}\n"

    output_path.write_text(content, encoding="utf-8")
    log(f"  📝 Guardado: {output_path.relative_to(BASE_DIR)}")
    return output_path


def cleanup_audio(video_id):
    """Elimina .m4a y .meta después de transcripción exitosa."""
    for ext in AUDIO_EXTENSIONS | {".meta"}:
        f = AUDIOS_DIR / f"{video_id}{ext}"
        if f.exists():
            f.unlink()
            log(f"  🗑 Eliminado: {f.name}")


# ─── Git ────────────────────────────────────────────────────────
def git(*args):
    """Ejecuta comando git en BASE_DIR."""
    cmd = ["git"] + list(args)
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=15, cwd=BASE_DIR)
    if r.returncode != 0 and r.stderr.strip():
        log(f"⚠ git {' '.join(args)}: {r.stderr[:100].strip()}")
    return r


# ─── Resultados ─────────────────────────────────────────────────
def save_results(results):
    """Guarda resultados en pipeline_results.json (mergeando con existente)."""
    existing = {}
    if RESULTS_FILE.exists():
        try:
            existing = json.loads(RESULTS_FILE.read_text())
        except (json.JSONDecodeError, Exception):
            existing = {}
    existing[RESULTS_KEY] = results
    RESULTS_FILE.write_text(
        json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    log(f"  📊 Resultados guardados en {RESULTS_FILE.name}")


# ─── Main ───────────────────────────────────────────────────────
def main():
    log("=" * 60)
    log("PIPELINE WHISPER — Transcripción de audios pendientes")
    log(f"Modelo: {WHISPER_MODEL} | Device: {WHISPER_DEVICE} | Threads: {WHISPER_THREADS}")
    log(f"Audios dir: {AUDIOS_DIR}")
    log("=" * 60)

    # ── 1. Escanear audios ──
    audio_files = []
    for f in sorted(AUDIOS_DIR.iterdir()):
        if f.suffix in AUDIO_EXTENSIONS:
            video_id = f.stem
            meta_file = AUDIOS_DIR / f"{video_id}.meta"
            if not meta_file.exists():
                log(f"  ⚠ {f.name} no tiene .meta, se salta")
                continue
            audio_files.append((video_id, f, meta_file))

    if not audio_files:
        log("📭 No hay audios pendientes para procesar")
        return 0

    log(f"🎯 Audios encontrados: {len(audio_files)}")
    for vid, apath, _ in audio_files:
        size_mb = apath.stat().st_size / (1024 * 1024)
        log(f"  • {vid} ({size_mb:.1f} MB)")

    # ── 2. Cargar modelo Whisper ──
    log(f"\n🔧 Cargando modelo Whisper '{WHISPER_MODEL}'...")
    t0 = time.time()
    model = WhisperModel(
        WHISPER_MODEL,
        device=WHISPER_DEVICE,
        cpu_threads=WHISPER_THREADS,
        compute_type=WHISPER_COMPUTE,
    )
    log(f"  ✅ Modelo cargado en {time.time() - t0:.1f}s")

    # ── 3. Procesar cada audio ──
    results = []
    total_ok = 0
    total_fail = 0

    for video_id, audio_path, meta_path in audio_files:
        log(f"\n─── {video_id} ───")
        try:
            streamer, titulo = parse_meta(meta_path)
            log(f"  Streamer: {streamer}")
            log(f"  Título: {titulo[:80]}")

            text, info = transcribe_audio(audio_path, model)

            if not text.strip():
                log(f"  ⚠ Transcripción vacía para {video_id}")
                total_fail += 1
                results.append({
                    "video_id": video_id,
                    "streamer": streamer,
                    "status": "empty",
                })
                continue

            # Guardar transcripción
            out_path = save_transcript(video_id, streamer, titulo, text, WHISPER_MODEL)

            # Registrar en processed_videos.txt
            save_processed(video_id, titulo, streamer)

            # Limpiar audio y meta
            cleanup_audio(video_id)

            total_ok += 1
            results.append({
                "video_id": video_id,
                "streamer": streamer,
                "title": titulo,
                "char_count": len(text),
                "language": info.language,
                "language_probability": round(info.language_probability, 2),
                "output": str(out_path.relative_to(BASE_DIR)),
                "status": "ok",
            })

        except Exception as e:
            log(f"  ❌ Error procesando {video_id}: {e}")
            total_fail += 1
            results.append({
                "video_id": video_id,
                "streamer": streamer if 'streamer' in dir() else "?",
                "status": "error",
                "error": str(e),
            })

    # ── 4. Resumen ──
    log(f"\n{'=' * 60}")
    log(f"RESUMEN: {total_ok} OK, {total_fail} errores")
    log(f"{'=' * 60}")

    # Guardar resultados
    save_results({
        "timestamp": datetime.now().isoformat(),
        "total": len(audio_files),
        "ok": total_ok,
        "fail": total_fail,
        "items": results,
    })

    # ── 5. Git commit + push ──
    if total_ok > 0:
        log(f"\n📤 Git commit + push...")
        git("add", "-A")
        r = git("diff", "--cached", "--quiet")
        if r.returncode != 0:
            today = datetime.now().strftime("%Y-%m-%d")
            msg = f"[whisper] {today} — {total_ok} transcripciones desde audio"
            git("commit", "-m", msg)
            r = git("push")
            log(f"✅ Push exitoso — {total_ok} transcripciones por Whisper")
        else:
            log("📭 Sin cambios para commit")
    else:
        log("⚠ No se transcribió nada, saltando git commit")

    return 0 if total_ok > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
