# Estrategias de Trading (Consolidado)

> Documento generado el 2026-05-29 a partir de 12 archivos fuente de 3 streamers: ArgenTrader, ZCoinTV y ScottFDX.

---

## Visión General

Este documento consolida todas las estrategias de trading documentadas de cuatro streamers hispanohablantes. Cada estrategia ha sido extraída directamente de los archivos fuente originales, preservando los criterios concretos sin añadir interpretaciones. Los campos no especificados en las fuentes se marcan explícitamente como "No especificado".

Las estrategias abarcan múltiples mercados (índices, criptomonedas, oro, forex), temporalidades (desde 1min hasta diario) y estilos (scalping, intradía, swing, bots automatizados). Algunas estrategias comparten fundamentos (EMA 12, pivotes, Volume Profile, Wyckoff) aplicados a distintos activos.

---

## ArgenTrader

### 1. Estrategia de Apertura (Caja)

- **Mercado/Activo**: SP500, Nasdaq, Dow Jones, Russell (americanos); Nikkei (asiático); DAX, Eurostoxx 50 (europeos)
- **Temporalidad**: 5 minutos (confirmación de ruptura); rango formado 1 hora antes de apertura hasta 25 min después
- **Condiciones de Entrada**:
  1. Esperar que el indicador dibuje la caja (rango de volatilidad pre-apertura)
  2. Ruptura confirmada solo con CIERRE de vela en 5min (NO mecha)
  3. Entrada con orden LÍMITE en el nivel exacto de ruptura
  4. Máximo 2 horas esperando ruptura → cancelar si no ocurre
  5. Si el precio va directo a TP sin testear la entrada → cancelar
- **Stop Loss**: No especificado explícitamente (implícito en la estructura de gestión por parciales con movimiento a break even tras TP1)
- **Take Profit**:
  - TP1: ratio 1:1 → cerrar 50%, mover SL a break even
  - TP2: ratio 1:2.5 o divergencia RCI en 5min
  - TP3: ratio 1:5 o divergencia RCI en temporalidad horaria
- **Gestión**: Parciales en tres tramos (50% + resto en TP2 y TP3)
- **Herramientas**: Indicador de caja (no especificado nombre); RCI para divergencias
- **Notas**:
  - Filtrar por amplitud: >35 pts en SP500 o >350-400 pts en Nikkei → NO operar
  - Divergencia RCI en contra → reducir riesgo o filtrar
  - Operar a favor de la tendencia horaria (más agresivo a favor, más estricto en contra)

### 2. Estrategia PUP + RSI (BTC 5m)

- **Mercado/Activo**: Bitcoin (BTC)
- **Temporalidad**: 5 minutos (entrada); horario (contexto y cierre del 25%)
- **Condiciones de Entrada**:
  - **Short**: El precio deja un pivote VERDE (PUP) y cierra POR DEBAJO de la EMA 12
  - **Long**: El precio deja un pivote ROJO (PUP) y cierra POR ENCIMA de la EMA 12
  - **Solo entrar si**: RSI(14) está en zona extrema O hay divergencia RSI-precio
  - Entrada con orden LÍMITE en el nivel del cruce con la EMA (NO a mercado)
- **Stop Loss**:
  - Short: por ENCIMA del máximo del pivote
  - Long: por DEBAJO del mínimo del pivote
- **Take Profit**: Ratio fijo 1.17
- **Gestión**:
  - Al tocar TP → cerrar 75% de la posición, mover SL a break even
  - Dejar correr el 25% restante
  - Cierre del 25% restante: cuando aparezca divergencia entre precio y RSI en gráfico HORARIO
