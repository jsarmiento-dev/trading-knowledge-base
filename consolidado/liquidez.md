# Liquidez en Trading (Consolidado)

## Visión General
La liquidez es el combustible del mercado: dinero disponible reflejado en órdenes pendientes, stop loss y liquidaciones. Los grandes jugadores (instituciones, ballenas) necesitan liquidez concentrada para ejecutar órdenes fuertes sin deslizamiento, y para ello cazan los stops del trader minorista. El mercado no se mueve para hacerte rico, se mueve para encontrar liquidez. Entender dónde está la liquidez es la diferencia entre ser el cazador o ser la presa.

## Lo que dice cada Streamer

### ArgenTrader
- **Definición de liquidez**: dinero disponible reflejado en órdenes pendientes, stop loss y liquidaciones. Los grandes jugadores necesitan liquidez concentrada para ejecutar sin deslizamiento.
- **Pool de liquidez**: zona del gráfico donde se aglomeran muchas liquidaciones. Por arriba del precio = shorts atrapados. Por debajo = longs atrapados.
- **Caza de Stop-Loss (Liquidity Sweep)**: el precio va directamente a zonas de liquidez para activar stops y liquidar posiciones antes de continuar su movimiento real.
- **Contrapartida**: para que alguien compre, otro debe vender. Los grandes necesitan suficiente liquidez del lado opuesto.
- **Herramientas**: Coinglass (gratis, heatmap de liquidaciones), Trade Different (USD 89/mes, heatmap profesional + TradingView), TensorChart (gratis, órdenes pendientes en libro).
- **Setup Liquidity Sweep**: identificar tendencia clara → esperar barrido completo de pool → confirmar con vela envolvente (engulfing) → SL por debajo/encima del barrido en zona SIN liquidez → TP en pool del lado opuesto.
- **Reglas clave**: NUNCA poner stop-loss justo en un pool de liquidez; filtrar 50x-100x para scalping; revisar mapa de liquidaciones ANTES de cada entrada; la liquidez es complemento, NO el corazón de la estrategia; si el precio ya barrió un pool, esperar al siguiente en dirección opuesta.
- **Frase**: "El precio está constantemente en busca de liquidez, porque ahí es donde los grandes pueden posicionarse sin mover demasiado el mercado. Si no entendés dónde está la liquidez, tarde o temprano vas a SER la liquidez."

## Puntos de Acuerdo
- El mercado busca liquidez, no hacerte rico. Los grandes necesitan liquidez del retail para posicionarse.
- Los stops del trader minorista concentrados en niveles obvios son el objetivo de la caza de liquidez.
- NUNCA colocar el stop loss en zonas obvias de liquidez concentrada.
- La paciencia es esencial: esperar a que el barrido/trampa ocurra ANTES de entrar.
- La liquidez es una herramienta de confirmación, no la razón principal para entrar.

## Puntos de Desacuerdo o Complementarios
- **Herramientas**: ArgenTrader menciona herramientas concretas (Coinglass, Trade Different, TensorChart, indicador Leviathan en TradingView).
- **Enfoque**: ArgenTrader tiene un enfoque sistemático con setup definido (Liquidity Sweep: tendencia + barrido + engulfing).
- **Activo**: ArgenTrader habla de liquidez de forma general aplicable a cualquier activo.
- **Entrada**: ArgenTrader entra tras barrido + vela envolvente. Confirmación post-barrido con engulfing.

## Reglas Operativas Consolidadas
1. **Identificar pools de liquidez** ANTES de cada entrada usando heatmaps (Coinglass, Trade Different) y/o niveles obvios de soporte/resistencia.
2. **NUNCA colocar el stop loss** justo en un pool de liquidez concentrada.
3. **Esperar el barrido completo**: el precio debe barrer la zona de liquidez y dar señal de agotamiento/rechazo.
4. **Confirmar antes de entrar**: vela envolvente (engulfing) tras el barrido completo.
5. **Stop Loss** en zona SIN liquidez concentrada, por debajo del mínimo del barrido (largos) o encima del máximo (cortos).
6. **Take Profit** en el pool de liquidez del lado opuesto.
7. **No operar en la ruptura, operar en la ruptura fallida**: si el precio rompe y vuelve a cerrar dentro del rango, es la señal de que la cacería terminó.
8. **Si el precio ya barrió un pool**, esperar al siguiente en dirección opuesta.
9. **La liquidez es complemento**, no el corazón de la estrategia. Integrar con tendencia, estructura y patrones de velas.
10. **Scalping**: filtrar liquidaciones de alto apalancamiento (50x-100x), temporalidad 5m-15m.
11. **Actitud mental**: mirar los gráficos con mirada de depredador, no de presa.

## Fuentes
- [ArgenTrader — Conceptos: Liquidez](../streamers/argentrader/conceptos/liquidez.md)
- [ArgenTrader — Setup: Liquidity Sweep](../streamers/argentrader/setups/liquidity-sweep.md)
