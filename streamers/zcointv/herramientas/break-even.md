# Break Even (Gestión Dinámica de la Operativa)

## Definición
El break even es una herramienta avanzada de gestión dinámica de la operativa que consiste en mover el stop loss al punto de entrada (o por encima/por debajo según dirección) para que, si el trade se regresa al precio de entrada, se cierre automáticamente sin pérdidas. Forma parte esencial de la gestión de riesgos profesional.

## Fuente: ZCoinTV

## Conceptos Clave

### Los Tres Pilares de un Trade
Todo trade debe tener definidos tres elementos:
1. **Punto de entrada**: donde la estrategia considera correcto buscar la operación
2. **Take Profit (TP)**: punto de salida exitosa (total o parcial)
3. **Stop Loss (SL)**: punto de invalidación donde se rescata el capital remanente

El break even se relaciona directamente con el punto de entrada y el stop loss.

### ¿Qué es exactamente el Break Even?
- En **largos**: colocar el SL por encima del punto de entrada
- En **cortos**: colocar el SL por debajo del punto de entrada
- Si el precio regresa al entry, el trade se cierra sin pérdidas (en tablas)

### ⚠️ Advertencia Crítica: Esperanza Matemática
El uso **indiscriminado** del break even **rompe la esperanza matemática** de una estrategia. Un trade puede ir momentáneamente a zona negativa sin que eso signifique que sea un mal trade. Si se coloca break even automáticamente por miedo, se cortan trades que luego irían a TP.

### Criterio Correcto de Uso
El break even se utiliza **solo cuando se han revertido las probabilidades del trade**. Es decir:
- Abriste el trade porque era más probable TP que SL
- Si algo cambia y ahora al regresar al entry es más probable SL que TP → **pones break even**
- No es una cuestión de miedo, es una cuestión de probabilidades

### Stop Profit
El stop profit es al break even lo que el break even es al stop loss:
- Si ya tienes BE puesto, y al llegar a X punto es más probable ir a BE que a TP
- En ese caso colocas un **stop profit** para asegurar una pequeña ganancia
- Ejemplo: colocar stop profit en el POC (Point of Control del Volume Profile)

### Trailing Stop
El trailing stop es la **automatización** del break even y del stop profit. En lugar de hacerlo manualmente con análisis, el sistema va moviendo el stop conforme el precio avanza a favor. Es un "primo hermano" del break even.

### Niveles Clave para Colocación
- **HVN** (High Volume Nodes): zonas de alto volumen negociado
- **LVN** (Low Volume Nodes): zonas de bajo volumen → el precio las cruza rápido
- **POC** (Point of Control): nivel de mayor volumen en el perfil
- La vulneración de un nodo clave puede determinar la aceleración hacia otro nodo

## Reglas Operativas
1. **NUNCA** usar break even de forma automática o indiscriminada al abrir el trade
2. Solo colocar break even cuando el regreso al punto de entrada indique que ahora es más probable SL que TP
3. El criterio de inversión de probabilidades depende de la metodología (Wyckoff, Price Action, nodos de volumen)
4. Usar stop profit como escalón intermedio entre break even y take profit
5. Tener **confianza en la estrategia** — no mover stops por miedo (psicotrading)
6. Los HVN, LVN y POC son niveles técnicos ideales para colocar BE y stop profit
7. Si el precio llega a un nivel donde es más probable BE que TP, asegurar ganancia parcial con stop profit

## Frase Destacada
> "El break even se utiliza cuando consideramos que se han revertido las probabilidades de un trade. Si al regresar al punto de entrada es más probable el stop loss que el TP, ese es el momento de poner el break even."
