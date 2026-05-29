# Estrategia PUP + RSI (BTC 5m)

## Definición
Estrategia de trading para Bitcoin en temporalidad de 5 minutos basada en dos indicadores: el **PUP** (indicador privado de pivotes + EMA 12) y el **RSI** (índice de fuerza relativa, longitud 14). Creada por Zcoin TV y Scott FDX, utilizada diariamente en vivo por ArgenTrader. Probada en más de 2,000 operaciones.

## Fuente
- **Video**: [La Estrategia de Trading de Criptomonedas MÁS RENTABLE en 2025](https://youtube.com/watch?v=-8LBMNGqvXk)
- **Canal**: ArgenTrader
- **Creadores**: Zcoin TV y Scott FDX
- **ID**: -8LBMNGqvXk

## Conceptos Clave

### Indicadores Necesarios
1. **PUP (PuPu)** — Indicador privado (enlace en descripción del video):
   - Genera pivotes (línea roja/verde escalonada).
   - EMA exponencial de 12 periodos (línea blanca).
   - Configuración: "entrada de datos" → 12 y 400.

2. **RSI (Índice de Fuerza Relativa)** — Indicador público:
   - Longitud: 14.
   - Se usa como filtro de validez y para medir fuerza mediante divergencias.

### Estructura de la Entrada
- **Short**: El precio deja un pivote VERDE y cierra POR DEBAJO de la EMA 12.
- **Long**: El precio deja un pivote ROJO y cierra POR ENCIMA de la EMA 12.

### Gestión de la Operación
- **Entrada**: Orden LÍMITE en el nivel exacto donde el precio cruzó la EMA (NO a mercado).
- **Stop Loss**: 
  - Short: por ENCIMA del máximo del pivote.
  - Long: por DEBAJO del mínimo del pivote.
- **Take Profit**: Ratio fijo **1.17**.
- **Gestión post-TP1**:
  - Al tocar el TP → cerrar **75%** de la posición.
  - Mover SL al punto de entrada (break even).
  - Dejar correr el **25%** restante.
- **Cierre del 25% restante**: Cuando aparezca una **divergencia entre precio y RSI en gráfico HORARIO**.

### Sistema de Riesgo (RSI Divergencias)
- **Riesgo COMPLETO** (ej: 2% de cuenta): Cuando hay DIVERGENCIA entre precio y RSI.
  - Divergencia alcista: precio hace mínimos más bajos pero RSI hace mínimos más altos → posible subida.
  - Divergencia bajista: precio hace máximos más altos pero RSI hace máximos más bajos → posible caída.
- **Mitad de Riesgo** (ej: 1% de cuenta): Cuando NO hay divergencia pero el RSI llegó a zona extrema.

## Filtros Operativos

1. **Evitar compresión contra la EMA**: Si el precio viene usando la EMA como resistencia/soporte y se comprime demasiado (SL muy cercano), filtrar la operativa.
2. **Evitar la "escalerita de la muerte"**: Múltiples entradas contra-tendencia consecutivas donde el RSI pierde direccionalidad. El precio sigue subiendo/bajando pero el RSI no acompaña.
3. **Operar a favor de la tendencia horaria**: Identificar la tendencia en gráfico HORARIO y buscar solo entradas a favor (mayor probabilidad de acierto).
4. **Complementar con zonas de interés**: Esperar que el PUP genere un pivote justo en un soporte, resistencia, POC o bloque de órdenes válido.
5. **Cancelar si no testea**: Si la orden límite no es testeada y el precio ya tocó el TP, cancelar la operativa. Ese trade ya se completó.

## Reglas Operativas

1. Configurar PUP (12/400) y RSI (14) en TradingView.
2. Esperar pivote + cierre por debajo/encima de la EMA.
3. **Solo entrar si**: RSI está en zona extrema o hay divergencia.
4. Colocar orden LÍMITE en el nivel del cruce con la EMA.
5. Definir SL por encima/debajo del pivote y TP en ratio 1.17.
6. Si el precio no testea la orden → cancelar cuando llegue al TP.
7. Al tocar TP: cerrar 75%, SL a break even.
8. Cerrar el 25% restante con divergencia en RSI horario.
9. **Riesgo completo** si hay divergencia RSI-precio, **mitad de riesgo** si no.
10. **NUNCA operar todas las señales** — filtrar con los criterios anteriores.

## Frase Destacada
> "Esta estrategia no es 100% mecánica. Nuestra rentabilidad va a depender de qué tan bien sepamos filtrar las operativas. Si tomamos absolutamente todas, seguramente no seamos rentables."
