# Grid Bots (Pionex)

## Definición
Bot automatizado que coloca múltiples órdenes de compra en la parte inferior y múltiples órdenes de venta en la parte superior de un rango definido, obteniendo ganancia de la diferencia de precio en cada fluctuación.

## Fuente: ArgenTrader

## Modos
- **Long**: compra abajo, vende arriba (sesgo alcista)
- **Short**: abre cortos arriba, cierra abajo (sesgo bajista)
- **Neutral**: opera ambos lados dentro del rango (máxima eficiencia lateral)

## Métricas
- **Ganancia de Rejilla (Grid Profit)**: beneficio consolidado y realizado. Es la métrica CLAVE.
- **Trend PNL**: ganancia/pérdida no realizada. Es momentáneo, desaparece si el mercado gira.

## Estrategia de Liberación
Cuando la ganancia de rejilla iguala la inversión real (break even), retirar ese monto y dejar el bot con "dinero de la casa".

## Reglas Operativas
1. Apalancamiento máximo 5x, preferible 3x
2. Operar solo en mercados laterales o consolidaciones
3. Definir rango con soportes/resistencias válidos del análisis técnico
4. Cerrar bot cuando precio rompe el rango
5. Monitorear Grid Profit, no Trend PNL
6. Más rejillas = más operaciones por oscilación
7. Configuración manual > copiar estrategias de terceros
8. Hacer seguimiento periódico del track record

## Ventaja Psicológica
El bot elimina las 3 fuentes de error humano: emociones, dudas y errores de ejecución.

## Frase Destacada
> "El trader muchas veces no vende cuando tiene que vender por codicia. Muchas veces no compra cuando tiene que comprar por miedo. Y ahí es donde todo se desordena."
