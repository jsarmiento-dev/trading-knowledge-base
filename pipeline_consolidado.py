#!/usr/bin/env python3
"""
Pipeline Consolidado de Trading Streamer Intel.
Procesa 4 streamers secuencialmente para evitar rate limit de NVIDIA NIM.

Streamers:
1. ArgenTrader - https://www.youtube.com/@ArgenTraderr/videos
2. ZCoinTV - https://www.youtube.com/@ZCoinTV/videos
3. ScottFDX - https://www.youtube.com/@ScottFDX/videos
4. NovaTrader - https://www.youtube.com/@nova-trader/videos (usa /streams y /shorts)
"""

import os
import sys
import json
import time
import subprocess
import re
import glob
import datetime
from pathlib import Path

# Configuración
BASE_DIR = Path("/home/ubuntu/proyects/trading")
PROCESSED_FILE = BASE_DIR / "processed_videos.txt"
STREAMERS_DIR = BASE_DIR / "streamers"

# Streamers configurados
STREAMERS = [
    {
        "name": "ArgenTrader",
        "channel": "https://www.youtube.com/@ArgenTraderr/videos",
        "folder": "ArgenTrader",
        "extra_urls": []
    },
    {
        "name": "ZCoinTV",
        "channel": "https://www.youtube.com/@ZCoinTV/videos",
        "folder": "ZCoinTV",
        "extra_urls": []
    },
    {
        "name": "ScottFDX",
        "channel": "https://www.youtube.com/@ScottFDX/videos",
        "folder": "ScottFDX",
        "extra_urls": []
    },
    {
        "name": "NovaTrader",
        "channel": "https://www.youtube.com/@nova-trader/videos",
        "folder": "NovaTrader",
        "extra_urls": [
            "https://www.youtube.com/@nova-trader/streams",
            "https://www.youtube.com/@nova-trader/shorts"
        ]
    }
]

MAX_VIDEOS_PER_STREAMER = 3
DELAY_BETWEEN_STREAMERS = 60  # segundos
DELAY_AFTER_429 = 120  # segundos

def log(msg):
    """Imprimir con timestamp."""
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)

def run_cmd(cmd, timeout=120):
    """Ejecutar comando y retornar (exit_code, output)."""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return result.returncode, result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return -1, "TIMEOUT"
    except Exception as e:
        return -1, str(e)

def load_processed_videos():
    """Cargar videos ya procesados desde processed_videos.txt."""
    processed = {}
    if PROCESSED_FILE.exists():
        for line in PROCESSED_FILE.read_text().splitlines():
            if "|" in line:
                parts = line.split("|")
                if len(parts) >= 1:
                    video_id = parts[0].strip()
                    processed[video_id] = line.strip()
    log(f"Videos ya procesados: {len(processed)}")
    return processed

def save_processed_video(video_id, date_str, title):
    """Agregar video a processed_videos.txt."""
    with open(PROCESSED_FILE, "a") as f:
        f.write(f"{video_id}|{date_str}|{title}\n")
    log(f"Agregado a processed_videos.txt: {video_id}")

def get_channel_videos(channel_url, max_videos=10):
    """
    Obtener lista de videos de un canal usando yt-dlp --flat-playlist.
    Retorna lista de dicts: [{'id': ..., 'title': ...}, ...]
    """
    cmd = f"""yt-dlp --flat-playlist --print "%(id)s|%(title)s" --playlist-end {max_videos} "{channel_url}" """
    log(f"Obteniendo videos de: {channel_url}")
    code, output = run_cmd(cmd, timeout=60)
    
    if code != 0:
        log(f"Error obteniendo videos: {output[:500]}")
        return []
    
    videos = []
    for line in output.splitlines():
        line = line.strip()
        if "|" in line and not line.startswith("WARNING") and not line.startswith("ERROR"):
            parts = line.split("|", 1)
            if len(parts) == 2:
                video_id = parts[0].strip()
                title = parts[1].strip()
                videos.append({"id": video_id, "title": title})
    
    log(f"Encontrados {len(videos)} videos en {channel_url}")
    return videos

