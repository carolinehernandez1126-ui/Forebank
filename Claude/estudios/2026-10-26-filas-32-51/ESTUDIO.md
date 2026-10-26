# Estudio 4: filas 32–51 de la lista. Decisiones discrecionales

| Campo | Valor |
|---|---|
| Autor | Claude, `claude-opus-5-5` (Claude Code). Fundamentales apoyados por dos subagentes de Claude; los datos técnicos y de posicionamiento, la verificación y las decisiones son míos |
| Cierre | 2026-10-26 ~12:50 UTC (07:50 America/Bogota). Datos de mercado de las 12:40 UTC, verificados de nuevo a las 12:45 UTC (NEAR 4,5609 · PUMP 0,004257 · BTC 80.208) |
| Activos | KAITO, LDO, LIGHTER, LINK, LIT, LTC, MON, MOODENG, NEAR, ONDO, OP, PENDLE, PENGU, PEPE, PNUT, POL, POPCAT, PUMP, RENDER, SP |
| Enfoque | **Por instrucción del propietario, la decisión no depende de backtests.** Se basa en la estructura técnica actual, el posicionamiento en derivados, el contexto de mercado, los fundamentales y los catalizadores, con probabilidades estimadas explícitamente. **Las probabilidades son juicio de Claude, no frecuencias calibradas** |
| Límites aplicados | Riesgo ≤ 0,25% por trade; riesgo abierto total ≤ 0,5%; RR neto ≥ 2 con costos de 55 bps por lado; tope de profundidad del Lab (1% de los asks a 10 bps); regla de liquidez (spread ≤ 20 bps, volumen ≥ 250k USD); el gate del Lab exige ≥ 250 velas diarias |

## Decisiones

| Activo | Decisión | Plan / disparador |
|---|---|---|
| **NEAR** | **COMPRA CONDICIONADA (orden límite)** | Límite 4,4000 · stop 4,0200 (−8,6%) · objetivo 5,4000 (+22,7%) · RR neto 2,22 · **0,20% de riesgo = 100 USD** (~234,5 NEAR, ~1.032 USD) · válida hasta el 2026-11-02 00:00 UTC |
| **PUMP** | **COMPRA CONDICIONADA (orden límite), tamaño mínimo** | Límite 0,004000 · stop 0,003560 (−11%) · objetivo 0,005100 (+27,5%) · RR neto 2,18 · el tope de profundidad del Lab limita el nocional a ~290 USD (72.500 PUMP; riesgo de 35 USD = 0,07%) · válida hasta el 2026-11-02 |
| PEPE | ESPERAR | Largos minoristas saturados. Solo se considera tras una barrida hasta 3,80e-6 (stop 3,45e-6, objetivo 4,75e-6, RR 2,32, 0,10% de riesgo) y si el ratio long/short de cuentas baja de 2,0 |
| LINK | ESPERAR | Tendencia bajista (máximos decrecientes). Se reactiva con un cierre diario > 12,06 (último máximo decreciente) |
| LTC | ESPERAR | Tendencia bajista apoyada en el soporte de 56,65. Se reactiva con un cierre diario > 59,42; si pierde 55, el siguiente soporte es 51,6 |
| ONDO | ESPERAR | Tendencia bajista. Se reactiva con un cierre diario > 0,4222 |
| RENDER | ESPERAR | En el soporte de 1,718 sin señal de giro. Se reactiva con un cierre diario > 1,943 |
| OP | ESPERAR | −24% en 30 días. Se reactiva con un cierre diario > 0,1294 (SMA20) |
| POL | ESPERAR | Se reactiva con un cierre diario > 0,0976 |
| PENGU | **EVITAR** | Desbloqueo ~17-nov, cierre de Abstract el 15-dic y libro muy delgado (4k USD). Se reconsidera con un cierre diario > 0,00841 después del desbloqueo |
| MON | **EVITAR** | Cliff el 24-nov de ~56% del circulante y libro muy delgado (1k USD a 10 bps). Se reconsidera solo después del desbloqueo |
| LIGHTER | NO OPERABLE (aún) | Solo 70 velas diarias en Kraken; el gate del Lab exige 250 |
| KAITO, LDO, LIT, MOODENG, PENDLE, PNUT, POPCAT | NO ELEGIBLES | Liquidez en Kraken: KAITO (30k USD al día), LDO (spread de 27 bps), LIT (59 bps, 20k USD), MOODENG (41 bps), PENDLE (20,5 bps), PNUT (49 bps), POPCAT (71 bps) |
| SP | NO ELEGIBLE | No hay par USD en Kraken |

