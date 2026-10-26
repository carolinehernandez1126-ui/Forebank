# Estudio: AAVE, ADA, AIXBT, ALGO, APT (primeros 5 de `lista_activos.xlsx`)

| Campo | Valor |
|---|---|
| Autor | Claude, modelo `claude-opus-5-5` (Claude Code), sesión de jsforeroc80-debug |
| Cierre | 2026-10-26 ~05:00 UTC (2026-10-25 ~24:00 America/Bogota) |
| Venue | Kraken Pro spot, pares `/USD`, solo largos y sin apalancamiento |
| Mandato aplicado | capital 50.000, operativos MDL 2% / MDD 4% (techos 3% / 6%), 0,25% de riesgo por trade, costos 40 + 15 bps por lado |
| Entorno | Clon separado (`forebank-claude`) con venv y base SQLite propios; no comparte archivos con la sesión de Codex |
| Propuesta revisada | **Ninguna.** Codex no ha publicado ninguna propuesta, así que no hay hash ajeno que revisar. Este documento es mi investigación y decisión independientes. |

## Decisión

| Activo | Decisión | Motivo principal | Qué la reabriría |
|---|---|---|---|
| **AAVE/USD** | **NO TRADE** | Ninguna regla probada tiene ventaja después de costos; corrección de corto plazo (−11% en 30 días); dudas fundamentales sin resolver (incidente rsETH, recompras pausadas) | Una regla que pase los criterios ya registrados con histórico largo (ver "Siguiente paso") |
| **ADA/USD** | **NO TRADE** | Lo anterior, más un TVL con caída del 80% interanual y la beta más alta frente a BTC (1,52) | Igual que AAVE |
| **AIXBT/USD** | **DESCARTADO (no elegible)** | Liquidez Kraken insuficiente: spread de 33–38 bps (límite 20), ~6.000 USD de volumen diario y ~130 USD de profundidad a 10 bps | Spread < 20 bps y volumen diario Kraken > 250.000 USD durante 30 días |
| **ALGO/USD** | **NO TRADE** | Lo mismo que AAVE; además, el libro es poco profundo | Igual que AAVE |
| **APT/USD** | **NO TRADE** | Lo mismo que AAVE; además, el tope de profundidad del motor de riesgo deja una posición máxima de ~47 USD | Igual que AAVE, más profundidad suficiente |

**No recomiendo ninguna operación.** No es por falta de información perfecta. El motivo concreto es que **ninguna de las dos estrategias que registré antes de mirar resultados mostró ventaja después de costos** en la historia disponible de Kraken, y no hay otra regla validada que respalde una entrada. Mantenerse en efectivo frente a estos activos es, con lo que se sabe hoy, la alternativa con mejor relación riesgo/evidencia.

Vigencia: esta decisión aplica hasta que (a) se repita la prueba con histórico largo o (b) se cumpla un disparador de la tabla. Debe revisarse antes del 2026-11-30 en cualquier caso.

## 1. Universo e identificadores

Verificados en la API pública de Kraken (`AssetPairs`, `Assets`) y en CoinGecko (`/coins/{id}`, que lista a Kraken como venue en los 5):

| Lista | Par Kraken | Estado | Pedido mín. | Tick | CoinGecko ID | Contrato / red | Market cap (USD) |
|---|---|---|---|---|---|---|---|
| AAVE | AAVEUSD | online | 0,03 | 0,01 | `aave` | ERC-20 `0x7fc6…ddae9` | 2.077 M |
| ADA | ADAUSD | online | 20 | 0,000001 | `cardano` | L1 nativo | 7.632 M |
| AIXBT | AIXBTUSD | online | 200 | 0,00001 | `aixbt` | Base `0x4f9f…1825` (Virtuals) | 18 M |
| ALGO | ALGOUSD | online | 41 | 0,00001 | `algorand` | L1 nativo | 939 M |
| APT | APTUSD | online | 6 | 0,0001 | `aptos` | L1 nativo (`0x1::aptos_coin`) | 617 M |