def filter_new_videos(videos, processed):
    """Filtrar videos que ya fueron procesados."""
    new = []
    for v in videos:
        if v["id"] not in processed:
            new.append(v)
    return new

def download_subtitles(video_id, video_title, output_dir):
    """
    Descargar subtítulos automáticos en español usando yt-dlp.
    Guarda archivos .vtt en output_dir.
    Retorna la ruta al archivo .vtt si tuvo éxito, None si falló.
    """
    # Crear directorio temporal para subtítulos
    sub_dir = output_dir / "subtitles"
    sub_dir.mkdir(parents=True, exist_ok=True)
    
    # Limpiar archivos anteriores en sub_dir
    for f in sub_dir.glob("*.vtt"):
        f.unlink()
    
    cmd = f"""yt-dlp --write-auto-subs --sub-lang es --skip-download --output "{sub_dir}/%(id)s.%(ext)s" "https://www.youtube.com/watch?v={video_id}" """
    log(f"Descargando subtítulos para: {video_id}")
    code, output = run_cmd(cmd, timeout=120)
    
    if code != 0:
        log(f"Error descargando subtítulos: {output[:300]}")
        return None
    
    # Buscar archivo .vtt descargado
    vtt_files = list(sub_dir.glob("*.vtt"))
    if vtt_files:
        return vtt_files[0]
    
    # También buscar .es.vtt
    vtt_files = list(sub_dir.glob("*.es.vtt"))
    if vtt_files:
        return vtt_files[0]
    
    log(f"No se encontró archivo .vtt para {video_id}")
    return None

def vtt_to_text(vtt_path):
    """
    Convertir archivo .vtt a texto plano.
    Elimina timestamps, etiquetas HTML y líneas vacías duplicadas.
    """
    try:
        with open(vtt_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        log(f"Error leyendo VTT: {e}")
        return ""
    
    text_lines = []
    prev_line = ""
    
    for line in lines:
        line = line.strip()
        # Saltar líneas vacías, números de índice, timestamps y etiquetas WEBVTT
        if not line:
            continue
        if line.isdigit():
            continue
        if re.match(r"[\d:,\.]+ --> [\d:,\.]+", line):
            continue
        if line == "WEBVTT":
            continue
        if line.startswith("<") and line.endswith(">"):
            # Eliminar etiquetas HTML simples
            line = re.sub(r"<[^>]+>", "", line)
        if not line:
            continue
        # Evitar duplicados consecutivos
        if line != prev_line:
            text_lines.append(line)
            prev_line = line
    
    full_text = " ".join(text_lines)
    # Limpiar espacios múltiples
    full_text = re.sub(r"\s+", " ", full_text).strip()
    return full_text

def summarize_with_llm(text, prompt_instruction):
    """
    Usar NVIDIA NIM (modelo configurado) para resumir/extraer conocimiento.
    Como estamos en un script autónomo, usamos la API de OpenRouter (el modelo configurado es tencent/hy3-preview).
    Usamos curl + OpenRouter API key desde variable de entorno.
    """
    # Por ahora, guardamos el texto para procesamiento posterior
    # En producción, aquí se llamaría al LLM
    return text[:2000]  # placeholder

def ensure_streamer_dirs(streamer_folder):
    """Asegurar que existan los directorios para un streamer."""
    base = STREAMERS_DIR / streamer_folder
    (base / "conceptos").mkdir(parents=True, exist_ok=True)
    (base / "setups").mkdir(parents=True, exist_ok=True)
    (base / "herramientas").mkdir(parents=True, exist_ok=True)
    # reglas.md se crea/append en la base
    return base

def save_concept(base_dir, title, content):
    """Guardar un concepto como .md en conceptos/."""
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:50]
    path = base_dir / "conceptos" / f"{slug}.md"
    with open(path, "w") as f:
        f.write(f"# {title}\n\n")
        f.write(content)
    log(f"Guardado concepto: {path}")
    return path

def save_setup(base_dir, title, content):
    """Guardar un setup como .md en setups/."""
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:50]
    path = base_dir / "setups" / f"{slug}.md"
    with open(path, "w") as f:
        f.write(f"# {title}\n\n")
        f.write(content)
    log(f"Guardado setup: {path}")
    return path

