## Definición
Guía paso a paso para crear tu propio bot de trading automatizado conectando alertas de TradingView con WunderTrading. Este método permite traducir cualquier estrategia de análisis técnico de TradingView en órdenes automáticas ejecutadas en exchanges sin necesidad de programación avanzada — solo requiere configurar alertas con condiciones claras y conectarlas a WunderTrading como puente hacia el exchange.

**Fuente:** ZCoinTV

## Conceptos Clave
- **TradingView como cerebro:** Las estrategias se diseñan visualmente en TradingView usando indicadores, price action y alertas. TradingView es el motor de análisis; WunderTrading es el ejecutor
- **WunderTrading como puente:** Plataforma que recibe la alerta de TradingView vía webhook y la traduce en una orden real en el exchange conectado (Bitget, Binance, Bybit, etc.)
- **Alerta → Orden:** Cada alerta de TradingView contiene un mensaje con formato específico que WunderTrading interpreta para decidir: dirección (long/short), tamaño, apalancamiento, stop loss y take profit
- **Sin código complejo:** No se requiere saber programar Pine Script avanzado — solo configurar alertas con condiciones claras y un mensaje bien estructurado
- **Gestión de riesgo integrada:** El bot puede incluir SL y TP en cada orden, y WunderTrading permite configurar trailing stop y break even automático
- **Lógica de filtro:** Se pueden programar múltiples condiciones en una sola alerta de TradingView para filtrar entradas (ej. RSI + EMA + volumen)

## Configuración Paso a Paso

### 1. Preparar la Estrategia en TradingView
- Diseñar la estrategia con indicadores y condiciones de entrada claras
- Usar la función de alerta (`Alt + A`) para crear la condición
- En el mensaje de la alerta, usar la sintaxis de WunderTrading:
  - `{{ticker}}` — símbolo automático
  - `side=long` o `side=short` — dirección
  - `tp=1.5%` — take profit porcentual
  - `sl=0.75%` — stop loss porcentual
  - `leverage=5` — apalancamiento

### 2. Conectar con WunderTrading
1. Crear cuenta en [WunderTrading](https://wundertrading.com)
2. Conectar exchange (Bitget, Binance, etc.) mediante API keys
   - **IMPORTANTE**: Las API keys deben tener permisos de trading de futuros habilitados
   - NUNCA activar el permiso de retiro (withdrawal)
3. En TradingView → Alertas → Notificaciones → Webhook URL
4. Pegar la URL de webhook proporcionada por WunderTrading

### 3. Configurar el Bot en WunderTrading
- **Tipo de orden**: Market (recomendado para bots) o Limit
- **Tamaño de posición**: Fijo o porcentaje del balance
- **Modo de margen**: Aislado (obligatorio)
- **Apalancamiento**: ≤5x (recomendado por ZCoinTV)
- **Filtros adicionales**: Número máximo de posiciones simultáneas, cooldown entre trades
- **Gestión avanzada**: Trailing stop, break even automático, DCA en drawdown (con precaución)

### 4. Probar en Demo
- WunderTrading ofrece paper trading para testear sin riesgo
- Verificar que las alertas se ejecutan correctamente
- Comprobar que SL y TP se colocan en los niveles esperados
- Dejar correr en demo mínimo 1-2 semanas antes de usar dinero real

## Reglas Operativas
1. Solo automatizar estrategias que ya domines en trading manual — si no eres rentable manualmente, el bot no te hará rentable
2. Configurar las API keys del exchange SIN permiso de retiro (withdrawal) por seguridad
3. Usar apalancamiento ≤5x en bots automáticos — el bot no adapta riesgo a volatilidad inesperada
4. SIEMPRE incluir stop loss en cada alerta — una alerta sin SL es una bomba de tiempo
5. Probar el bot en cuenta demo mínimo 2 semanas antes de usar fondos reales
6. Monitorear el bot periódicamente — no es "configurar y olvidar"
7. WunderTrading permite pausar/desactivar bots manualmente — tener criterio para apagar en condiciones adversas
8. Limitar número de posiciones simultáneas (máximo 2-3) para no sobreexponerse
9. Verificar que el mensaje de la alerta contiene la sintaxis correcta — un typo puede abrir una orden sin SL
10. Documentar la lógica de cada bot: qué estrategia implementa, en qué condiciones se activa, cuándo se debe apagar

## Frase Destacada
> "El bot va a hacer exactamente lo que nosotros le digamos que haga. Si nosotros no sabemos lo que estamos haciendo, el bot tampoco lo va a saber. No hay magia: primero aprende a tradear, luego automatiza."