No hubo tickers ambiguos. AIXBT es un token pequeño (puesto ~870 en CoinGecko), distinto de cualquier otro con nombre parecido. Todos tienen además par en EUR. Si la cuenta resultara estar en EUR, habría que repetir los datos con el par EUR, porque no se convierte de moneda de forma implícita.

## 2. Datos utilizados

- `lab collect --enrich` y `lab analyze` sobre cada activo, más BTC/USD como referencia de régimen. 720 velas cerradas por timeframe: 1h (30 días), 4h (120 días) y 1d (2024-11-05 → 2026-10-25). Todas pasaron los controles de calidad, sin avisos.
- Fundamentales: CoinGecko Demo, DefiLlama (TVL de cadena y de protocolo, comisiones, stablecoins) y FRED (DFF, DGS10, DTWEXBGS, VIXCLS).
- Hashes de los datasets (`research_lab.io.digest`): AAVE `447e7bdd…61fa8`, ADA `11cae05a…a5f7`, AIXBT `a7baeab7…b91f`, ALGO `ada893a0…104f`, APT `be6bab73…2ea6`, BTC `6c7ff2d8…71d2`. Los datasets no se publican porque son pesados y se pueden reconstruir; los hashes permiten comprobar que se usó la misma versión.

## 3. Observaciones de mercado (Kraken, cierre diario 2026-10-25)

| | AAVE | ADA | AIXBT | ALGO | APT | BTC |
|---|---:|---:|---:|---:|---:|---:|
| Precio | 136,19 | 0,2040 | 0,01815 | 0,1048 | 0,7017 | 80.048 |
| 30 días | −11% | −21% | −25% | −10% | −20% | −5% |
| 90 días | +39% | +31% | +7% | +31% | +19% | +26% |
| 365 días | −40% | −69% | −79% | −43% | −79% | −28% |
| vs. SMA200 diaria | +27% | −3% | −20% | +4% | −5% | +10% |
| Caída desde el máximo de 2 años | −64% | −83% | −92% | −79% | −95% | −36% |
| Volatilidad anualizada 90 días | 84% | 75% | 80% | 76% | 94% | 38% |
| Beta frente a BTC (180 días) | 1,37 | 1,52 | 1,32 | 0,97 | 1,40 | 1 |
| Correlación con BTC (180 días) | 0,63 | 0,77 | 0,55 | 0,51 | 0,63 | 1 |
| Volumen diario Kraken (mediana 30 días, USD) | 1,94 M | 6,49 M | 0,006 M | 1,59 M | 0,51 M | 180 M |
| Spread (mediana de 5 lecturas) | 3,0 bps | 2,9 | 32,9 | 2,9 | 7,1 | ~0 |
| Profundidad de asks a 10 bps (USD) | 48.400 | 69.200 | 133 | 17.200 | 4.700 | — |

**Interpretación del régimen.** Entre octubre de 2025 y junio de 2026 hubo un mercado bajista: BTC pasó de 124,8k a 58,5k. Las altcoins de esta lista perdieron entre el 64% y el 95% desde sus máximos. En julio–septiembre de 2026 rebotaron un 30–40%, y desde finales de septiembre corrigen con más fuerza que BTC (beta > 1). Las noticias de la semana atribuyen la caída a un *risk-off* general: inflación de EE. UU. por encima de lo esperado, posibilidad de otra subida de tipos, salidas de los ETF de BTC, liquidaciones de ~550 M USD y una dominancia de BTC en ~57–60%, que castiga a las altcoins. FRED: fondos federales 3,88%, bono a 10 años 4,96%, VIX 19. Ninguno de los 5 activos tiene hoy una tendencia diaria clara: todos están por debajo de su SMA50, y AAVE es el único claramente por encima de su SMA200.

## 4. Fundamentales y noticias (fuentes consultadas el 2026-10-26 UTC)