- **Herramientas**: Indicador PUP (privado, config 12/400), EMA 12, RSI(14) en TradingView
- **Notas**:
  - **Riesgo completo** (ej: 2% de cuenta) si hay divergencia RSI-precio
  - **Mitad de riesgo** (ej: 1% de cuenta) si NO hay divergencia pero RSI llegó a zona extrema
  - Filtrar compresión contra EMA (SL muy cercano → no operar)
  - Evitar "escalerita de la muerte": múltiples entradas contra-tendencia con RSI sin direccionalidad
  - Operar a favor de tendencia horaria
  - Complementar con zonas de interés (soporte, resistencia, POC, bloque de órdenes)
  - Cancelar si orden límite no es testeada y precio ya tocó TP
  - NO operar todas las señales: filtrar activamente
  - Probada en más de 2,000 operaciones

### 3. Retrocesos con Fibonacci (FVG Entry)

- **Mercado/Activo**: No especificado (aplicable a cualquier activo con tendencia)
- **Temporalidad**: Temporalidad alta recomendada (más fiable)
- **Condiciones de Entrada**:
  - **Tendencia Alcista (Long)**:
    1. Identificar tendencia alcista (máximos y mínimos crecientes)
    2. Identificar fractal operativo (último impulso que rompió máximo anterior)
    3. Trazar Fibonacci de mínimo a máximo del fractal
    4. Esperar retroceso a 0.382 (tendencia acelerada) o 0.618 (RSI débil/divergencia)
    5. Buscar confirmación en el nivel ANTES de entrar
  - **Tendencia Bajista (Short)**:
    1. Confirmar cambio de estructura o tendencia bajista
    2. Identificar fractal operativo bajista
    3. Trazar Fibonacci de máximo a mínimo
    4. Esperar retroceso a 0.382 o 0.618 para cortos
    5. Buscar confirmación
- **Stop Loss**: Por debajo/encima del nivel de Fibonacci
- **Take Profit**: A favor de la tendencia, dejando correr (sin ratio fijo)
- **Gestión**: No especificada
- **Herramientas**: Fibonacci, RSI como complemento
- **Notas**:
  - RSI con fuerza alcista → esperar retroceso a 0.382
  - Divergencia bajista en RSI → esperar retroceso a 0.618
  - No usar en rangos laterales

### 4. Entrada tras Barrido de Liquidez

- **Mercado/Activo**: No especificado (genérico)
- **Temporalidad**: 5m y 15m (máximo 1h)
- **Condiciones de Entrada**:
  1. Identificar tendencia clara
  2. Esperar que el precio barra COMPLETAMENTE el pool de liquidez (inferior en largos, superior en cortos)
  3. Confirmar con patrón de vela envolvente (engulfing) tras el barrido
- **Stop Loss**:
  - Largos: por debajo del mínimo del barrido, en zona SIN liquidez concentrada
  - Cortos: por encima del máximo del barrido, en zona SIN liquidez concentrada
- **Take Profit**: En el pool de liquidez del lado opuesto
- **Gestión**: Esperar barrido COMPLETO (a veces hay un segundo extremo para limpiar residuos)
- **Herramientas**: Indicador "Liquidation Levels by Leviathan" (TradingView); Config: CBD, OFF, OFF, 0.5, sin burbujas, solo 50x (blanco) y 100x (rojo)
- **Notas**:
  - Si hay mucha liquidez en la zona de stop prevista → NO entrar
  - La liquidez es complemento, no el corazón de la estrategia

### 5. Entradas con Perfil de Volumen

- **Mercado/Activo**: No especificado (genérico)
- **Temporalidad**: Perfil en temporalidad alta (diario/semanal), ejecución en baja
- **Condiciones de Entrada** (4 variantes):
  - **Ruptura con Volumen Alto**: Precio rompe POC o HVN con gran volumen → ruptura válida (convicción)
  - **Apoyo en POC con Bajo Volumen**: Tras romper POC, precio vuelve a apoyarse con bajo volumen → nivel aceptado, anticipa continuación
  - **Aceleración en LVN**: Precio entra en zona de bajo volumen → acelera hacia siguiente HVN/POC; buscar entrada en destino
  - **Retorno al Value Area**: Precio tiende a volver al área de valor (70% del volumen); usar como confluencia para entradas contra-tendencia de corto plazo
