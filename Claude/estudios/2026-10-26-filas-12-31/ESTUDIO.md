# Estudio 3: filas 12–31 de la lista y sistema C1T v1.1

| Campo | Valor |
|---|---|
| Autor | Claude, `claude-opus-5-5` (Claude Code). Investigación fundamental apoyada por dos subagentes de Claude; los datos cuantitativos, la verificación y las decisiones son míos |
| Cierre | 2026-10-26 ~08:00 UTC (03:00 America/Bogota) |
| Activos | BNB, BONK, BTC, CVR, DOGE, DOT, ENA, ETC, ETH, ETHFI, FARTCOIN, FIL, FLOKI, GRASS, HBAR, HYPE, ICP, INJ, JTO, JUP |
| Sistema | [Forebank C1T](../2026-10-26-sistema-c1t/ESTUDIO.md), reglas congeladas. Este estudio no cambia ninguna regla de señal |

## Decisión

1. **NO TRADE en los 20 activos hoy.** Ninguno tiene señal de C1T. Los más cercanos a romper su máximo de 50 días están a +9% (BTC y BNB), +19,6% (INJ) y +20,5% (ETH).
2. **C1T pasa a la versión 1.1, sin cambiar las reglas de señal:**
   - El universo se amplía de 13 a **24 activos** aplicando la regla de liquidez ya fijada. Entran DOT, ENA, ETH, FARTCOIN, FIL, HBAR, HYPE, ICP, INJ, JTO y JUP.
   - El riesgo por trade baja de 0,20% a **0,10%** por la regla de tamaño registrada: con 24 activos, el percentil 95 del MDD por bootstrap da −4,26% con 0,20% y −4,04% con 0,15%, y ambos superan el 4%.
3. **El sistema sigue en paper trading.** La nueva evidencia fuera de muestra es favorable pero no cambia la conclusión: en el régimen 2024-11 → 2026-10 la ventaja es ≈ 0.
4. **No elegibles para operar:**
   - **CVR:** no existe como activo en CoinGecko ni en Kraken. Lo más probable es que sea una errata de CRV (Curve, con par CRVUSD en Kraken), pero **no sustituyo un ticker ambiguo** sin confirmación.
   - **ETC:** 116k USD de volumen diario en Kraken y 85 USD de profundidad.
   - **ETHFI:** 163k USD de volumen.
   - **FLOKI:** 51k USD de volumen.
   - **GRASS:** spread de 29 bps.

## Elegibilidad en Kraken (mediana de 3 lecturas del libro y del volumen diario de 30 días)

| Activo | Par | Spread | Volumen diario | Profundidad a 10 bps | ¿Elegible? |
|---|---|---:|---:|---:|---|
| BNB | BNBUSD | 0,1 bps | 1,23 M | 42.336 | Sí |
| BONK | BONKUSD | 3,3 | 0,61 M | 8.908 | Sí |
| BTC | XXBTZUSD | 0,0 | 180 M | 7,38 M | Sí |
| CVR | — | — | — | — | **No (no existe)** |
| DOGE | XDGUSD | 0,0 | 4,29 M | 128.379 | Sí |
| DOT | DOTUSD | 2,9 | 1,78 M | 27.144 | Sí |
| ENA | ENAUSD | 9,6 | 3,80 M | 37.688 | Sí |
| ETC | XETCZUSD | 17,2 | 0,12 M | 85 | **No** |
| ETH | XETHZUSD | 0,0 | 60,6 M | 1,87 M | Sí |
| ETHFI | ETHFIUSD | 15,6 | 0,16 M | 2.516 | **No** |
| FARTCOIN | FARTCOINUSD | 15,9 | 1,08 M | 10.307 | Sí |
| FIL | FILUSD | 10,9 | 1,47 M | 22.263 | Sí |
| FLOKI | FLOKIUSD | 13,1 | 0,05 M | 1.941 | **No** |
| GRASS | GRASSUSD | 29,0 | 0,58 M | 7.503 | **No** |
| HBAR | HBARUSD | 3,9 | 2,16 M | 17.518 | Sí |
| HYPE | HYPEUSD | 2,6 | 9,73 M | 139.549 | Sí |
| ICP | ICPUSD | 7,7 | 1,58 M | 3.929 | Sí |
| INJ | INJUSD | 7,7 | 2,11 M | 12.930 | Sí |
| JTO | JTOUSD | 8,6 | 0,34 M | 782 | Sí (libro muy delgado) |
| JUP | JUPUSD | 11,7 | 1,16 M | 5.484 | Sí |

