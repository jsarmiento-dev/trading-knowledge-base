#!/usr/bin/env python3
"""
Pipeline CONSOLIDADO de trading streamer intel.
Procesa 4 streamers secuencialmente para evitar rate limit.
"""

import os
import sys
import json
import time
import subprocess
from datetime import datetime
from pathlib import Path

# Configuración
STREAMERS = [
    {
        'name': 'ArgenTrader',
        'channel': 'https://www.youtube.com/@ArgenTraderr/videos',
        'dir': 'ArgenTrader'
    },
    {
        'name': 'ZCoinTV',
        'channel': 'https://www.youtube.com/@ZCoinTV/videos',
        'dir': 'ZCoinTV'
    },
    {
        'name': 'ScottFDX',
        'channel': 'https://www.youtube.com/@ScottFDX/videos',
        'dir': 'ScottFDX'
    },
    {
        'name': 'NovaTrader',
        'channel': 'https://www.youtube.com/@nova-trader/videos',
        'dir': 'NovaTrader',
        'extra_channels': [
            'https://www.youtube.com/@nova-trader/streams',
            'https://www.youtube.com/@nova-trader/shorts'
        ]
    }
]

BASE_DIR = Path.home() / "proyects/trading"
PROCESSED_FILE = BASE_DIR / "processed_videos.txt"
STREAMERS_DIR = BASE_DIR / "streamers"
MAX_VIDEOS_PER_STREAMER = 3
DELAY_BETWEEN_STREAMERS = 60  # segundos
RATE_LIMIT_DELAY = 120  # segundos si recibimos 429

