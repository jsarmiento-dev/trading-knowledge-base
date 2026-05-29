# Bots de Trading — Consolidado

## Visión General

Los bots de trading automatizado, específicamente los **Grid Bots de Futuros en modo Neutral**, son identificados por los 3 streamers como la herramienta óptima para operar mercados laterales y rangos sin necesidad de predecir la dirección. El bot elimina las 3 fuentes de error humano (emociones, dudas, errores de ejecución), pero **no elimina la necesidad de criterio humano** en gestión de riesgo, selección de activos y definición de stops. La combinación ideal es: metodología de análisis (Wyckoff) para definir dirección + bot grid para ejecución automatizada + gestión de riesgo humana.

---

## Lo que dice cada Streamer

### ArgenTrader — Grid Bots (Pionex)
Presenta los fundamentos del grid bot como concepto:

- **3 modos**: Long (sesgo alcista), Short (sesgo bajista), Neutral (opera ambos lados, máxima eficiencia lateral).
- **Métrica clave**: Grid Profit (beneficio realizado consolidado), NO Trend PNL (ganancia/pérdida no realizada, momentánea).
- **Estrategia de liberación**: cuando el Grid Profit iguala la inversión (break even), retirar el capital original y operar con "dinero de la casa".
- **Apalancamiento**: máximo 5x, preferible 3x.
- **Entorno**: solo mercados laterales o consolidaciones, con rango definido por soportes/resistencias del AT.
- **Número de grids**: a más rejillas, más operaciones por oscilación.
- **Configuración manual** > copiar estrategias de terceros.
- **Ventaja psicológica**: el bot elimina emociones, dudas y errores de ejecución. El trader muchas veces no vende por codicia ni compra por miedo.

### ZCoinTV — Gestión de Riesgo con Bots
Establece los principios de seguridad operativa:

- **Selección de activos**: empezar SOLO con Bitcoin (high cap, menor volatilidad). No operar activos que no sepas tradear manualmente.
- **Bots manuales vs automáticos**: manuales solo si tienes experiencia en trading (tú defines parámetros). Automáticos: probar con capital pequeño, no fiarse de históricos con % altos.
- **El bot NO tiene criterio**: maneja mecánica (abrir/cerrar según reglas), pero no sabe cuánto dinero tienes, qué % de pérdida es aceptable, dónde poner el SL correctamente. El criterio lo aporta el humano.
- **Stop Loss IMPRESCINDIBLE**: nunca usar un bot sin SL. Error común: "el bot se encarga". El bot no sabe gestión de riesgo.
- **Las 3 patas del trading y los bots**:
  - Análisis técnico/fundamental → el bot puede ayudar
  - Psicotrading → desaparece con bots (el bot no tiene emociones)
  - **Gestión de riesgo → sigue en tus manos**, no la descuides
- **Riesgo máximo**: 5% de la cuenta de futuros en un solo stop loss.
- **Apalancamiento controlado**: punto de liquidación lejos del stop loss.

### ZCoinTV — Wyckoff Automatizado con Bots de Grid
Estrategia avanzada que integra metodología Wyckoff con bots:

- **Principio**: Wyckoff define qué va a hacer el rango (romper arriba/abajo). Una vez identificada la dirección, el bot ejecuta dentro del rango con SL en punto estructural de invalidación.

**Correspondencia Wyckoff → Bot**:

| Fase Wyckoff | Dirección del Bot | Stop Loss |
|-------------|-------------------|-----------|
| Acumulación / Reacumulación | LONG (solo largos) | Por debajo del spring |
| Distribución / Redistribución | SHORT (solo cortos) | Por encima del UTAD |
| Fase B (sin dirección) | NEUTRAL | Límites superior/inferior del rango |

