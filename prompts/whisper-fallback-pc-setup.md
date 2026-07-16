# Whisper Fallback — Configuración en PC Local

## Objetivo

Modificar `transcript_downloader.py` (PC local, Windows) para que cuando un video no tenga subtítulos automáticos, descargue el **audio** y lo suba al repositorio. Luego el VPS lo tomará, lo transcribirá con Whisper y guardará la transcripción.

---

## Archivo a modificar

**Ruta:** `C:/trading-knowledge-base/transcript_downloader.py`

---

## Cambios necesarios

### 1. Agregar constante AUDIOS_DIR

Al inicio del archivo, después de `STREAMERS`:

```python
STREAMERS = ["ArgenTrader", "ZCoinTV", "ScottFDX", "NovaTrader", "MambaFx", "PuntoDeEntrada"]
AUDIOS_DIR = BASE / "audios_pendientes"
```

### 2. Modificar la sección [3/4] — descarga de transcripciones

Localizar el bloque donde después de ejecutar `yt-dlp --write-auto-subs` se evalúa `result.returncode`. Actualmente hay dos caminos:

- **returncode == 0** (subtítulos encontrados) → procesa VTT → guarda .txt
- **returncode != 0** → log "❌ Error"

**Cambio:** Cuando `returncode != 0` o cuando no se encuentra ningún archivo de subtítulos (el `else` después del `for ext in`), en lugar de solo loguear, descargar el audio.

#### Código modificado (sección relevante):

```python
if result.returncode == 0:
    encontrado = False
    for ext in [".vtt", ".srt", ".json"]:
        files = list(destino.glob(f"{p['vid']}*{ext}"))
        if files:
            # ... (procesamiento actual del VTT a TXT, igual que antes) ...
            encontrado = True
            break
    if not encontrado:
        log(f"   ⚠ Sin subtítulos — descargando audio para Whisper...")
        _download_audio(p['vid'], p['streamer'], p['titulo'])
else:
    log(f"   ⚠ yt-dlp falló ({result.stderr[:60].strip()}) — descargando audio para Whisper...")
    _download_audio(p['vid'], p['streamer'], p['titulo'])
```

### 3. Agregar función `_download_audio`

Antes de `main()` o al final del archivo:

```python
def _download_audio(video_id, streamer, titulo=""):
    """Descarga el audio de un video que no tiene subtítulos."""
    AUDIOS_DIR.mkdir(parents=True, exist_ok=True)
    output_template = str(AUDIOS_DIR / f"{video_id}.%(ext)s")

    cmd = [YT_DLP,
           "-f", "bestaudio[ext=m4a]/bestaudio",
           "--output", output_template,
           "--quiet",
           "--no-embed-thumbnail",
           "--no-playlist",
           f"https://www.youtube.com/watch?v={video_id}"]
    if COOKIES.exists():
        cmd = [YT_DLP, "--cookies", str(COOKIES)] + cmd[1:]

    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        if r.returncode == 0:
            # Buscar el archivo descargado
            for f in AUDIOS_DIR.glob(f"{video_id}.*"):
                if f.suffix in [".m4a", ".webm", ".opus", ".mp3"]:
                    log(f"   ✅ Audio descargado: {f.name}")
                    # Guardar metadata para que el VPS sepa a qué streamer pertenece
                    meta_file = AUDIOS_DIR / f"{video_id}.meta"
                    meta_file.write_text(f"{streamer}|{titulo}", encoding="utf-8")
                    return
            log(f"   ⚠ Audio descargado pero no se encontró el archivo")
        else:
            log(f"   ❌ Error descargando audio: {r.stderr[:80].strip()}")
    except subprocess.TimeoutExpired:
        log(f"   ❌ Timeout descargando audio ({video_id})")
    except Exception as e:
        log(f"   ❌ Excepción: {e}")
```

### 4. Actualizar el commit para incluir audios

En la sección [4/4], después del `git add -A`, verificar si hay audios nuevos:

```python
# 4. Commit y push
log(f"\n[4/4] Subiendo {descargados} transcripción(es) y audios...")
git("add", "-A")

# Verificar si hay cambios concretos
r = git("diff", "--cached", "--quiet")
if r.returncode != 0:
    # Contar audios nuevos
    nuevos_audios = len(list(AUDIOS_DIR.glob("*.m4a"))) + len(list(AUDIOS_DIR.glob("*.webm")))
    fecha = datetime.now().strftime("%Y-%m-%d")
    msg = f"[transcripciones] {fecha} - {descargados} transcripciones"
    if nuevos_audios:
        msg += f", {nuevos_audios} audios p/Whisper"
    git("commit", "-m", msg)
    git("push")
    log(f"✅ Push exitoso — {descargados} transcripciones, {nuevos_audios} audios")
else:
    log("📭 Sin cambios para commit")
```

### 5. Actualizar STREAMERS

Agregar `"PuntoDeEntrada"` a la lista si no está:

```python
STREAMERS = ["ArgenTrader", "ZCoinTV", "ScottFDX", "NovaTrader", "MambaFx", "PuntoDeEntrada"]
```

---

## Estructura de archivos resultante

```
C:/trading-knowledge-base/
├── processed_videos.txt
├── transcript_downloader.py
├── streamers/
│   ├── ArgenTrader/transcripciones/
│   ├── ZCoinTV/transcripciones/
│   └── ...
└── audios_pendientes/          ← NUEVO
    ├── NE51v_uACng.m4a         ← audios sin transcripción
    ├── NE51v_uACng.meta        ← metadata: streamer|título
    ├── nNGPWcJAJSc.m4a
    └── nNGPWcJAJSc.meta
```

---

## Notas importantes

- El audio se descarga en formato **m4a** (AAC) — es el más compatible con Whisper
- Cada audio lleva un archivo `.meta` adjunto con el nombre del streamer y título
- El VPS usará `faster-whisper` para transcribir y dejará el `.txt` con la nota:
  ```
  # Transcripción generada por Whisper (IA) — video sin subtítulos automáticos
  ```
- Después de transcribir, el VPS **eliminará** el `.m4a` y `.meta`
- El pipeline sigue funcionando igual para videos que SÍ tienen subtítulos

## Verificación

Después de los cambios, ejecuta manualmente:

```powershell
cd C:\trading-knowledge-base
python transcript_downloader.py
```

Y verifica que:
1. Los videos sin subtítulos (ej: PuntoDeEntrada) generen archivos `.m4a` en `audios_pendientes/`
2. Los videos con subtítulos sigan funcionando igual
3. Se haga commit y push correctamente
