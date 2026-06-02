# Mapa de Calor de Liquidaciones

## Definición
Herramienta que visualiza las zonas donde se concentran órdenes de liquidación forzosa de posiciones apalancadas. También conocido como **Liquidation Heat Map**.

## Cómo funciona
- Las posiciones apalancadas tienen un precio de liquidación. Si el precio llega a ese nivel, el exchange cierra forzosamente la posición.
- El mapa de calor agrupa estas liquidaciones en clusters, mostrando los niveles de mayor concentración.

## Utilidad
- Identificar niveles donde el precio podría ser "atraído" para **cazar liquidaciones**.
- Las ballenas pueden empujar el precio hacia estas zonas para liquidar posiciones masivas.
- Ayuda a anticipar movimientos direccionales violentos.

## Cita clave (NovaTrader)
> "Acá está lleno de personas que van en corto y van a ser liquidadas... el exchange les va a cerrar forzosamente su posición."

## Consideraciones importantes
- Cuanto más tiempo el precio se mantenga en rango, **más liquidaciones se acumulan** en ambos lados.
- Más liquidaciones acumuladas = más volátil será el movimiento posterior.
- No confundir con stops de traders — las liquidaciones son forzosas por el exchange.

## Relación con la estrategia
NovaTrader espera que Bitcoin liquide posiciones en corto (subiendo) o en largo (bajando) para luego buscar entradas con la estrategia de 3 pasos.