def log(msg):
    """Imprime mensaje con timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {msg}")

def load_processed_videos():
    """Carga la lista de videos ya procesados."""
    processed = set()
    if PROCESSED_FILE.exists():
        with open(PROCESSED_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    # Formato: ID|YYYY-MM-DD|TITLE
                    parts = line.split('|')
                    if parts:
                        processed.add(parts[0])  # El ID es la primera parte
    return processed

def save_processed_video(video_id, title):
    """Agrega un video a la lista de procesados."""
    today = datetime.now().strftime("%Y-%m-%d")
    with open(PROCESSED_FILE, 'a') as f:
        f.write(f"{video_id}|{today}|{title}\n")
    log(f"Video guardado en processed_videos.txt: {video_id}")

def get_videos_from_channel(channel_url, max_videos=10):
    """Obtiene la lista de videos de un canal usando yt-dlp."""
    cmd = [
        '/home/ubuntu/.yt-dlp-venv/bin/yt-dlp',
        '--flat-playlist',
        '--print-json',
        '--playlist-end', str(max_videos),
        channel_url
    ]
    
    log(f"Ejecutando: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode != 0:
            log(f"Error ejecutando yt-dlp: {result.stderr}")
            return []
        
        videos = []
        for line in result.stdout.strip().split('\n'):
            if line:
                try:
                    data = json.loads(line)
                    videos.append({
                        'id': data.get('id', ''),
                        'title': data.get('title', ''),
                        'url': f"https://www.youtube.com/watch?v={data.get('id', '')}"
                    })
                except json.JSONDecodeError:
                    continue
        
        log(f"Obtenidos {len(videos)} videos de {channel_url}")
        return videos
        
    except subprocess.TimeoutExpired:
        log("Timeout ejecutando yt-dlp")
        return []
    except Exception as e:
        log(f"Error obteniendo videos: {e}")
        return []

def filter_new_videos(videos, processed_set):
    """Filtra videos que ya han sido procesados."""
    new_videos = []
    for video in videos:
        if video['id'] not in processed_set:
            new_videos.append(video)
        else:
            log(f"Video ya procesado, saltando: {video['id']} - {video['title']}")
    
    return new_videos

def ensure_streamer_dirs(streamer_dir):
    """Asegura que existan los directorios del streamer."""
    base = STREAMERS_DIR / streamer_dir
    (base / "conceptos").mkdir(parents=True, exist_ok=True)
    (base / "setups").mkdir(parents=True, exist_ok=True)
    (base / "herramientas").mkdir(parents=True, exist_ok=True)
    return base

def download_transcript(video_url, video_id, output_dir):
    """Descarga la transcripción de un video."""
    cmd = [
        '/home/ubuntu/.yt-dlp-venv/bin/yt-dlp',
        '--write-auto-subs',
        '--sub-lang', 'es',
        '--skip-download',
        '--output', str(output_dir / f"{video_id}"),
        video_url
    ]
    
    log(f"Descargando transcripción: {video_url}")
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if result.returncode != 0:
            log(f"Error descargando transcripción: {result.stderr}")
            return None
        
        # Buscar archivo .vtt generado
        vtt_files = list(output_dir.glob(f"{video_id}*.vtt"))
        if vtt_files:
            return vtt_files[0]
        else:
            log("No se encontró archivo .vtt generado")
            return None
            
    except Exception as e:
        log(f"Error descargando transcripción: {e}")
        return None

def vtt_to_text(vtt_file):
    """Convierte archivo .vtt a texto plano."""
    try:
        with open(vtt_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Filtrar líneas de metadatos de WebVTT
        text_lines = []
        for line in lines:
            line = line.strip()
            # Saltar líneas vacías, timestamps, y metadatos
            if not line or line == 'WEBVTT' or '-->' in line:
                continue
            # Saltar números de secuencia
            if line.isdigit():
                continue
            # Saltar etiquetas de estilo
            if line.startswith('<') and line.endswith('>'):
                continue
            text_lines.append(line)
        
        # Unir líneas duplicadas (subtítulos que se repiten)
        unique_lines = []
        for line in text_lines:
            if not unique_lines or line != unique_lines[-1]:
                unique_lines.append(line)
        
        return ' '.join(unique_lines)
        
    except Exception as e:
        log(f"Error convirtiendo VTT a texto: {e}")
        return ""

def process_streamer(streamer):
    """Procesa un streamer completo."""
    log(f"\n{'='*60}")
    log(f"PROCESANDO STREAMER: {streamer['name']}")
    log(f"{'='*60}\n")
    
    # Asegurar directorios
    streamer_base = ensure_streamer_dirs(streamer['dir'])
    
    # Cargar videos procesados
    processed = load_processed_videos()
    
    # Obtener videos del canal principal
    videos = get_videos_from_channel(streamer['channel'])
    
    # Si es NovaTrader, también obtener de /streams y /shorts
    if 'extra_channels' in streamer:
        for extra_channel in streamer['extra_channels']:
            extra_videos = get_videos_from_channel(extra_channel)
            videos.extend(extra_videos)
    
    if not videos:
        log(f"No se encontraron videos para {streamer['name']}")
        return {
            'streamer': streamer['name'],
            'videos_procesados': [],
            'mensaje': 'No se encontraron videos'
        }
    
    # Filtrar videos nuevos
    new_videos = filter_new_videos(videos, processed)
    
    if not new_videos:
        log(f"Todos los videos ya han sido procesados para {streamer['name']}")
        return {
            'streamer': streamer['name'],
            'videos_procesados': [],
            'mensaje': 'Sin videos nuevos'
        }
    
    # Limitar a MAX_VIDEOS_PER_STREAMER
    if len(new_videos) > MAX_VIDEOS_PER_STREAMER:
        log(f"Limitando a {MAX_VIDEOS_PER_STREAMER} videos nuevos (había {len(new_videos)})")
        new_videos = new_videos[:MAX_VIDEOS_PER_STREAMER]
    
    log(f"Procesando {len(new_videos)} videos nuevos para {streamer['name']}")
    
    resultados = []
    
    for i, video in enumerate(new_videos, 1):
        log(f"\n--- Video {i}/{len(new_videos)}: {video['title']} ---")
        
        # Descargar transcripción
        vtt_file = download_transcript(video['url'], video['id'], streamer_base)
        
        if vtt_file and vtt_file.exists():
            # Convertir a texto
            transcript = vtt_to_text(vtt_file)
            
            if transcript:
                log(f"Transcripción extraída: {len(transcript)} caracteres")
                
                # Guardar transcripción para procesamiento posterior
                transcript_file = streamer_base / f"{video['id']}_transcript.txt"
                with open(transcript_file, 'w', encoding='utf-8') as f:
                    f.write(transcript)
                
                resultados.append({
                    'video_id': video['id'],
                    'title': video['title'],
                    'transcript_file': str(transcript_file),
                    'transcript_length': len(transcript)
                })
                
                # Marcar como procesado
                save_processed_video(video['id'], video['title'])
                
                # Limpiar archivo .vtt
                vtt_file.unlink(missing_ok=True)
            else:
                log("Transcripción vacía, saltando video")
        else:
            log("No se pudo descargar transcripción, saltando video")
        
        # Pequeña pausa entre videos
        if i < len(new_videos):
            time.sleep(5)
    
    return {
        'streamer': streamer['name'],
        'videos_procesados': resultados,
        'mensaje': f'{len(resultados)} videos procesados exitosamente'
    }

def main():
    """Función principal del pipeline."""
    log("=== INICIANDO PIPELINE CONSOLIDADO ===")
    log(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    resultados_totales = []
    
    for i, streamer in enumerate(STREAMERS, 1):
        log(f"\n{'#'*60}")
        log(f"STREAMER {i}/{len(STREAMERS)}: {streamer['name']}")
        log(f"{'#'*60}")
        
        resultado = process_streamer(streamer)
        resultados_totales.append(resultado)
        
        # Esperar entre streamers para evitar rate limit
        if i < len(STREAMERS):
            log(f"\nEsperando {DELAY_BETWEEN_STREAMERS} segundos antes del siguiente streamer...")
            time.sleep(DELAY_BETWEEN_STREAMERS)
    
    log("\n=== PIPELINE COMPLETADO ===")
    log(f"Resultados: {json.dumps(resultados_totales, indent=2, ensure_ascii=False)}")
    
    # Guardar resultados para siguiente etapa
    results_file = BASE_DIR / "pipeline_results.json"
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(resultados_totales, f, indent=2, ensure_ascii=False)
    
    log(f"Resultados guardados en: {results_file}")
    
    return resultados_totales

if __name__ == "__main__":
    main()