**Riesgo total si se llenan ambas órdenes:** 0,27% del equity (100 + 35 USD), por debajo del 0,5%. NEAR y PUMP están correlacionados con el riesgo cripto general, así que el riesgo se trata como si fuera uno solo.

**Interruptor global:** si BTC cierra un día por debajo de **76.000** (la zona de mínimos de oct-2026 está en 76.000–76.900), se cancelan las órdenes no ejecutadas y no se abren posiciones nuevas. Los stops ya colocados se mantienen.

**Regla FOMC (27–28 oct):** las dos órdenes están por debajo del precio actual, así que solo se llenan si hay una caída. Si se llenan durante el FOMC, se respeta el stop sin moverlo. No se compra a mercado antes del anuncio.

## Contexto de mercado (2026-10-26 12:40 UTC)

| Indicador | Lectura | Interpretación |
|---|---|---|
| BTC | 80.048 · −4,8% en 30 días · +9,7% sobre SMA200, −2,1% bajo SMA50 · RSI diario 42 | Corrección dentro de una tendencia de medio plazo todavía alcista; soporte inmediato en 79.709 |
| ETH | 2.326 · −13,6% en 30 días · RSI 34 | Más débil que BTC |
| Fear & Greed | 50 (hace 7 días 59; hace 30 días 70) | Enfriamiento, sin pánico |
| Dominancia de BTC | 59,5% | Rotación desde altcoins hacia BTC: viento en contra para altcoins |
| Capitalización total | 2,71 T USD, −2,7% en 24 h | Presión vendedora |
| Funding y open interest de BTC | +0,8 pb cada 8 h; open interest −1,8% en 7 días y −5,9% en 30 días | Desapalancamiento ordenado |
| Long/short de cuentas en BTC | 1,66 → 2,17 en 7 días | Los minoristas compran la caída: señal contraria levemente negativa |
| Macro | FOMC el 27–28 oct; salidas de ETF de BTC y ETH en octubre; fondos federales 3,88% | Riesgo de evento en las próximas 48 h |

**Lectura general:** es un mercado de corrección con rotación hacia BTC. En este entorno solo compro **activos con fuerza relativa demostrada, en soportes y con el apalancamiento ya limpio**, nunca altcoins en tendencia bajista. Probabilidades subjetivas para los próximos 30 días: BTC por encima de 76.000 ~65%; un nuevo tramo bajista de altcoins (otro −15% en el agregado) ~35%.

## Análisis técnico y de posicionamiento (19 activos con par en Kraken)

| Activo | 30 días | 90 días | vs. SMA50 | vs. SMA200 | RSI diario | Fuerza vs. BTC (30 días) | Funding (8 h) | Open interest 7 días |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| NEAR | −7,3% | **+172%** | **+7,4%** | **+89%** | 48 | **−2,7%** | −0,03 pb | −11,5% |
| PEPE | −4,8% | +51,5% | +5,1% | +24,1% | 51 | 0,0% | +1,0 pb | +9,2% |
| PUMP | +0,9% | +99,9% | −10,1% | +52,0% | 41 | **+6,0%** | +0,2 pb | −14,2% |
| RENDER | −11,6% | +21,8% | −3,2% | +2,2% | 42 | −7,2% | +0,5 pb | −11,4% |
| LINK | −17,9% | +36,7% | −10,1% | +15,0% | 36 | −13,7% | +0,9 pb | −8,3% |
| LTC | −21,9% | +23,2% | −7,6% | +8,8% | 37 | −17,9% | +0,8 pb | −2,9% |
| ONDO | −25,9% | +3,2% | −8,2% | +10,4% | 39 | −22,1% | −0,1 pb | −7,4% |
| OP | −24,2% | +27,9% | −10,0% | −1,2% | 40 | −20,4% | 0,0 pb | −0,3% |
| POL | −23,2% | +21,3% | −12,2% | 0,0% | 36 | −19,3% | −0,3 pb | −6,9% |
| PENGU | −27,3% | +25,7% | −10,2% | −2,7% | 40 | −23,6% | +0,3 pb | −3,8% |
| MON | −18,4% | +7,1% | −14,8% | −14,4% | 40 | −14,3% | −0,1 pb | −4,5% |
| LIGHTER | −34,5% | — | −20,9% | — | 43 | −31,2% | — | — |
| No elegibles | KAITO −30%, LDO −26%, LIT −29%, MOODENG −24%, PENDLE −23%, PNUT −27%, POPCAT −31% | | | | | | | |