def save_tool(base_dir, title, content):
    """Guardar una herramienta como .md en herramientas/."""
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:50]
    path = base_dir / "herramientas" / f"{slug}.md"
    with open(path, "w") as f:
        f.write(f"# {title}\n\n")
        f.write(content)
    log(f"Guardado herramienta: {path}")
    return path

def append_rules(base_dir, rules_text):
    """Agregar reglas a reglas.md (append-only)."""
    path = base_dir / "reglas.md"
    with open(path, "a") as f:
        f.write(f"\n## {datetime.date.today().isoformat()}\n\n")
        f.write(rules_text)
        f.write("\n")
    log(f"Append a reglas.md: {path}")
    return path

def process_video_transcript(transcript_text, video_title, video_id, streamer_name, base_dir):
    """
    Procesar la transcripción para extraer conocimiento.
    Usa el LLM para extraer conceptos, setups, herramientas y reglas.
    
    Como estamos en un script autónomo, vamos a:
    1. Guardar la transcripción completa como .txt
    2. Extraer conocimiento básico con regex/heurísticas
    3. Dejar marcadores para procesamiento con LLM posterior
    """
    # Guardar transcripción completa
    transcripts_dir = base_dir / "transcripts"
    transcripts_dir.mkdir(parents=True, exist_ok=True)
    transcript_path = transcripts_dir / f"{video_id}.txt"
    with open(transcript_path, "w") as f:
        f.write(f"# {video_title}\n\n")
        f.write(transcript_text)
    log(f"Guardada transcripción: {transcript_path}")
    
    # Extraer conceptos básicos (palabras clave de trading)
    trading_keywords = [
        "soporte", "resistencia", "tendencia", "volumen", "rsi", "macd", "media móvil",
        "fibonacci", "retroceso", "extension", "liquidez", "order block", "fair value gap",
        "fvg", "smart money", "manipulación", "distribución", "acumulación", "stop loss",
        "take profit", "risk reward", "gestión de riesgo", "psicotrading", "velas japonesas",
        "patrón", "figura", "triángulo", "banderín", "doble techo", "doble suelo",
        "head and shoulders", "hombro cabeza hombro", "divergencia", "convergencia"
    ]
    
    found_concepts = []
    transcript_lower = transcript_text.lower()
    for kw in trading_keywords:
        if kw in transcript_lower:
            found_concepts.append(kw)
    
    # Guardar conceptos encontrados
    if found_concepts:
        concepts_text = "\n".join([f"- {c}" for c in set(found_concepts)])
        save_concept(base_dir, f"Conceptos de {video_title[:50]}", 
                     f"Video: {video_title}\n\nConceptos mencionados:\n{concepts_text}\n\n(Transcripción pendiente de procesamiento con LLM)")
    
    # Extraer reglas mencionadas (líneas con "siempre", "nunca", "regla", "importante")
    rules = []
    for line in transcript_text.split(". "):
        line_lower = line.lower()
        if any(word in line_lower for word in ["siempre", "nunca", "regla", "importante", "obligatorio", "debes"]):
            rules.append(line.strip())
    
    if rules:
        rules_text = "\n".join([f"- {r}" for r in rules[:10]])
        append_rules(base_dir, f"Video: {video_title}\n\n{rules_text}\n")
    
    return {
        "concepts": found_concepts,
        "rules_count": len(rules)
    }