- **Timing**: activar bot después de la fase C (spring o UTAD confirmados). Tradear la fase D.
- **Ejemplo acumulación**: identificar acumulación → spring (barrida inferior) = fase C → bot LONG → SL debajo del spring. Si la acumulación falla, SL ejecutado con pérdida controlada (2-5%).
- **Fase B con Neutral**: solo en temporalidades altas (4h, diario). En 15min la fase B dura muy poco.
- **Spot vs Futuros**: spot para swing (horizonte amplio), futuros para corto plazo.
- **Prerrequisito**: dominar Wyckoff primero. Sin eso, la estrategia no funciona.

### ZCoinTV — Bots Grid de Futuros en Bitget (Herramienta)
Guía práctica de configuración en la plataforma:

- **Malla (grid)**: órdenes escalonadas aritméticas (valores fijos) o geométricas (porcentajes).
  - Aritmético → rangos pequeños, mercados muy laterales.
  - Geométrico → mercados tendenciales, rangos con expansión amplia.
- **3 modos**: Long, Short, Neutral (misma lógica de ArgenTrader).
- **Configuración de malla**: límite inferior en soporte, límite superior en resistencia. Número de grids define cuántas órdenes escalonadas.
- **Apalancamiento**: ≤5x, ideal 2-3x. Define el punto de liquidación. A más apalancamiento, más riesgo.
- **Configuración avanzada**:
  - Stop loss: obligatorio.
  - Precio de activación: bot no opera hasta que precio llegue a X.
  - Activación por RSI / Bollinger.
  - Grid trailing: malla se mueve con el precio (experimental).
  - **Transferencia automática de margen: NO recomendado** (puede drenar fondos sin control).
- **Estrategias IA predefinidas**: útiles para explorar, pero el objetivo es crear bots propios.
- **Modo Long/Short para principiantes**: SL más claro que en neutral.
- **Neutral**: solo con rangos bien definidos (soporte y resistencia claros).

### ScottFDX — El Mejor Bot: Grid de Futuros en Bitget
Resultado de meses de pruebas con todos los bots de Bitget:

- **Grid de Futuros Neutral como #1**: aprovecha tanto largos como cortos sin predecir dirección.
- **Futuros > Spot**: el Grid Spot solo compra barato y vende caro (solo subidas). El de Futuros Neutral especula en ambas direcciones.
- **Caso real ASTER**: 43 días activo, colocado en el momento de la caída, pérdida máxima acumulada muy pequeña, excelente crecimiento posterior pese a la corrección.

**Configuraciones por nivel de riesgo**:

| Nivel | Rejillas | Rango | Apalancamiento | Perfil |
|-------|----------|-------|----------------|--------|
| Conservador | ~10 | Amplio | Bajo | Menos operaciones, menos riesgo |
| Moderado | ~20-25 | Medio | Moderado | Balance riesgo/operaciones |
| Agresivo | 50-80+ | Estrecho | Mayor | Más operaciones, más exposición |

- **Ejemplo Bitcoin**: rango $75,000-$95,000, 80 rejillas, apalancamiento 5x, capital $1,000 → capital fragmentado en 80 órdenes pequeñas.
- **Apalancamiento**: Bitcoin permite más; con altcoins REDUCIR siempre.
- **IA vs Manual**: no usar estrategias IA predefinidas. Crear bot manual en modo neutral da control total.
- **Gestión flexible**: se puede parar, modificar y reactivar sin coste. Si el precio sale de la malla y vuelve, el bot reintroduce órdenes automáticamente.
- **Configuración de salida**: precio mínimo de salida como SL (bajo mínimos), precio máximo de TP (zona de máximos).

---

## Puntos de Acuerdo