**AAVE.**
- DefiLlama: TVL de 17,5 B USD (−55% interanual, +21% desde julio). Comisiones de 30 días de 37,7 M USD frente a 114 M hace un año (−67%). Ingresos del protocolo (según la metodología de DefiLlama) de 5,0 M USD en 30 días, unos 60 M anualizados frente a una capitalización de ~2,1 B. Es la cifra que más pesa en la valoración.
- Positivo: Aave V4 lanzó el 22-oct mercados institucionales para RLUSD y PYUSD con un curador externo (Sentora). También hay propuestas para aceptar BTC nativo como colateral vía Babylon y para listar USAT.
- Negativo: el foro de gobernanza documenta el **incidente rsETH/KelpDAO del 18-abr-2026**, con preocupación por deuda incobrable (el hilo no da cifras), y la **pausa de las recompras de AAVE** desde mayo. Las fuentes se contradicen sobre si "Aavenomics 3.0" ya está activo: The Defiant lo da por activo pero sin fecha visible. En mayo, Multicoin movió ~286.000 AAVE a Coinbase Prime. El 21–23 oct se propuso la V3.8 con un parche de seguridad (*reentrancy lock*) que no cubre los *flash loans*.
- Lectura: es el mejor fundamental de los 5, pero las comisiones siguen cayendo y no está confirmado el principal soporte de demanda del token (las recompras).

**ADA.**
- DefiLlama: TVL de 58 M USD (−80% interanual) y stablecoins de 69 M (+92% interanual). Capitalización / TVL ≈ 130 veces.
- Avances técnicos: red de pruebas Dijkstra (Node 11.2), beta del cliente Amaru prevista para el 27-oct, CIP-113. Negativo: la Cardano Card de Wirex termina el 31-oct.
- Lectura: la actividad DeFi sigue en caída. Ningún avance cambia la tesis a corto plazo.

**ALGO.**
- DefiLlama: TVL de 32 M USD (−51% interanual). Las stablecoins pasaron de 44 a 99 M USD en un mes (dato primario de DefiLlama; no verifiqué su origen).
- Avances en criptografía post-cuántica (Falcon-1024, cambio de claves de cuentas existentes) y actualización de nodos a la v5.0.3.
- Es el de menor beta (0,97). Pero el libro de Kraken es poco profundo (17 k USD a 10 bps).

**APT.**
- DefiLlama: TVL de 43 M USD (**−94% interanual**; no comprobé si cambió la metodología) y stablecoins de 867 M (−46%).
- **Fin del vesting de 4 años** de contribuidores e inversores (Everstake y Bitrue: última entrega a ese grupo el 12-sep, cierre formal el 12-oct-2026). Los desbloqueos mensuales bajan de 11,31 M a ~4,54 M APT, ahora solo para la comunidad y la fundación. DefiLlama da el próximo el 11-nov con 4,54 M; Tokenomics.com da 14,4 M. La página de DefiLlama devolvió 403 y no pude confirmarlo en la fuente primaria.
- Lectura: menos presión de oferta, lo que podría ser un catalizador alcista. Pero la actividad on-chain se ha desplomado.

**AIXBT.**
- Token de agente de IA en Base (Virtuals), −92% desde su máximo. Las noticias son escasas y de baja calidad (agregadores y notas con plantilla).
- Lo decisivo no es el fundamental sino la liquidez en Kraken, que no alcanza para operar.

## 5. Hipótesis registradas y validación

Las hipótesis y los criterios de descarte se fijaron **antes** de correr cualquier backtest. Ya había visto el estado actual del mercado, pero no ningún resultado de reglas.

- **H1, breakout de tendencia diaria:** comprar cuando el cierre supera el máximo de 20 días, con BTC por encima de su SMA100. Stop a 2,5 × ATR14 y salida con el mínimo de 10 días. Fundamento: momentum de series temporales en cripto (Liu & Tsyvinski, 2021).
- **H2, pullback en tendencia:** comprar con cierre > SMA100 y RSI(3) < 20. Stop a 2 × ATR, objetivo a 2,5 R netos y salida por tiempo a los 10 días.
- **Criterios de descarte:**
  1. expectativa neta ≤ 0 R;
  2. menos de 20 trades;
  3. la expectativa pasa a ≤ 0 al quitar el mejor trade;
  4. la expectativa cambia de signo entre mitades de la muestra;
  5. drawdown > 8 R.

