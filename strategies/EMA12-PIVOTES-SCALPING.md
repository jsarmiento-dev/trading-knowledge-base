# ESTRATEGIA DE SCALPING EMA 12 + PIVOTES
## Documentación Técnica Completa — Basada en ZCoinTV

**Creado por:** Freqtrade Trading Bot (Jesús Sarmiento)  
**Fecha de consolidación:** 2026-06-10  
**Fuente principal:** ZCoinTV ( canal de YouTube )  
**Documentos base consultados:**
- `setups/oro-scalping-ema12-pivotes.md`
- `setups/sp500-scalping.md`
- `setups/volume-profile-scalping.md`
- `herramientas/vwap.md`
- `herramientas/scalping-bitget-altcoins.md`
- `conceptos/medias-moviles.md`
- `conceptos/errores-comunes-trading.md`
- `conceptos/gestion-riesgo-bots.md`
- `conceptos/risk-reward-ratio.md`
- `conceptos/patrones-velas-japonesas.md`
- `conceptos/analisis-bitcoin-10min.md`
- `herramientas/break-even.md`

---

## 1. DESCRIPCión GENERAL

### 1.1 Qué es esta estrategia
Sistema de scalping diseñado para temporalidad de **5 minutos** que combina tres herramientas principales:
- **EMA 12** como filtro de tendencia y señal de entrada
- **Pivotes de precio** como niveles de soporte/resistencia dinámicos
- **Volume Profile** como confirmación adicional (opcional pero recomendado)

### 1.2 Principios rectores (según ZCoinTV)
> "Nunca usar medias móviles como señal única — siempre requieren confluencia"  
> — ZCoinTV, documento `conceptos/medias-moviles.md`

> "El bot no tiene criterio, el bot maneja cuestiones mecánicas. Somos nosotros los que tenemos que aportar esos criterios."  
> — ZCoinTV, documento `conceptos/gestion-riesgo-bots.md`

### 1.3 Activos recomendados
- **Alta liquidez:** BTC/USDT, ETH/USDT (menor volatilidad, spreads ajustados)
- **Mid-caps:** BNB/USDT, SOL/USDT (mayor volatilidad, requiere stops más amplios)
- **Evitar:** Low-caps, memecoins (volatilidad extrema, riesgo de mechazos)

**Nota:** ZCoinTV recomienda: "practicar SIEMPRE en demo antes de usar dinero real (mínimo 2-3 meses de consistencia)" — `conceptos/errores-comunes-trading.md`

---

## 2. COMPONENTES TÉCNICOS

### 2.1 EMA 12 (Media Móvil Exponencial de 12 periodos)

**Qué es:** Más reactiva y rápida que SMA. Da más peso a las velas recientes.  
**Por qué 12:** Cubre la última hora de negociación (12 velas × 5 min).  
**Configuración visual:**
- Velas huecas + EMA como línea continua
- Color: preferiblemente azul claro o verde según preferencia

**Regla de uso:**
- Precio **CERRADO** por **encima** de EMA 12 → condición alcista (largos)
- Precio **CERRADO** por **debajo** de EMA 12 → condición bajista (cortos)

**⚠️ CRÍTICO: El precio cierra, no toca. Se requiere un CIERRE completo.**

### 2.2 Pivotes de precio

**Qué son:** Mínimos y máximos locales donde el precio ha rebotado. En TradingView se detectan con el indicador "Pivot Points" o manualmente identificando extremos locales.

**Tipos relevantes para esta estrategia:**
- **M"nimo local** = pivote inferior → soporte → para LARGOS
- **Máximo local** = pivote superior → resistencia → para CORTOS

### 2.3 Volume Profile (complementario, no obligatorio)

**Función:** Actúa como filtro adicional de confluencia.

