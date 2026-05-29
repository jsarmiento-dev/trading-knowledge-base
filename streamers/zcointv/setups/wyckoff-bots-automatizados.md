# Wyckoff Automatizado con Bots de Grid

## Definición
Estrategia avanzada que combina la **metodología Wyckoff** (análisis de acumulación/distribución) con **bots de grid trading** (futuros/spot) para automatizar entradas en largos o cortos una vez identificada la fase C del proceso Wyckoff. Los niveles de stop loss se definen según la estructura Wyckoff (spring, UTAD), lo que da puntos de invalidación claros y naturales para el bot.

## Fuente: ZCoinTV
- **Video**: "Cómo hacer trading con Wyckoff automáticamente (Bots Avanzados)"
- **ID**: bJb_mUeR01Y
- **Prerrequisitos**: playlist completa de Wyckoff + videos introductorios de bots + videos de grid trading

## Conceptos Clave

### Principio Fundamental
Wyckoff ayuda a definir **qué va a hacer el rango** (romper arriba o abajo). Una vez identificada la dirección, los bots se usan para ejecutar dentro del rango con un stop loss colocado en un punto estructural evidente de invalidación.

### Correspondencia Wyckoff → Bot

| Fase Wyckoff | Dirección del Bot | Stop Loss |
|-------------|-------------------|-----------|
| **Acumulación / Reacumulación** (rompe arriba) | **LONG** (solo largos) | Por debajo del spring |
| **Distribución / Redistribución** (rompe abajo) | **SHORT** (solo cortos) | Por encima del UTAD |
| **Fase B** (sin dirección clara) | **NEUTRAL** (largos y cortos) | Límites superior/inferior del rango |

### Timing: Fase C como Disparador
- El bot se activa **después de ocurrida la fase C**
- Fase C ideal: con **spring** (acumulación) o **UTAD** (distribución) — dilatación fuerte que confirma dirección
- Una vez confirmada la fase C, se tradea la **fase D** (LPS/SOS en acumulación, LPY/SOW en distribución)

### Ejemplo: Acumulación con Spring
1. Se identifica acumulación en temporalidad alta
2. Ocurre spring (barrida por la parte inferior) = fase C
3. Se coloca bot **LONG**
4. Límite inferior de la malla: niveles de soporte
5. Límite superior: niveles de resistencia principales
6. **Stop loss por debajo del spring** (ej: si spring está en 97,500, SL debajo de eso)
7. Si la acumulación falla tras el spring, el SL se ejecuta con pérdida controlada (2-5%)

### Fase B con Bot Neutral
- Cuando el rango aún no tiene dirección clara (fase B), usar bot **NEUTRAL**
- El bot abre largos abajo y cortos arriba
- **Preferir temporalidades altas** (4h, diario) para fase B: en 15min la fase B puede durar muy poco y la malla no funciona bien
- Ideal para swing trading o rangos amplios en el tiempo

## Reglas Operativas
1. **Saber Wyckoff primero**: sin la playlist de Wyckoff, esta estrategia no tiene sentido.
2. **Esperar la fase C**: el bot se activa solo después de spring (long) o UTAD (short). No antes.
3. **Fase B = neutral**: solo cuando el rango es amplio y en temporalidad alta (4h o más).
4. **Stop loss estructural**: siempre por debajo del spring (long) o por encima del UTAD (short).
5. **Riesgo máximo 5%**: si el SL se ejecuta, la pérdida no debe superar el 5% de la cuenta de futuros.
6. **Apalancamiento bajo**: punto de liquidación siempre más allá del stop loss.
7. **Acumulaciones y reacumulaciones → LONG**. Distribuciones y redistribuciones → SHORT.
8. **Spot vs Futuros**: spot para horizonte temporal amplio (swing), futuros para corto plazo.

## Frase Destacada
> "Es bastante evidente que si la acumulación se va a cumplir, ese spring no se debería vulnerar y por tanto ese stop loss se va a respetar. Si estamos en fase C con spring o UTAD, podemos ya pasar a trabajar ese rango con long o con short."