### NEAR: tesis de compra
- **Estructura:** subió de 1,54 (julio) a 6,00 (inicio de octubre) y lleva unas 3 semanas en una consolidación lateral entre 4,25 y 5,50, con volumen decreciente (de 30–50 M a 13–18 M USD diarios). Es el patrón típico de una bandera o rango de continuación tras un impulso. Precio: 4,59, por encima de la SMA50 (4,27) y muy por encima de la SMA200.
- **Posicionamiento:** open interest −11,5% en 7 días, funding ≈ 0 y ratio de cuentas a la baja (1,48 → 1,31). El apalancamiento especulativo ya salió. Los grandes traders siguen largos (2,11).
- **Fuerza relativa:** es el único de los 20 que casi no ha perdido frente a BTC en 30 días (−2,7%).
- **Plan:** comprar en la parte baja del rango (4,40), no en medio. El stop en 4,02 queda por debajo de los mínimos de 4h (4,25) y del diario (4,29), con un margen de ~0,5 ATR: si se pierde 4,25, el rango se rompe y la tesis queda invalidada. El objetivo en 5,40 queda justo bajo el techo del rango (5,45).
- **Probabilidades (subjetivas):** ~55% de que la orden se llene en 7 días. Si se llena, ~45% de que llegue al objetivo antes que al stop. Valor esperado por trade ejecutado ≈ 0,45 × 2,22 − 0,55 × 1 ≈ **+0,45 R**.
- **Qué la invalida:** cierre diario < 4,25 antes de que se llene la orden (se cancela), interruptor de BTC, o un evento negativo específico de NEAR (ver fundamentales).

### PUMP: tesis de compra de tamaño mínimo
- **Estructura:** subió de 0,0018 a 0,0068 en 90 días; ahora comprime entre 0,0038 y 0,0052 con volumen a la baja. Cotiza +52% sobre su SMA200 y es el único con fuerza relativa positiva frente a BTC en 30 días (+6%).
- **Posicionamiento:** minoristas ligeramente cortos (0,90), grandes traders largos (1,98) y open interest −14% en 7 días. Hay potencial de squeeze sin exceso de largos.
- **Plan:** límite en 0,00400, sobre la zona de soporte 0,0038–0,0039; stop en 0,00356, bajo los mínimos de oscilación de 0,00376–0,00379; objetivo en 0,00510, bajo la resistencia de 0,0052.
- **Tamaño:** el tope de profundidad del Lab lo limita a ~290 USD. Lo acepto: el libro de PUMP en Kraken es delgado (29k USD a 10 bps) y un activo con un ATR del 13% justifica un tamaño menor.
- **Probabilidades (subjetivas):** ~50% de que se llene la orden; si se llena, ~42% de llegar al objetivo. Valor esperado ≈ **+0,34 R**.

### PEPE: por qué espero
Técnicamente está bien (por encima de sus medias y con fuerza relativa neutral). Pero los largos minoristas están saturados (ratio de cuentas 2,53 y subiendo, open interest +9% y funding positivo) y en 4h marca máximos decrecientes (5,11 → 4,54e-6). Es el perfil típico de una barrida hacia los mínimos de oscilación de 3,77e-6 antes de seguir. Solo entraría después de esa barrida.

### Activos en tendencia bajista (LINK, LTC, ONDO, RENDER, OP, POL, PENGU, MON)
Todos tienen máximos y mínimos decrecientes, caen entre −12% y −27% en 30 días frente a BTC y cotizan bajo su SMA20 y su SMA50. Comprar en soporte ahí sería apostar por un suelo sin confirmación. Cada uno tiene su nivel de reactivación en la tabla. Probabilidad subjetiva de que alguno dé ese cierre en 2 semanas: ~25–30% cada uno; casi todo depende de BTC.

## Fundamentales y catalizadores

**Identidades:** Kraken lista **LIGHTER** (Lighter, el DEX de perpetuos; en CoinGecko su símbolo es "LIT") y **LIT**, que en Kraken es Litentry: un ticker huérfano, porque el token migró a Heima (HEI) en feb-2025. La fila "LIT" de la lista es ambigua entre los dos. Ninguno es operable hoy. **MON** = Monad (L1).

