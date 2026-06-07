#!/usr/bin/env python3
"""
Extrae videos de canales de YouTube usando curl + parsing HTML
Evita bloqueos de yt-dlp usando headers de navegador real
"""
import subprocess
import json
import re
from datetime import datetime
from pathlib import Path

def get_video_ids(channel_url, max_videos=10):
    """Extrae IDs de videos de un canal usando curl"""
    cmd = [
        'curl', '-s',
        '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        channel_url
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        html = result.stdout
        
        # Buscar videoIds en el HTML
        video_ids = re.findall(r'"videoId":"([^"]+)"', html)
        
        # Eliminar duplicados manteniendo orden
        seen = set()
        unique_ids = []
        for vid in video_ids:
            if vid not in seen:
                seen.add(vid)
                unique_ids.append(vid)
                
        return unique_ids[:max_videos]
    except Exception as e:
        print(f"Error extrayendo de {channel_url}: {e}")
        return []

def get_video_info(video_id):
    """Obtiene título y fecha del video"""
    cmd = [
        'curl', '-s',
        '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        f'https://www.youtube.com/watch?v={video_id}'
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        html = result.stdout
        
        # Extraer título
        title_match = re.search(r'"title":"([^"]+)"', html)
        title = title_match.group(1) if title_match else "Unknown Title"
        
        # Fecha aproximada (hoy)
        date = datetime.now().strftime('%Y-%m-%d')
        
        return {
            'id': video_id,
            'title': title,
            'date': date
        }
    except Exception as e:
        print(f"Error obteniendo info de {video_id}: {e}")
        return None

def load_processed_videos(filepath):
    """Carga videos ya procesados"""
    processed = set()
    path = Path(filepath)
    
    if path.exists():
        with open(path, 'r') as f:
            for line in f:
                parts = line.strip().split('|')
                if parts:
                    processed.add(parts[0])  # El ID está primero
                    
    return processed

def save_processed_video(filepath, video_id, date, title):
    """Guarda video como procesado"""
    with open(filepath, 'a') as f:
        f.write(f"{video_id}|{date}|{title}\n")

if __name__ == '__main__':
    # Probar con ArgenTrader
    channel_url = "https://www.youtube.com/@ArgenTraderr/videos"
    
    print(f"Extrayendo videos de {channel_url}...")
    video_ids = get_video_ids(channel_url, max_videos=10)
    
    print(f"Encontrados {len(video_ids)} videos:")
    for vid in video_ids[:5]:
        print(f"  - {vid}")
    
    # Verificar cuáles son nuevos
    processed = load_processed_videos('/home/ubuntu/proyects/trading/processed_videos.txt')
    new_videos = [vid for vid in video_ids if vid not in processed]
    
    print(f"\nVideos nuevos: {len(new_videos)}")
    for vid in new_videos[:3]:
        print(f"  - {vid}")
