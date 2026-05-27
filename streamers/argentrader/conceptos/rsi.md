# RSI (Relative Strength Index)

## Definición
Oscilador que mide la fuerza de una tendencia o movimiento. Oscila entre 0 y 100. Configuración estándar: período 14, niveles 70/50/30.

## Fuente: ArgenTrader

## Interpretación Correcta
- **Sobrecompra (>70)** y **Sobreventa (<30)**: indican FUERZA direccional, NO señal automática de reversión
- **Línea 50**: punto de equilibrio. Cruce = cambio de momentum
- Usar solo sobrecompra/sobreventa para comprar/vender = aprovechar solo el 10% del indicador

## Divergencias
- **Divergencia bajista**: precio hace máximos más altos, RSI hace máximos más bajos → agotamiento alcista
- **Divergencia alcista**: precio hace mínimos más bajos, RSI hace mínimos más altos → agotamiento bajista
- **Válida solo si**: al menos UN pico en zona extrema (>70 o <30). Las más potentes tienen AMBOS en zona extrema
- **Barrido**: si el RSI hace nuevo pico, la divergencia queda anulada

## Reglas Operativas
1. El RSI es COMPLEMENTO, no la base de la estrategia
2. Divergencia solo es válida con al menos un pico en zona extrema
3. No operar divergencias "en el vacío" — deben coincidir con zonas de interés
4. En movimientos tendenciales fuertes, esperar cruce de 50 para entrar a favor
5. Usar multi-temporalidad: dirección en 1h, entrada en 5min
6. NO operar cuando RSI está sin direccionalidad (oscilando entre 30-70)
7. NUNCA operar contra tendencia fuerte, aunque haya divergencias
8. Diferenciar divergencias reales (dos picos separados) de oscilaciones internas

## Frase Destacada
> "El precio es como un tren que va a toda velocidad y no se puede frenar de un momento para otro. Se va desacelerando, dejando pautas divergentes entre el precio y el RSI."