1. **Grid de Futuros modo Neutral como configuración óptima**: ArgenTrader, ZCoinTV y ScottFDX coinciden en que el modo neutral (largos abajo + cortos arriba) es el más versátil para mercados laterales.
2. **Apalancamiento bajo (≤5x, ideal 2-3x)**: los 3 streamers son consistentes. ArgenTrader: ≤5x, preferible 3x. ZCoinTV: ≤5x, puntos de liquidación lejos. ScottFDX: ≤5x, menos en altcoins.
3. **Stop Loss SIEMPRE y obligatorio**: ArgenTrader lo asume; ZCoinTV lo enfatiza como innegociable; ScottFDX configura precio mínimo de salida.
4. **Empezar con Bitcoin**: ZCoinTV y ScottFDX coinciden en que BTC es más "elegante" y menos ruidoso para bots. ArgenTrader no especifica pero opera con criterio similar.
5. **No usar estrategias IA predefinidas**: ZCoinTV y ScottFDX recomiendan crear bots manuales propios sobre confiar en IA de la plataforma.
6. **Más rejillas = más operaciones por oscilación**: concepto consistente en los 3.
7. **Configuración manual sobre copiar**: todos enfatizan que el trader debe definir sus propios parámetros.
8. **Capital de prueba pequeño al empezar**: ZCoinTV y ScottFDX lo recomiendan explícitamente.
9. **Mercados laterales/consolidaciones = mejor entorno**: los grid bots brillan en rangos, no en tendencias fuertes que rompan la malla.
10. **El bot elimina el factor emocional**: ArgenTrader lo destaca como ventaja; ZCoinTV dice que el psicotrading "desaparece" con bots.
11. **El criterio humano en gestión de riesgo sigue siendo indispensable**: ZCoinTV es el más enfático. Los otros lo asumen en sus reglas.

---

## Desacuerdo / Complementario

| Aspecto | Diferencias y complementos |
|---------|---------------------------|
| **Plataforma** | ArgenTrader habla de Pionex. ZCoinTV y ScottFDX de Bitget. El concepto de grid bot es el mismo. Complementario: diferentes exchanges, misma mecánica. |
| **Metodología Wyckoff** | Exclusivo de ZCoinTV. Aporta una capa de análisis para decidir cuándo usar Long, Short o Neutral. ArgenTrader y ScottFDX no integran Wyckoff. Es un complemento avanzado valioso. |
| **Niveles de riesgo** | ScottFDX es el único que detalla 3 niveles (conservador, moderado, agresivo) con parámetros concretos. Complementa las reglas generales de los otros. |
| **% de riesgo máximo** | ZCoinTV: 5% por operación. ArgenTrader no especifica %. ScottFDX no da % fijo pero sugiere capital pequeño. ZCoinTV es el más preciso en este parámetro. |
| **Estrategia de liberación** | Exclusiva de ArgenTrader: retirar capital al llegar a break even y operar con ganancias. No mencionada por otros. Complemento útil de gestión de capital. |
| **Grid Profit vs Trend PNL** | ArgenTrader enfatiza mirar solo Grid Profit (realizado), no Trend PNL (no realizado). ZCoinTV y ScottFDX no lo mencionan pero es implícito en su enfoque. |
| **Bots automáticos vs manuales** | ZCoinTV advierte específicamente sobre bots automáticos (IA no controlada). ScottFDX refuerza: no usar estrategias IA predefinidas. Visión alineada. |
| **Temporalidades para Wyckoff** | ZCoinTV especifica que fase B con Neutral solo funciona en 4h/diario. Detalle táctico no cubierto por otros. |
| **Aritmético vs Geométrico** | Detalle de ZCoinTV sobre cómo espaciar órdenes en la malla. No cubierto por ArgenTrader ni ScottFDX. |
| **Transferencia automática de margen** | ZCoinTV advierte NO activarla. ScottFDX menciona que existe pero no toma postura fuerte. |
| **Spot vs Futuros** | ScottFDX dice que Grid Spot es "el caso más sencillo" pero limitado a subidas. ZCoinTV: spot para swing, futuros para corto plazo. ArgenTrader no distingue explícitamente. |
| **Bot como ventaja psicológica** | ArgenTrader: elimina 3 fuentes de error. ZCoinTV: psicotrading desaparece con bots. ScottFDX: no aborda el ángulo psicológico directamente. |

