# Setup: Estrategia de Apertura (Caja)

## Fuente: ArgenTrader

## Concepto
Rango de volatilidad formado 1 hora antes de la apertura del mercado hasta 25 minutos después. Solo requiere 1 indicador y 2 horas al día.

## Mercados
- Americano: SP500, Nasdaq, Dow Jones, Russell
- Asiático: Nikkei
- Europeo: DAX, Eurostoxx 50

## Reglas de Entrada
1. Esperar que el indicador dibuje la caja
2. Ruptura confirmada solo con CIERRE de vela en 5min (NO mecha)
3. Entrada: orden LÍMITE en el nivel exacto de ruptura
4. Máximo 2 horas esperando ruptura → cancelar si no ocurre
5. Si precio va directo a TP sin testear entrada → cancelar

## Gestión de Parciales
- **TP1**: ratio 1:1 → cerrar 50%, mover SL a break even
- **TP2**: ratio 1:2.5 o divergencia RCI en 5min
- **TP3**: ratio 1:5 o divergencia RCI en temporalidad horaria

## Filtros
- Amplitud excesiva: >35 pts SP500, >350-400 pts Nikkei → NO operar
- Divergencia RCI en contra → reducir riesgo o filtrar
- Seguir tendencia horaria: más agresivo a favor, más estricto en contra
