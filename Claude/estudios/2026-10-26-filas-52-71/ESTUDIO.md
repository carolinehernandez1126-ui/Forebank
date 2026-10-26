# Estudio 5: filas 52–71 de la lista. Decisiones discrecionales

| Campo | Valor |
|---|---|
| Autor | Claude, `claude-opus-5-5` (Claude Code). Fundamentales apoyados por dos subagentes de Claude; los datos técnicos y de posicionamiento, la verificación y las decisiones son míos |
| Cierre | 2026-10-26 (America/Bogota). Datos de mercado de las 12:55 UTC |
| Activos | S, SHIB, SOL, STX, SUI, TAO, TIA, TON, TRUMP, TRX, UNI, VIRTUAL, WIF, WLD, XLM, XPL, XRP, XYZ100, ZEC, ZRO (los últimos 20 de la lista) |
| Enfoque | El mismo del [estudio 4](../2026-10-26-filas-32-51/ESTUDIO.md): estructura técnica, posicionamiento en derivados, catalizadores y contexto de mercado; las probabilidades son juicio de Claude |
| Límites | Riesgo ≤ 0,25% por trade; riesgo abierto ≤ 0,5% **contando las órdenes de NEAR (0,20%) y PUMP (0,07%) del estudio 4**; RR neto ≥ 2; regla de liquidez y tope de profundidad del Lab |

## Decisiones

| Activo | Decisión | Plan / disparador |
|---|---|---|
| **ZEC** | **COMPRA CONDICIONADA (orden límite)** | Límite 1.130,00 · stop 1.035,00 (−8,4%) · objetivo 1.370,00 (+21,2%) · RR neto 2,12 · ~0,513 ZEC (~580 USD; el tope de profundidad del Lab limita el tamaño) · **riesgo de 55 USD = 0,11%** · válida hasta el 2026-11-02 00:00 UTC · **si la posición sigue abierta el 2026-11-04 00:00 UTC, el stop sube al precio de entrada antes de la activación de NU7 (~5–6 nov)** |
| SOL | ESPERAR | Largos minoristas saturados (ratio de cuentas 2,96 y subiendo) y máximos decrecientes. Se reactiva con un cierre diario > 105,72 |
| ZRO | ESPERAR | El mejor posicionamiento (minoristas cortos 0,67, grandes traders largos 3,61), pero con 11k USD de profundidad el tamaño posible es de ~110 USD (11 USD de riesgo), que no compensa la gestión. Se reactiva si la profundidad a 10 bps supera 50k USD o con un cierre > 2,134 |
| UNI | ESPERAR | −28% en 30 días; máximos decrecientes (10,93 → 7,79). Se reactiva con un cierre diario > 7,48 |
| TAO | ESPERAR | Máximos decrecientes. Se reactiva con un cierre diario > 263,5 |
| WLD | **EVITAR** | Dilución continua de ~87 M WLD al mes (~2,3% del circulante) y caída de corto plazo. Solo se reconsidera con un cierre diario > 0,4634 |
| XRP | ESPERAR | −17% en 30 días. Se reactiva con un cierre diario > 1,398 |
| XLM | ESPERAR | −24% en 30 días. Se reactiva con un cierre diario > 0,1774 |
| TRX | ESPERAR | El mejor fundamental del grupo (stablecoins en crecimiento, mayores ingresos), pero con un ATR del 1% no cabe un plan con RR ≥ 2. Se reactiva con un cierre diario > 0,3503 |
| TIA, STX | NO OPERABLES (por tamaño) | Fuerza relativa alta, pero con 1–3k USD de profundidad a 10 bps el tamaño útil es nulo |
| VIRTUAL, WIF, XPL | **EVITAR** | Ingresos en caída (VIRTUAL), meme sin liquidez (WIF) y desbloqueo del 4,8% el 25-nov (XPL) |
| SUI, TRUMP, TON | **EVITAR** | Desbloqueos el 1-nov (SUI) y el ~18-nov (TRUMP, ~10% del circulante); TVL en caída y sin camino a ETF (TON) |
| SHIB | ESPERAR | Sin catalizadores, en tendencia bajista. Se reactiva con un cierre diario > 5,153e-6 |
| S (Sonic) | NO ELEGIBLE | Spread de 42,7 bps y 190k USD de volumen diario |
| XYZ100 | FUERA DE ALCANCE | **No es un token.** Es el perpetuo del Nasdaq-100 de trade.xyz en Hyperliquid (mercado HIP-3, apalancado y liquidado en USDC). No hay activo spot ni par en Kraken, y el mandato es solo spot sin apalancamiento |