---

## Reglas Consolidadas

### Selección y Preparación
1. Empezar SIEMPRE con Bitcoin (BTC). Es más "elegante", menos ruidoso y más predecible en rangos que altcoins o low caps.
2. No operar con bots activos que no sepas tradear manualmente. El criterio sobre el activo lo aporta el trader.
3. Aprender y dominar la metodología Wyckoff antes de integrar bots direccionales (Long/Short según acumulación/distribución).

### Configuración del Bot
4. **Usar Grid de Futuros en modo Neutral como bot principal**: permite beneficiarse de largos y cortos sin predecir la dirección.
5. **NUNCA activar un bot sin Stop Loss**. El bot no tiene criterio de gestión de riesgo. Definir el SL según estructura técnica y tolerancia al riesgo.
6. **Apalancamiento máximo 5x, ideal 2-3x**. Punto de liquidación siempre más allá del stop loss. En altcoins, reducir aún más el apalancamiento.
7. **Crear bots manuales**, no usar estrategias IA predefinidas de la plataforma.
8. Definir el rango con soporte y resistencia válidos del análisis técnico. Límite inferior en soporte, superior en resistencia con margen para volatilidad.
9. A más rejillas (50-80+), más fragmentado el capital y más operaciones de corto plazo. A menor número (~10), perfil conservador con menos operaciones.
10. Usar espaciado **aritmético** para rangos pequeños/mercados muy laterales. **Geométrico** para rangos amplios/tendenciales.

### Gestión de Riesgo
11. Máximo 5% de la cuenta de futuros en riesgo por operación (distancia SL).
12. Probar bots nuevos con capital pequeño. Escalar gradualmente tras validar track record.
13. No activar transferencia automática de margen (puede drenar fondos de spot sin control).
14. Monitorear Grid Profit (beneficio realizado), no Trend PNL (no realizado momentáneo).

### Estrategia Wyckoff + Bots (Avanzado)
15. Acumulación/Reacumulación → bot LONG, con SL por debajo del spring.
16. Distribución/Redistribución → bot SHORT, con SL por encima del UTAD.
17. Fase B sin dirección clara → bot NEUTRAL, solo en temporalidades altas (4h o diario).
18. Activar el bot solo después de confirmada la fase C (spring o UTAD). No antes.

### Operación y Mantenimiento
19. Para principiantes en bots: empezar con modo Long o Short (SL más claro que Neutral).
20. Modo Neutral solo cuando el rango tenga soporte y resistencia bien definidos.
21. Si el precio sale temporalmente de la malla, no hacer nada. Al reingresar, el bot reintroduce órdenes automáticamente.
22. Se puede parar, modificar parámetros y reactivar el bot sin coste adicional.
23. Cuando el Grid Profit iguale la inversión inicial, considerar retirar el capital original y operar con "dinero de la casa".
24. Cerrar el bot si el precio rompe el rango de forma definitiva (cambio de estructura).
25. Hacer seguimiento periódico del track record y ajustar parámetros según condiciones del mercado.

---

## Fuentes

| Streamer | Concepto | Archivo |
|----------|----------|---------|
| ArgenTrader | Grid Bots (Pionex) | `argentrader/conceptos/grid-bots.md` |
| ZCoinTV | Gestión de riesgo con bots | `zcointv/conceptos/gestion-riesgo-bots.md` |
| ZCoinTV | Wyckoff automatizado con bots | `zcointv/setups/wyckoff-bots-automatizados.md` |
| ZCoinTV | Bots grid de futuros en Bitget | `zcointv/herramientas/bots-grid-futuros-bitget.md` |
| ScottFDX | El mejor bot de trading (Bitget) | `scottfdx/herramientas/mejor-bot-trading-cripto-bitget-grid-futuros.md` |
