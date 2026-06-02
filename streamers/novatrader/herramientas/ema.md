# EMA (Exponential Moving Average)

**Fuente:** NovaTrader — BITCOIN HOY ¿HASTA DONDE PUEDE SUBIR? (2) (ID: x7O40C-A_U0)

## Uso en la estrategia
La EMA se usa como **filtro de confirmación** para las entradas. El precio debe cerrar por arriba (long) o por debajo (short) de la EMA correspondiente para validar la entrada.

## Periodos mencionados
- **EMA 12:** periodo rápido, usado en la estrategia de 5 minutos
- **EMA 50:** media plazo, coincide con POC en algunos casos
- **EMA 100:** soporte/resistencia dinámico
- **EMA 200:** soporte/resistencia dinámico de largo plazo

## MultiEMA (indicador personalizado)
Nova desarrolló un indicador propio llamado MultiEMA que permite:
- Elegir qué EMA se muestra en cada temporalidad
- Configurar por separado: EMA 50 para 5min, EMA 12 para 15min, EMA 200 para 4h, etc.

## Configuración
Se configura desde TradingView seleccionando el periodo deseado y ajustando la visibilidad por intervalo de tiempo.