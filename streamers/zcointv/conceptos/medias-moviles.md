## Definición
Las medias móviles son herramientas que calculan el promedio de precios de un número concreto de velas, suavizando la acción del precio para interpretar mejor su direccionalidad y las tendencias. Existen varios tipos (simples, exponenciales, ponderadas por volumen) con aplicaciones diferenciadas según la temporalidad y el estilo de trading.

**Fuente:** ZCoinTV

## Conceptos Clave
- **Media móvil simple (SMA):** Promedio equitativo de las últimas N velas. Más útil en temporalidades altas (swing trading, spot largo plazo) porque filtra ruido. Las más comunes: 20, 50, 100 y 200 periodos
- **Media móvil exponencial (EMA):** Da más peso a las velas recientes y menos a las antiguas. Más reactiva y rápida que la SMA. Ideal para day trading y scalping. ZCoinTV usa EMA de 12 periodos anclada a 5 min (cubre la última hora de negociación)
- **VWAP (Volume Weighted Average Price):** Media móvil ponderada por volumen. Muy usada en scalping para sesiones cortas. La estrategia típica: buscar largos cuando el precio rompe VWAP al alza y lo retestea como soporte; buscar cortos cuando lo confirma como resistencia
- **Anclaje de temporalidad:** Se puede fijar una media móvil a una temporalidad superior a la del gráfico (ej. EMA de 20 en diario viendo gráfico horario) para filtrar ruido sin perder la referencia de tendencia mayor
- **Cruces de medias móviles:** Técnica para detectar cambios de tendencia (ej. cruce de SMA 50 y 200 en diario). Útil en trading de largo plazo. ZCoinTV no los usa en directo pero reconoce su validez
- **Nunca usar medias móviles solas:** Siempre deben conjugarse con otro elemento: divergencia RSI, soportes/resistencias, o estrategia adicional. No son indicadores absolutos

## Reglas Operativas
28. En temporalidades bajas (scalping/day trading): usar EMA o VWAP, más reactivas
29. En temporalidades altas (swing/spot): preferir SMA, que filtra mejor el ruido
30. Anclar la media móvil a una temporalidad superior a la que se está tradeando (ej. EMA en diario para trading en 1H/4H)
31. Nunca usar medias móviles como señal única — siempre requieren confluencia (RSI, soporte/resistencia, divergencia)
32. Configurar velas huecas + medias como puntos/círculos para visualizar cruces fácilmente
33. El VWAP es especialmente útil en sesiones de scalping: romper y retestear + confluencia adicional
34. Los cruces de medias móviles (50/100/200) en diario o semanal sirven para detectar cambios de tendencia macro
35. Hacer backtesting antes de adoptar cualquier configuración de medias móviles en un activo específico

## Frase Destacada
> "Las medias móviles, como cualquier indicador de trading, queremos conjugarlo con algún elemento adicional — una divergencia precio RSI, soportes y resistencias, algún tipo de estrategia adicional. Nunca por sí solas."
