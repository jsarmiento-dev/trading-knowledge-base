# Bots de Grid de Futuros en Bitget

## Definición
Los bots de grid de futuros en Bitget son herramientas de trading automatizado que utilizan una **malla (grid)** de órdenes escalonadas para abrir y cerrar posiciones largas o cortas dentro de un rango de precios definido. El bot trabaja con tres modos direccionales: **long** (solo largos), **short** (solo cortos) y **neutral** (largos abajo + cortos arriba), permitiendo adaptar la automatización a acumulaciones, distribuciones o rangos sin dirección clara.

## Fuente: ZCoinTV
- **Video**: "Cómo usar bots de futuros en Bitget de forma rentable"
- **ID**: 4ozS13DqQ_Q
- **Playlist**: Tutoriales de bots de Bitget

## Conceptos Clave

### ¿Qué es un Grid de Futuros?
- Bot que trabaja con el concepto de **malla**: órdenes de compra/venta escalonadas
- Las órdenes se distribuyen según criterios **aritméticos** (valores fijos) o **geométricos** (porcentajes)
- El usuario define: límites superior/inferior, número de grids, apalancamiento, stop loss
- Disponible para todos los pares USDT y USDC en futuros de Bitget

### Tres Modos del Bot

| Modo | Comportamiento | Caso de Uso |
|------|---------------|-------------|
| **Long** | Solo abre largos, cierra parciales al subir | Acumulaciones (fase D), tendencias alcistas |
| **Short** | Solo abre cortos, cierra parciales al bajar | Distribuciones (fase D), tendencias bajistas |
| **Neutral** | Largos en la parte baja, cortos en la parte alta | Rangos laterales (fase B Wyckoff) sin dirección clara |

### Aritmético vs Geométrico

| Tipo | Cómo espacia las órdenes | Mejor para |
|------|-------------------------|------------|
| **Aritmético** | Valores fijos ($100, $200, $500) | Rangos pequeños, fluctuaciones frecuentes, mercados muy laterales |
| **Geométrico** | Porcentajes (1%, 2%, 3%) | Mercados tendenciales, rangos con expansión amplia |

### Configuración de la Malla (Ejemplo)
1. Identificar rango en el gráfico con soporte y resistencia claros
2. Límite inferior: precio mínimo donde el bot opera → idealmente en soporte
3. Límite superior: precio máximo donde el bot opera → idealmente en resistencia
4. Número de grids: define cuántas órdenes escalonadas dentro del rango
5. Una vez superados los límites, el bot deja de abrir nuevas operaciones (mantiene las abiertas)

### Apalancamiento
- **Usar SIEMPRE apalancamiento bajo** (≤5x, idealmente 2-3x)
- El apalancamiento define el punto de liquidación = stop loss efectivo
- A más apalancamiento, más cerca está la liquidación y más riesgo
- En modo neutral, verificar liquidación tanto por arriba (shorts) como por abajo (longs)

### Configuración Avanzada
- **Stop loss**: obligatorio; define precio de salida por pérdidas
- **Precio de activación**: el bot no opera hasta que el precio llegue a X
- **Activación por RSI / Bollinger**: abrir bot solo en sobreventa/sobrecompra
- **Condiciones de finalización**: cerrar bot al alcanzar niveles de RSI/Bollinger
- **Grid trailing**: la malla se mueve con el precio (experimental)
- **Transferencia automática de margen**: NO recomendado activarlo
- **Reserve fund protection**: activado por defecto

### Estrategias IA Predefinidas
- Bitget ofrece estrategias creadas por IA con datos de rentabilidad histórica, inversión mínima y duración recomendada
- Útil para explorar, pero el objetivo es aprender a **crear tus propios bots**

## Reglas Operativas
1. **Empieza con Bitcoin**: es más "elegante" y menos ruidoso que altcoins/low caps para bots.
2. **Siempre usa stop loss**: nunca actives un bot sin SL definido. El bot no tiene criterio de gestión de riesgo.
3. **Apalancamiento bajo (≤5x)**: puntos de liquidación lejos, margen de seguridad amplio.
4. **Vigila el bot**: monitorea qué está haciendo, especialmente al principio.
5. **Modo Long/Short para empezar**: el stop loss es más claro que en neutral; ideal para principiantes en bots.
6. **Neutral solo con rangos bien definidos**: soporte y resistencia claros antes de configurar.
7. **Prueba con capital pequeño**: si es tu primera vez con un tipo de bot, arriesga poco.
8. **No actives transferencia automática de margen**: puede drenar fondos de spot sin control.

## Frase Destacada
> "Nunca uséis un bot sin poner un punto de stop loss o sin tener clara la gestión de riesgo, porque al final si el bot enfrenta una situación de volatilidad o habéis hecho algún parámetro equivocado, se os puede liquidar la cuenta."
