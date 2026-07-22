#!/usr/bin/env bash
# pipeline_completo.sh — Ejecuta descarga + whisper + consolidado
set -euo pipefail

BASE="/home/ubuntu/proyects/trading"
cd "$BASE"

echo "[pipeline_completo] $(date '+%Y-%m-%d %H:%M:%S') — Iniciando"

# FASE 0: Sincronizar con GitHub (traer audios/transcripts del PC)
echo ""
echo "═══ FASE 0: Git pull — sincronizar con PC ═══"
git pull origin main 2>&1 || echo "[WARN] git pull falló — continuando con repo local"

# FASE 1: Descubrir y descargar transcripciones
echo ""
echo "═══ FASE 1: Pipeline de descarga ═══"
python3 pipeline_download.py || echo "[WARN] pipeline_download.py exit code: $?"

# FASE 2: Transcribir audios pendientes con Whisper
echo ""
echo "═══ FASE 2: Whisper — Transcripción de audios ═══"
python3 pipeline_whisper.py || echo "[WARN] pipeline_whisper.py exit code: $?"

# FASE 3: Consolidado (si existe)
if [ -f pipeline_consolidado.py ]; then
    echo ""
    echo "═══ FASE 3: Consolidado ═══"
    python3 pipeline_consolidado.py || echo "[WARN] pipeline_consolidado.py exit code: $?"
fi

echo ""
echo "[pipeline_completo] $(date '+%Y-%m-%d %H:%M:%S') — Completado"
