# Media Móvil (Moving Average)

## Parámetros
- **Período**: 12 (MA de 12, probablemente EMA o SMA en temporalidad de 5 minutos).

## Función en la Estrategia
Actúa como **filtro de confirmación** en el Paso 2 de la estrategia de 3 pasos.

### Paso 2 - Confirmación (Gatillo)
1. El RSI marca un pico extremo (sobrecompra/sobreventa).
2. Se espera que el precio **rompa la media móvil** en la dirección deseada.
3. Se confirma con un **cierre de vela** que haya cruzado la media móvil.

> "Paso número dos, la confirmación que sería el cierre de vela por encima o por debajo de la media móvil."

## Uso
- **Para longs**: Precio cruza la media móvil hacia arriba + cierre de vela por encima.
- **Para shorts**: Precio cruza la media móvil hacia abajo + cierre de vela por debajo.

## Nota
NovaTrader menciona específicamente MA de 12 sin especificar si es SMA o EMA. La función es actuar como línea de tendencia dinámica en 5 minutos para confirmar que el impulso está cambiando de dirección.