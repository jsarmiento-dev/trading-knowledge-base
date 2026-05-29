## Definición
El VWAP (Volume-Weighted Average Price) es un indicador de análisis técnico que muestra el precio medio de un activo ponderado por el volumen negociado en cada vela. A diferencia de las medias móviles (que ponderan por tiempo o dan preferencia a velas recientes), el VWAP da más peso a las velas con mayor volumen, revelando el "precio justo" del activo durante la sesión.

**Fuente:** ZCoinTV

## Conceptos Clave
- **VWAP vs SMA (Media Móvil Simple):** La SMA pondera todas las velas por igual. El VWAP da más peso a las velas con más volumen negociado
- **VWAP vs EMA (Media Móvil Exponencial):** La EMA da más peso a las velas recientes. El VWAP da más peso a las velas con más volumen, independientemente de cuándo ocurrieron
- **Anclaje por sesión:** Configuración estándar para day trading/scalping. El VWAP se reinicia al inicio de cada sesión (00:00 UTC)
- **Anclaje semanal/mensual:** Para operativas de medio plazo. El VWAP se calcula desde el inicio de la semana/mes
- **Bandas VWAP:** El VWAP + desviaciones estándar que crean canales similares a las Bandas de Bollinger. Algunos operadores las usan para entradas contra-tendencia

## Configuración en TradingView
1. Buscar "VWAP" en indicadores (no confundir con "Anchored VWAP")
2. Configurar anclaje a "Session" para scalping/day trading
3. Opcional: eliminar las bandas superior e inferior desde Estilo → desmarcar (el autor no las usa)
4. Para cuentas gratuitas sin slots de indicadores: usar la herramienta VWAP manual desde el panel izquierdo (clic en inicio de sesión)
5. Cambiar color y grosor a preferencia

## Reglas Operativas
1. **Filtro direccional (uso principal):**
   - Precio POR DEBAJO del VWAP → CUIDADO con operativas CORTAS (el precio tiende a subir hacia el VWAP)
   - Precio POR ENCIMA del VWAP → CUIDADO con operativas LARGAS (el precio tiende a bajar hacia el VWAP)
2. **Trades de rebote en VWAP:** Buscar confluencia del VWAP con Volume Profile o niveles de soporte/resistencia para entradas de rebote
3. **Magnetización:** El precio tiende a volver al VWAP durante la sesión. Si el precio está lejos del VWAP, esperar que eventualmente lo alcance
4. No usar el VWAP como señal aislada: siempre conjugar con al menos otra herramienta (Volume Profile, Fibonacci, estructura de precio)
5. Principalmente efectivo en day trading y scalping; en temporalidades altas usar anclaje semanal
6. El VWAP no es un filtro "duro" — es una advertencia, no una prohibición absoluta de tomar trades en contra

## Frase Destacada
> "El VWAP no solo es un nivel en el cual el precio tiende a rebotar, sino que sobre todo es una media a la que el precio tiende a ir."