- **Stop Loss**: No especificado
- **Take Profit**: No especificado
- **Gestión**:
  - Confirmar rupturas con volumen vertical
  - Actualizar perfil cuando cambia de rango
- **Herramientas**: Volume Profile, volumen vertical
- **Notas**:
  - No operar dentro del ruido de consolidación
  - Esperar salida del área de valor o toque de nivel clave
  - Combinar con acción de precio y patrones de reversión

---

## ZCoinTV

### 1. Estrategia Intradía para Bitcoin

- **Mercado/Activo**: Bitcoin (BTC/USDT)
- **Temporalidad**: Top-down: Diario → 4h → 1h → 15min → 5min (entrada)
- **Condiciones de Entrada**:
  - **Análisis Previo (Top-Down)**:
    1. Diario: Identificar tendencia general, estructura Wyckoff vigente (acumulación/distribución/reacumulación)
    2. 4 horas: Precisar fase Wyckoff activa, S/R clave, POC del volume profile
    3. 1 hora: Confirmar dirección intradía, HVN/LVN relevantes
    4. 15 minutos: Buscar setup de entrada
  - **LARGOS**:
    1. Contexto: Fase D de acumulación/reacumulación Wyckoff (SOS confirmado) o tendencia alcista en diario
    2. Precio sobre VWAP en 1h (filtro direccional)
    3. En 15min: Pullback a HVN o soporte horizontal relevante
    4. Entrada: Vela de 5min que cierra por ENCIMA de la EMA 12 tras el pullback
    5. Confluencia obligatoria: RSI(14) no sobrecomprado + volumen aumentando en vela de entrada
  - **CORTOS**:
    1. Contexto: Fase D de distribución/redistribución Wyckoff (SOW confirmado) o tendencia bajista en diario
    2. Precio bajo VWAP en 1h (filtro direccional)
    3. En 15min: Pullback a LVN o resistencia horizontal relevante
    4. Entrada: Vela de 5min que cierra por DEBAJO de la EMA 12 tras el pullback
    5. Confluencia obligatoria: RSI(14) no sobrevendido + volumen aumentando en vela de entrada
- **Stop Loss**: Por debajo/encima del último mínimo/máximo local con margen de ~0.15-0.25%
- **Take Profit**:
  - TP1: Primer HVN o POC en la dirección del trade (~50% posición)
  - TP2: Siguiente nivel estructural relevante (~30% posición)
  - TP3: Dejar correr 20% restante con trailing stop en EMA 12 de 5min
- **Gestión**: Al alcanzar TP1, mover SL al entry (break even); Risk/Reward mínimo 1:2 global
- **Herramientas**: EMA 12 (5min), VWAP (1h, anclaje sesión), RSI(14), Volume Profile; Exchange: Binance, Bybit o Bitget; Complementos: Order book, CVD (Cumulative Volume Delta)
- **Notas**:
  - Bitcoin respeta excepcionalmente bien los niveles Wyckoff en temporalidades ≥4h
  - Entrar solo con confirmación de volumen, no solo price action
  - Mejor momento: solapamiento europeo-americano (13:00–17:00 UTC)
  - Evitar fines de semana y cierres diarios (23:00–00:00 UTC)
  - Lunes (gap de fin de semana) y viernes (cierre semanal) requieren precaución
  - Si precio en fase B Wyckoff (rango), priorizar scalping sobre swings
  - Requisito previo: dominar metodología Wyckoff y análisis top-down

### 2. Oro Scalping EMA 12 + Pivotes

- **Mercado/Activo**: Oro (XAU/USD); alternativa crypto: PAXG (Pax Gold)
- **Temporalidad**: 5 minutos
- **Condiciones de Entrada**:
  1. Confirmar dirección del DXY (índice del dólar) — correlación inversa con el oro
  2. Esperar formación de un pivote en 5min:
     - Largo: pivote inferior (mínimo)
     - Corto: pivote superior (máximo)
  3. Esperar vela que CIERRE por encima (largo) o por debajo (corto) de la EMA 12
  4. Entrada en el cruce del cierre de la vela con la EMA 12 (orden limit)