## Prueba fuera de muestra del sistema congelado

La adenda 3 de [HIPOTESIS_REGISTRADAS.md](../2026-10-26-sistema-c1t/HIPOTESIS_REGISTRADAS.md) se registró antes de correr esta prueba. Las filas 17–31 nunca se habían usado. Historia: Binance spot diario. FARTCOIN, GRASS y HYPE no tienen historia útil en Binance, así que para ellos se usaron velas de Kraken.

| Prueba (15 activos no vistos) | Trades | R por trade | Sin el mejor | Profit factor |
|---|---:|---:|---:|---:|
| C1T train (≤ 2022) | 39 | +0,51 | +0,40 | 2,56 |
| C1T validación (2023 → 2024-11-04) | 63 | **+0,24** | **+0,04** | 1,52 |
| C1T holdout (2024-11-05 → 2026-10-25) | 67 | +0,03 | −0,05 | 1,07 |
| C1T todo el periodo | 169 | +0,22 | +0,15 | 1,54 |
| C1 sin trailing, todo el periodo (referencia) | 106 | **+1,13** | +0,87 | 3,31 |
| C1 sin trailing, validación | 33 | +2,05 | +1,44 | 5,24 |

**Lectura:**
- En activos que el sistema nunca vio, C1T **sí supera la validación de mi protocolo** (+0,24 R, positivo al quitar el mejor trade). En el universo original no la superaba. Eso refuerza que la regla no es un sobreajuste a los primeros activos.
- El holdout vuelve a dar ≈ 0. En el régimen bajista de 2025–26 la estrategia no gana.
- La referencia sin trailing (C1) confirma, con más fuerza que antes, que **existe una prima de tendencia grande**: +1,13 R por trade en activos no vistos. La mayor parte se pierde al limitar la devolución de ganancias para cumplir el MDD del 4%.

Por activo, en todo el periodo (muestras pequeñas, solo informativo, **no se usa para elegir activos**): ETH +0,48 R (30 trades), INJ +0,58 R (16), FIL +0,53 R (9), HBAR +0,17 R (23), DOT −0,31 R (19), JUP −0,69 R (6).

## Cartera C1T v1.1 (24 activos, valoración diaria a mercado, 2018–2026)

| Riesgo por trade | Trades | Rentab. anual | MDD | Peor día | Sharpe | Bootstrap p95 MDD | Bootstrap p95 en 1 año | ¿Cumple la regla? |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 0,25% | 213 | 1,39% | −1,96% | −0,55% | 0,88 | −4,41% | −2,19% | No |
| 0,20% | 236 | 1,16% | −1,85% | −0,54% | 0,80 | −4,26% | −2,13% | No |
| 0,15% | 255 | 0,96% | −1,86% | −0,54% | 0,73 | −4,04% | −1,96% | No (por 0,04 pp) |
| **0,10%** | 284 | **0,98%** | **−1,73%** | −0,56% | 0,83 | **−3,22%** | −1,58% | **Sí** |

Con más activos, el tope de riesgo abierto (0,5%) se reparte entre más posiciones simultáneas. Por eso la rentabilidad casi no cambia al reducir el riesgo por trade.

## Fundamentales (resumen; fuentes consultadas el 2026-10-26, ver abajo)

**Contexto general:**
- FOMC el 27–28 de octubre (fecha del calendario de la Fed, no verificada en una fuente).
- En octubre, salidas de los ETF spot de BTC (~−707 M al día 13) y de ETH (~−715 M entre el 1 y el 13), después de un septiembre con entradas (+2,65 B en BTC). Las cifras vienen en parte de agregadores de calidad media.