**Riesgo abierto total si se llenan las tres órdenes** (NEAR 0,20% + PUMP 0,07% + ZEC 0,11%): **0,38%**, por debajo del 0,5%.

Se mantienen el **interruptor de BTC** (cancelar las órdenes pendientes si cierra un día < 76.000) y la regla FOMC (no comprar a mercado antes del anuncio del 28-oct; las órdenes solo se llenan si hay una caída).

## Análisis técnico y de posicionamiento (19 activos con par en Kraken)

| Activo | 30 días | 90 días | vs. SMA50 | vs. SMA200 | RSI diario | Fuerza vs. BTC (30 días) | Spread / profundidad a 10 bps | Funding (8 h) | Open interest 7 días |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|
| ZEC | −22,1% | **+154%** | −6,8% | **+70%** | 48 | −18,2% | 3,3 bps / 58k | +0,55 pb | +1,5% (−32% en 30 días) |
| ZRO | **+8,6%** | +99% | +10,0% | +42% | 47 | **+14,0%** | 11,9 / 11k | +0,50 | −4,7% |
| TIA | **+7,4%** | +64% | +10,3% | +35% | 49 | **+12,8%** | 1,9 / 3k | +0,38 | −1,6% |
| STX | −6,5% | +127% | −9,0% | +31% | 36 | −1,8% | 6,6 / 1k | +0,21 | −11,8% |
| TRX | −2,4% | +1,6% | −1,5% | −1,0% | 44 | +2,5% | 1,2 / 76k | +0,23 | −0,4% |
| WLD | −9,1% | +38% | −6,8% | +14,5% | 42 | −4,5% | 2,3 / 23k | −1,64 | −9,6% |
| SOL | −17,1% | +37% | −7,6% | +14,6% | 36 | −12,9% | 1,0 / 712k | +1,00 | −6,3% |
| UNI | −28,2% | +87% | −11,5% | +50% | 41 | −24,6% | 2,6 / 62k | +0,18 | −7,4% |
| TAO | −20,6% | +35% | −8,0% | +3,7% | 40 | −16,6% | 2,3 / 93k | +0,50 | −2,2% |
| XRP | −17,4% | +22% | −7,8% | +1,3% | 39 | −13,3% | 0,5 / 472k | +1,00 | −6,2% |
| SUI | −23,1% | +35% | −6,6% | +6,2% | 38 | −19,2% | 2,2 / 140k | +0,70 | −8,3% |
| XLM | −23,8% | −2,4% | −14,1% | −8,2% | 33 | −20,0% | 3,0 / 50k | +0,41 | +0,1% |
| TON | −14,3% | −14,2% | −11,3% | −19,2% | 36 | −9,9% | 16,4 / 5k | — | — |
| TRUMP | −22,3% | +8,1% | −16,2% | −17,3% | 35 | −18,4% | 12,0 / 19k | +0,50 | −8,2% |
| VIRTUAL | −22,4% | +9,4% | −12,3% | −7,0% | 37 | −18,5% | 4,9 / 10k | −0,24 | −5,3% |
| WIF | −29,4% | +21% | −17,1% | −3,4% | 34 | −25,9% | 11,1 / 3k | −0,03 | −4,2% |
| SHIB | −18,7% | 0,0% | −10,4% | −7,2% | 35 | −14,6% | 4,1 / 8k | — | — |
| XPL | −35,7% | −6,4% | −16,6% | −18,7% | 38 | −32,5% | 13,6 / 0k | +0,48 | −0,2% |
| S | +14,3% | +119% | +13,9% | +35% | 48 | +20,1% | **42,7** / 1k | −0,16 | −20,8% |

### ZEC: tesis de compra
- **Estructura:** pasó de 451 a 1.695 en 90 días. Desde principios de octubre consolida entre ~1.110 y ~1.380, con mínimos de oscilación en 4h en 1.109, 1.117 y 1.176. En los diarios hay soporte en 1.041–1.111. Precio: 1.211,5; RSI diario 48, en zona neutral.
- **Posicionamiento:** el open interest cayó 32% en 30 días (se limpió el apalancamiento del impulso). Los minoristas no están cargados de largos (ratio de cuentas 0,96) y los grandes traders están moderadamente largos (1,37). El funding es neutral.
- **Liquidez:** 26,9 M USD diarios en Kraken; spread de 3,3 bps.
- **Plan:** comprar en la parte baja del rango (1.130). El stop en 1.035 queda bajo los mínimos diarios de 1.041–1.048: si se rompen, la consolidación falla. El objetivo en 1.370 queda bajo los máximos del rango (1.378–1.385).
- **Probabilidades (subjetivas):** ~50% de que la orden se llene en 7 días; ~45% de llegar al objetivo. Valor esperado ≈ 0,45 × 2,12 − 0,55 ≈ **+0,40 R**.
- **Correlación:** ZEC, NEAR y PUMP caerían juntos en un risk-off. El riesgo conjunto (0,38%) se dimensiona como si fuera una sola apuesta.