| Activo | Catalizadores y fundamentales (≤ 45 días) | Sesgo | Efecto en la decisión |
|---|---|---|---|
| NEAR | ETF spot con staking de Bitwise (NRR) desde el 29-sep (~66 M USD en activos); nearcore 2.14 aumenta la quema de comisiones; incidente de seguridad de ~3,8 M el 1-oct; comisiones on-chain pequeñas (216k USD en 30 días); sin desbloqueos | Neutral-positivo | **Confirma la compra condicionada** |
| MON | **Cliff el 24-nov: ~6,66 B MON ≈ 56% del circulante** (Tokenomist; otra fuente dice 16,6 B, con datos desactualizados); la emisión supera en mucho a la quema; cotiza por debajo del precio de la venta pública | Muy negativo | **ESPERAR → EVITAR hasta después del 24-nov** |
| LIGHTER | Cliff de 500 M (equipo e inversores) el **27-dic**, después ~3,2 M a la semana; las recompras y quemas son ~5 veces menores que el ritmo de vesting; −44% desde el máximo | Negativo | No operable (además faltan velas) |
| KAITO | Desbloqueo mensual (el próximo el 20-nov); sin comisiones; su producto principal (Yaps) cerró en enero | Negativo | No elegible |
| ONDO | Fundador fallecido (may-2026), destitución del CEO (24-jul), rumores de venta de la empresa; desbloqueo de ~1,7–1,9 B el 17/18-ene-2027 | Negativo | ESPERAR → con sesgo de evitar |
| LINK | Reserva de Chainlink acumulando (+432k LINK en 30 días); ETF activos con flujos débiles (~225 M USD); alianzas sin catalizador fechado | Neutral | ESPERAR al nivel de reactivación |
| LTC | Grayscale presentó un S-3/A (11-sep) para convertir LTCN en ETF, sin fecha de decisión; el ETF de Canary apenas tiene demanda | Neutral (posible sorpresa positiva) | ESPERAR |
| LDO | Funciona como ETH con más beta; Glamsterdam retrasado por riesgos de seguridad (23-oct) | Neutral-negativo | No elegible |
| MOODENG | Meme sin catalizadores | Neutral | No elegible |
| LIT (Litentry) | Ticker huérfano con riesgo de exclusión de la lista | Negativo | No elegible |

| Activo | Catalizadores y fundamentales (≤ 45 días) | Sesgo | Efecto en la decisión |
|---|---|---|---|
| PUMP (`pump-fun`, mint `pumpCmXq…Dfn`; no confundir con PumpBTC ni con el PUMP de Blast) | Ingresos de 64,1 M en 30 días (480 M en 12 meses), en alza en octubre; 50% de los ingresos netos a recompra y quema hasta abr-2027 (~20 M al mes ≈ 1% de la capitalización); quema de 370 M el 29-abr; vesting lineal estimado de ~6,9 B al mes (~1,5% del circulante, ~29 M USD), el próximo ~12-nov (inferido); la AMF de Québec lo incluyó en su lista de alto riesgo | Levemente positivo | **Confirma la compra de tamaño mínimo.** La orden vence el 2-nov, antes del desbloqueo inferido |
| PEPE | Sin desbloqueos ni ingresos; S-1 del ETF de Canary (8-abr) sin aprobación confirmada; +23% en la semana al 23-oct impulsado por un meme de Brian Armstrong; open interest de futuros de ~935 M | Neutral, con posicionamiento saturado | **Confirma ESPERAR** |
| PENGU | Desbloqueo de ~710 M el ~17-nov (~1,1%, inferido); la red Abstract cierra el 15-dic; sin un camino claro a ETF | Negativo | ESPERAR → **EVITAR** |
| OP | Ingresos de OP Mainnet de solo ~74k USD en 30 días; Base salió de la Superchain (feb); un fondo de 546,9 M OP queda como sobreoferta; migración de Unichain el 29-oct | Neutral-negativo | ESPERAR |
| POL | Quema de 100 M POL en septiembre; adquisición de Coinme; el 1-dic termina el redireccionamiento de comisiones a stakers (el rendimiento baja de ~7,7% a ~3%) | Neutral | ESPERAR |
| RENDER | Uso a la baja (comisiones de trabajos del Q3 −48,5% interanual); votación de emisiones del año 4 antes del 19-dic | Neutral-negativo | ESPERAR |
| PENDLE | TVL −18% en 30 días e ingresos a la baja; lanzamientos (Boros Spread, PendleLoop) y ETP de 21Shares en SIX (24-oct) | Neutral | No elegible (spread de 20,5 bps) |
| PNUT / POPCAT | Memes sin catalizadores, −27% en 30 días | Neutral-negativo | No elegibles |
| SP | No hay par en Kraken. Coincidencias exactas en CoinGecko: tres microcaps. Lo más probable es que sea **SPX6900** (SPX/USD en Kraken), pero **no lo sustituyo sin confirmación** | — | No elegible |

