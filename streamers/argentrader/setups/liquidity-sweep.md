# Setup: Entrada tras Barrido de Liquidez

## Fuente: ArgenTrader

## Condiciones de Entrada
1. Identificar tendencia clara
2. Esperar que el precio barra completamente el pool de liquidez (inferior en largos, superior en cortos)
3. Confirmar con patrón de vela envolvente (engulfing) tras el barrido

## Gestión
- **Stop Loss**: por debajo del mínimo del barrido (largos) o encima del máximo (cortos), en zona SIN liquidez concentrada
- **Take Profit**: en el pool de liquidez del lado opuesto
- **Esperar barrido COMPLETO**: a veces hace un segundo extremo para limpiar residuos

## Herramientas
- Indicador "Liquidation Levels by Leviathan" (TradingView)
- Config: CBD, OFF, OFF, 0.5, sin burbujas, solo 50x (blanco) y 100x (rojo)
- Temporalidad: 5m y 15m (máximo 1h)

## Notas
- Si hay mucha liquidez en la zona de stop prevista → NO entrar
- La liquidez es complemento, no el corazón de la estrategia