def process_streamer(streamer_config, processed_videos):
    """
    Procesar un streamer: obtener videos, filtrar nuevos, descargar subtítulos,
    procesar transcripciones.
    """
    name = streamer_config["name"]
    channel = streamer_config["channel"]
    folder = streamer_config["folder"]
    extra_urls = streamer_config.get("extra_urls", [])
    
    log(f"=== PROCESANDO STREAMER: {name} ===")
    
    # Asegurar directorios
    base_dir = ensure_streamer_dirs(folder)
    
    # Obtener videos del canal principal
    videos = get_channel_videos(channel, max_videos=10)
    
    # Obtener videos de URLs extra (streams, shorts) para NovaTrader
    for extra_url in extra_urls:
        extra_videos = get_channel_videos(extra_url, max_videos=5)
        videos.extend(extra_videos)
    
    # Filtrar videos ya procesados
    new_videos = filter_new_videos(videos, processed_videos)
    log(f"Videos nuevos para {name}: {len(new_videos)}")
    
    if not new_videos:
        log(f"Sin videos nuevos de {name}")
        return {"streamer": name, "new_videos": 0, "processed": []}
    
    # Limitar a MAX_VIDEOS_PER_STREAMER por día
    if len(new_videos) > MAX_VIDEOS_PER_STREAMER:
        log(f"Limitando a {MAX_VIDEOS_PER_STREAMER} videos de {len(new_videos)} encontrados")
        new_videos = new_videos[:MAX_VIDEOS_PER_STREAMER]
    
    results = []
    for i, video in enumerate(new_videos):
        video_id = video["id"]
        video_title = video["title"]
        log(f"Procesando video {i+1}/{len(new_videos)}: {video_title[:60]}")
        
        # Descargar subtítulos
        vtt_path = download_subtitles(video_id, video_title, base_dir)
        if not vtt_path:
            log(f"No se pudieron obtener subtítulos para {video_id}, saltando...")
            continue
        
        # Convertir VTT a texto
        transcript_text = vtt_to_text(vtt_path)
        if not transcript_text or len(transcript_text) < 100:
            log(f"Transcripción muy corta para {video_id}, saltando...")
            continue
        
        # Procesar transcripción
        extraction = process_video_transcript(transcript_text, video_title, video_id, name, base_dir)
        
        # Guardar en processed_videos.txt
        today = datetime.date.today().isoformat()
        save_processed_video(video_id, today, video_title)
        processed_videos[video_id] = f"{video_id}|{today}|{video_title}"
        
        results.append({
            "video_id": video_id,
            "title": video_title,
            "concepts": extraction["concepts"],
            "rules_count": extraction["rules_count"]
        })
        
        # Limpiar archivos temporales
        if vtt_path.exists():
            vtt_path.unlink()
    
    log(f"=== TERMINADO {name}: {len(results)} videos procesados ===")
    return {"streamer": name, "new_videos": len(new_videos), "processed": results}

def git_commit_push():
    """Hacer git add, commit y push."""
    cmd = f"""cd {BASE_DIR} && git add -A && git commit -m "[Consolidado] {datetime.date.today().isoformat()} — Conceptos de streamers" && git push origin main"""
    log("Haciendo git commit y push...")
    code, output = run_cmd(cmd, timeout=30)
    if code != 0:
        log(f"Error en git: {output[:500]}")
        return False
    log("Git commit/push exitoso")
    return True

def main():
    log("=== INICIANDO PIPELINE CONSOLIDADO ===")
    
    # Cargar videos ya procesados
    processed_videos = load_processed_videos()
    
    # Procesar streamers secuencialmente
    all_results = []
    for i, streamer in enumerate(STREAMERS):
        result = process_streamer(streamer, processed_videos)
        all_results.append(result)
        
        # Esperar entre streamers para evitar rate limit
        if i < len(STREAMERS) - 1:
            log(f"Esperando {DELAY_BETWEEN_STREAMERS} segundos antes del siguiente streamer...")
            time.sleep(DELAY_BETWEEN_STREAMERS)
    
    # Git commit y push
    git_commit_push()
    
    # Generar resumen
    log("=== RESUMEN DEL PIPELINE ===")
    total_videos = sum(r["new_videos"] for r in all_results)
    for r in all_results:
        log(f"  {r['streamer']}: {r['new_videos']} videos nuevos, {len(r['processed'])} procesados")
        for p in r["processed"]:
            log(f"    - {p['video_id']}: {p['title'][:50]}")
            if p["concepts"]:
                log(f"      Conceptos: {', '.join(p['concepts'][:5])}")
    
    log(f"TOTAL videos procesados: {total_videos}")
    log("=== PIPELINE TERMINADO ===")
    
    return all_results

if __name__ == "__main__":
    main()
