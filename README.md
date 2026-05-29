# 🧠 Trading Knowledge Base

Base de conocimiento de trading automatizada — extrae, resume y organiza aprendizajes de streamers de trading en YouTube. Este repositorio es el **Layer 3 (Capa 3)** de un sistema de 3 capas que alimenta un futuro software de trading.

---

## 🎯 Objetivo

Convertir cientos de horas de contenido de trading en YouTube en una base de conocimiento estructurada, versionada y consultable. Cada concepto, setup, herramienta y regla queda documentado en archivos `.md` organizados por tema. Esto será el **blueprint** para construir un software de trading propio (Fase 3 del roadmap).

---

## 📡 Streamer Monitoreado

| Streamer | Canal | Idioma | Enfoque | Horario de stream |
|----------|-------|--------|---------|-------------------|
| **ArgenTrader** | [@ArgenTraderr](https://www.youtube.com/@ArgenTraderr) | Español (argentino) | ICT/SMC, cripto, futuros, grid bots, liquidez, análisis técnico | ~4:00 PM UTC-6 |

---

## 🏗️ Estrategia de 3 Capas

```
CAPA 1: Resumen diario (Telegram)
  └─ Resumen formateado que llega cada noche al usuario
      ↓
CAPA 2: Memoria etiquetada (Hermes memory)
  └─ Conceptos guardados con tags [ArgenTrader] CATEGORÍA:
      ↓
CAPA 3: Base de conocimiento (este repositorio)
  └─ Archivos .md organizados por streamer/tema, versionados en Git
      ↓
  🎯 FASE 3: Software de trading — usa esta base como blueprint
```

**Este repositorio es la Capa 3.** Las otras capas viven dentro del agente Hermes que lo genera.

---

## 📁 Estructura del Repositorio

```
trading-knowledge-base/
├── README.md                          ← Este archivo
├── .gitignore
├── processed_videos.txt               ← Registro de videos ya procesados
├── streamers/
│   └── argentrader/
│       ├── conceptos/                 ← Conceptos teóricos explicados
│       │   ├── liquidez.md            │  Pools, barridos, herramientas
│       │   ├── estructura-smc.md      │  BOS, ChoCh, Liquidity Grab
│       │   ├── volumen.md             │  Vertical + Perfil, POC, HVN, LVN
│       │   ├── fibonacci.md           │  0.382/0.618, fractal operativo
│       │   ├── rsi.md                 │  Divergencias, zonas extremas
│       │   ├── apalancamiento.md      │  Calk, modo aislado, gestión riesgo
│       │   └── grid-bots.md           │  Pionex, Grid Profit, break even
│       ├── setups/                    ← Estrategias con criterios concretos
│       │   ├── liquidity-sweep.md     │  Entrada tras barrido de liquidez
│       │   ├── fvg-entry.md           │  Entrada en Fair Value Gap
│       │   ├── estrategia-apertura-caja.md │  Ruptura de rango de apertura
│       │   └── volumen-profile-entry.md    │  Entrada con perfil de volumen
│       ├── herramientas/              ← Tools, plataformas, indicadores
│       │   ├── tradingview.md         │  Indicadores y configuraciones
│       │   ├── pionex.md              │  Exchange con bots de trading
│       │   └── coinglass-tdifferent-tensorchart.md │  Herramientas de liquidez
│       └── reglas.md                  ← Principios operativos compilados
└── comparativas/                      ← Comparaciones cross-streamer (futuro)
```

---

## 🤖 Pipeline Automatizado (Cron)

El conocimiento se genera automáticamente mediante **Hermes Agent** corriendo en Windows:

```
        4 PM (-6)              8 PM (-6)                   9 PM (-6)
    ┌──────────────┐       ┌──────────────┐           ┌──────────────┐
    │ ArgenTrader  │       │  Cron        │           │  Watchdog    │
    │ hace directo │ ──→  │  procesa VOD │ ──→ 📱   │  verifica    │
    │ 1.5 - 3 hrs  │       │  + push git  │           │  estado      │
    └──────────────┘       └──────────────┘           └──────────────┘
```

### Cron Principal: `ArgenTrader Daily Intel`
- **ID**: `453d0d9976d2`
- **Schedule**: `0 20 * * *` (8:00 PM UTC-6, todos los días)
- **Skills**: `trading-streamer-intel` + `youtube-content`
- **Provider**: DeepSeek (el que estaba activo al crearse)
- **Delivery**: Telegram (al chat del usuario)

**Flujo de cada ejecución:**
1. `yt-dlp` obtiene últimos 10 videos del canal
2. Compara IDs contra `processed_videos.txt`
3. Para cada video nuevo → extrae transcripción (español) → resume conceptos
4. Guarda en memoria de Hermes (Capa 2)
5. Escribe/actualiza archivos `.md` (Capa 3 — este repositorio)
6. `git add -A && git commit && git push`
7. Entrega resumen formateado a Telegram (Capa 1)
8. Actualiza `processed_videos.txt`

### Watchdog: `ArgenTrader Watchdog`
- **ID**: `eb9c3cc5a7c2`
- **Schedule**: `0 21 * * *` (9:00 PM UTC-6, 1h después del principal)
- **Script**: `scripts/check_trading_cron.py`
- **Sin agente** (`no_agent: true`) — solo ejecuta el script
- **Delivery**: Solo envía mensaje si detecta `(FAILED)` en los últimos 2 días
- Si el cron principal funcionó → silencio total

---

## 🔧 Cómo Trabaja un Agente con Este Repositorio

### Al procesar un video nuevo

1. **Leer** `processed_videos.txt` para saber qué videos ya existen
2. **Extraer transcripción** con `fetch_transcript.py` (del skill `youtube-content`)
3. **Resumir** extrayendo: conceptos, setups, herramientas, errores, reglas, psicología
4. **Escribir/actualizar** los `.md` correspondientes en `streamers/<nombre>/`
5. **Commit** con formato: `[StreamerName] YYYY-MM-DD — Breve descripción`
6. **Push** al remote `origin`

### Convenciones de archivos

- **Lenguaje**: Español
- **Cada archivo** `.md` tiene estructura: Definición → Fuente → Conceptos Clave → Reglas Operativas → Frase Destacada
- **IDs de video** se registran en `processed_videos.txt` como: `VIDEO_ID|YYYY-MM-DD|TITLE`
- **Formato de commit**: `[StreamerName] YYYY-MM-DD — What was learned`

### Al agregar un nuevo streamer

Crear `streamers/<nombre>/` con la misma estructura de subdirectorios:
```
streamers/<nombre>/
├── conceptos/
├── setups/
├── herramientas/
└── reglas.md
```

Registrar el canal en el skill `trading-streamer-intel`, crear cron job, y listo.

---

## 🔑 Configuración SSH

El remote de Git usa SSH con la clave personal del usuario:

```
Remote:  git@github-personal:jsarmiento-dev/trading-knowledge-base.git
Host:    github-personal → IdentityFile ~/.ssh/id_ed25519
```

Para que el cron pueda hacer push automático, el agente SSH debe estar corriendo con la clave cargada.

---

## 📋 Skill de Hermes

Este repositorio es mantenido por el skill **`trading-streamer-intel`** (v1.2.0):

- **Ubicación**: `~/AppData/Local/hermes/skills/trading/trading-streamer-intel/SKILL.md`
- **Requiere**: `youtube-content` skill, `yt-dlp`, `youtube-transcript-api`
- **Script de transcripción**: `skills/media/youtube-content/scripts/fetch_transcript.py`

---

## 🚀 Roadmap

| Fase | Estado | Descripción |
|------|--------|-------------|
| **Fase 1** | ✅ Activo | Pipeline automático — 1 streamer, cron diario, watchdog |
| **Fase 2** | 🔜 Planeado | +2 streamers, comparativas cross-streamer, conceptos verificados/refutados |
| **Fase 3** | 🔮 Futuro | Software de trading que usa esta base como motor de conocimiento |

---

## ⚠️ Pitfalls Conocidos

- **Transcripts de VODs**: YouTube tarda ~2-3h tras el directo en generar subtítulos → cron a 8 PM
- **Memoria no disponible en cron**: el `memory` tool puede fallar en entornos cron → los `.md` son el fallback
- **Timeout de transcripción**: videos de 3h pueden tardar → chunking de 40K chars con 2K overlap
- **Network errors**: si el cron falla por conexión, el watchdog alerta a las 9 PM
- **Git push sin remote**: si el remote no está configurado, el commit local igual preserva el conocimiento

---

*Última actualización: 2026-05-29*
*Repositorio mantenido por Hermes Agent (usuario: Jesús Sarmiento)*