| Elemento | Función en largos | Función en cortos |
|----------|-----------------|-------------------|
| **HVN** | Actúa como soporte | Actúa como resistencia |
| **LVN** | Zona rápida, ideal para stops | Zona rápida, ideal para stops |
| **POC** | Imán de precio (TP1) | Imán de precio (TP1) |

---

## 3. CONDICIONES DE ENTRADA DETALLADAS

### 3.1 Para LARGOS (Long)

**Paso 1 — Contexto (temporalidad superior):**
1. Analizar temporalidad de 1h o 4h (método top-down)
2. Confirmar dirección general alcista
3. Identificar soportes/resistencias horizontales clave
4. Revisar RSI(14) en temporalidad superior: buscar que NO esté sobrecomprado (>70)

**Paso 2 — Identificación en 5 minutos:**
5. Identificar **pivote inferior** (mínimo local) reciente
6. Esperar formación de vela que se cierre por **encima** de la EMA 12
7. **Confirmación recomendada:**
   - RSI(14) saliendo de sobreventa (subiendo de <30)
   - Volumen creciente en vela de entrada
   - Patrón de reversión alcista (Martillo, Envolvente Alcista — `conceptos/patrones-velas-japonesas.md`)

**Paso 3 — Precisión de entrada:**
8. **Orden LIMIT** en el cierre de la vela con la EMA 12
9. No entrar por market — esperar confirmación del cierre
10. Si el precio regresa sin cierre por encima, NO entrar

### 3.2 Para CORTOS (Short)

**Paso 1 — Contexto (temporalidad superior):**
1. Analizar temporalidad de 1h o 4h (método top-down)
2. Confirmar dirección general bajista
3. Identificar soportes/resistencias horizontales clave
4. Revisar RSI(14): buscar que NO esté sobrevendido (<30)

**Paso 2 — Identificación en 5 minutos:**
5. Identificar **pivote superior** (máximo local) reciente
6. Esperar formación de vela que se cierre por **debajo** de la EMA 12
7. **Confirmación recomendada:**
   - RSI(14) saliendo de sobrecompra (bajando de >70)
   - Volumen creciente en vela de entrada
   - Patrón de reversión bajista (Estrella Fugaz, Envolvente Bajista)

**Paso 3 — Precisión de entrada:**
8. **Orden LIMIT** en el cierre de la vela con la EMA 12
9. No entrar por market — esperar confirmación del cierre
10. Si el precio regresa sin cierre por debajo, NO entrar

---

## 4. GESTIÓN DE LA OPERACIÓN (TRADE MANAGEMENT)

### 4.1 Definición de Stop Loss (SL)

**Ubicación del SL (según ZCoinTV):**
- **Largos:** En el extremo del pivote inferior, con margen adicional de 0.1-0.2% por spread
- **Cortos:** En el extremo del pivote superior, con margen adicional de 0.1-0.2%
- **NO ajustar exactamente al pivote:** Dejar un colchón para evitar que el mechazo lo toque

**Ejemplo numérico:**
```
Pivote inferior = 60,200 USDT
Spread estimado = 0.15%
SL = 60,200 - (0.15% × 60,200) = 60,200 - 90.3 = 60,109.7 USDT
```

### 4.2 Definición de Take Profit (TP)

**Gestión en DOS TRAMOS (según ZCoinTV):**

| Tramo | Porcentaje posición | Target | Acción |
|-------|-------------------|--------|--------|
| **TP1** | 75% de la posición | Ratio 1.7 × distancia SL | Cerrar y mover SL a breakeven |
| **TP2** | 25% restante | Correr con trailing stop o hasta agotamiento | Dejar correr el movimiento |

**¿Qué es el Ratio 1.7?**
```
Ratio = Distancia al TP1 ÷ Distancia al SL
Ratio 1.7 significa que TP1 está al 170% de la distancia del SL

Ejemplo:
Entry = 60,200
SL = 60,109.7 (distancia = 90.3)
TP1 = 60,200 + (90.3 × 1.7) = 60,200 + 153.51 = 60,353.51 USDT
```

