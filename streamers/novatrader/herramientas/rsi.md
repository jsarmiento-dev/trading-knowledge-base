# RSI (Relative Strength Index)

**Fuente:** NovaTrader — BITCOIN HOY ¿HASTA DONDE PUEDE SUBIR? (2) (ID: x7O40C-A_U0)

## Configuración recomendada por Nova
- **Longitud:** 14 periodos (por defecto)
- **Estilo:** desactivar la línea amarilla/secundaria (dejar solo la línea principal del RSI)

## Interpretación
- **Sobrecompra (>70):** indica que el impulso alcista está muy forzado, posible retroceso
- **Sobreventa (<30):** indica que el impulso bajista está muy forzado, posible rebote
- **50 puntos:** nivel neutral. Cuando el RSI retrocede a 50 tras un pico, puede estar listo para el siguiente movimiento

## Divergencias (función principal en la estrategia)
- **Divergencia alcista:** precio marca mínimo más bajo, RSI marca mínimo más alto → tendencia bajista pierde fuerza
- **Divergencia bajista:** precio marca máximo más alto, RSI marca máximo más bajo → tendencia alcista pierde fuerza

## Notas
- No confiar en divergencias con picos muy pequeños (fractales) — suelen barrerse
- La divergencia ideal se da cuando el RSI retrocede hasta ~50 puntos entre el primer pico y el segundo
- El RSI no es una señal de entrada por sí solo — necesita confirmación de precio (cierre de vela)