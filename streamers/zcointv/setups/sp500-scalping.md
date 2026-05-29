# Setup: Estrategia de Scalping Rentable para SP500

## Fuente: ZCoinTV
- **Video**: Estrategia de Trading SP500 Scalping RENTABLE
- **ID**: rKzz0x_XT20
- **Link**: https://youtube.com/watch?v=rKzz0x_XT20

## Descripción
Estrategia de scalping para el índice SP500 (US500 en brokers CFD) utilizando combinación de EMA 12, pivotes de precio y volume profile. Diseñada para gráfico de 5 minutos con gestión de posición en dos tramos, aprovechando las características específicas del SP500: alta liquidez institucional, spreads ajustados y movimientos predecibles en sesiones de alta actividad.

## Condiciones de Entrada

### Para LARGOS (Long)
1. Confirmar dirección general en temporalidad de 1h o 4h (top-down)
2. Identificar pivote inferior (mínimo local) en gráfico de 5min
3. Esperar vela que CIERRE por encima de la EMA 12
4. **Entrada**: En el cruce del cierre de la vela con la EMA 12 (orden limit)
5. **Confluencia deseable**: Volume Profile muestra HVN como soporte cercano + RSI(14) saliendo de sobreventa

### Para CORTOS (Short)
1. Confirmar dirección general en temporalidad de 1h o 4h (top-down)
2. Identificar pivote superior (máximo local) en gráfico de 5min
3. Esperar vela que CIERRE por debajo de la EMA 12
4. **Entrada**: En el cruce del cierre de la vela con la EMA 12 (orden limit)
5. **Confluencia deseable**: Volume Profile muestra HVN como resistencia cercana + RSI(14) saliendo de sobrecompra

## Gestión

- **Stop Loss**: Último extremo del pivote con margen adicional por spread (no ajustarlo exactamente al pivote)
- **Take Profit 1**: Ratio 1.7 (distancia SL × 1.7) — cerrar 75% de la posición
- **Take Profit 2**: Dejar correr 25% restante con trailing stop o hasta agotamiento del movimiento
- **Break Even**: Tras alcanzar TP1, mover SL al entry point
- **Risk/Reward**: Mínimo 1:1.7 en el 75% de la posición

## Horarios Óptimos
- **Sesión americana (14:30–21:00 UTC)**: Mayor volumen, mejores setups
- **Evitar**: Primera hora de apertura (14:30–15:30 UTC) si hay volatilidad extrema por noticias
- **Sesión europea (07:00–14:30 UTC)**: Movimientos más técnicos, menos volumen pero buena predictibilidad
- **Evitar sesión asiática**: Bajo volumen, spreads más amplios, ruido excesivo

## Herramientas
- **Plataforma**: SimpleFX (CFDs) o Bitget (futuros con crypto como margen)
- **Indicadores**: EMA 12, Pivotes de precio, Volume Profile, RSI(14)
- **Temporalidad contexto**: 1h o 4h
- **Temporalidad entrada**: 5min
- **Complementos**: Análisis del VIX (índice de volatilidad) como filtro de sesión

## Notas
- El SP500 tiene correlación inversa con el DXY en muchos contextos — verificar antes de operar
- Las noticias de USD (FOMC, NFP, CPI) afectan directamente al SP500 — consultar calendario económico
- Durante earnings season, la volatilidad intradía aumenta significativamente
- El SP500 en temporalidades bajas (5min) respeta muy bien soportes/resistencias y HVN/LVN
- Para operar SP500 con criptomonedas como margen: crear subcuenta crypto en SimpleFX o usar futuros en Bitget
- **Requisito previo**: Dominar la estrategia de scalping con EMA 12 y pivotes antes de aplicarla al SP500
