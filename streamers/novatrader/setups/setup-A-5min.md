# Estrategia de 5 Minutos — Setup A

**Fuente:** NovaTrader — BITCOIN HOY ¿HASTA DONDE PUEDE SUBIR? (2) (ID: x7O40C-A_U0)

## Descripción
Setup de entrada con **riesgo reducido** (half risk / mitad de riesgo). Se activa cuando el RSI llega a sobrecompra/sobreventa y el precio cierra por debajo/arriba de la EMA correspondiente.

## Configuración
- **Temporalidad:** 5 minutos (principal)
- **Indicadores:** RSI (14 periodos, por defecto) + EMA (periodo a criterio)
- **RSI:** línea amarilla desactivada en estilo, solo la línea principal

## Pasos del Setup A

### Para Long (alcista)
1. **Paso 1:** RSI en zona de **sobreventa** (< 30)
2. **Paso 2:** Vela cierra **por arriba** de la EMA
3. **Ejecución:** entrada en la apertura de la siguiente vela post-cierre

### Para Short (bajista)
1. **Paso 1:** RSI en zona de **sobrecompra** (> 70)
2. **Paso 2:** Vela cierra **por debajo** de la EMA
3. **Ejecución:** entrada en la apertura de la siguiente vela post-cierre

## Gestión del Setup A
- **Riesgo:** mitad del riesgo habitual (50%)
- **Take Profit 1:** ratio 1:2
- **Break Even:** mover SL al break even cuando sea posible
- **Parcial:** correr el resto del parcial tras TP1

## Notas importantes
- Nunca entrar antes del cierre de vela — esperar confirmación siempre
- Si el setup A falla (el precio no continúa) y luego hay divergencia, se activa el **Setup B**
- Picos de sobrecompra/sobreventa muy pequeños suelen barrerse — esperar confirmación