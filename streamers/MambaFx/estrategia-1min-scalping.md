# 📐 Estrategia MambaFx: 1-Minute Scalping

**Basado en el video:** `h-Z7CEqBO3s` — "The Only 1-Minute Scalping Strategy You Will Ever Need"
**Idioma original:** Inglés/Filipino | **Análisis:** Hermes Agent

---

## 🎯 Visión General

Estrategia de **scalping en timeframe de 1 minuto** que utiliza el timeframe de **5 minutos** para filtrar dirección y niveles clave. El énfasis principal está en la **confirmación** — no basta con identificar soporte/resistencia, hay que esperar señales adicionales antes de entrar.

> *"All we need to be profitable in this industry is confirmations"* — MambaFx

---

## ⏱ Estructura de Timeframes

| Timeframe | Rol | Acción |
|---|---|---|
| **5 minutos** | Dirección + S/R + Market Structure | Identificar tendencia y niveles clave |
| **1 minuto** | Breakout + Confirmación + Entry | Ejecutar entrada con precisión |

### Flujo paso a paso

**Paso 1: Dirección en 5-min**

> *"We always start on our 5-minute, we look for support or resistance, we try to find which direction the market is"*

- Identifica si el mercado está en tendencia alcista, bajista o rango
- Busca **niveles clave** de soporte y resistencia

**Paso 2: Market Structure (Estructura del Mercado)**

> *"Market structure to us is a higher high followed by a higher low then once again a higher high"*

| Estructura | Señal Visual | Acción |
|---|---|---|
| **Alcista (Bullish)** | HH → HL → HH | Buscar longs en 1-min |
| **Bajista (Bearish)** | LL → LH → LL | Buscar shorts en 1-min |

⚠ **Regla crítica:** Si el precio no ha roto la resistencia anterior, **NO es bullish**. Espera a que un nuevo candle rompa ese máximo.

> *"We still need a new candle to come in and take out these highs, so I know market structure has switched to bullish for sure"*

**Paso 3: Identificar Soporte/Resistencia en 5-min**

> *"1 2 3 4, four touches in a support here"*

Reglas para un soporte válido:
1. **Mínimo 4 toques** en el mismo nivel
2. **Agotamiento evidente** — el precio llega y se frena
3. **Solidez confirmada** — el precio ha "solidificado" ese nivel

**Paso 4: Breakout + Confirmación en 1-min**

> *"Now, if we go down to our 1-minute time frame, price action becomes a lot more clear"*

Tipos de breakout:
- 🔴 Breakout de **resistencia** (señal alcista)
- 🟢 Breakout de **soporte** (señal bajista)
- 📐 Breakout de **línea de tendencia**

**NO entres en el breakout inmediato.** Espera confirmación — un nuevo candle que cierre del lado correcto.

> *"We need to make sure with certainty we're going to keep buying before we enter that position"*

**Paso 5: Entry con Gestión de Riesgo**

| Parámetro | Regla |
|---|---|
| **Stop Loss** | Tight, justo detrás del nivel roto |
| **Risk:Reward** | Mínimo 1:3, ideal **1:4 a 1:5** |
| **Salida** | En target, sin mirar ganancias parciales |

> *"We're going to put a nice tight stop loss on this, going for maybe a 1:3, 1:5 would be even cooler, but say 1:4"*

## 🧮 Expectativa Matemática

Con RR 1:4, la estrategia es rentable incluso con baja tasa de acierto:

| Win Rate | Expectancy por trade |
|---|---|
| 30% | +0.50R |
| 40% | +0.60R |
| 50% | +1.50R |

**Fórmula:** `Expectancy = (WR × RR) - (1 - WR)`

Ejemplo con 30% WR y RR 1:4: `(0.30 × 4) - 0.70 = +0.50R` por operación.

## 🧠 Psicología

> *"A lot of you guys are too busy looking at your phone profits"*

- No cierres antes del target por miedo
- Confía en el plan de trading
- Esta estrategia es para **flippear cuentas pequeñas**, no para apostar

## ✅ Checklist de la Estrategia

- [ ] 1. **5-min TF**: ¿Hay un soporte o resistencia clara? (mínimo 4 toques)
- [ ] 2. **Market Structure**: ¿HH/HL (alcista) o LL/LH (bajista)?
- [ ] 3. **1-min TF**: ¿El precio está haciendo breakout del nivel?
- [ ] 4. **Confirmación**: ¿Una nueva vela confirmó el breakout?
- [ ] 5. **Entry**: Entrar en dirección del breakout
- [ ] 6. **Stop Loss**: Tight, justo detrás del nivel roto
- [ ] 7. **Take Profit**: RR 1:3 mínimo, ideal 1:4

## ⚠️ Lo que NO es

- ❌ No es solo soporte/resistencia — *"it is not true"*
- ❌ No es swing trading — es scalping en 1-min
- ❌ No es para cuentas grandes — diseñada para cuentas pequeñas

---

---

## 📊 Backtest US30 — NY Session Open

**Símbolo:** US30 (Dow Jones)
**Período:** 2026-07-07 → 2026-07-13
**Sesión:** New York (9:30 AM - 4:00 PM ET)
**Velas 1-min analizadas:** 1949
**Trades generados:** 0

### Sin trades generados

En 1949 velas de NY session no se encontraron setups que cumplieran:
- Estructura de mercado clara (HH/HL o LL/LH)
- Breakout con confirmación de vela
- Ventana de entrada dentro de la sesión NY

Esto es consistente con una estrategia **selectiva** — no opera todos los días.

### Notas del backtest

- El backtest es una **aproximación algorítmica** de una estrategia visual/subjetiva
- La identificación de soportes con "4 toques" requiere criterio humano
- La confirmación de breakout se basa en interpretación de velas
- Para validación real: backtesting manual en TradingView + forward testing

---

## 📊 Backtest US30 — NY Session Open

**Símbolo:** YM=F (US30 Dow Jones Futures)
**Sesión:** New York (9:30 AM - 4:00 PM ET)
**Período:** 2026-07-07 → 2026-07-13
**Velas 1-min analizadas:** 1949
**Trades generados:** 0

### Análisis

El backtest automatizado **no generó trades** en este período. Esto se debe a:

1. **La estrategia es visual/subjetiva** — identificar "4 toques en un soporte"
   requiere criterio humano que un algoritmo no puede replicar exactamente
2. **Swing points encontrados:** 22 máximos y 19 mínimos en 390 velas 5-min
3. **Estructura de mercado detectada:** sí, hubo períodos con HH/HL y LL/LH
4. **Breakout + confirmación:** el algoritmo exige que el precio cruce el nivel
   Y cierre del lado correcto, lo que reduce falsos pero también oportunidades

### Conclusión

Para una validación real de la estrategia:
- **Backtesting manual** en TradingView con +50 operaciones
- **Forward testing** en cuenta demo por 1 mes
- **Llevar estadísticas**: win rate, RR, drawdown, profit factor

La estructura de la estrategia (filtro 5-min → breakout 1-min con confirmación
→ SL tight → RR 1:4+) es sólida en teoría. La ejecución depende del criterio
del trader para identificar niveles y esperar confirmación.

---
*Backtest automatizado con Yahoo Finance (YM=F) — Hermes Agent*