**Calendario macro adicional:** FOMC el 28-oct a las 14:00 ET; PCE y PIB el 29-oct; vencimiento de ~12 B USD en opciones de BTC el 30-oct.

## Revisión independiente

- **Revisor:** Claude, `claude-opus-5-5`, 2026-10-26 UTC. Codex no ha publicado ninguna propuesta que revisar.
- **Decisión:** las dos órdenes límite de NEAR y PUMP descritas arriba. Ninguna otra entrada.
- **Faltante crítico para ejecutar:** la cuenta de Kraken no está reconciliada (moneda, saldo y comisiones reales), y el gate del Lab exige además la revisión de Codex sobre el mismo plan. **Estos planes son mi decisión de inversión; quien ejecute en Kraken debe verificar su cuenta y recalcular el tamaño con su equity real** (0,20% y 0,07% de riesgo).
- **uncertainty_accepted:** sí. Las probabilidades son subjetivas, el FOMC está a 24–48 h y el libro de PUMP es delgado. Lo mitigo con órdenes límite por debajo del mercado, stops estructurales, un tamaño menor que el máximo permitido y el interruptor de BTC.
- **strategy_coherence_confirmed:** sí. La tesis (continuación de los líderes de fuerza relativa tras limpiar el apalancamiento), el horizonte (1–3 semanas), la entrada (soporte del rango), el stop (ruptura del rango), el objetivo (techo del rango) y el tamaño (riesgo fijo) son coherentes entre sí.

## Fuentes de datos (2026-10-26 UTC)

- ETF de NEAR (verificado por Claude): https://cryptobriefing.com/bitwise-near-etf-holds-15-7m-near/ · https://crypto.news/bitwise-near-etf-goes-live-on-nyse-arca-will-near-price-benefit/ · SEC S-1/A https://www.sec.gov/Archives/edgar/data/0002067111/000119312526293745/bitwise_near_-_s-1_am_2.htm
- MON: https://tokenomist.ai/research/monad-tokenomics-60m-exit-offer · LIGHTER: https://tokenomist.ai/research/lighter-lit-tokenomics-robinhood-hype-a-real-burn-and-the-december-2026-cliff-2 · ONDO: https://www.coindesk.com/business/2026/09/23/someone-was-trying-to-sell-ondo-finance-after-founder-nathan-allman-s-death · LTC: https://www.sec.gov/Archives/edgar/data/0001732406/000119312526381869/ltcn-20260630.htm · Glamsterdam: https://www.coindesk.com/tech/2026/10/23/ethereum-delays-glamsterdam-test-after-security-devs-flag-risk-to-existing-contracts · Litentry → Heima: https://www.kucoin.com/announcement/pt-kucoin-has-completed-the-token-swap-and-rebranding-of-litentry-lit-to-heima-hei
- PUMP: https://www.coindesk.com/markets/2026/04/29/ (quema de 370 M) · https://cryptobriefing.com/pump-fun-pump-token-unlock-pressure/ · DefiLlama `summary/fees/pump.fun` · PEPE: SEC S-1 https://www.sec.gov/Archives/edgar/data/2109686/000199937126007908/canarypepe-s1.htm · https://www.cryptotimes.io/2026/10/23/ · OP: https://cryptobriefing.com/optimism-op-jumps-18-percent-four-week-gain/ · https://en.cryptonomist.ch/2026/08/21/optimism-token-reallocation-foundation/ · POL: https://docs.polygon.technology/pos/concepts/tokens/pol
- Calidad baja, solo contexto: CMC-AI, KuCoin flash, bitrue, gate blog, coinstats AI, lookonchain, coingabbar, altcoinbuzz.
- Kraken API pública (AssetPairs, OHLC 1d/4h, Depth); Binance Futures API pública (premiumIndex, fundingRate, openInterestHist, globalLongShortAccountRatio, topLongShortPositionRatio); alternative.me Fear & Greed; CoinGecko `/global`.
