## Definición
Estrategia de scalping para oro (XAU/USD) basada en la combinación de una EMA 12, pivotes de precio y volume profile. Diseñada para gráfico de 5 minutos con gestión de posición en dos tramos.

**Fuente:** ZCoinTV

## Conceptos Clave
- **Indicador de pivotes:** detecta automáticamente niveles donde el precio ha rebotado (mínimos/máximos locales)
- **EMA 12:** media móvil exponencial de 12 periodos como filtro de entrada
- **Gestión en dos tramos:** 75% de la posición con ratio 1.7, 25% restante con breakeven y trailing
- **Broker recomendado:** SimpleFX (CFDs con buen volumen)
- **Alternativa crypto:** Pax Gold (PAXG) tokenizado en exchanges como Bitget

## Reglas Operativas
1. Confirmar dirección del DXY (índice del dólar) antes de buscar entrada — correlación inversa con el oro
2. Esperar formación de un pivote en el gráfico de 5 minutos:
   - **Largo:** pivote inferior (mínimo)
   - **Corto:** pivote superior (máximo)
3. Esperar vela que CIERRE por encima (largo) o por debajo (corto) de la EMA 12
4. Entry point en el cruce del cierre de la vela con la EMA 12 (usar orden limit)
5. Stop Loss: último extremo del pivote con un pequeño margen adicional (no ajustarlo exactamente al pivote por el spread)
6. Primer Take Profit: ratio 1.7 (distancia SL × 1.7) — cerrar 75% de la posición
7. Tras primer TP: mover Stop Loss a breakeven (punto de entrada)
8. Dejar correr el 25% restante hasta señal contraria o agotamiento del movimiento
9. Complementar con divergencias RSI (14) en temporalidades superiores (4H, diario) para swing trading

## Frase Destacada
> "Analizar el oro y tradearlo no es difícil. Solo necesitamos las herramientas adecuadas y el conocimiento oportuno."