- **Stop Loss**: Último extremo del pivote con margen adicional (no ajustarlo exactamente al pivote por el spread)
- **Take Profit**:
  - TP1: Ratio 1.7 (distancia SL × 1.7) — cerrar 75% de la posición
  - TP2: Dejar correr el 25% restante hasta señal contraria o agotamiento del movimiento
- **Gestión**: Tras TP1, mover SL a break even
- **Herramientas**: EMA 12, indicador de pivotes, Volume Profile; Broker recomendado: SimpleFX (CFDs); Complemento: divergencias RSI(14) en 4H/diario para swing
- **Notas**:
  - Correlación inversa oro-DXY: confirmar dirección del dólar antes de operar
  - Complementar con divergencias RSI en temporalidades superiores para swing trading

### 3. SP500 Scalping Rentable

- **Mercado/Activo**: SP500 (US500 en brokers CFD)
- **Temporalidad**: 5 minutos (entrada); 1h o 4h (contexto)
- **Condiciones de Entrada**:
  - **LARGOS**:
    1. Confirmar dirección general en 1h o 4h (top-down)
    2. Identificar pivote inferior (mínimo local) en 5min
    3. Esperar vela que CIERRE por encima de la EMA 12
    4. Entrada en el cruce con orden limit
    5. Confluencia deseable: Volume Profile muestra HVN como soporte + RSI(14) saliendo de sobreventa
  - **CORTOS**:
    1. Confirmar dirección general en 1h o 4h (top-down)
    2. Identificar pivote superior (máximo local) en 5min
    3. Esperar vela que CIERRE por debajo de la EMA 12
    4. Entrada en el cruce con orden limit
    5. Confluencia deseable: Volume Profile muestra HVN como resistencia + RSI(14) saliendo de sobrecompra
- **Stop Loss**: Último extremo del pivote con margen adicional por spread
- **Take Profit**:
  - TP1: Ratio 1.7 — cerrar 75% de la posición
  - TP2: Dejar correr 25% restante con trailing stop o hasta agotamiento
- **Gestión**: Tras TP1, mover SL al entry; Risk/Reward mínimo 1:1.7 en el 75%
- **Herramientas**: EMA 12, Pivotes de precio, Volume Profile, RSI(14); Plataforma: SimpleFX (CFDs) o Bitget (futuros); Complemento: VIX como filtro de sesión
- **Notas**:
  - Correlación inversa SP500-DXY en muchos contextos
  - Noticias USD (FOMC, NFP, CPI) afectan directamente — consultar calendario económico
  - Earnings season aumenta volatilidad intradía
  - SP500 respeta muy bien S/R y HVN/LVN en temporalidades bajas
  - Evitar sesión asiática (bajo volumen, spreads amplios)
  - Sesión óptima: americana (14:30–21:00 UTC); evitar primera hora si volatilidad extrema por noticias
  - Requisito previo: dominar scalping con EMA 12 y pivotes

### 4. Volume Profile Scalping

- **Mercado/Activo**: No especificado (genérico, aplicable a múltiples activos)
- **Temporalidad**: 5min o 15min (entrada); 1h o 4h (contexto)
- **Condiciones de Entrada**:
  - **LARGOS**:
    1. Identificar POC, VAH, VAL en 1h o 4h como contexto
    2. Precio rompe por encima del VAL y busca VAH o POC
    3. Entrada: Pullback al VAL o HVN cercano que actúa como soporte
    4. Confluencia deseable: patrón de vela de reversión alcista + RSI no sobrecomprado
  - **CORTOS**:
    1. Identificar POC, VAH, VAL en 1h o 4h como contexto
    2. Precio rompe por debajo del VAH y busca VAL o POC
    3. Entrada: Pullback al VAH o HVN cercano que actúa como resistencia
    4. Confluencia deseable: patrón de vela de reversión bajista + RSI no sobrevendido