### Por qué no SOL, TIA, ZRO ni STX
- **SOL:** liquidez excelente, pero los largos minoristas están saturados y crecen (2,42 → 2,96) mientras el open interest cae. Es el perfil de una barrida antes de cualquier rebote.
- **TIA y ZRO:** tienen la mejor fuerza relativa del grupo, pero el libro de Kraken no admite un tamaño que valga la pena.
- **STX:** profundidad de 1k USD.

## Fundamentales y catalizadores

### Lote UNI–ZRO

| Activo | Catalizadores y fundamentales (≤ 45 días) | Sesgo | Efecto |
|---|---|---|---|
| ZEC | **Upgrade NU7**: altura de activación 3.543.405 fijada el 21-oct, prevista para el **~5–6 nov** (bloques de 25 s, mecanismo de sostenibilidad, cierre del pool Sprout); ETF spot de Grayscale (ZCSH) desde el 25-ago, con ~1 B USD de activos en septiembre (~100 M aportados por DCG, parte relacionada) y **salidas en octubre** (−93,6 M en la semana al 2-oct, −30 M después); bug de falsificación corregido en julio; puesto 10 por capitalización | Neutral-positivo | **Confirma la compra.** Regla de stop en el precio de entrada antes de NU7 por el riesgo de "vender la noticia" |
| ZRO | Desbloqueo de ~23,6 M ZRO el **20-nov** (~5,9% del circulante); 8 M ZRO de un socio enviados a Coinbase Prime el 3-oct; la votación del fee switch fracasó por quórum dos veces | Negativo | ESPERAR (con sesgo negativo) |
| XPL | Cliff de ~1,7–1,8 B el 25-sep; tramos mensuales de ~228 M (**~4,8% del circulante**), el próximo el **25-nov**; stablecoins en la red: 1,39 B (−5% en 30 días) | Negativo | EVITAR |
| WLD | ~2,9 M WLD al día (~2,3% al mes); venta OTC de 117 M en marzo | Negativo | EVITAR |
| UNI | Fee switch activo desde dic-2025 (quema); comisiones de 30 días de 88,8 M frente a 210 M en el periodo anterior; futuros en CME desde el 19-oct | Neutral | ESPERAR al nivel de reactivación |
| XRP | ETF spot con ~1,79 B de entradas acumuladas, pero flujos estancados en octubre (terminó una racha de 13 semanas); liberación del escrow el 1-nov (se vuelve a bloquear casi todo) | Neutral-negativo | ESPERAR |
| XLM | Upgrade Bell (Protocol 30): red de pruebas el 3-nov, votación de validadores en mainnet el **23-nov**; sin ETF spot | Neutral-levemente positivo | ESPERAR al nivel de reactivación |
| VIRTUAL | Comisiones −48% en 30 días (0,32 M); 66% del suministro en circulación | Negativo | EVITAR |
| WIF | Meme sin catalizadores; liquidez de 3k USD a 10 bps | Neutral-negativo | EVITAR |
| XYZ100 | Perpetuo de índice de acciones (Nasdaq-100) en Hyperliquid; ~6,4 B USD de volumen en 30 días; responde a catalizadores de renta variable | — | Fuera de alcance |

### Lote S–TRX