### 4.3 Break Even (BE)

**Cuándo mover a BE (según ZCoinTV):**
> "El break even se utiliza cuando consideramos que se han revertido las probabilidades de un trade. Si al regresar al punto de entrada es más probable el stop loss que el TP, ese es el momento de poner el break even."

- **Señal:** Tras alcanzar TP1
- **Acción:** Mover SL al punto de entrada (entry price)
- **Criterio:** No mover por miedo, sino porque las probabilidades se revirtieron

### 4.4 Trailing Stop (TP2)

Para el tramo del 25% restante:
- Opción A: Dejar hasta que el movimiento se agote (señal contraria)
- Opción B: Trailing stop en EMA 12
- Opción C: Trailing stop con offset de 0.5-1%

---

## 5. REGISTRO DE REGLAS OPERATIVAS (Consolidado ZCoinTV)

### 5.1 Riesgo/Reward (ratio riesgo/beneficio)
```
Ratio = Distancia al TP ÷ Distancia al SL
```- Ratio mínimo recomendado por ZCoinTV: **1:1.5** (para cualquier operativa)
- Ratio de esta estrategia: **1:1.7** en el 75% de la posición
- Criterio de ZCoinTV: "si el ratio es <1.5, cuestionar seriamente la operativa"

### 5.2 Tres elementos obligatorios antes de entrar
1. **Stop Loss definido**
2. **Take Profit definido**
3. **Calculo de ratio riesgo/recompensa (≥1.5)**

### 5.3 Los 5 Errores que matan la estrategia (según ZCoinTV)
| # | Error | Consecuencia | Solución |
|---|-------|-------------|----------|
| 1 | Empezar con dinero real sin práctica demo | Pérdida total, frustración | 2-3 meses en demo |
| 2 | No usar Stop Loss | Liquidación de cuenta SIEMPRE | SL obligatorio ante inserción |
| 3 | No tener plan de trading | Decisiones inconsistentes | Escribir criterios, seguirlos |
| 4 | Exceso de apalancamiento | Liquidación instantánea | Máximo 5x en futuros |
| 5 | Dejarse llevar por emociones | Comprar en máximos, vender en mínimos | Disciplina, control emocional |

### 5.4 Gestión de riesgo fundamental
- Máximo **5% de la cuenta por operación** (ZCoinTV: gestión-riesgo-bots.md)
- **Bot sin criterio de gestión**: el trader define el riesgo, no el bot
- **Apalancamiento**: Máximo 5x en futuros
- **Selección de activos**: Solo activos conocidos y con alta liquidez

---

## 6. CONFIGURACIÓN VISUAL EN TRADINGVIEW

### 6.1 Setup recomendado para ZCoinTV

**Indicadores:**
1. **EMA 12** (diferente color, línea gruesa)
2. **RSI(14)** (panel inferior)
3. **Volume Profile** (volumen por precio sobre gráfico)
4. Puntos pivote (auto-detectados o manuales)

**Velas:**
- Tipo: Velas huecas (engullantes) — mejores para ver el cuerpo
- Color cuerpo alcista: Verde claro
- Color cuerpo bajista: Rojo claro

### 6.2 Temporalidades en pantalla
- **Gráfico principal:** 5 minutos (acción)
- **Gráfico secundario (opcional):** 1h o 4h (contexto)

---

## 7. CONSIDERACIONES DE TEMPORIZACIÓN

### 7.1 Horarios Óptimos (zonas horarias basadas en UTC)

| Sesión | Horario UTC | Características |
|--------|------------|----------------|
| **Sesión Europea** | 07:00-14:30 UTC | Movimientos técnicos, buena predictibilidad |
| **Solapamiento Euro-Americano** | 14:30-17:00 UTC | Mayor volumen, mejor fluidez |
| **Sesión Americana** | 14:30-21:00 UTC | Mayor volumen, mejores setups |
| **Evitar:** | 21:00-07:00 UTC | Bajo volumen, spreads amplios, ruido |