- **Stop Loss**: En el LVN siguiente o en el extremo opuesto del value area
- **Take Profit**:
  - TP1: POC (~50% posición)
  - TP2: Extremo opuesto del value area (VAH en largos, VAL en cortos)
- **Gestión**: Al llegar al POC, mover SL al entry; Risk/Reward mínimo 1:2
- **Herramientas**: Volume Profile (TradingView, gratuito en versión básica); RSI para divergencias; patrones de velas japonesas
- **Notas**:
  - Estrategia probabilística, no determinista
  - Funciona mejor dentro del value area (rango)
  - Si precio rompe con fuerza fuera del VA → esperar, no perseguir
  - LVN = zonas de tránsito rápido (ideales para colocar stops)
  - HVN = zonas de estacionamiento (precio se detiene y acumula)
  - POC actúa como imán de precio
  - Combinar con S/R horizontales tradicionales
  - Requisito previo: entender qué es Volume Profile

### 5. Wyckoff Automatizado con Bots de Grid

- **Mercado/Activo**: Criptomonedas (futuros/spot)
- **Temporalidad**: 4h o diario (para identificar fases Wyckoff); ejecución automatizada vía bot
- **Condiciones de Entrada**:
  - **Fase C como disparador**: bot se activa solo DESPUÉS de ocurrida la fase C
  - **Acumulación/Reacumulación** (rompe arriba) → Bot LONG
  - **Distribución/Redistribución** (rompe abajo) → Bot SHORT
  - **Fase B** (sin dirección clara) → Bot NEUTRAL (largos y cortos)
  - Fase C ideal con spring (acumulación) o UTAD (distribución)
- **Stop Loss**:
  - Long: por debajo del spring
  - Short: por encima del UTAD
  - Neutral: límites superior/inferior del rango
- **Take Profit**: No especificado (gestionado por la malla del bot)
- **Gestión**:
  - Riesgo máximo: 5% de la cuenta de futuros
  - Apalancamiento bajo: punto de liquidación siempre más allá del stop loss
  - Fase B: preferir temporalidades altas (4h, diario); en 15min la fase B puede durar muy poco
  - Spot para horizonte amplio (swing), futuros para corto plazo
- **Herramientas**: Bot de grid (futuros/spot); análisis Wyckoff manual para identificar fases
- **Notas**:
  - Requisito: dominar metodología Wyckoff (playlist completa)
  - Acumulaciones y reacumulaciones → LONG; Distribuciones y redistribuciones → SHORT
  - Si acumulación falla tras el spring, SL se ejecuta con pérdida controlada
  - Si el spring no se vulnera, el stop loss se respeta

---

## ScottFDX

### 1. Mejor Bot de Trading Cripto — Bitget Grid Futuros

- **Mercado/Activo**: Criptomonedas (BTC, ETH, SOL, DOGE, LTC, BCH, UNI)
- **Temporalidad**: No especificada (operación automatizada continua)
- **Condiciones de Entrada**:
  - Bot Grid de Futuros en modo NEUTRAL (largos y cortos simultáneos)
  - Rango inferior por debajo de mínimos recientes, rango superior por encima de máximos
  - Configuraciones: Conservadora (~10 rejillas, rango amplio, bajo apalancamiento), Moderada (~20-25 rejillas), Agresiva (50-80+ rejillas, rango estrecho, mayor apalancamiento)
  - Ejemplo concreto BTC: rango $75,000-$95,000, 80 rejillas, apalancamiento 5x, capital $1,000
- **Stop Loss**: Precio mínimo de salida (por debajo de mínimos)
- **Take Profit**: Precio máximo de TP (zona de máximos)
- **Gestión**:
  - Capital fragmentado en N rejillas (órdenes pequeñas)
  - Si el precio sale de la malla: al reingresar, el bot reintroduce órdenes automáticamente
  - Bot se puede parar, modificar y reactivar sin coste
  - Transferencia automática de profit y margen disponible en configuración avanzada