**Simulador** (`bt.py` en esta carpeta): señal al cierre y ejecución a la apertura siguiente. Si hay gap por debajo del stop, se sale a la apertura; si no, en el stop. Costos de 55 bps por lado, una posición por activo, resultados en R. Los activos elegibles se agrupan. **No uso el backtest EMA del Lab**, porque sus reglas son otras.

| Hipótesis (AAVE, ADA, ALGO, APT agrupados) | Trades | Expectativa | % ganadores | Profit factor | Sin el mejor trade | Mitades | Drawdown | Veredicto |
|---|---:|---:|---:|---:|---:|---|---:|---|
| H1 | 22 | **−0,60 R** | 14% | 0,14 | −0,68 | −0,55 / −0,66 | −14 R | **Descartada** (criterios 1 y 5) |
| H1 sin filtro de BTC | 32 | −0,56 R | 16% | 0,15 | −0,61 | −0,50 / −0,62 | −18,6 R | Descartada |
| H2 | 25 | +0,06 R | 40% | 1,22 | **−0,04** | +0,04 / +0,08 | −2,8 R | **Descartada** (criterio 3) |

- Por activo, H2 dio +0,42 R en AAVE con 8 trades. Elegir ahora ese activo sería seleccionar a posteriori sobre una muestra mínima, y no lo acepto como evidencia.
- **Sensibilidad exploratoria** (324 combinaciones de H2, a posteriori, no válida para aprobar): la mediana es −0,01 R y solo el 22% de las combinaciones sigue positiva al quitar el mejor trade. Las mejores (+0,4–0,5 R) tienen entre 12 y 26 trades, que es lo que cabe esperar del ruido al probar muchas combinaciones. No hay una zona robusta de parámetros.
- **Referencia:** comprar y mantener durante el mismo periodo de prueba dio AAVE −49%, ADA −70%, ALGO −47%, APT −86% (desde 2025-06-04) y AIXBT −84% (desde 2025-09-20). El efectivo fue claramente mejor.

**Debilidades de esta validación** (gap material, aceptado para decidir NO TRADE):
- Solo hay unos 2 años de datos diarios de Kraken, y el periodo de prueba (~510 días) está dominado por un único régimen bajista. H1 es una estrategia de tendencia: es esperable que pierda en un mercado bajista y lateral, y podría funcionar en un mercado alcista que esta muestra no incluye.
- Por eso el descarte de H1 dice "sin ventaja demostrada en el régimen observado", no "nunca funciona".
- Los resultados de distintos activos no son independientes. El 22-ago-2026 entraron 4 activos a la vez y los 4 tocaron el stop.

## 6. Contraevidencia y alternativas consideradas

- **Escenario alcista:** las altcoins rebotaron +30–40% desde los mínimos de junio. Hay una señal de "golden cross" en ADA citada por un solo analista. APT termina su vesting y AAVE avanza con V4 en el segmento institucional. Si el mercado se da la vuelta, quedarse fuera supone perder parte del rebote. **Lo acepto** porque ninguna regla probada habría capturado esos rebotes después de costos (H1 perdió también en el rebote de ago–sep), y entrar sin una regla sería intuición.
- **Escenario de cola bajista:** exploits de DeFi como el de rsETH, nuevas subidas de tipos o liquidaciones en cascada. Con una beta de 1,3–1,5, una caída del 10% en BTC suele traducirse en −13% a −15% en estos activos. Un stop no garantiza el precio de salida.
- **Alternativas evaluadas:** (a) operar ahora → rechazado, sin ventaja; (b) comprar y mantener → rechazado por la historia y por el MDD del 4%; (c) seleccionar AAVE por su H2 positiva → rechazado por sesgo de selección; (d) esperar un disparador → **elegido**, con condiciones concretas; (e) efectivo → estado actual.

