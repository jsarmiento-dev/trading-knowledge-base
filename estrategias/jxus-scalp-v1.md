# ⚡ JXUS-SCALP v1.0

**Estrategia propia de 1-Minute Scalping**
*Diseñada por Jesús Sarmiento & Hermes Agent — Julio 2026*

---

## 🎯 Filosofía

JXUS-Scalp no es una copia de una sola estrategia. Es una **fusión de lo mejor**
de cada escuela de trading analizada, seleccionada para un objetivo específico:
**pasar challenges de prop firms** y **flippear cuentas pequeñas** en la sesión de NY.

### Componentes por escuela

| Fuente | Qué tomamos | Por qué |
|---|---|---|
| **MambaFx** | RR 1:4, tight SL, simplicidad | Disciplina de riesgo + ejecución limpia |
| **ICT/SMC** | Market Structure, FVG, Liquidity Sweep | Evitar fakeouts + entradas precisas |
| **ProRealAlgos** | Touch & Turn | Operar rangos laterales |
| **Pro Trading School** | Drawing S/R, confirmación | Claridad visual |
| **TTrades** | Fractal multi-TF, scaling | Flexibilidad en tendencias fuertes |

---
## 📐 LOS 3 SETUPS DE JXUS-SCALP

JXUS-Scalp tiene **3 configuraciones** que cubren todas las condiciones del mercado:

| Setup | Mercado | Inspiración |
|---|---|---|
| **JXUS Momentum** 🚀 | Tendencia clara (HH/HL o LL/LH) | ICT BOS + MambaFx |
| **JXUS Touch** 🖐️ | Rango lateral (sin estructura) | ProRealAlgos Touch & Turn |
| **JXUS Fractal** 🔮 | Tendencia fuerte + corrección | TTrades + ICT OTE |

---

## ⏱ VENTANAS DE OPERACIÓN (Time-based Bias)

Tomado de ICT Silver Bullet. Solo operar en estas horas (zona NY):

| Ventana | Hora ET | Qué buscar | Actividad |
|---|---|---|---|
| **NY Open** 🟢 | 9:30 - 11:00 AM | JXUS Momentum | ✅ Máxima volatilidad |
| **NY Lunch** 🟡 | 11:00 - 2:00 PM | JXUS Touch (rangos) | ⚠ Media |
| **NY Close** 🟢 | 2:00 - 4:00 PM | JXUS Fractal | ✅ Alta volatilidad |
| **Fuera de NY** ❌ | Cualquier otra | NO OPERAR | Bloqueado |

**Regla de oro:** Si no es NY open o NY close, no operes JXUS-Scalp.
Las probabilidades caen significativamente fuera de estas ventanas.

---
## 📊 ACTIVOS RECOMENDADOS

| Activo | Símbolo | Spread | Ideal para |
|---|---|---|---|
| **US30 (Dow)** | YM=F | ~1-2 pts | JXUS Momentum |
| **Nasdaq** | NQ=F | ~1-2 pts | JXUS Momentum |
| **S&P 500** | ES=F | ~0.25 pts | JXUS Touch |
| **Gold** | GC=F | ~0.1 pts | JXUS Fractal |

---
## 🚀 SETUP 1: JXUS Momentum

**Para mercados en tendencia (85% de las operaciones deberían ser este setup)**

### Filtro de dirección (5-min)

1. Identificar **estructura de mercado** en 5-min:
   - **Alcista:** Higher High → Higher Low confirmado
   - **Bajista:** Lower Low → Lower High confirmado
2. Si la estructura NO es clara → saltar, buscar JXUS Touch

### Identificar Liquidity Sweep (ICT)

Antes del breakout real, el mercado suele:
1. **Barrer stops** por debajo del mínimo anterior (para luego ir alcista)
2. **Barrer stops** por encima del máximo anterior (para luego ir bajista)

> **No entres en el primer breakout. Espera el sweep.**

### Detectar el FVG (Fair Value Gap)

Después del sweep, busca un **FVG** en 1-min:
- 3 velas consecutivas donde la vela del medio deja un hueco de precio
- La sombra de la 1ra vela NO se superpone con la sombra de la 3ra

### Entry (1-min)

| Condición | LONG | SHORT |
|---|---|---|
| Sweep | Liquidity sweep de mínimo | Liquidity sweep de máximo |
| FVG | FVG alcista presente | FVG bajista presente |
| Displacement | Vela grande alcista | Vela grande bajista |
| Confirmación | Cierre por encima del FVG | Cierre por debajo del FVG |

**Entry:** Límite de compra/venta en el FVG (ICT OTE)
**SL:** Justo debajo del mínimo del sweep (para LONG) o arriba del máximo (SHORT)
**TP:** RR 1:4 mínimo

### Diagrama visual
```
LONG SETUP:

Precio
  ↑
  |     ╔══════ FVG ══════╗
  |     ║                 ║
  |     ║    ▼ ENTRY     ║
  |     ║                 ║
  |     ╚═════════════════╝
  |          ↑
  |          │ Sweep de mínimo
  |          │ (liquidity grab)
  |          ●
  |          │
  |     SL aquí (justo debajo)
  ├──────────────────────────► Tiempo
```

---
## 🖐️ SETUP 2: JXUS Touch

**Para mercados en rango lateral (cuando no hay estructura clara)**

Inspirado en ProRealAlgos "Touch and Turn".

### Identificar el rango

