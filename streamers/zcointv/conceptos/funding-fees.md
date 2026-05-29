# Funding Fees (Tasas de Financiación)

## Definición
Los funding fees (tasas de financiación) son comisiones periódicas que se pagan o cobran entre operadores con posiciones abiertas en futuros. Son un mecanismo que mantiene el precio del futuro anclado al precio spot. Se liquidan **cada 8 horas** (3 veces al día) en todos los exchanges de criptomonedas. Pueden ser **positivos** (pagas) o **negativos** (cobras), y aplican tanto a posiciones largas como cortas.

## Fuente: ZCoinTV
- **Video**: "¿Qué son los Funding Fees y cómo ganar dinero con ellos?"
- **ID**: DHgFolNDAqE

## Conceptos Clave

### Mecanismo de Funding Fee
| Escenario | Efecto |
|-----------|--------|
| **Funding positivo + estás en LARGO** | Tú **pagas** a los que están en corto |
| **Funding positivo + estás en CORTO** | Los largos **te pagan** a ti |
| **Funding negativo + estás en LARGO** | Los cortos **te pagan** a ti |
| **Funding negativo + estás en CORTO** | Tú **pagas** a los que están en largo |

- La **parte interesante**: no siempre hay que pagar. Muchas veces **te pagan a ti**.
- Es una comisión entre traders, no va al exchange (salvo una pequeña parte).
- Ocurre en **todos los pares de futuros de todos los exchanges crypto**.

### Bot de Arbitraje de Tasas de Financiación (Bitget)
- Bitget ofrece un bot **automático** específico para funding fees
- Ruta: Trading → Bots → Futuros → **Arbitraje de tasas de financiación**
- Funciona automáticamente, sin configuración manual compleja
- Disponible para Bitcoin, Ethereum, Solana, Pepe y otros activos

### Métricas del Bot
- **APR**: rendimiento porcentual anualizado. Revisar SIEMPRE el de 90 días, no el de 3 días.
- **Tasa de financiación actual**: se muestra con cuenta regresiva hasta el próximo cobro
- **Historial**: permite ver tasas pasadas y su volatilidad

### Ejemplos de APR (aproximados del video)
| Activo | APR 90 días aprox |
|--------|-------------------|
| Bitcoin | ~6.24% |
| Ethereum | ~7.28% |
| Solana | ~3.92% |
| Pepe | ~17-18% (mucho más volátil) |

### Volatilidad del Funding Fee = Riesgo
- Activos con funding fee muy cambiante (Pepe, meme coins) → **mayor riesgo**
- Activos con funding fee más estable (BTC, ETH) → **menor riesgo**
- Un APR alto en 3 días puede venirse abajo o volverse negativo semanas después

## Reglas Operativas
1. **Usar cantidades pequeñas** al principio: probar cómo funciona sin arriesgar mucho capital.
2. **Fijarse en el APR de 90 días**, no en el de 3 días (muy poco tiempo, puede ser engañoso).
3. **Preferir activos de menor volatilidad** para empezar: Bitcoin, Ethereum.
4. **No confundir con staking**: no es beneficio garantizado, tiene riesgo y renta variable.
5. **Configuración de lote**: poner montos por lote bajos (ej. 30-60 USDT) para tener margen de maniobra si el bot no gusta.
6. **Monitorear historial** de tasas para evaluar estabilidad del funding fee del activo.
7. El bot solo se puede crear, monitorear y finalizar; el funcionamiento es automático.

## Frase Destacada
> "Muchas veces el funding fee nos paga a nosotros. Los funding fees no son solo una comisión a pagar: puede ser una forma interesante de sacarle un beneficio al mercado."