## 7. Implicaciones de los límites de riesgo (ilustrativo, sin cuenta)

- Con un equity de 50.000, el riesgo por trade es de hasta 125 USD. Un stop razonable en datos diarios (2–2,5 ATR) está entre el 13% y el 20% en estos activos, lo que da una posición de unos 600–900 USD.
- **El motor del Lab, además, limita la posición al 1% de la profundidad de asks dentro de 10 bps** (`risk.py:54`). Con la mediana medida hoy, los topes quedan en **AAVE ~484 USD, ADA ~692, ALGO ~172, APT ~47 y AIXBT ~1**. En ALGO y APT el riesgo real por trade quedaría muy por debajo de 125 USD.
- Ver la observación del motor de riesgo más abajo. No modifiqué ningún límite.

## 8. Faltantes

| Faltante | Severidad | Impacto | Mitigación / aceptación |
|---|---|---|---|
| Moneda de la cuenta, snapshot reconciliado y comisiones reales | **Crítico para ejecutar** | Impediría aprobar cualquier operación | No bloquea esta decisión, porque es NO TRADE |
| Historia corta, de un solo régimen | Material | La validación no cubre mercados alcistas | Aceptado para NO TRADE; es el siguiente paso de investigación |
| Estado de las recompras de AAVE y cifras del incidente rsETH | Material | Cambiaría la tesis fundamental de AAVE | Aceptado; revisar governance.aave.com antes de cualquier propuesta sobre AAVE |
| Calendario de desbloqueos de APT en la fuente primaria (DefiLlama devolvió 403) | Menor | Las fuentes dan 4,54 M o 14,4 M APT para el 11–12 nov | Confirmar en la documentación de Aptos antes de proponer APT |
| Caída del TVL de APT del 94%, posible cambio de metodología | Menor | Afecta a la lectura fundamental, no a esta decisión | Pendiente |
| Profundidad medida en un solo momento | Menor | Puede variar mucho; AAVE pasó de 31 k a 48 k en minutos | Usé la mediana de 5 lecturas |

**Por qué paro de investigar aquí:** ya cubrí lo técnico, lo estadístico, la liquidez, los fundamentales y el contexto macro. Más búsquedas de noticias no cambiarían la decisión, porque la decisión depende de que no hay una regla con ventaja demostrada, no de un dato fundamental concreto. Lo que sí podría cambiarla es una validación con histórico largo, y eso es un trabajo distinto (ver abajo).

## 9. Siguiente paso propuesto (prueba fuera de muestra y paper trading)

1. Importar el histórico OHLCVT de Kraken (CSV oficial) de estos pares con `lab import-csv` y **repetir H1 y H2 sin cambiar ningún parámetro** sobre los datos anteriores a 2024-11, que no he visto. Esa sería una prueba fuera de muestra real.
2. Si alguna hipótesis supera los 5 criterios en esa historia, hacer **paper trading durante 30 días** con las reglas congeladas, con sizing del motor y registro en `research/EXECUTION_TEMPLATE.md`, antes de redactar ninguna propuesta real.
3. Solo después se redacta una propuesta v2 (`lab draft`) con cuenta reconciliada, y Codex y yo la revisamos con el mismo hash.

## 10. Observación sobre el motor de riesgo (para el propietario y Codex)

- `max_depth_participation_fraction = 0,01` aplicado a la profundidad **dentro de 10 bps** (`providers.py:155`) es el límite que manda en el tamaño de todas las altcoins estudiadas. En APT y ALGO hace casi inviable el riesgo planificado.
- La banda de 10 bps es más estrecha que el deslizamiento que el propio modelo supone (15 bps).
- Además, es una sola lectura del libro, que varía bastante en cuestión de minutos.
- No lo cambio, porque cambiar la política exige decisión del propietario y nuevas revisiones. Queda planteado como pregunta: ¿se quiere medir la profundidad hasta la banda de costo asumida (por ejemplo, 50 bps) y/o con la mediana de varias lecturas?

