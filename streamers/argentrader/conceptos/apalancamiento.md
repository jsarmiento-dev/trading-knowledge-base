# Apalancamiento y Gestión de Riesgo

## Definición
El apalancamiento es un multiplicador del capital expuesto. NO define el riesgo de una operación — el riesgo lo define el porcentaje de la cuenta arriesgado en el stop loss.

## Fuente: ArgenTrader

## Principio Fundamental
> "El apalancamiento no modifica nuestro riesgo siempre y cuando sepamos utilizarlo correctamente. Lo que define nuestro riesgo es nuestro stop loss."

Con un stop loss bien definido y gestión de riesgo fija, el riesgo en dólares es idéntico con 5x, 20x o 55x.

## Reglas de Apalancamiento
1. **Subir apalancamiento al máximo posible** siempre que el punto de liquidación quede DETRÁS del stop loss
2. Si la liquidación queda antes del SL → bajar apalancamiento
3. Stop loss amplio (swing) → menos apalancamiento. Stop loss ajustado (scalping) → más apalancamiento
4. Más apalancamiento NO implica más comisiones (se calculan sobre valor nominal, no sobre margen)
5. Más apalancamiento = menos margen bloqueado = más capital para diversificar

## Gestión de Riesgo
- Cuentas ≥ $1,000: 1-2% de riesgo por operación
- Cuentas chicas ($100-$500): hasta 5%, nunca >10%
- **Siempre modo AISLADO, nunca CRUZADO**

## Herramienta: Calculadora Calk
Calculadora gratuita. Inputs: tamaño de cuenta, % riesgo, long/short, entrada, SL, TP.
Outputs: riesgo en $, margen necesario, tamaño de lote, liquidación, ratio R/R, PNL estimado.

## Flujo de Trabajo
1. Analizar en Binance Spot (mayor volumen)
2. Copiar precios exactos del exchange de futuros real
3. Ingresar datos en Calk
4. Ajustar apalancamiento hasta liquidación detrás del SL
5. Configurar exchange: modo AISLADO, apalancamiento indicado
6. Usar "valor de coste" (margen) para tamaño
7. Colocar SL al precio exacto

## Frase Destacada
> "El apalancamiento no modifica nuestro riesgo siempre y cuando sepamos utilizarlo correctamente. Lo que nos define nuestro riesgo es nuestro stop loss."