- **Herramientas**: Bitget (Grid de Futuros); NO usar estrategias predefinidas de IA (crear bot manual)
- **Notas**:
  - Grid Spot solo aprovecha subidas; Grid Futuros Neutral aprovecha ambas direcciones
  - Bitcoin permite mayor apalancamiento; altcoins REDUCIRLO siempre
  - Caso real ASTER: 43 días activo con excelente rendimiento pese a corrección del activo
  - Bot #1 según pruebas exhaustivas de ScottFDX

### 2. Ganar Dinero con Trading de Cryptos (Paso a Paso)

- **Mercado/Activo**: Criptomonedas (BTC, altcoins), acciones, índices (SP500)
- **Temporalidad**: No especificada (conceptos generales)
- **Condiciones de Entrada** (marco general, no estrategia específica):
  1. Proyectar dirección (corrección = short, impulso = long)
  2. Definir punto de entrada
  3. Colocar stop loss en zona segura (invalidación)
  4. Establecer take profit
  5. Aplicar gestión de riesgo (control de apalancamiento)
  6. Cerrar posición al alcanzar objetivo
- **Stop Loss**: Definir en zona de invalidación
- **Take Profit**: Definir antes de operar
- **Gestión**:
  - Empezar en cuenta demo antes de dinero real
  - Controlar apalancamiento: menos = menos riesgo
  - NUNCA usar apalancamiento "para jugar"
  - Shorts para aprovechar caídas y cubrir posiciones largas en spot
  - Tener estrategia definida — no operar sin método
- **Herramientas**: Exchange de futuros (Bitget); permite tradear criptos y acciones (Alibaba, Intel, IBM, MicroStrategy, Coinbase, McDonald's)
- **Notas**:
  - Diferencia Spot vs Futuros: Spot solo gana en subidas; Futuros permite ganar en ambas direcciones
  - "El precio sube por las escaleras y baja por el ascensor"
  - Altcoins pueden caer >90% en bear market → shorts muy rentables
  - Comunidad de Discord con curso gratuito de estrategias
  - **Este archivo es un marco conceptual/educativo, no una estrategia concreta con criterios de entrada definidos**

---

## Tabla Comparativa

| Streamer | Estrategia | Activo | Temporalidad | Tipo |
|----------|-----------|--------|-------------|------|
| ArgenTrader | Apertura (Caja) | SP500, Nasdaq, DJ, Russell, Nikkei, DAX, Eurostoxx 50 | 5min | Intradía / Ruptura |
| ArgenTrader | PUP + RSI | BTC | 5min | Scalping |
| ArgenTrader | Retrocesos Fibonacci | Genérico | Alta (no especificada) | Swing / Tendencia |
| ArgenTrader | Liquidity Sweep | Genérico | 5m-15m (máx 1h) | Intradía / Reversión |
| ArgenTrader | Volume Profile Entry | Genérico | Alta (diario/semanal) → baja | Multi-estrategia |
| ZCoinTV | Bitcoin Intradía | BTC/USDT | 5min (top-down D→4h→1h→15m→5m) | Intradía / Wyckoff |
| ZCoinTV | Oro Scalping EMA12+Pivotes | XAU/USD | 5min | Scalping |
| ZCoinTV | SP500 Scalping | SP500 (US500) | 5min | Scalping |
| ZCoinTV | Volume Profile Scalping | Genérico | 5min/15min | Scalping / Day Trading |
| ZCoinTV | Wyckoff + Bots Grid | Criptomonedas | 4h/diario (análisis) + bot continuo | Swing / Automatizado |
| ScottFDX | Bitget Grid Futuros | Cripto (BTC, ETH, SOL, DOGE, LTC, BCH, UNI) | Continuo (bot) | Automatizado |
| ScottFDX | Trading Crypto Paso a Paso | Cripto, acciones, índices | No especificada | Educativo / Conceptos |

---

*Documento generado a partir de 12 archivos fuente. Todos los criterios provienen directamente de los archivos originales; los campos marcados como "No especificado" no estaban presentes en las fuentes.*