| Activo | Datos clave | Lectura |
|---|---|---|
| BTC | 80.314 USD, −36% desde el máximo (126.080, 6-oct-2025); flujos de ETF negativos en octubre | Neutral-bajista hasta el FOMC; es el filtro de régimen del sistema |
| ETH | TVL de 48,6 B; comisiones de la cadena en alza (10,4 → 12,9 → 15,4 M por cada 30 días); Glamsterdam en la red de pruebas Hoodi desde hoy, sin fecha en mainnet; salidas de los ETF | El fundamental mejora, pero el flujo es negativo |
| BNB | Quema trimestral número 37 (~1,65 M BNB) según una fuente de calidad baja, coherente con el suministro en CoinGecko; comisiones de BSC −33% en 30 días; ETF VBNB con solo ~2,6 M USD | Mixto |
| DOGE | Inflación fija (~3,2% anual); ETF sin entradas y posible cierre del de Bitwise (sin confirmar) | Bajista: sin demanda fundamental |
| DOT | +45% en septiembre; referéndum de la stablecoin dotUSD pendiente; Grayscale abandonó su ETF de DOT; casi sin comisiones | Bajista |
| ENA | TVL de 5,0 B (−7% en 30 días), USDe 4,58 B (−7%), comisiones −32%; desbloqueo de los inversores completado el 5-oct; ~134 M ENA al mes (~1%) para equipo y fundación en noviembre y diciembre; las recompras solo empiezan cuando USDe llegue a 7,5 B | Bajista: contracción y dilución |
| ETC / ETHFI | No elegibles por liquidez. ETHFI: TVL −13% en 30 días, recompras con datos contradictorios | — |
| BONK | Desde dic-2025, el 51% de las comisiones de Bonk.fun se usa para comprar BONK para un trust, en vez de quemarlo; sin noticias recientes | Bajista |
| HYPE | Comisiones en máximos (91 M en septiembre, 687 M de ingresos en 12 meses); ~97–99% de las comisiones se dedica a recompras; ETF de Bitwise y Grayscale con salidas el 22-oct; desbloqueo del equipo ~6-nov, de 1,2 M o 9,9 M (las fuentes no coinciden; el segundo sería ~4,5% del circulante); −21% desde el máximo del 23-sep | El mejor fundamental del lote, pero con riesgo de dilución sin aclarar |
| JUP | Comisiones a la baja (18,2 M en ago → 12,6 M en lo que va de octubre); Jupuary (700 M JUP) solo aplazado; emisiones del equipo suspendidas | Neutral-bajista |
| JTO | Último desbloqueo de inversores el **7-nov** (~17 M JTO, ~3,2% del circulante); captura de ingresos muy baja (~0,5 M al mes); pierde cuota de clientes en Solana | Bajista hasta el 7-nov |
| FIL | Vesting de 6 años terminado el **15-oct-2026**: la emisión baja ~75% (≈ 21 M FIL al año); upgrade Solstice el 20-oct; la demanda pagada de almacenamiento sigue siendo mínima | Mejora la oferta, no la demanda |
| ICP | Mission 70 (reducción de la inflación de al menos 70%) aprobada en abril; la quema va por detrás del plan; disputa pública con NEAR el 22-oct | Bajista |
| INJ | Sin desbloqueos (suministro de 100 M, deflacionario); ETF de Canary y 21Shares pendientes de la SEC; rally del +30% el 16-oct por reuniones en Washington, ya diluido; comisiones de solo 0,2–0,3 M al mes | Especulativo: hay opcionalidad de ETF |
| HBAR | ETF de Canary activo (las cifras de activos no coinciden entre fuentes); upgrade en noviembre; −52% interanual | Bajista |
| FARTCOIN | Memecoin sin desbloqueos; historial de manipulación (pérdida de 1,5 M en el HLP de Hyperliquid en abril) y una caída repentina del 26% en junio | Pura beta; el riesgo de cola es alto |
| GRASS / FLOKI | No elegibles. GRASS: desbloqueo el 28-oct (~12,4 M) y una autoridad de mint que, según una fuente, sigue activa. FLOKI: noticias recicladas de PR pagado | — |
| CVR | No identificable de forma fiable (posibles CAVIAR, Polkacover inactivo, CVR2 en Base…); no hay par en Kraken | Excluido |

## Faltantes

| Faltante | Severidad | Tratamiento |
|---|---|---|
| Cuenta de Kraken reconciliada, moneda y comisiones | Crítico para operar en real | El sistema está en paper trading |
| Ventaja ≈ 0 en el régimen 2025–26 | Material | Paper trading con criterios de promoción ya fijados |
| Historia corta de HYPE (271 días), FARTCOIN y GRASS (≈ 640) | Menor | Entran por la regla de liquidez; el sistema exige 210 días de historia antes de dar señal |
| Qué activo quería decir CVR | Menor | Excluido; si el propietario aclara que es CRV, se evalúa con la misma regla |
| Fuentes de calidad media en noticias y flujos de ETF | Menor | Marcadas; no intervienen en la señal |

## Revisión independiente