**Nota crucial:** ZCoinTV no menciona sesiones específicamente para esta estrategia, pero el análisis top-down (1h/4h) requiere contexto de sesión para determinar dirección.

---

## 8. REGLAS DE NO AMBIGüEDAD (Anti-Déjà vu)

> **"No hay entradas si..."**

1. **NO entradas si:** El pivote no está claramente definido (dos al menos que hayan servido como S/R anteriormente)
2. **NO entradas si:** No se ha confirmado el cierre de vela (esperar la confirmación, NO adelantarse)
3. **NO entradas si:** El ratio espe tipo R:R < 1.5 (incluso con confluencia completa)
4. **NO entradas si:** No se ha analizado 1h-4h (método top-down obligatorio)
5. **NO entradas si:** Se ha modificado el tiempo de exposición (ej. riesgo de noticias, eventos macro)
6. **NO entradas si:** El RSI no confirma la dirección (RSI → no poner largos si >70, ni cortos si <30)
7. **NO entradas si:** Volumen decreciente en vela de entrada (significa probable falso breakout)

---

## 9. GLOSARIO DE TÉRMINOS

| Término | Definición | Relevancia |
|---------|-----------|------------|
| **EMA 12** | Media móvil exponencial de 12 periodos | Señal de entrada/filtro |
| **Pivote** | Máximo o mínimo local de precio | Define SL y contexto S/R |
| **HVN** | High Volume Node (nodo alto volumen) | Soporte/Resistencia |
| **LVN** | Low Volume Node (nodo bajo volumen) | Zona rápida, ideal para stops |
| **POC** | Point of Control (máximo volumen) | Imán de precio (TP1) |
| **Ratio 1.7** | TP1 al 170% de la distancia del SL | Gestión en dos tramos |
| **BE** | Break Even (sin pérdidas) | Protección tras TP1 |
| **Top-Down** | Analizar temporalidades altas → bajas | Contexto antes de entrar |
| **Confluencia** | Multiplicidad de señales convergentes | Confirmación de entrada |
| **Vela de cierre** | Vela confirmada terminada | Factor obligatorio para entra |

---

## 10. CHECKLIST PRE-OPERACIÓN

Antes de cada trade, verificar: ✓ Análisis top-down (1h o 4h) realizado ✓ Dirección identificada ✓ Pivote claramente definido ✓ RSI confirma la dirección (no extremo) ✓ Ratio ≥ 1.5 calculado ✓ SL y TP definidos ✓ Hora dentro de sesión óptima ✓ Volumen adecuado ✓ Patrón de reversión (preferible pero no obligatorio) ✓ Orden LIMIT colocada (NO market) ✓ Emociones bajo control

---

*Última actualización: 2026-06-10*
*Documento consolidado por: Freqtrade Bot (Jesús Sarmiento)*
*Contacto: jsarmiento1614@gmail.com*

---

## ANEXO A: Fuentes ZCoinTV consolidadas

Documentos concretos revisados y sus contribuciones a esta estrategia: 1. `setups/oro-scalping-ema12-pivotes.md` — Base de la estrategia EMA12 + pivotes 2. `setups/sp500-scalping.md` — Adaptación SP500, confirmaciones adicionales 3. `conceptos/errores-comunes-trading.md` — Pitfalls clave a evitar 4. `conceptos/medias-moviles.md` — Uso de EMA vs SMA, configuración visual 5. `conceptos/risk-reward-ratio.md` — Ratio 1.5-2.0, gestión pre-operativa 6. `herramientas/break-even.md` — Movimiento correcto de BE 7. `herramientas/scalping-bitget-altcoins.md` — Ajustes por activo (BTC/ETH)

*Todas las frases destacadas y citas atribuidas corresponden a transcripciones originales de ZCoinTVdocumentados en los archivos base.*