1. Dibujar **mínimo 2 toques** en soporte y **mínimo 2 toques** en resistencia
2. El rango debe tener al menos 15 velas 5-min de ancho (~75 min)
3. Si el rango es muy estrecho (< 0.2% del precio) → saltar

### Entry

| Condición | LONG (en soporte) | SHORT (en resistencia) |
|---|---|---|
| Toque | Precio toca el soporte | Precio toca la resistencia |
| Vela de rechazo | Sombra larga inferior | Sombra larga superior |
| Confirmación | Siguiente vela cierra alcista | Siguiente vela cierra bajista |

**Entry:** En la apertura de la 2da vela después del toque
**SL:** 0.1% por debajo del soporte (LONG) o 0.1% arriba de la resistencia (SHORT)
**TP:** Hasta el otro extremo del rango (1:1) o RR 1:2 si el rango lo permite

### Diferencia con JXUS Momentum

- JXUS Momentum opera **a favor** de la estructura (breakout)
- JXUS Touch opera **en contra** de los extremos del rango (reversión)
- No mezclar. Si hay estructura → Momentum. Si no hay → Touch.

---
## 🔮 SETUP 3: JXUS Fractal

**Para tendencias fuertes con corrección**

Inspirado en TTrades Fractal Model + ICT OTE.

### Condiciones

1. Tendencia clara en 15-min (HH/HL o LL/LH sostenido)
2. Corrección de al menos 3 velas en 1-min
3. Corrección dentro de la zona OTE (Fibonacci 0.618-0.79)

### Entry

| Condición | LONG | SHORT |
|---|---|---|
| Tendencia 15-min | Alcista | Bajista |
| Corrección | Baja al 0.618-0.79 Fib | Sube al 0.618-0.79 Fib |
| Señal | Cierre alcista en zona OTE | Cierre bajista en zona OTE |

**Entry:** Límite en zona OTE con confirmación de vela
**SL:** Por debajo del mínimo de corrección (LONG) o arriba del máximo (SHORT)
**TP:** RR 1:4 o anterior High/Low de tendencia (el que llegue primero)

---
## 📋 REGLAS DE GESTIÓN DE RIESGO

### Por operación

| Parámetro | Regla |
|---|---|
| **Riesgo por trade** | 0.5% - 1% de la cuenta |
| **RR mínimo** | 1:3 (ideal 1:4) |
| **Máximo drawdown diario** | 3% |
| **Máximo trades por día** | 5 |
| **Mínimo trades por día** | 0 (no forzar) |

### Gestión de la operación

1. **SL al breakeven** cuando el precio alcanza RR 1:1
2. **Trailing stop** de 0.1% después de RR 1:2
3. **Salir 50% en TP1 (RR 1:2)**, dejar 50% correr a TP2 (RR 1:4)

### Reglas de disciplina

- ❌ No operar fuera de ventanas NY
- ❌ No operar durante noticias (NFP, FOMC, CPI)
- ❌ No operar si perdiste 3 operaciones seguidas (stop diario)
- ❌ No operar si no hay setup claro (no forzar)
- ✅ Si no estás seguro → NO ENTRES

---
## ✅ CHECKLIST PRE-ENTRADA (imprimir y tener al lado)

### JXUS Momentum:
- [ ] ¿Es NY Open (9:30-11:00) o NY Close (14:00-16:00)?
- [ ] ¿Hay estructura clara en 5-min (HH/HL o LL/LH)?
- [ ] ¿Hubo liquidity sweep del mínimo/máximo anterior?
- [ ] ¿Hay un FVG claro en 1-min?
- [ ] ¿Hay displacement (vela grande en dirección del trade)?
- [ ] ¿El SL cabe dentro del RR 1:4?

### JXUS Touch:
- [ ] ¿Es NY Lunch (11:00-14:00)?
- [ ] ¿Hay rango claro con 2+ toques en cada lado?
- [ ] ¿Precio tocó el extremo con rechazo (sombra)?
- [ ] ¿Siguiente vela confirmó la dirección?
- [ ] ¿El rango es lo suficientemente ancho?

### JXUS Fractal:
- [ ] ¿Tendencia clara en 15-min?
- [ ] ¿Corrección de al menos 3 velas en 1-min?
- [ ] ¿Corrección llegó a zona OTE (0.618-0.79)?
- [ ] ¿Confirmación de vela en la zona?

---
## 📊 BACKTESTING

---

## 📊 BACKTEST RESULTADOS PRELIMINARES

**Período:** 2026-07-07 → 2026-07-13
**Símbolo:** YM=F (US30 Dow Jones Futures)
**Sesión:** NY (9:30-16:00 ET)
**Velas 1-min:** 1949

### TOUCH
| Métrica | Valor |
|---|---|
| Trades | 5 |
| Win Rate | 20.0% |
| Total R | -1.88 |
| Avg RR | -0.38 |

| # | Dir | Entry | Exit | P&L | RR |
|---|---|---|---|---|---|
| 1 | LONG | $53,140 | $53,263 | $+123 | 2.12 |
| 2 | LONG | $52,661 | $52,570 | $-91 | -1.0 |
| 3 | LONG | $52,579 | $52,499 | $-80 | -1.0 |
| 4 | LONG | $52,511 | $52,444 | $-67 | -1.0 |
| 5 | LONG | $52,442 | $52,371 | $-71 | -1.0 |

---
*Backtest automatizado con Yahoo Finance (YM=F) — Julio 2026*