- **Revisor:** Claude, `claude-opus-5-5`, 2026-10-26 UTC. Codex no ha publicado ninguna propuesta que revisar.
- **Veredicto sobre una operación real hoy:** NO TRADE. No hay señal y la cuenta no está reconciliada.
- **Sistema:** C1T v1.1 en paper trading. Los criterios para pasar a capital real no cambian: al menos 15 trades en paper desde el 2026-10-26, con expectativa > 0 que siga > 0 al quitar el mejor trade, MDD ≤ 2%, cuenta reconciliada y revisión de Codex.

## Fuentes (consultadas el 2026-10-26 UTC)

- Kraken API pública (AssetPairs, OHLC, Depth); Binance API pública (`/api/v3/klines`); CoinGecko; DefiLlama (protocolos ethena y ether.fi, comisiones de cadenas, stablecoins); CoinPaprika (búsqueda de CVR).
- ETF y macro: https://cointelegraph.com/markets/bitcoin-etf-inflows-billion-strongest-week-october · https://www.idnfinancials.com/digital-asset/69849/bitcoin-etfs-absorb-us134-4-million-in-early-october · https://www.kucoin.com/news/flash/october-20-etf-flows-bitcoin-gains-eth-and-sol-lose (calidad baja)
- ENA: https://tokenomist.ai/research/ethena-bought-out-its-sellers-and-deleted-the-investor-unlock-calendar-the-buyback-replacing-it-arms-at-7-5b-usde · https://www.fxstreet.com/cryptocurrencies/news/ena-jumps-over-20-as-ethena-pushes-to-end-investor-unlock-overhang-202608280244
- BNB: https://blockchain.news/news/bnb-36th-token-burn-2026 · https://www.vaneck.com/us/en/investments/bnb-etf-vbnb/resources/ · https://www.coingabbar.com/en/bnb-news-today-bnb-token-burn-total-supply-tokenized-stocks (calidad baja)
- DOGE: https://yellow.com/news/dogecoin-etf-inflows-bitwise-october
- BONK: https://whale-alert.io/stories/9667aa65e5a5/Bonkfun-directs-51-of-platform-fees-to-buy-BONK-for-BNKKs-Digital-Asset-Trust-Swiss-BONK-ETP-launched
- ETHFI: https://blockworks-research.beehiiv.com/p/etherfi-s-neobank-rerating · https://tokenomist.ai/ether-fi
- ETC: https://www.boerse-express.com/news/articles/ethereum-classic-fifthening-zwischen-august-und-oktober-2026-901282
- HYPE: https://www.fxstreet.com/cryptocurrencies/news/hyperliquid-strategies-lifts-buyback-to-100m-as-hype-trades-21-off-peak-202610240520 · https://247wallst.com/investing/cryptocurrency/2026/10/10/hyperliquid-buys-back-its-own-token-daily-is-this-why-hype-stays-close-to-its-high/ · https://tokenomist.ai/research/hype-tokenomics-330k-or-9-9m-hype-unlocks · https://bitwiseinvestments.com/newsroom/bitwise-launches-spot-hyperliquid-etf-bhyp
- JUP: https://www.chaincatcher.com/en/article/2293219 · JTO: https://app.tokenomics.com/tokenomics/jito/unlocks · https://www.tokenpost.com/news/investing/32644
- FIL: https://cryptobriefing.com/filecoin-six-year-vesting-ends-fil-issuance/ · https://en.cryptonomist.ch/2026/10/22/fil-price-feed-filecoin/
- ICP: https://internetcomputer.org/whitepapers/mission70.pdf · https://ambcrypto.com/icp-crypto-faces-fresh-pressure-why-dfinity-accuses-near-of-ip-theft/
- INJ: https://invezz.com/news/2026/10/16/injective-explodes-30-as-white-house-talks-put-10-inj-breakout-in-focus/ · https://cryptobriefing.com/injective-ceo-us-inj-etfs-before-2027/
- HBAR: SEC 10-Q https://www.sec.gov/Archives/edgar/data/0002039458/000199937126017437/hbr-10q_063026.htm · GRASS: https://messari.io/project/get-grass · https://milkroad.com/news/grass-revenue-is-real-but-token-sink-is-broken/
- Calidad baja, solo contexto: coinedition, crypto.com AI feed, coinotag, bitrue, kucoin, CMC-AI, hokanews, tokenradar, TechBullion/openpr (PR pagado).
