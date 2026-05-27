# Liquidez en Trading

## Definición
La liquidez es el combustible del mercado: dinero disponible reflejado en órdenes pendientes, stop loss y liquidaciones. Los grandes jugadores (instituciones, ballenas) necesitan liquidez concentrada para ejecutar órdenes fuertes sin deslizamiento.

## Fuente: ArgenTrader

## Conceptos Clave

### Pool de Liquidez
Zona del gráfico donde se aglomeran muchas liquidaciones. Si están por arriba del precio = posiciones short atrapadas. Si están por debajo = posiciones long atrapadas. Son los niveles clave a identificar.

### Caza de Stop-Loss (Liquidity Sweep)
El precio va directamente a zonas de liquidez para activar stops y liquidar posiciones antes de continuar su movimiento real. El mercado barre stops de operadores sobreapalancados para generar contrapartida.

### Contrapartida
Para que alguien compre, otro debe vender. Los grandes necesitan suficiente liquidez del lado opuesto para ejecutar sin mover el precio en su contra. El trader minorista con poco capital no genera suficiente contrapartida.

## Herramientas para Identificar Liquidez

| Herramienta | Precio | Función |
|-------------|--------|---------|
| Coinglass | Gratis | Liquidation heatmap 24h a 1 mes. Filtrar por exchange (Binance), activo, temporalidad. Barra filtro default 0.85 |
| Trade Different | USD 89/mes | Heatmap profesional + TradingView integrado. Filtrar por horas exactas, apalancamiento (10x-100x). Paleta: azul→celeste→verde→amarillo→rojo |
| TensorChart | Gratis | Órdenes pendientes en libro. Config: Heatmaps lower precision 2, opacidad max, volumen min max; Boll Studios delta diverse 150 |

## Reglas Operativas
1. NUNCA poner stop-loss justo en un pool de liquidez
2. Analizar liquidez en exchange de mayor volumen (Binance)
3. Scalping: filtrar 50x-100x (liquidaciones más cerca del precio)
4. Temporalidad acorde al tipo de operación: 15min-1h intraday, 24h-1sem swing
5. Revisar mapa de liquidaciones ANTES de cada entrada
6. La liquidez es complemento, NO el corazón de la estrategia
7. Si el precio ya barrió un pool, esperar al siguiente en dirección opuesta

## Frase Destacada
> "El precio está constantemente en busca de liquidez, porque ahí es donde los grandes pueden posicionarse sin mover demasiado el mercado. Si no entendés dónde está la liquidez, tarde o temprano vas a SER la liquidez."