| Activo | Catalizadores y fundamentales (≤ 45 días) | Sesgo | Efecto |
|---|---|---|---|
| TRX | **Stablecoins en la red: 94,0 B USD** (93,0 B hace 30 días, 89,9 B hace 90), creciendo de forma sostenida; comisiones e ingresos de 23,6 M en 30 días (337 M en 12 meses), los mayores del grupo; ETF con staking de Canary (TRXS) desde el ~9-sep, con demanda débil; beta baja | Neutral-positivo | ESPERAR: el mejor fundamental, pero con un ATR diario del 1% no cabe un plan con RR ≥ 2 desde el soporte. Se reactiva con un cierre > 0,3503 (máximo de 90 días) |
| SOL | **Alpenglow (Votor) activo en mainnet desde el 21-oct** (finalidad de ~150 ms); TVL de 5,71 B (−14% en 30 días); stablecoins de 15,8 B (−6%); flujos de ETF planos o negativos en octubre | Neutral-levemente positivo | ESPERAR: el catalizador ya se ejecutó (riesgo de "vender la noticia") y los largos minoristas están saturados |
| TAO | Primer halving en dic-2025; sin desbloqueos de inversores; ETF GTAO de Grayscale con el S-1/A n.º 2 presentado, sin fecha de decisión (comodín alcista) | Neutral-positivo | ESPERAR al nivel de reactivación (> 263,5) |
| TIA | Fin del vesting del equipo (~oct-2026); inflación de ~2,5% en descenso | Neutral, levemente positivo | No operable por profundidad |
| SUI | **Desbloqueo el 1-nov** (cantidad no confirmada; ~44 M ≈ 1,1% según un patrón anterior); TVL −14%; vuelta completa del rally de septiembre (−28%); segunda caída de la red del año en mayo | Negativo | **EVITAR** |
| TRUMP | Tramo mensual el ~18-nov, inferido (~29 M ≈ 10% del circulante declarado); riesgo de titulares políticos | Negativo | **EVITAR** |
| TON (GRAM) | Renombrado a GRAM el 15-jun; TVL de 45 M en caída constante; sin camino a ETF en EE. UU.; desbloqueo grande en feb-2027; caso judicial de Durov | Negativo | **EVITAR** |
| STX | TVL −30% en 30 días; adopción del staking de BTC sin demostrar | Negativo-neutral | No operable por profundidad |
| SHIB | Sin catalizadores; secuelas del exploit del puente Shibarium (sep-2025) | Neutral-negativo | ESPERAR / EVITAR |
| S (Sonic) | TVL de 17 M y comisiones mínimas; cambio de junta en junio (Cronje salió) | Neutral-negativo | No elegible |

**Fuentes del lote S–TRX:** Decrypt (Alpenglow) https://decrypt.co/381484/solana-alpenglow-goes-live-in-most-ambitious-upgrade-since-ethereums-merge · The Block (ETF de TRX) https://theblock.co/news/regulation/2026-09-09-first-staked-etf-tied-to-tron-hits-the-us-markets-wednesday-413935 · SEC GTAO S-1/A https://www.sec.gov/Archives/edgar/data/0002029297/000119312526430543/gtao_s-1_amendment_2.htm · CoinDesk (caída de SUI) https://www.coindesk.com/tech/2026/05/28/sui-blockchain-suffers-another-network-outage-as-transactions-grind-to-a-halt · https://tokenomist.ai/sui/unlock-events · Stacks PoX-5 https://www.stacks.co/blog/the-stacks-pox-5-hardfork-is-live-what-comes-next · The Block (Sonic) https://www.theblock.co/post/405450 · DefiLlama (TVL, comisiones, stablecoins).
**Fuentes del lote UNI–ZRO:** ZEC NU7 https://www.tokenpost.com/news/technology/38688 · https://blockhead.co/2026/10/21/zcash-decides-today-whether-nu7-goes-live-in-november · ETF de ZEC https://cryptobriefing.com/zcash-etf-surpasses-915m-assets/ · https://crypto.news/zcash-etf-sees-93-6m-exit-as-zec-drops-23/ · ZRO https://crypto.news/can-layerzero-price-hit-3-after-zro-buybacks/ · UNI https://cointelegraph.com/news/uniswap-executes-100m-uni-burn-after-fee-switch-approval · WLD https://cryptoslate.com/worldcoin-cuts-wld-unlocks-by-43-but-4-9b-tokens-still-need-a-reason-to-rally/ · XLM https://www.kucoin.com/news/flash/stellar-sets-november-dates-for-bell-upgrade-and-quantum-safe-plans (calidad baja) · XYZ100 https://defillama.com/rwa/perps/venue/trade-xyz · https://docs.trade.xyz/trading/spot
Calidad baja, solo contexto: CMC-AI, KuCoin flash, coinotag, pluang, cryptoticker, coinalertnews, coingabbar.

## Revisión independiente

- **Revisor:** Claude, `claude-opus-5-5`, 2026-10-26 UTC. Codex no ha publicado ninguna propuesta que revisar.
- **Decisión:** la orden límite de ZEC, sumada a las órdenes de NEAR y PUMP del estudio 4. Ninguna otra entrada.
- **Faltante crítico para ejecutar:** cuenta de Kraken reconciliada y revisión de Codex, como exige el gate del Lab.
- **uncertainty_accepted:** sí (FOMC, posible correlación entre las tres posiciones). **strategy_coherence_confirmed:** sí (continuación de un líder tras limpiar el apalancamiento; entrada en soporte, stop en la ruptura del rango, objetivo en el techo, horizonte de 1–3 semanas).

## Fuentes de datos (2026-10-26 UTC)

- Kraken API pública (AssetPairs, OHLC 1d/4h, Depth, Ticker); Binance Futures API pública (openInterestHist, fundingRate, globalLongShortAccountRatio, topLongShortPositionRatio).