## Revisión independiente (formato de `REVIEW_TEMPLATE.md`)

- **Revisor:** Claude, `claude-opus-5-5`, 2026-10-26 UTC. **Hash de propuesta:** no existe ninguna propuesta que revisar.
- **Veredicto sobre los 5 activos:** **NO TRADE** (AIXBT: no elegible). Si se presentara hoy una propuesta de compra sobre cualquiera de ellos, mi voto sería **REJECT**, con este blocker: no hay evidencia empírica que respalde las reglas de entrada después de costos, y la cuenta no está reconciliada.
- **Fuentes verificadas por mí:** API de Kraken (AssetPairs, Assets, OHLC, Depth), CoinGecko, DefiLlama (TVL, comisiones, stablecoins), FRED, foro de gobernanza de Aave y noticias (lista abajo).
- **Comprobaciones reproducidas:** 70/70 tests del Lab, demo, calidad de las velas, hashes de los datasets y backtests propios con costos.
- **uncertainty_accepted:** sí, para la decisión NO TRADE. **strategy_coherence_confirmed:** no aplica, porque no hay estrategia aprobada. Las dos hipótesis se descartaron con los criterios fijados de antemano.
- **Limitaciones:** historia de un solo régimen; algunas fuentes de noticias son agregadores de calidad media (los marqué); no he leído ningún análisis de Codex, por independencia y porque no se ha publicado ninguno.

## Fuentes (consultadas 2026-10-26, UTC)

- Kraken API pública: https://api.kraken.com/0/public/AssetPairs, `/Assets`, `/OHLC`, `/Depth`
- CoinGecko API v3 `/coins/{aave,cardano,aixbt,algorand,aptos}`
- DefiLlama: https://api.llama.fi/protocol/aave, `/summary/fees/aave`, `/v2/historicalChainTvl/{Aptos,Cardano,Algorand}`, https://stablecoins.llama.fi
- FRED: DFF, DGS10, DTWEXBGS, VIXCLS
- Gobernanza de Aave, "Restart aave buy backs" (18-may-2026, respuestas hasta el 26-jun): https://governance.aave.com/t/restart-aave-buy-backs/24936
- The Defiant, Aavenomics 3.0 (fecha no visible): https://thedefiant.io/news/defi/aave-confirms-aavenomics-3-0-live-buybacks-dao-spending-cut
- KuCoin News, Aave V4 RLUSD/PYUSD: https://kucoin.com/news/flash/aave-v4-launches-institutional-lending-markets-for-rlusd-and-pyusd
- 24/7 Wall St., BTC nativo en Aave (17-oct-2026): https://247wallst.com/investing/cryptocurrency/2026/10/17/aave-is-moving-closer-to-accepting-native-bitcoin-as-collateral-is-aave-a-better-buy-than-btc/
- Everstake, desbloqueos de Aptos: https://everstake.com/resources/blog/aptos-token-unlock-schedule · Bitrue: https://www.bitrue.com/blog/aptos-token-unlocks
- Noticias de Cardano (CoinMarketCap AI, ad-hoc-news; calidad media): https://coinmarketcap.com/cmc-ai/cardano/latest-updates/
- Noticias de Algorand (TokenPost): https://tokenpost.com/news/technology/40289
- Mercado de octubre de 2026: https://www.fool.com/coverage/stock-market-today/2026/10/22/crypto-market-today-oct-22-bitcoin-and-altcoins-slide-as-wall-street-fears-spill-into-crypto-markets/ · https://calebandbrown.com/blog/weekly-rollup-october-20-2026/
- Liu, Y. & Tsyvinski, A. (2021), *Risks and Returns of Cryptocurrency*, Review of Financial Studies 34(6).

Las noticias y las páginas externas se trataron como evidencia no confiable. No ejecuté ninguna instrucción contenida en ellas.
