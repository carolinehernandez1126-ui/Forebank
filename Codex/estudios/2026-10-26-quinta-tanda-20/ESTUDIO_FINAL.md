# Estudio final — quinta tanda de veinte filas

**Codex ·26 de octubre de 2026, America/Bogota.** Universo original A52: A71. Investigación propia y de especialistas Codex autorizados, sin lectura del estudio Claude antes de congelar esta conclusión. Mercado real Kraken, `synthetic=false`. Se publica únicamente investigación final y conclusiones; cuentas, claves, snapshots y scripts de sesión quedan locales.

## Decisión

**Prioridad entre propuestas igualmente válidas: SOL → XRP → XLM → UNI.** Se conservan como alternativas subordinadas SUI, TAO, SHIB, VIRTUAL, WLD, WIF, TON, TRUMP, STX. Son escenarios de compra spot condicionada, no órdenes actuales ni una cartera simultánea. Hay 14 filtros de precio/costo/liquidez/calidad aprobados sobre 19 datasets; ZEC pasa la aritmética pero queda pospuesto por evento, además de cinco configuraciones rechazadas. La vigésima fila es un producto fuera del alcance spot, documentado abajo. Señales actuales en los candidatos del filtro:0; la aprobación de cuenta y consenso siguen ausentes.

Se permite **piloto real con ventaja estadística no demostrada**, máximo 0.05% de equity por trade, una posición experimental global y una entrada nueva por día UTC. El presupuesto es compartido con las tandas anteriores, no se abre otro por llegar a nuevos activos. No se exige un backtest ganador, pero se conserva su contraevidencia. Prioridad por ejecución y congruencia, no por el mayor ratio o rentabilidad histórica.

Primera reconsideración de nuevas entradas:29 oct 00 UTC, después de confirmar comunicado FOMC y mercado estable. [Fed, reunión 27–28 oct](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm), consulta 26-10-2026 UTC, sin fecha editorial individual verificada. La fecha es un filtro de evento elegido para el piloto, no una regla de Kraken ni orden de comprar ese día. ZEC tiene además una condición de evento propia.

Esta tanda permite cerrar 70 filas revisadas del Excel, sin presentar SP/XYZ100 como spot elegible. La comparación de propuestas se facilita con identidad, cutoff, reglas, costos y riesgo; una opinión más segura no demuestra estar más cerca de la verdad. No hay READY, firma de Claude o ejecución manual autorizada por este documento.

## Identificación y procedencia

Filas en orden: S, SHIB, SOL, STX, SUI, TAO, TIA, TON, TRUMP, TRX, UNI, VIRTUAL, WIF, WLD, XLM, XPL, XRP, XYZ100, ZEC, ZRO. Excel original sin modificar. Fechas reales de colección UTC:2026-10-26 T18:01:55.715179+00:00 a 2026-10-26 T18:04:29.035353+00:00. Segundo libro con hora individual en tabla; no es simultáneo con el primero. Calidad:57/57 series aprobadas. Se conserva la vela cerrada y se excluye la mutable. La documentación anuncia 720 entradas; los payloads pueden incluir 721 contando la mutable, y se usan los datos realmente observados.

LIGHTER corresponde a Lighter, mientras LIT corresponde a Litentry legado según las fichas oficiales distintas de Kraken. No se mezcló Lighter con el token antiguo que migró a Heima. TON usa el mismo activo nativo ahora denominado Gram por su proyecto, no unJettonGRAM. POL/S/RENDER se identifican según sus representaciones actuales sin empalmar por silencio MATIC/FTM/RNDR. Online en el registro internacional no certifica elegibilidad regional ni saldo real.

| Fila | Entrada | Par exacto Kraken | ID CoinGecko | Diarias | Mínimo unidades /tick | Decisión |
| --- | --- | --- | --- | --- | --- | --- |
| 52 | S | SUSD | sonic-3 | 539 | 120 / 0.0001 | DESCARTAR CONFIGURACIÓN |
| 53 | SHIB | SHIBUSD | shiba-inu | 720 | 770000 / 0.000000001 | SECUNDARIO CONDICIONADO |
| 54 | SOL | SOLUSD | solana | 720 | 0.05 / 0.01 | PRINCIPAL CONDICIONADO |
| 55 | STX | STXUSD | blockstack | 720 | 13 / 0.0001 | SECUNDARIO CONDICIONADO |
| 56 | SUI | SUIUSD | sui | 720 | 5 / 0.0001 | SECUNDARIO CONDICIONADO |
| 57 | TAO | TAOUSD | bittensor | 720 | 0.015 / 0.0001 | SECUNDARIO CONDICIONADO |
| 58 | TIA | TIAUSD | celestia | 720 | 11 / 0.0001 | DESCARTAR CONFIGURACIÓN |
| 59 | TON | TONUSD | the-open-network | 720 | 3.5 / 0.001 | SECUNDARIO CONDICIONADO |
| 60 | TRUMP | TRUMPUSD | official-trump | 646 | 2.5 / 0.001 | SECUNDARIO CONDICIONADO |
| 61 | TRX | TRXUSD | tron | 720 | 16 / 0.000001 | DESCARTAR CONFIGURACIÓN |
| 62 | UNI | UNIUSD | uniswap | 720 | 0.7 / 0.0001 | PRINCIPAL CONDICIONADO |
| 63 | VIRTUAL | VIRTUALUSD | virtual-protocol | 621 | 6 / 0.0001 | SECUNDARIO CONDICIONADO |
| 64 | WIF | WIFUSD | dogwifcoin | 720 | 20 / 0.0001 | SECUNDARIO CONDICIONADO |
| 65 | WLD | WLDUSD | worldcoin-wld | 600 | 9 / 0.0001 | SECUNDARIO CONDICIONADO |
| 66 | XLM | XXLMZUSD | stellar | 720 | 25 / 0.000001 | PRINCIPAL CONDICIONADO |
| 67 | XPL | XPLUSD | plasma | 396 | 50 / 0.0001 | DESCARTAR CONFIGURACIÓN |
| 68 | XRP | XXRPZUSD | ripple | 720 | 4 / 0.00001 | PRINCIPAL CONDICIONADO |
| 69 | XYZ100 | sin spotUSD | sin sustitución | no aplicable | no aplicable | FUERA DE ALCANCE |
| 70 | ZEC | XZECZUSD | zcash | 720 | 0.004 / 0.01 | POSPUESTO NU7 |
| 71 | ZRO | ZROUSD | layerzero | 720 | 2.5 / 0.001 | DESCARTAR CONFIGURACIÓN |

La identidad de plataformas/contratos se contrastó con el ID exacto y detalles CoinGecko, la red y documentación primaria. Las direcciones son identidad de investigación, no instrucciones de depósito. No sustituir wrapped/native, ticker duplicado o canje pendiente. Para una operación, verificar instrumento y red admitidos directamente en la cuenta.

Fuentes dinámicas de adquisición: [Kraken OHLC](https://docs.kraken.com/api-reference/market-data/get-ohlc-data),[AssetPairs](https://api.kraken.com/0/public/AssetPairs),[Depth](https://api.kraken.com/0/public/Depth),[CoinGecko](https://api.coingecko.com/api/v3/coins/list?include_platform=true). Consultas 26-10-2026 UTC; fecha editorial no aplicable. Ninguna historia fue sustituida por otra bolsa. Código del Lab congelado en`a2c4f006983a4ae15bbc35d07e38f8e55e6c160f`; no se afirma probar otra versión de main o de Claude.

| Token | Representación /identificador contrastado |
| --- | --- |
| S | nativo; sin contrato ERC20 inferido |
| SHIB | 0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce |
| SOL | nativo; sin contrato ERC20 inferido |
| STX | nativo; sin contrato ERC20 inferido |
| SUI | nativo; sin contrato ERC20 inferido |
| TAO | nativo; sin contrato ERC20 inferido |
| TIA | nativo; sin contrato ERC20 inferido |
| TON | nativo; sin contrato ERC20 inferido |
| TRUMP | 6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN |
| TRX | nativo; sin contrato ERC20 inferido |
| UNI | 0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984 |
| VIRTUAL | {'Base': '0x0b3e328455c4059EEb9e3f84b5543F74E24e7E1b', 'Ethereum': '0x44ff8620b8cA30902395A7bD3F2407e1A091BF73', 'Solana': '3iQL8BFS2vE7mww4ehAqQHAsbmRNCrPxizWAT2Zfyr9y'} |
| WIF | EKpQGSJtjMFqKZ9KQanSqYXRcF8fBopzLHYxdM65zcjm |
| WLD | {'Ethereum': '0x163f8C2467924be0ae7B5347228CABF260318753', 'World Chain': '0x2cFc85d8E48F8EAB294be644d9E25C3030863003', 'Optimism': '0xdC6fF44d5d932Cbd77B52E5612Ba0529DC6226F1'} |
| XLM | nativo; sin contrato ERC20 inferido |
| XPL | nativo; sin contrato ERC20 inferido |
| XRP | nativo; sin contrato ERC20 inferido |
| ZEC | nativo; sin contrato ERC20 inferido |
| ZRO | ethereum: 0x6985884c4392d348587b19cb9eaaf157f13271cd; base: 0x6985884c4392d348587b19cb9eaaf157f13271cd; polygon-pos: 0x6985884c4392d348587b19cb9eaaf157f13271cd; binance-smart-chain: 0x6985884c4392d348587b19cb9eaaf157f13271cd; arbitrum-one: 0x6985884c4392d348587b19cb9eaaf157f13271cd; optimistic-ethereum: 0x6985884c4392d348587b19cb9eaaf157f13271cd; avalanche: 0x6985884c4392d348587b19cb9eaaf157f13271cd |

## Técnico y estadístico

Indicadores calculados 1 h/4 h/1 d: SMA/EMA20/50/200, RSI14, MACD12/26/9, ATR14, ADX14, Bollinger 20/2, Donchian 20, OBV, VWAP20/sesión UTC y volumen z 20. No contar medias/RSI/MACD como confirmaciones independientes. La etiqueta de tendencia por medias no asegura precio sobre EMA200. VWAP y volúmenes corresponden a Kraken; no representan todos los venues. Valores indicativos, no cotización de ejecución.

La tabla resume estructura diaria, momentum de los tres horizontes y fuerza ADX; los dossiers locales conservan todos los indicadores calculados. Un RSI bajo o varias medias cercanas no obligan a reversión.

| Activo | Cierre1h /d | EMA20d /50d /200d | RSI1h /4h /d | ADX14d | ATRd/cierre | MACD hist.d |
| --- | --- | --- | --- | --- | --- | --- |
| S | 0.0464 / 0.0472 | 0.050141592232 / 0.043586989174 / 0.04646400185 | 44.6 / 32.5 / 48.0 | 47.5 | 12.17% | -0.001405612615 |
| SHIB | 0.000004876 / 0.000004842 | 0.000005153455 / 0.000005261209 / 0.000005563059 | 54.0 / 44.8 / 35.2 | 31.4 | 5.00% | -0.00000002666 |
| SOL | 101.26 / 101.25 | 106.499223473205 / 106.099580410382 / 98.203267555163 | 49.8 / 46.2 / 35.9 | 26.4 | 4.42% | -0.626947733052 |
| STX | 0.3062 / 0.3047 | 0.353020326476 / 0.329894188636 / 0.272450806653 | 53.6 / 42.6 / 35.7 | 30.2 | 11.33% | -0.01431607996 |
| SUI | 0.9164 / 0.919 | 1.010507271972 / 0.979277937133 / 0.979462208149 | 49.3 / 38.0 / 38.4 | 21.9 | 7.49% | -0.019234683709 |
| TAO | 253.2052 / 252.4882 | 270.239223669761 / 267.495508646275 / 251.227436375483 | 54.2 / 47.7 / 39.6 | 22.7 | 7.40% | -3.552400356195 |
| TIA | 0.5467 / 0.5316 | 0.555933512667 / 0.498744124569 / 0.462903528639 | 60.6 / 42.1 / 48.6 | 34.8 | 11.49% | -0.013802698623 |
| TON | 1.223 / 1.251 | 1.353400727155 / 1.397308763298 / 1.521844780029 | 43.5 / 34.2 / 36.4 | 27.3 | 5.45% | -0.015056721343 |
| TRUMP | 1.701 / 1.649 | 1.813303230607 / 1.903370170935 / 2.400123269501 | 64.9 / 48.6 / 35.4 | 23.7 | 7.43% | -0.011243545456 |
| TRX | 0.330398 / 0.329912 | 0.331536036335 / 0.333167363624 / 0.32825209766 | 55.6 / 55.0 / 43.9 | 9.4 | 1.05% | -0.000103879988 |
| UNI | 7.0998 / 6.9141 | 7.40326423724 / 7.260967593942 / 5.527374743353 | 61.1 / 55.2 / 40.7 | 29.7 | 8.47% | -0.067107526937 |
| VIRTUAL | 0.6176 / 0.62 | 0.681682589103 / 0.694138529806 / 0.696087622945 | 49.2 / 41.0 / 36.9 | 25.5 | 7.39% | -0.007967746077 |
| WIF | 0.1802 / 0.1788 | 0.204300841672 / 0.20749466467 / 0.217298431836 | 52.6 / 37.7 / 33.6 | 31.4 | 8.82% | -0.002983967042 |
| WLD | 0.4412 / 0.45 | 0.509914254884 / 0.484254085575 / 0.443921495189 | 44.8 / 32.6 / 42.2 | 16.9 | 11.84% | -0.010511236035 |
| XLM | 0.168803 / 0.167827 | 0.184351589913 / 0.190000716558 / 0.191085839739 | 49.6 / 40.4 / 32.9 | 27.3 | 5.60% | -0.001737638396 |
| XPL | 0.0743 / 0.0737 | 0.081163422385 / 0.085547840261 / 0.119859912537 | 56.6 / 48.2 / 37.8 | 19.0 | 9.49% | -0.000590852012 |
| XRP | 1.2962 / 1.29489 | 1.347222102993 / 1.363828184075 / 1.371487942606 | 52.9 / 47.7 / 39.3 | 19.3 | 4.61% | -0.00404302699 |
| ZEC | 1241.63 / 1211.5 | 1229.114673355747 / 1191.609125120316 / 807.783972938808 | 58.3 / 58.1 / 48.3 | 21.0 | 9.65% | 2.359531929577 |
| ZRO | 1.675 / 1.762 | 1.856855928643 / 1.659151408996 / 1.382488222596 | 44.1 / 42.3 / 47.2 | 30.8 | 11.97% | -0.057628256058 |

| Activo | Ret7d /30d /90d | Vol.anuald | VaR95d /CVaR95d | MDD precio | BetaBTC1h /corr. /N |
| --- | --- | --- | --- | --- | --- |
| S | -8.70% / 14.29% / 118.52% | 104.9% | 7.94% / 10.99% | -96.7% | 1.80 / 0.33 / 715 |
| SHIB | -2.75% / -18.73% / 0.14% | 78.0% | 5.79% / 8.88% | -87.5% | 1.42 / 0.76 / 715 |
| SOL | -2.66% / -17.10% / 36.58% | 77.0% | 5.87% / 8.49% | -76.2% | 1.47 / 0.86 / 715 |
| STX | -14.27% / -6.48% / 126.54% | 95.8% | 7.82% / 10.95% | -95.7% | 1.81 / 0.46 / 715 |
| SUI | -7.73% / -23.12% / 35.07% | 98.3% | 7.02% / 9.83% | -87.7% | 2.13 / 0.74 / 715 |
| TAO | -6.61% / -20.62% / 34.67% | 100.7% | 7.78% / 10.43% | -79.6% | 2.03 / 0.74 / 715 |
| TIA | -16.43% / 7.39% / 63.77% | 113.3% | 8.58% / 12.09% | -96.8% | 2.15 / 0.45 / 715 |
| TON | -7.20% / -14.26% / -14.20% | 76.3% | 6.12% / 9.09% | -82.6% | 1.17 / 0.50 / 715 |
| TRUMP | -4.57% / -22.29% / 8.06% | 119.4% | 7.98% / 12.90% | -97.0% | 1.70 / 0.63 / 715 |
| TRX | -0.72% / -2.43% / 1.61% | 80.1% | 2.94% / 5.41% | -51.0% | 0.13 / 0.31 / 715 |
| UNI | -3.86% / -28.24% / 86.71% | 105.8% | 7.47% / 10.69% | -87.1% | 2.09 / 0.74 / 715 |
| VIRTUAL | -5.53% / -22.38% / 9.41% | 134.8% | 9.32% / 13.00% | -78.9% | 2.17 / 0.72 / 715 |
| WIF | -9.61% / -29.44% / 21.22% | 122.8% | 9.60% / 13.09% | -96.8% | 1.92 / 0.69 / 715 |
| WLD | -7.99% / -9.07% / 37.74% | 128.5% | 8.98% / 13.04% | -87.8% | 2.24 / 0.55 / 715 |
| XLM | -5.57% / -23.84% / -2.36% | 104.5% | 5.85% / 8.86% | -74.4% | 1.57 / 0.72 / 715 |
| XPL | -3.79% / -35.75% / -6.35% | 139.9% | 11.06% / 16.13% | -96.2% | 1.90 / 0.61 / 715 |
| XRP | -0.83% / -17.43% / 21.56% | 84.7% | 5.43% / 8.33% | -72.1% | 1.43 / 0.84 / 715 |
| ZEC | 7.28% / -22.11% / 154.52% | 138.3% | 8.65% / 12.74% | -71.7% | 2.33 / 0.70 / 715 |
| ZRO | -5.57% / 8.56% / 98.87% | 108.4% | 8.53% / 11.85% | -90.1% | 2.17 / 0.43 / 715 |

Volatilidad anualizada con 365 d; VaR/CVaR empíricos de una diaria, no techo ni predicción. El MDD de precio usa muestras de distinta longitud y no es el del sistema/cuenta. El beta/correlaciónBTC usa retornos 1 h en timestamps comunes, no precios ni una correlación entre puntos faltantes; referenciaBTC descargada 2026-10-26 T22:37:54.075516+00:00. Matriz diaria completa:395 observaciones; excluyendo instrumentos con menos 250 diarias:395. La estabilidad de correlación no está demostrada; varios tokens comparten factorcripto y no diversifican mágicamente.

## Macro, oferta y actividad económica

FRED es contexto conocido al capturar, no una feature retrospectiva del backtest. Se conserva fecha de observación y metadata de realtime de la respuesta, sin certificar vintages históricos ni estimar sorpresas monetarias.

| Serie | Última observación | Valor | Inicio muestra /delta |
| --- | --- | --- | --- |
| DFF | 2026-10-22 | 3.88 | 2026-09-23 / 0.0000 |
| DGS10 | 2026-10-22 | 4.96 | 2026-09-11 / 0.0000 |
| DTWEXBGS | 2026-10-16 | 121.4048 | 2026-09-08 / 3.4921 |
| VIXCLS | 2026-10-23 | 19.45 | 2026-09-14 / 2.3500 |

Fuentes consultadas 26-10-2026 UTC: [DFF](https://fred.stlouisfed.org/series/DFF),[DGS10](https://fred.stlouisfed.org/series/DGS10),[DTWEXBGS](https://fred.stlouisfed.org/series/DTWEXBGS),[VIXCLS](https://fred.stlouisfed.org/series/VIXCLS). VIX mide opciones de acciones estadounidenses, no volatilidad de cripto. La fecha exacta de publicación/vintage de cada observación no se certifica. Tipos/dólar y FOMC son contexto, no una prueba causal sobre cada token.

Capitalización, FDV y oferta son agregados CoinGecko capturados, sin una valoración porDCF o derecho accionario implícito. FDV no siempre utiliza un máximo teórico, y un gran circulante no certifica ausencia de unlocks o emisión futura. Los productos de staking, bonos, RWA, validadores y tokens-agente tienen riesgos/retornos distintos del token spot.

| Activo | Capitalización /FDV MUSD | Circulante /total reportados |
| --- | --- | --- |
| S | 181.20 / 181.20 | 3885497663 / 3885497663 |
| SHIB | 2874.44 / 2875.70 | 589238269922951.4 / 589495727506602 |
| SOL | 59741.64 / 64465.46 | 589819516.7913522 / 636456971.1115342 |
| STX | 574.99 / 574.99 | 1877982108.390809 / 1877982108.390809 |
| SUI | 3774.63 / 9165.56 | 4118270447.6403894 / 10000000000 |
| TAO | 2870.75 / 5316.37 | 11339645.9251 / 21000000 |
| TIA | 538.69 / 644.86 | 985890000.526906 / 1180197182.279935 |
| TON | 3463.78 / 6442.29 | 2835101627.034786 / 5273011526.246236 |
| TRUMP | 479.48 / 1701.10 | 281867936.287632 / 1000000000 |
| TRX | 31398.03 / 31398.04 | 95014987423.89874 / 95015016249.75464 |
| UNI | 4437.22 / 6300.59 | 624490422.480362 / 886738418.7861971 |
| VIRTUAL | 408.21 / 620.01 | 658385841.8252224 / 1000000000 |
| WIF | 179.99 / 179.99 | 998926392 / 998926392 |
| WLD | 1644.16 / 4417.49 | 3721933655.276899 / 10000000000 |
| XLM | 5956.22 / 8454.27 | 35227371822.40089 / 50001786837.39717 |
| XPL | 354.12 / 743.78 | 4761111111.1111 / 10000000000 |
| XRP | 82157.75 / 129667.50 | 63351197653 / 99985589443 |
| ZEC | 21126.59 / 21126.59 | 17007557.9780448 / 17007559.5405448 |
| ZRO | 670.25 / 1675.73 | 399976127.7281288 / 1000000000 |

El contraste DeFiLlama es un agregado secundario de actividad, no ingresos deholders o auditoría. No confundirTVL de un protocolo conTVL de su cadena, beneficio neto o reservas utilizables por este piloto. Endpoints y timestamps se conservan localmente; los siguientes valores solo dimensionan contexto.

| Protocolo | TVL USD | Fecha dato /obtenciónUTC | Endpoint |
| --- | --- | --- | --- |
| uniswap | 3731169965 | 1793045843 / 2026-10-26T22:38:15.367316+00:00 | https://api.llama.fi/protocol/uniswap |
| stargate | 4556029 | 1793051099 / 2026-10-26T22:38:16.320265+00:00 | https://api.llama.fi/protocol/stargate |

## Investigación fundamental y decisión por fila

Hechos del emisor/exchange y limitaciones se separan de hipótesis Codex. Consulta primaria 26-10-2026 UTC; «sin fecha editorial» significa no visible/verificada, no actualidad certificada. Los especialistas trabajaron sin precios ni resultados de backtest y sin leer Claude. La selección de trades es de Codex después de unir esos hechos con el Lab. No se ejecutaron instrucciones insertadas en documentos externos.

### Fila 52 — S: Sonic

**Observaciones fundamentales.** S paga gas y permite staking/validación/gobernanza. La tokenómica incluye emisiones para expansión institucional, airdrop y financiación; la fuente declara una primera emisión institucional de 472,372,662.8 S el 4 de septiembre de 2025 y financiación de 47,625,000 S/año durante seis años, con quema de lo no utilizado. No es oferta FTM invariable tras migrar. La ausencia de nueva emisión para recompensas de bloques en los cuatro primeros años no excluye las emisiones de otros programas. El documento prevé 1.75% anual para block rewards después de ese periodo. Kraken informa que completó migración FTM a S y retiró mercados FTM; la equivalencia 1:1 es de migración, no garantía de paridad futura de mercado.  Gas y seguridad dan utilidad; el rendimiento por staking requiere bloqueo y riesgos distintos del spot. No imputar ingresos de desarrolladores o programas institucionales como dividendo S.

**Contraevidencia.** Oferta adicional y decisiones de gobernanza; Competencia EVM y demanda de red no auditada; Riesgos de migración, puente y concentración

**Evento/seguimiento.** El blog de 7 de abril de 2026 fijó cierre de infraestructura legado Opera para 30 de junio de 2026; no presentarlo como evento futuro ni como cierre del Sonic Gateway/ERC20 route.

Fuente: [Sonic Labs](https://docs.soniclabs.com/sonic/s-token); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Reglas y programas del emisor; no auditoría de balances y demanda..

Fuente: [Kraken](https://support.kraken.com/in/articles/migration-of-ftm-to-s); publicación/actualización:2026-09-01; consulta:2026-10-26 UTC. Alcance: Fecha corresponde a actualización de artículo; migración ocurrió mayo 2025..

Fuente: [Sonic Labs](https://www.soniclabs.com/blog/sonics-successful-network-migration-what-this-means-for-fantom-opera/); publicación/actualización:2026-04-07; consulta:2026-10-26 UTC. Alcance: El anuncio no se usa como instrucción de transferencia ni garantía de redes actuales de Kraken..

**Observaciones de mercado.** Soporte 4 h 0.0461; techo bruto 0.0463; techo admisible 0.0463; stop 0.0448; target 0.0435 USD. RR neto-1.646 y estrés doble costo-1.514. Barreras diarias: ema_20=0.050141592232; ema_50=0.043586989174; ema_200=0.04646400185. No se presupone que desaparezcan antes del target. DiagnósticoQ:0 fills,0.00000% sobre equity hipotético, sin validación independiente.

**Hipótesis, congruencia y decisión de Codex.** La geometría/ratio y los libros fallan; no asumir que todoS mantiene la economía antigua FTM. Descartar este diseño y esperar estructura coherente con ejecución válida. Estado: DESCARTAR CONFIGURACIÓN. No se convierte en una orden por actualizar esta ficha.

**Faltantes específicos.** material: Emisión/circulante netos y utilización orgánica actual; mitigación: No inferir escasez solo de migración 1:1 o quema; conservar tamaño experimental.

### Fila 53 — SHIB: Shiba Inu

**Observaciones fundamentales.** La página oficial distingue SHIB comunitario/meme, BONE gas/seguridad, LEASH y TREAT con roles distintos. Publica contrato Ethereum y representaciones en otras redes. La actividad o recompensas de BONE no son ingresos automáticos de SHIB. El proyecto describe quemas de tokens procedentes de mecanismos multichain; el puente usa lock/mint y burn/unlock 1:1. Quemar una representación al regresar al origen no es la misma reducción económica que quemar oferta canónica.  Atención, comunidad y mecanismos de reducción de oferta potenciales; no se verificó derecho a beneficios para un holder SHIB spot. No afirmar que cada trade centralizado en Kraken dispara una quema on-chain.

**Contraevidencia.** Separación de captura de valor entre tokens del ecosistema; Quemar cantidades nominales grandes puede ser pequeño relativo a oferta; Demanda pagadora y concentración no auditadas

**Evento/seguimiento.** No se confirmó catalizador próximo con fecha exacta; no se reproducen titulares del medio del ecosistema sobre ballenas como dato on-chain auditado.

Fuente: [Shiba Inu ecosystem](https://shib.io/tokens); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Marketing del emisor, datos dinámicos; no auditoría ni promesa de precio..

Fuente: [Shiba Inu docs](https://docs.shib.io/bridge/token-compatibility); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Mecánica de representación, no garantía de ausencia de riesgo de bridge..

**Observaciones de mercado.** Soporte 4 h 0.000004756; techo bruto 0.000004773; techo admisible 0.000004773; stop 0.000004679; target 0.000005261 USD. RR neto 2.965 y estrés doble costo 1.907. Barreras diarias: ema_20=0.000005153455; ema_50=0.000005261209; ema_200=0.000005563059. No se presupone que desaparezcan antes del target. DiagnósticoQ:2 fills,-0.09997% sobre equity hipotético, sin validación independiente.

**Hipótesis, congruencia y decisión de Codex.** Alternativa especulativa de rango con dos pérdidas diagnósticas. SHIB no recibe automáticamente gas o recompensas BONE deShibarium; tamaño pequeño y rechazo de soporte obligatorio. Estado: SECUNDARIO CONDICIONADO. Pasa el filtro en una zona de compra aún no activada.

**Faltantes específicos.** material: Balance neto de quemas y concentración de oferta; mitigación: No calcular valoración o rentabilidad por la narrativa deflacionaria; contrastar libro y mantener tamaño pequeño.

### Fila 54 — SOL: Solana

**Observaciones fundamentales.** SOL paga fees. La documentación actual divide la fee base 50% quema/50% validador y asigna 100% de las priority fees al validador; no se quema la mitad de todos los ingresos de transacción. El FAQ de staking describe inflación inicial 8%, desinflación anual 15% y tasa terminal 1.5%. Esos son parámetros de diseño, no una medición de la tasa exacta de hoy ni yield del tenedor spot. La página de upgrades marca Agave 4.3/Alpenglow como enviado en octubre 2026 y activo, con Agave 4.4 esperado para noviembre. Esa página es estado del proyecto, no prueba de adopción económica ni garantía de ausencia de fallos.  Demanda de gas y seguridad, quema parcial y recompensas de participación; no dividendos por mantener SOL spot. Más transacciones no implican proporcionalmente más ingresos, dadas fees bajas, abstracción y cambios de capacidad.

**Contraevidencia.** Emisión puede exceder quemas; Riesgo de disponibilidad/concentración de validadores y ejecución de upgrades; Uso especulativo y competencia, ingreso del validador no igual a ingreso del holder

**Evento/seguimiento.** Actualización Alpenglow octubre es un cambio tecnológico declarado; despliegue noviembre es plan, no evento ejecutado. No se trata SIMD0550 sobre doble desinflación como cambio aprobado sin comprobar votación/activación.

Fuente: [Solana](https://solana.com/docs/core/fees); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Reglas de fees, no net issuance ni beneficio de la red..

Fuente: [Solana](https://solana.com/staking); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: FAQ de parámetros y modelos; las tasas de staking dependen de participación y comisiones..

Fuente: [Solana](https://solana.com/upgrades); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Página dinámica; planned no significa realizado..

Fuente: [Solana Developer Forums; proponentes Lostin/0 xIchigo](https://forum.solana.com/t/simd-0550-proposal-to-double-disinflation/4874); publicación/actualización:2026-06-02; consulta:2026-10-26 UTC. Alcance: Propuesta/discusión no prueba implementación actual..

**Observaciones de mercado.** Soporte 4 h 98.51; techo bruto 98.93; techo admisible 98.88; stop 96.93; target 106.09 USD. RR neto 2.009 y estrés doble costo 1.207. Barreras diarias: ema_20=106.499223473205; ema_50=106.099580410382; ema_200=98.203267555163. No se presupone que desaparezcan antes del target. DiagnósticoQ:0 fills,0.00000% sobre equity hipotético, sin validación independiente.

**Hipótesis, congruencia y decisión de Codex.** Primera opción de este bloque por profundidad y un objetivoM de retorno a EMA50. Solo la parte baja de la zona cumple RR2: se impone el techo algebraico 98.88 USD, inferior al techo bruto 98.93. No perseguir precio. Estado: PRINCIPAL CONDICIONADO. Pasa el filtro en una zona de compra aún no activada.

**Faltantes específicos.** material: Parámetro inflacionario exacto actual y estado de propuestas de gobernanza; mitigación: Evitar tasas APR o fechas de reducción no verificadas; el piloto no incluye staking.

### Fila 55 — STX: Stacks

**Observaciones fundamentales.** Stacking requiere bloquear STX y participar como signer o mediante pool para recibir BTC comprometido por mineros. Un holder spot no recibe esas recompensas automáticamente y Stacks no debe describirse simplemente como PoS. La documentación de minería describe premios 1000,500,250 y 125 STX por tenure en etapas de cuatro años, con 125 STX perpetuos después. No presentar un max_supply de agregador como un techo rígido perpetuo sin reconciliar esa regla.  Gas y seguridad/incentivos de Stacks; expansión de aplicaciones Bitcoin puede aumentar demanda. El rendimiento de stacking y sBTC exige productos/acciones distintas del spot y no se incorpora al PnL de esta estrategia.

**Contraevidencia.** Dependencia de adopción Bitcoin DeFi y economía de mineros; Riesgos de signers, disponibilidad y contratos; Emisión continuada y captura de valor no igual al valor total de BTC bloqueado

**Evento/seguimiento.** No se confirmó catalizador próximo de fecha precisa. No se trata lanzamiento histórico de sBTC/Nakamoto como evento futuro.

Fuente: [Stacks docs](https://docs.stacks.co/understand-stacks/stacking); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Mecánica de participación, no rendimiento garantizado..

Fuente: [Stacks docs](https://docs.stacks.co/learn/block-production/mining); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Calendario por protocolo; no una medición actual del circulante o rentabilidad del minero..

**Observaciones de mercado.** Soporte 4 h 0.2928; techo bruto 0.2949; techo admisible 0.2949; stop 0.2833; target 0.3298 USD. RR neto 2.129 y estrés doble costo 1.561. Barreras diarias: ema_20=0.353020326476; ema_50=0.329894188636; ema_200=0.272450806653. No se presupone que desaparezcan antes del target. DiagnósticoQ:0 fills,0.00000% sobre equity hipotético, sin validación independiente.

**Hipótesis, congruencia y decisión de Codex.** Alternativa de capacidad pequeña y ratio ajustado. La actividad deBitcoin no se convierte en yield deSTX spot; las recompensas deStacking requieren otra posición. Vigilar barreras antes de EMA50. Estado: SECUNDARIO CONDICIONADO. Pasa el filtro en una zona de compra aún no activada.

**Faltantes específicos.** material: Actividad orgánica y recompensas efectivas no auditadas; mitigación: No imputar yield BTC a spot; operar solo hipótesis de precio con horizonte acotado.

### Fila 56 — SUI: Sui

**Observaciones fundamentales.** El emisor fija oferta máxima 10,000 M SUI; aproximadamente 5% estaba disponible al lanzamiento y el resto se libera gradualmente. El gráfico es estimativo y el calendario depende del despliegue de la asignación de Foundation; no se infiere una fecha exacta del próximo unlock de agregadores discrepantes. La Foundation describe recompras diarias usando rendimiento de stablecoins; aclara que los SUI comprados NO se queman, sino que se redistribuyen/reinvierten en ecosistema. Reporta ingresos brutos y parte del mes corriente como estimada, no beneficio neto auditado.  Gas, staking, seguridad y liquidez nativa. Las recompras pueden generar demanda, pero no reducen automáticamente la oferta ni dan dividendos al holder spot. Uso de stablecoins y reducción de fees no implican crecimiento proporcional de ingresos por gas.

**Contraevidencia.** Liberaciones de oferta futuras; Emisor puede desplazar distribución estimada; Ingresos/recompras no equivalen a quema neta o beneficios distribuibles; Riesgos técnicos, de validadores y competencia

**Evento/seguimiento.** Hay liberaciones periódicas. Fuentes secundarias consultadas discrepaban entre 1 y 3 noviembre y montos; se rechaza publicar una cifra precisa no confirmada por primaria. Revisar datos oficiales antes de una entrada cuyo horizonte cruce esa fecha.

Fuente: [Sui Foundation](https://www.sui.io/token-schedule); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Calendario estimativo del emisor, no venta futura cierta ni pronóstico de precio..

Fuente: [Sui Foundation](https://www.sui.io/buybacks); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Dashboard del emisor con bruto/estimaciones; no se usan los contadores como auditoría..

**Observaciones de mercado.** Soporte 4 h 0.8989; techo bruto 0.9041; techo admisible 0.9041; stop 0.898; target 1.1611 USD. RR neto 15.342 y estrés doble costo 9.038. Barreras diarias: ema_20=1.010507271972; ema_50=0.979277937133; ema_200=0.979462208149. No se presupone que desaparezcan antes del target. DiagnósticoQ:0 fills,0.00000% sobre equity hipotético, sin validación independiente.

**Hipótesis, congruencia y decisión de Codex.** Alternativa con buen libro, pero targetR distante y oferta futura relevante. Las recompras del emisor no implican quema. Un RR muy alto con stop cercano no estima valor esperado positivo. Estado: SECUNDARIO CONDICIONADO. Pasa el filtro en una zona de compra aún no activada.

**Faltantes específicos.** material: Monto/fecha exactos de próxima liberación y balance neto de oferta; mitigación: Aceptar incertidumbre explícita a tamaño pequeño o posponer si el horizonte del plan cruza el evento sin claridad.

### Fila 57 — TAO: Bittensor

**Observaciones fundamentales.** La documentación actual informa techo 21 M TAO, halvings por umbrales de emisión total y primer halving en diciembre 2025. La emisión descrita hoy es 0.5 TAO/bloque, aproximadamente 3600/día; no tratar el primer halving como catalizador futuro. Recycling puede retrasar alcanzar el próximo umbral. d TAO introdujo tokens alpha específicos de subnet y pools; TAO y alpha tienen economías de emisión distintas. Comprar TAO spot no equivale a apostar en una subnet ni a recibir sus ingresos o rendimiento de staking.  TAO articula incentivos, staking y liquidez del ecosistema de subnets. La demanda por IA útil y el valor de los incentivos no están demostrados solo por emisiones o cotizaciones de alpha.

**Contraevidencia.** Incentivos subsidiados no equivalen a clientes externos pagando; Complejidad de subnet, pools y concentración; Escasez programada no garantiza demanda o rentabilidad; Modelos de emisión/alpha pueden cambiar con versiones

**Evento/seguimiento.** No asignar fecha fija al siguiente halving: depende de emisión neta y recycling, no de un calendario Bitcoin importado.

Fuente: [Bittensor docs](https://www.bittensor.com/docs/concepts/emissions); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Descripción técnica vigente, no auditoría de demanda o flujo de caja; números de snapshot dinámicos no fijados aquí..

Fuente: [Learn Bittensor](https://learnbittensor.org/concepts/tokenomics/tao-halving); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: La frase general sobre alpha independiente no debe confundirse con cómo cambia su componente de inyección. No se usa ese detalle para valorar TAO..

**Observaciones de mercado.** Soporte 4 h 242.408; techo bruto 243.7756; techo admisible 243.7756; stop 241.0766; target 301.0734 USD. RR neto 10.120 y estrés doble costo 6.387. Barreras diarias: ema_20=270.239223669761; ema_50=267.495508646275; ema_200=251.227436375483. No se presupone que desaparezcan antes del target. DiagnósticoQ:0 fills,0.00000% sobre equity hipotético, sin validación independiente.

**Hipótesis, congruencia y decisión de Codex.** Alternativa de tesis de red/IA con riesgos de incentivos, subredes y emisiones. El primer halving ya ocurrió: no venderlo como catalizador futuro. El targetR exige una recuperación amplia en siete días. Estado: SECUNDARIO CONDICIONADO. Pasa el filtro en una zona de compra aún no activada.

**Faltantes específicos.** material: Demanda externa pagadora, calidad de outputs de subnets y flujos auditados; mitigación: No valorar por el tamaño nominal del mercado IA ni incluir yield subnet en spot; tamaño experimental.

### Fila 58 — TIA: Celestia

**Observaciones fundamentales.** TIA paga disponibilidad de datos mediante PayForBlobs y participa en seguridad/gobernanza. No todo rollup que usa Celestia tiene que usar TIA como su propio gas. La documentación actual aclara inflación inicial 8%, reducción a~5% con Lotus julio 2025 y a~2.5% con v 6 noviembre 2025, seguida de desinflación 6.7% anual hacia 1.5%. Las recompensas de stake de tokens bloqueados se desbloquean al recibirse y aumentan circulante. No usar 8% como emisión actual. La tabla oficial establece aniversarios de desbloqueo el 30 octubre por el año bisiesto: seed/SeriesA&B liberan linealmente hasta año 2, corecontributors hasta año 3 eI+D hasta año 4. El 30 oct 2026 corresponde al fin de la ventana lineal de corecontributors, no necesariamente a un nuevo gran cliff puntual. El historial de upgrades confirma Matcha v 6 en Mainnet Beta el 24-11-2025; no se trata únicamente de propuesta o testnet.  Demanda de blobspace/seguridad puede sostener utilidad; bajos precios de DA o alta capacidad no garantizan ingresos suficientes frente a emisiones. Spot no cobra automáticamente recompensas de validación.

**Contraevidencia.** Oferta liberada y recompensas líquidas de tokens bloqueados; Competencia de otras soluciones DA; Capacidad técnica no prueba utilización pagadora; Emisión sigue positiva pese a reducción

**Evento/seguimiento.** 30-10-2026 está dentro del horizonte del piloto; revisar oferta y flujo alrededor del fin del tramo corecontributors. No inventar un monto o choque de venta de aniversario.

Fuente: [Celestia docs](https://docs.celestia.org/learn/TIA/overview/); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Su tabla abreviada conserva calendario inicial; priorizar página de supply actual para cambios de inflación..

Fuente: [Celestia docs](https://docs.celestia.org/learn/TIA/staking-governance-supply/); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Reglas de distribución, no cantidad vendida futura; aniversarios no implican venta puntual..

Fuente: [Celestia docs](https://docs.celestia.org/operate/maintenance/network-upgrades/); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Distinguir Mocha/testnet de Mainnet Beta; aquí se usó la fila mainnet..

Fuente: [Celestia Improvement Proposals](https://cips.celestia.org/cip-041.html); publicación/actualización:2025-07-28; consulta:2026-10-26 UTC. Alcance: Fecha de creación de CIP Final; la implementación se confirma por historial mainnet y supply..

**Observaciones de mercado.** Soporte 4 h 0.5155; techo bruto 0.5199; techo admisible 0.5199; stop 0.4976; target 0.4987 USD. RR neto-0.961 y estrés doble costo-0.968. Barreras diarias: ema_20=0.555933512667; ema_50=0.498744124569; ema_200=0.462903528639. No se presupone que desaparezcan antes del target. DiagnósticoQ:0 fills,0.00000% sobre equity hipotético, sin validación independiente.

**Hipótesis, congruencia y decisión de Codex.** ObjetivoM incompatible con entrada; se descarta esta geometría. El fin de un tramo de vesting del 30 oct no debe llamarse gran cliff nuevo ni comprar automáticamente por menor emisión. Estado: DESCARTAR CONFIGURACIÓN. No se convierte en una orden por actualizar esta ficha.

**Faltantes específicos.** material: Monto efectivo de oferta disponible alrededor del 30 oct y demanda orgánica por DA; mitigación: No anunciar un cliff no documentado; si no hay claridad suficiente, posponer nueva entrada que cruce el evento y no retocar stop para compensar.

### Fila 59 — TON: Gram, formerly Toncoin, native coin of The Open Network

**Observaciones fundamentales.** La web oficial identifica Gram como moneda nativa antes llamada Toncoin, usada para fees, validación y voto. El canal oficial anunció el cambio efectivo el 15 de junio de 2026 a las 12:00 UTC. Es un cambio de nombre del mismo activo, sin swap ni redominación; el alias TON del venue debe registrarse explícitamente. La página actual no permite certificar una tasa de emisión vigente. El factsheet histórico estimaba 0.6% anual: no tratar ese parámetro de 2022 como medición actual ni como supply cap. Demanda potencial por gas, staking/seguridad y aplicaciones integradas con Telegram. Tener spot no implica recibir automáticamente staking ni beneficios empresariales de Telegram.

**Contraevidencia.** Riesgo de concentración del ecosistema, actividad subsidiada y dependencia de adopción; usuarios de Telegram no equivalen a usuarios pagadores de la cadena.

**Evento/seguimiento.** Renombre ya ocurrido, no catalizador futuro ni operación de migración pendiente.

Fuente: [fuente primaria](https://ton.org/); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

Fuente: [fuente primaria](https://t.me/s/toncoin); publicación/actualización:2026-06, anuncio de vigencia 2026-06-15 T12:00:00 Z; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

Fuente: [fuente primaria](https://web-bo-i.kaiko.com/wp-content/uploads/sites/1/2026/06/20260612_notice_ton_gram_rebrand.pdf); publicación/actualización:2026-06-12; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

**Observaciones de mercado.** Soporte 4 h 1.155; techo bruto 1.16; techo admisible 1.16; stop 1.131; target 1.397 USD. RR neto 5.359 y estrés doble costo 3.854. Barreras diarias: ema_20=1.353400727155; ema_50=1.397308763298; ema_200=1.521844780029. No se presupone que desaparezcan antes del target. DiagnósticoQ:1 fills,-0.05000% sobre equity hipotético, sin validación independiente.

**Hipótesis, congruencia y decisión de Codex.** Mismo activo nativo ahora denominado Gram en la web oficial, conservando alias TON del venue; no comprar unJetton homónimo. Alternativa de capacidad reducida y muestra diagnóstica adversa. Estado: SECUNDARIO CONDICIONADO. Pasa el filtro en una zona de compra aún no activada.

**Faltantes específicos.** Material: emisión neta/actividad económica verificadas actuales y estado regional de Kraken. Crítico para identidad solo si el par no corresponde al activo nativo; no comprar un Jetton GRAM homónimo.

### Fila 60 — TRUMP: Official Trump

**Observaciones fundamentales.** El emisor lista suministro máximo 1,000 M, 200 M iniciales, desbloqueos durante 36 meses y 80% asignado a creadores/CIC Digital. Las comisiones de actividad comercial que describe la web pertenecen a entidades del emisor, no son un dividendo automático al holder. Oferta pendiente por desbloqueos: registrar concentración y dilución. No se verificó la cantidad exacta del siguiente unlock. Exposición especulativa a atención y promociones del Coin Club. Los términos niegan inversión y beneficios garantizados; las oportunidades de eventos son discrecionales.

**Contraevidencia.** Alta concentración, flujos de atención/política y posibilidad de cambios/cancelación de promociones; no valorar como acción ni como participación en ingresos de entidades afiliadas.

**Evento/seguimiento.** Web del emisor muestra Gala Dinner el 22 nov 2026 con snapshot 12 nov y scoring activo. Son condiciones promocionales, no un derecho de cobro ni garantía de presencia/beneficio. Fuente sin fecha editorial, consultada 26 oct.

Fuente: [fuente primaria](https://gettrumpmemes.com/); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

**Observaciones de mercado.** Soporte 4 h 1.617; techo bruto 1.625; techo admisible 1.625; stop 1.611; target 2.003 USD. RR neto 11.260 y estrés doble costo 6.817. Barreras diarias: ema_20=1.813303230607; ema_50=1.903370170935; ema_200=2.400123269501. No se presupone que desaparezcan antes del target. DiagnósticoQ:0 fills,0.00000% sobre equity hipotético, sin validación independiente.

**Hipótesis, congruencia y decisión de Codex.** Alternativa especulativa de baja prioridad por concentración/vesting y dependencia de atención política. No es exposición a una empresa ni promesa de beneficios políticos. TargetR remoto, sin catalizador verificable que obligue a entrar. Estado: SECUNDARIO CONDICIONADO. Pasa el filtro en una zona de compra aún no activada.

**Faltantes específicos.** Material: concentración efectiva de tenedores, calendario exacto/ventas del emisor y demanda no especulativa. Verificar red admitida por Kraken; no asumir que todas las representaciones son depositables.

### Fila 61 — TRX: TRON

**Observaciones fundamentales.** TRX paga recursos/fees y sirve para staking y voto en la red. La oferta neta depende de nuevas recompensas frente a quema por recursos; no es correcto afirmar deflación perpetua. El reporte del emisor de Q2 2026 informa 86.87 M TRX de emisión neta del trimestre, con 356.32 M emitidos y 269.45 M quemados. Es dato histórico de ese trimestre, no la tasa diaria del corte actual. Utilidad de settlement y recursos de la red, con demanda potencial por transferencias de stablecoins. Staking/energía no se incorpora como rendimiento automático de una compra spot.

**Contraevidencia.** Dependencia del uso de stablecoins, concentración de validadores y gobernanza; recursos obtenidos por staking pueden reducir quema aun si crece actividad. Volumen de stablecoins no equivale a rentabilidad del token.

**Evento/seguimiento.** No se verificó en esta revisión un evento futuro fechado dentro del horizonte del piloto; no confundir un reporte trimestral con un trigger de entrada.

Fuente: [fuente primaria](https://tron.network/trx); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

Fuente: [fuente primaria](https://trondao.org/research/tron-q2-2026-quarterly-report); publicación/actualización:2026-08-24; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

**Observaciones de mercado.** Soporte 4 h 0.328279; techo bruto 0.328566; techo admisible 0.328566; stop 0.327113; target 0.335856 USD. RR neto 0.719 y estrés doble costo-0.002. Barreras diarias: ema_20=0.331536036335; ema_50=0.333167363624; ema_200=0.32825209766. No se presupone que desaparezcan antes del target. DiagnósticoQ:2 fills,-0.09997% sobre equity hipotético, sin validación independiente.

**Hipótesis, congruencia y decisión de Codex.** No alcanza RR2 ni siquiera en la parte baja de la zona. La demanda de recursos de red o fees no cambia esa aritmética; esperar otra estructura sin mover el objetivo. Estado: DESCARTAR CONFIGURACIÓN. No se convierte en una orden por actualizar esta ficha.

**Faltantes específicos.** Material: supply neto actual, desglose económico/usuarios pagadores y concentración; el reporte es del emisor y no auditoría independiente.

### Fila 62 — UNI: Uniswap

**Observaciones fundamentales.** Documentación vigente: desde diciembre 2025 las comisiones protocolarias se usan para quemar UNI; las fuentes activas que enumera sonv 2/v 3, no todos los productos. El holder no posee un derecho individual o proporcional sobre ingresos. 1,000 M de emisión inicial. La documentación dice sin inflación activa, pero gobernanza conserva facultad de emitir hasta 2% anual. No declarar supply totalmente inmutable. Gobernanza y reducción de oferta por fees de uso efectivo; distinto de un dividendo. No atribuir al token el volumen bruto negociado ni todas las fees de LP.

**Contraevidencia.** Competencia entre DEX, caída del uso/fees, cambios de gobernanza y nuevas emisiones autorizables. Burn no implica que el precio vaya a subir.

**Evento/seguimiento.** La activación histórica de fees ya no es una mera propuesta. Nuevas fuentes de fees requieren gobernanza/implementación; no darv 4 uotras como activadas sinverificar.

Fuente: [fuente primaria](https://developers.uniswap.org/docs/ecosystem/governance/uni); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

Fuente: [fuente primaria](https://developers.uniswap.org/docs/protocols/protocol-fee/overview); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

**Observaciones de mercado.** Soporte 4 h 6.5078; techo bruto 6.5543; techo admisible 6.5543; stop 6.3137; target 7.2609 USD. RR neto 2.025 y estrés doble costo 1.451. Barreras diarias: ema_20=7.40326423724; ema_50=7.260967593942; ema_200=5.527374743353. No se presupone que desaparezcan antes del target. DiagnósticoQ:0 fills,0.00000% sobre equity hipotético, sin validación independiente.

**Hipótesis, congruencia y decisión de Codex.** Candidato principal con vínculo de fees a mecanismos de quema ya documentado, sin dividendo spot. El ratio base apenas supera 2: un empeoramiento pequeño de precio/costo puede invalidarlo. No usar un fee-switch supuestamente inactivo como tesis actual. Estado: PRINCIPAL CONDICIONADO. Pasa el filtro en una zona de compra aún no activada.

**Faltantes específicos.** Material: tasa de quema neta real al corte y cobertura exacta por cadena; métricas promocionales no auditadas.

### Fila 63 — VIRTUAL: Virtuals Protocol

**Observaciones fundamentales.** VIRTUAL funciona como activo base de liquidez y transacciones para tokens/agentes. Cada token de agente es una exposición distinta: comprarVIRTUAL no significa poseer todos sus ingresos o activos. Documentación oficial:1,000 M fijos sin futura inflación, tokens desbloqueados/vested;60% público,5%LP,35%tesorería. Desbloqueado no significa ya circulante. La tesorería puede distribuir incentivos bajo gobernanza y límite anual descrito, por lo que existe presión potencial sin nueva mint. Demanda por pares de liquidez y comercio de agentes. LockearLP no equivale a quemarVIRTUAL; requiere actividad económica real y persistente, no solo narrativa IA.

**Contraevidencia.** Actividad circular/subsidiada, dependencia de atención IA, seguridad de agentes/contratos y tesorería. Tokens de agentes pueden perder demanda aunque la infraestructura siga funcionando.

**Evento/seguimiento.** No se verificó un catalizador futuro fechado dentro del piloto; el roadmap de agentes/robótica no es un contrato de ingresos.

Fuente: [fuente primaria](https://whitepaper.virtuals.io/info-hub/usdvirtual-token-base-asset-for-ai-agents); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

Fuente: [fuente primaria](https://whitepaper.virtuals.io/info-hub/usdvirtual-token-base-asset-for-ai-agents/usdvirtual-token-distribution-and-tokenomics); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

Fuente: [fuente primaria](https://whitepaper.virtuals.io/info-hub/important-links-and-resources/virtuals-protocol-contract-addresses); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

**Observaciones de mercado.** Soporte 4 h 0.6051; techo bruto 0.6079; techo admisible 0.6079; stop 0.5927; target 0.6941 USD. RR neto 3.625 y estrés doble costo 2.530. Barreras diarias: ema_20=0.681682589103; ema_50=0.694138529806; ema_200=0.696087622945. No se presupone que desaparezcan antes del target. DiagnósticoQ:1 fills,-0.05000% sobre equity hipotético, sin validación independiente.

**Hipótesis, congruencia y decisión de Codex.** Alternativa vinculada al ecosistema de agentes, con riesgo de actividad incentivada/reflexiva. El diagnóstico pierde un stop; no inferir ingresos auditados de los tokens-agente. Estado: SECUNDARIO CONDICIONADO. Pasa el filtro en una zona de compra aún no activada.

**Faltantes específicos.** Material: ingresos auditados, usuarios pagadores netos de incentivos y distribución efectiva de tesorería.

### Fila 64 — WIF: dogwifhat

**Observaciones fundamentales.** La web del proyecto reconoce un meme de perro con sombrero y enlaza su contratoSolana. No se verificó allí un derecho contractual a ingresos ni beneficio empresarial. La ficha de Kraken publicada 11 ago 2025 informa 998,926,392 de supplymáximo ytodo circulante según el proveedor aesa fecha. No asumirqueesa ficha histórica mideexactamente la oferta del 26 oct 2026; cotejarregistroactual. Hipótesis de atención, comunidad y liquidez especulativa; no una valoración por descuento de caja.

**Contraevidencia.** Concentración, impulso reflexivo, caída de atención y gaps; la ausencia de unlock pendiente no asegura demanda ni profundidad Kraken.

**Evento/seguimiento.** No hay catalizador económico fechado confirmado en las fuentes revisadas.

Fuente: [fuente primaria](https://dogwifcoin.org/); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

Fuente: [fuente primaria](https://solscan.io/token/EKpQGSJtjMFqKZ9KQanSqYXRcF8fBopzLHYxdM65zcjm); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

Fuente: [fuente primaria](https://assets-cms.kraken.com/files/51n36hrp/facade/7b88022e2925b414f7e8fb0c98a01a63b08ec164.pdf); publicación/actualización:2025-08-11; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

**Observaciones de mercado.** Soporte 4 h 0.175; techo bruto 0.1759; techo admisible 0.1759; stop 0.1708; target 0.2074 USD. RR neto 4.195 y estrés doble costo 3.061. Barreras diarias: ema_20=0.204300841672; ema_50=0.20749466467; ema_200=0.217298431836. No se presupone que desaparezcan antes del target. DiagnósticoQ:0 fills,0.00000% sobre equity hipotético, sin validación independiente.

**Hipótesis, congruencia y decisión de Codex.** Alternativa especulativa con book pequeño y sin derechos contractuales de caja acreditados. Exigir señal y límites completos; no usar falta de ingresos como p-value o prohibición universal de piloto. Estado: SECUNDARIO CONDICIONADO. Pasa el filtro en una zona de compra aún no activada.

**Faltantes específicos.** Material: holderconcentration, calidad del volumen y ausencia de cashflow auditado; aceptable solo como piloto especulativo explícito con precio y liquidez válidos.

### Fila 65 — WLD: World, WLD token

**Observaciones fundamentales.** El whitepaper sitúaWLD en identidad/gobernanza; no equivale a una participación accionaria deToolsforHumanity. Distingue tokensdesbloqueados detokens circulantes y distribuciones de usuarios. Límite inicial 10,000 M; no se puede emitir porencimadeseumbral antes 24 jul 2038. Después, gobernanza puede activarhasta 1.5%anual, default 0. Continúa dilución circulante de unlocksdelineales: emisor anunció reducción delritmo agregado 43% a partir 24 jul 2026; no cliffmensual único. Adopción y utilidad futura de gobernanza/acceso al ecosistema, no un derecho automático a fees de identidad o beneficios empresariales.

**Contraevidencia.** Riesgos de privacidad/regulación, despliegue dehardware, gobernanza todavía en transición y crecimiento de oferta; usuariosverificados no prueban utilidadmonetaria oingresos alholder.

**Evento/seguimiento.** La reducción de unlocks de julio yaocurrió; no es una futura reducción pendiente ni fin de dilución.

Fuente: [fuente primaria](https://whitepaper.world.org/designing-for-scale/2026-03-24); publicación/actualización:2026-03-24; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

Fuente: [fuente primaria](https://world.org/pl-pl/blog/foundational-topics/tokenomics-milestone-wld-unlock-rate-to-decrease-by-43-in-july); publicación/actualización:2026-04-10; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

**Observaciones de mercado.** Soporte 4 h 0.4308; techo bruto 0.4344; techo admisible 0.4344; stop 0.4266; target 0.5894 USD. RR neto 11.916 y estrés doble costo 8.323. Barreras diarias: ema_20=0.509914254884; ema_50=0.484254085575; ema_200=0.443921495189. No se presupone que desaparezcan antes del target. DiagnósticoQ:1 fills,-0.05000% sobre equity hipotético, sin validación independiente.

**Hipótesis, congruencia y decisión de Codex.** Alternativa de riesgo elevado por distribución, adopción y contexto regulatorio. La reducción del ritmo deunlock no elimina liberación diaria. No asumir que adopción de identidad se convierte en ingreso del holder. Estado: SECUNDARIO CONDICIONADO. Pasa el filtro en una zona de compra aún no activada.

**Faltantes específicos.** Material: oferta neta efectivamente distribuida, demanda/ingresos y restricciones territoriales de cuenta.

### Fila 66 — XLM: Stellar lumen

**Observaciones fundamentales.** XLM paga fees, renta de contratos y reservas mínimas. La inflación protocolaria 1% terminó por voto el 28 oct 2019; no es una moneda con inflación minera continua. Oferta total cercana 50,000 M tras quema histórica; la distribución de la fundación puede seguir aumentando circulante sin nueva mint. No usar el ejemploAPI de 21 jul 2026 comoofertaactual. Necesidad operativa de fees/reservas y uso de red. Las fees se depositan en cuenta bloqueada, no se pagan como dividendo a holders ovalidadores; no rotularlas automáticamente como burnirreversible.

**Contraevidencia.** Adopción de activos emitidos enStellar no exige compra proporcionaldeXLM; fees bajas y tesorería pueden limitar captura porunidad deuso. Riesgo decontratos/anchorsexterno distinto delnativeasset.

**Evento/seguimiento.** No se verificó aquí un evento materialfechado dentro delhorizonte delpiloto.

Fuente: [fuente primaria](https://developers.stellar.org/docs/learn/fundamentals/lumens); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

Fuente: [fuente primaria](https://developers.stellar.org/docs/learn/fundamentals/fees-resource-limits-metering); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

**Observaciones de mercado.** Soporte 4 h 0.165886; techo bruto 0.16656; techo admisible 0.16656; stop 0.16329; target 0.19 USD. RR neto 4.225 y estrés doble costo 2.829. Barreras diarias: ema_20=0.184351589913; ema_50=0.190000716558; ema_200=0.191085839739. No se presupone que desaparezcan antes del target. DiagnósticoQ:2 fills,-0.05301% sobre equity hipotético, sin validación independiente.

**Hipótesis, congruencia y decisión de Codex.** Candidato principal por ejecución y zona de reversión verificable, sin atribuir al token ingresos de los emisores de activos deStellar. Dos fills diagnósticos dejan pérdida agregada: se acepta como contraevidencia a riesgo muy pequeño. Estado: PRINCIPAL CONDICIONADO. Pasa el filtro en una zona de compra aún no activada.

**Faltantes específicos.** Material: distribuciónfuturaSDF, demandaagregada porreservas y uso neto; no hay derecho albeneficioSDF.

### Fila 67 — XPL: Plasma

**Observaciones fundamentales.** XPL es el activo nativo de seguridad/fees dePlasma, orientada astablecoins. El diseño de transferencias USDt sinfees noimplica que cada dólar transferido compreXPL. Oferta inicial 10,000 M, nohardcapinmutable:40%ecosistema,25%equipo,25%inversores,10%ventapública. Equipo/inversores tienencliff 1 año yposteriorvest; inflación 5% bajandohacia 3% seactiva alponer enmarcha validadores externos/delegación, estadoactualnoverificado. Basefees se quema. Gasparaoperacionescomplejas, seguridad yquema de basefee según el diseño. Spot no obtiene automáticamente ingresos del productoPlasmaOne ni rewardsstaking.

**Contraevidencia.** Oferta pendiente, competenciaestables, uso subvencionado y diferencia entre moverstablecoins y demandarXPL. TVL inicial incentivado no prueba ingresos sostenibles.

**Evento/seguimiento.** Mainnet beta anunciado para 25 sep 2025. La fase posterioralcliffanual yaesmaterial en 2026, pero no se inventa el importe exacto liberado enoctubre ni un unlockúnico como ventaefectiva.

Fuente: [fuente primaria](https://www.plasma.org/company/blog/xpl-the-public-sale-and-its-role-in-the-plasma-ecosystem); publicación/actualización:2025-07-14; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

Fuente: [fuente primaria](https://www.plasma.org/company/blog/plasma-mainnet-beta-and-xpl); publicación/actualización:2025-09-18; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

**Observaciones de mercado.** Soporte 4 h 0.0706; techo bruto 0.071; techo admisible 0.071; stop 0.0701; target 0.0909 USD. RR neto 11.342 y estrés doble costo 7.389. Barreras diarias: ema_20=0.081163422385; ema_50=0.085547840261; ema_200=0.119859912537. No se presupone que desaparezcan antes del target. DiagnósticoQ:1 fills,-0.05000% sobre equity hipotético, sin validación independiente.

**Hipótesis, congruencia y decisión de Codex.** Spread superior al límite en ambas verificaciones; queda descartado aunque el ratio aparente sea grande. Transferencias gratuitas de un producto no significan queXPL no tenga riesgos de emisión o valor capturado débil. Estado: DESCARTAR CONFIGURACIÓN. No se convierte en una orden por actualizar esta ficha.

**Faltantes específicos.** Material: activaciónrealinflación/validadores, demandaagregada ycalendarioejecutadodeunlocks.

### Fila 68 — XRP: XRP Ledger native asset

**Observaciones fundamentales.** XRP se utiliza parafees/reservas ypuentesdeliquidez; lasfeesdestruyen unapequeña cantidadde XRP. No representa equity deRipple ni beneficio garantizado porcontratoscomerciales deRipple. Oferta preemitida, escrowdeRipple libera posiciones condicionales eneltiempo; distribuciónnocoincide automáticamenteconventas. La ficha deRipple informa 32,600 M enescrow al 30 jun 2026: dato deesa fecha, noactual. Utilidad detransferencias/liquidez yreduccióndeoferta porfees. El importe quemadoportransacción es pequeño; noinferir valoración apartirdelvolumenbruto de pagos.

**Contraevidencia.** Concentracióndeoferta, escrow/gobernanza, competenciadepagos ybrechaentreéxitoempresarialdeRipple ydemanda XRP. Riesgoregulatorioresidual sin convertirunlitigioyaterminadoenfuturocatalizador.

**Evento/seguimiento.** SEC7 ago 2025 confirmódesistimiento deapelaciónycontraapelación yresolución deesaaccióncivil; juiciofinal, multa 125,035,150 USD e injunction permanecen. Nopresentarlo comoexoneraciónglobal de todaoperación/jurisdicción.

Fuente: [fuente primaria](https://xrpl.org/docs/concepts/transactions/transaction-cost); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

Fuente: [fuente primaria](https://ripple.com/xrp/); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

Fuente: [fuente primaria](https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26369); publicación/actualización:2025-08-07; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

**Observaciones de mercado.** Soporte 4 h 1.2533; techo bruto 1.25875; techo admisible 1.25875; stop 1.24841; target 1.45518 USD. RR neto 7.522 y estrés doble costo 4.393. Barreras diarias: ema_20=1.347222102993; ema_50=1.363828184075; ema_200=1.371487942606. No se presupone que desaparezcan antes del target. DiagnósticoQ:0 fills,0.00000% sobre equity hipotético, sin validación independiente.

**Hipótesis, congruencia y decisión de Codex.** Candidato principal por libro y estructura de rango, no por una predicción jurídica o de adopción bancaria. El objetivo exige remontar medias; XRP no es acción deRipple ni participación automática en sus beneficios. Estado: PRINCIPAL CONDICIONADO. Pasa el filtro en una zona de compra aún no activada.

**Faltantes específicos.** Material: demandaeconómicaneta, ventasvsrelockdeescrow yregulaciónaplicablealoperador.

### Fila 69 — XYZ100: xyz: XYZ100 builder-deployed perpetual on Hyperliquid

**Observaciones fundamentales.** API oficialHyperliquidmeta, dexxyz, devuelve xyz: XYZ100 conmaxLeverage 30 ymarginTableId 30. La documentación deTradeXYZ yHIP3 describeperpetuosbuilder conoráculo, margining yliquidación. No se encontrópar Kraken spot ni untoken CoinGeckoconidentidadcoincidente. No aplicable. Elopeninterest deunperpetuo noes marketcap ni supplyspot. Exposición sintética deíndice mediantecontrato; noownershipdeacciones, dividendos nitokenemisión. No analizar tokenómicaficticia ni sustituirETF/Nasdaqspot.

**Contraevidencia.** Funding, liquidación, oráculo yvenue fuerade Kraken; inclusoapalancamiento 1 x no transformaelperpetuo enspot ni encajaconeste modeloderiesgo.

**Evento/seguimiento.** No aplicable almandatoactual; la filase conserva comoevaluada ynoelegible.

Fuente: [fuente primaria](https://docs.trade.xyz/); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

Fuente: [fuente primaria](https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-3-builder-deployed-perpetuals); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

Fuente: [fuente primaria](https://api.hyperliquid.xyz/info); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 T17:59:33.544799+00:00 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

**Decisión de Codex: FUERA DEL ALCANCE SPOT.** No hay par exacto en el registro Kraken consultado. No se fabrican precios, indicadores o backtests de un sustituto. XYZ100 figura como mercado builder-perpetual deHyperliquid, no como token Kraken spot. Se cuenta la fila como revisada por identidad/alcance, no como dataset completo.

**Faltantes específicos.** Crítico para operar: producto fueradelalcance. Requiere un mandato nuevode derivados, separado; no sehabilita aquí.

### Fila 70 — ZEC: Zcash

**Observaciones fundamentales.** MonedaPoW conopcionesprivadas/transparente ytecho 21 M. Elinterés enprivacidad esunatesisdeutilidad, nodecajaempresarial niretornoautomatico. Halvings ytecho 21 M se preservan en NU7. Menorblocktime no triplica emisión diaria: reward/3 eintervalosdehalvingajustados. No usar elrepartodevfundNU6 de 2024 comopolíticaactualcompletasinverificación. Demanda de pagos/almacenamiento conprivacidad yescasez deconsenso. Soportes dewallet/exchange/región pueden limitar elacceso; no asumir que una compra en Kraken tieneprivacidad shielded.

**Contraevidencia.** Riesgodeupgrade, nodos/wallets incompatibles, restriccionesregionales, deposits/retirossuspendidos ydeslistadoprivacycoins. Doblebreakdowntécnicopodríaampliarslippage.

**Evento/seguimiento.** ZcashFoundation 22 oct 2026: Zebra 7.0.0 estableconsoporte NU7; activaciónmainnetaltura 3,543,405, previstaalrededor 5 nov 2026. Cambia 75 s→25 s, modificafees/limits yrequiereupgrade. UnpilotoR7 diniciado 29 octcruzaelevento: posponeroponervencimientoprevio explícito, conpropuestayrevisiónnuevas; noajustarloa posteriori.

Fuente: [fuente primaria](https://z.cash/learn/does-zcash-have-a-max-supply/); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

Fuente: [fuente primaria](https://zfnd.org/zebra-7-0-0-release/); publicación/actualización:2026-10-22; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

Fuente: [fuente primaria](https://z.cash/learn/how-to-use-zcash/); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

**Observaciones de mercado.** Soporte 4 h 1117.29; techo bruto 1128.05; techo admisible 1126.97; stop 1037.4; target 1343.52 USD. RR neto 2.000 y estrés doble costo 1.670. Barreras diarias: ema_20=1229.114673355747; ema_50=1191.609125120316; ema_200=807.783972938808. No se presupone que desaparezcan antes del target. DiagnósticoQ:0 fills,0.00000% sobre equity hipotético, sin validación independiente.

**Hipótesis, congruencia y decisión de Codex.** Subzona matemáticamente válida, pero se pospone el piloto hasta verificar NU7 y normalización del venue. Una entradaR desde 29 oct puede cruzar la activación prevista alrededor 5 nov; no ignorar ese evento ni reutilizar hoy niveles después delupgrade. Estado: POSPUESTO NU7. No se convierte en una orden por actualizar esta ficha.

**Faltantes específicos.** Material antesdelpiloto: soportedelvenue ycronogramafinaldeupgrade/región. DisponibilidaddeAssetPaironline no certificajurisdicción. No seefectúanretiros.

### Fila 71 — ZRO: LayerZero

**Observaciones fundamentales.** Actualización oficial 3 jun 2026: oferta 1,000 M; recompras deStargatefinanciadasporingresos. Desdeabril 2026 seafirma 100% deingresosStargatearecompras, trasfinalizarrepartoveSTG. Elfee-switchdelprotocolo demensajeríadeLayerZero esotro mecanismo, contingente agobernanza; notratartodafeedeDVN/executor comoingresoZRO. Laactualización de 3 jun describió 514 M desbloqueados/486 Mvesting y 50 MrecompradosarelockhastaZero; soncifrasdeesa publicación, nofloatactualdel 26 oct. Distinguirmensualunlockdeventaefectiva yfondeoorgánicodecompradiscrecional. RecomprasStargate verificables yutilidadprevista deZero; comprasnoequivalensiempreaburn ni dividendos. Elcapturadefees deZero depende delmainnetyusoreal, novalorarlo comoingresoyaobservado.

**Contraevidencia.** Riesgosdeinteroperabilidad/DVN/configuración, exploitsdeapps, competencia, vestingydependenciadeunproducto paralasrecompras. ElobjetivodeARR noesresultadoauditado.

**Evento/seguimiento.** Zero/ATLAS soncatalizadores delroadmap. Calendariossecundariosseñalan 30 nov 2026, perono seconfirmóesafecha enunapublicaciónprimaria; no afirmarlacomocronogramafirme.

Fuente: [fuente primaria](https://www.layerzero.org/blog/the-zro-token); publicación/actualización:2026-06-03; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

Fuente: [fuente primaria](https://layerzero.foundation/zro-buybacks); publicación/actualización: sin fecha editorial verificada; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

Fuente: [fuente primaria](https://layerzero.network/blog/understanding-zro-buybacks); publicación/actualización:2025-12-01; consulta:2026-10-26 UTC. Alcance: Mecanismo declarado; no auditoría de resultados o solvencia..

**Observaciones de mercado.** Soporte 4 h 1.637; techo bruto 1.654; techo admisible 1.654; stop 1.571; target 1.659 USD. RR neto-0.131 y estrés doble costo-0.265. Barreras diarias: ema_20=1.856855928643; ema_50=1.659151408996; ema_200=1.382488222596. No se presupone que desaparezcan antes del target. DiagnósticoQ:0 fills,0.00000% sobre equity hipotético, sin validación independiente.

**Hipótesis, congruencia y decisión de Codex.** El recorrido hasta el targetM no paga los costos de entrada/salida. El tope algebraico RR2 queda fuera de la zona, por lo que se descarta. Las recomprasStargate no justifican target arbitrario más lejano. Estado: DESCARTAR CONFIGURACIÓN. No se convierte en una orden por actualizar esta ficha.

**Faltantes específicos.** Material: mainnetZero/ATLASyfechaactual, revenueactualneto, próximosunlocksejecutados; contratonativo/representaciónneedsregistroantesdecolectar.

## ReferenciasT/R y diagnóstico pertinente deQ

Referencias congeladas, sin optimización por activo: Tdiaria exige EMA50>EMA200, close>EMA200 y ruptura del máximo 20 previo excluida la barra actual; entrada alopen siguiente, gap máximo 1 ATR, stop=min(low 10, entrada−2 ATR), target 3 R, salida porstop/target/cierre bajo EMA50 alopen siguiente o 20 d. Rdiaria exige RSI14<30 yclose bajoBollinger inferior 20/2, stop 2 ATR, target 2.5 R, salida porstop/target/recuperación SMA20 alopen siguiente o 10 d. Su salida anticipada puede impedir el target nominal; no se atribuyen esos resultados aQ.

Warmup 200 diarias, desarrollo antes de últimas 120, holdout cronológico 120 y comienzo plano en cada segmento; tramo continuo no suma los segmentados. Si no quedan barras para desarrollo yholdout no se fabrica partición; con menos 201 ni siquiera hay tramo elegible. Referencias con riesgo 0.25%, tope activo 20%, equity hipotético ycostos 40 bpsfee+15 slip por lado compuestos. RRnominalneto>=2, stops primero ante dobletoque, gaps alopen, sin reentrada misma barra y liquidación al final. No modelan libro, cantidad mínima, monitor MDL ni exposición conjunta.

T/R yQ se evaluaron a la vista de datos históricos durante un proceso secuencial. Mantener parámetros de primeras tandas limita ajustes, pero no convierte este ejercicio enOOS independiente. Se cuentan todas las referencias y se registran intentos sinoperaciones; no se descarta piloto solo por falta de resultado positivo.

| Activo /familia | Ndev /retdev | Nhold /rethold | DDhold | Ncontinuo /retcontinuo | Ret hold doble costo |
| --- | --- | --- | --- | --- | --- |
| S/T | 0 / 0.0000% | 0 / 0.0000% | 0.0000% | 0 / 0.0000% | 0.0000% |
| S/R | 5 / -0.4690% | 1 / 0.2088% | -0.0680% | 6 / -0.0347% | 0.0000% |
| SHIB/T | 0 / 0.0000% | 0 / 0.0000% | 0.0000% | 0 / 0.0000% | 0.0000% |
| SHIB/R | 9 / 0.1339% | 0 / 0.0000% | 0.0000% | 9 / 0.2553% | 0.0000% |
| SOL/T | 2 / -0.2166% | 1 / -0.0606% | -0.1823% | 3 / -0.2771% | -0.0729% |
| SOL/R | 6 / -0.8398% | 0 / 0.0000% | 0.0000% | 6 / -0.8398% | 0.0000% |
| STX/T | 0 / 0.0000% | 1 / -0.0701% | -0.2623% | 1 / -0.0701% | -0.0793% |
| STX/R | 4 / 0.3070% | 2 / 0.2870% | -0.1792% | 6 / 0.5949% | -0.0831% |
| SUI/T | 2 / -0.3573% | 0 / 0.0000% | 0.0000% | 2 / -0.3573% | 0.0000% |
| SUI/R | 5 / -0.1671% | 0 / 0.0000% | 0.0000% | 5 / -0.1671% | 0.0000% |
| TAO/T | 1 / -0.2120% | 0 / 0.0000% | 0.0000% | 1 / -0.2120% | 0.0000% |
| TAO/R | 3 / 0.4930% | 0 / 0.0000% | 0.0000% | 3 / 0.4930% | 0.0000% |
| TIA/T | 0 / 0.0000% | 1 / -0.1573% | -0.1573% | 1 / -0.1573% | -0.1600% |
| TIA/R | 3 / 0.3804% | 0 / 0.0000% | 0.0000% | 3 / 0.3804% | 0.0000% |
| TON/T | 0 / 0.0000% | 0 / 0.0000% | 0.0000% | 0 / 0.0000% | 0.0000% |
| TON/R | 4 / -0.1605% | 0 / 0.0000% | 0.0000% | 4 / -0.1605% | 0.0000% |
| TRUMP/T | 0 / 0.0000% | 0 / 0.0000% | 0.0000% | 0 / 0.0000% | 0.0000% |
| TRUMP/R | 9 / 0.3821% | 0 / 0.0000% | 0.0000% | 9 / 0.3821% | 0.0000% |
| TRX/T | 7 / 0.2475% | 1 / -0.1953% | -0.1953% | 8 / 0.0518% | 0.0000% |
| TRX/R | 0 / 0.0000% | 0 / 0.0000% | 0.0000% | 0 / 0.0000% | 0.0000% |
| UNI/T | 1 / -0.2063% | 2 / 0.2200% | -0.1914% | 3 / 0.0133% | 0.1965% |
| UNI/R | 7 / 0.0847% | 0 / 0.0000% | 0.0000% | 7 / 0.0847% | 0.0000% |
| VIRTUAL/T | 0 / 0.0000% | 0 / 0.0000% | 0.0000% | 0 / 0.0000% | 0.0000% |
| VIRTUAL/R | 2 / 0.2855% | 0 / 0.0000% | 0.0000% | 2 / 0.2855% | 0.0000% |
| WIF/T | 0 / 0.0000% | 0 / 0.0000% | 0.0000% | 0 / 0.0000% | 0.0000% |
| WIF/R | 2 / -0.1529% | 0 / 0.0000% | 0.0000% | 2 / -0.1529% | 0.0000% |
| WLD/T | 0 / 0.0000% | 1 / -0.1515% | -0.1515% | 1 / -0.1515% | -0.1546% |
| WLD/R | 2 / 0.0202% | 0 / 0.0000% | 0.0000% | 2 / 0.0202% | 0.0000% |
| XLM/T | 1 / -0.1132% | 1 / -0.2500% | -0.2500% | 2 / -0.3629% | -0.2500% |
| XLM/R | 5 / 0.0217% | 0 / 0.0000% | 0.0000% | 5 / 0.0217% | 0.0000% |
| XPL/T | 0 / 0.0000% | 0 / 0.0000% | 0.0000% | 0 / 0.0000% | 0.0000% |
| XPL/R | 0 / 0.0000% | 0 / 0.0000% | 0.0000% | 0 / 0.0000% | 0.0000% |
| XRP/T | 2 / 0.5070% | 0 / 0.0000% | 0.0000% | 2 / 0.5070% | 0.0000% |
| XRP/R | 5 / 0.0373% | 0 / 0.0000% | 0.0000% | 5 / 0.0373% | 0.0000% |
| ZEC/T | 7 / 2.0967% | 4 / 1.0480% | -0.2216% | 11 / 3.1668% | 0.9430% |
| ZEC/R | 2 / 0.4076% | 0 / 0.0000% | 0.0000% | 2 / 0.4076% | 0.0000% |
| ZRO/T | 1 / -0.2225% | 1 / -0.1390% | -0.1798% | 2 / -0.3612% | -0.1424% |
| ZRO/R | 2 / 0.3893% | 0 / 0.0000% | 0.0000% | 2 / 0.3893% | 0.0000% |

| Activo/familia conholdout activo | Bootstrap p05 /p50 /p95 | N base /doble costo |
| --- | --- | --- |
| S/R | 0.0000% / 0.2003% / 0.5475% | 1 / 0 |
| SOL/T | -0.3556% / -0.0384% / 0.2179% | 1 / 1 |
| STX/T | -0.4159% / -0.0231% / 0.2263% | 1 / 1 |
| STX/R | -0.2376% / 0.2815% / 1.1429% | 2 / 1 |
| TIA/T | -0.3030% / -0.0732% / 0.0000% | 1 / 1 |
| TRX/T | -0.4975% / -0.1953% / 0.0000% | 1 / 0 |
| UNI/T | -0.2664% / 0.2095% / 0.8873% | 2 / 2 |
| WLD/T | -0.3117% / -0.0945% / 0.0356% | 1 / 1 |
| XLM/T | -0.5927% / -0.2413% / 0.0000% | 1 / 1 |
| ZEC/T | -0.1551% / 1.0873% / 2.5616% | 4 / 4 |
| ZRO/T | -0.2737% / -0.1004% / 0.0000% | 1 / 1 |

Bootstrap 2000 réplicas, bloques 10 d, seed 42; percentiles de retorno resampleado, no probabilidades de ganar ni corrección por elegir entre muchos activos. Con 1–3 operaciones informa poco. Sensibilidad de costos 80/30 bps por lado vuelve a simular filtros, por lo que pueden cambiar fills; no se desplazan barreras. Buy/hold de 20% ycash 80% es un experimento por activo, no una cartera de todos ellos; cash 0 no modela interés/inflación/custodia.

| Activo | Buy/hold20% ret holdout | DDholdout | Ret continuo elegible |
| --- | --- | --- | --- |
| S | 22.057% | -9.295% | -11.860% |
| SHIB | 2.767% | -5.621% | -13.307% |
| SOL | 8.450% | -5.292% | -8.493% |
| STX | 15.984% | -11.888% | -13.308% |
| SUI | 6.608% | -8.705% | -14.923% |
| TAO | 3.934% | -6.049% | -8.121% |
| TIA | 8.207% | -7.271% | -15.762% |
| TON | -4.208% | -6.929% | -11.690% |
| TRUMP | -0.255% | -11.656% | -16.244% |
| TRX | 0.340% | -1.395% | 4.287% |
| UNI | 26.844% | -15.302% | 2.894% |
| VIRTUAL | 3.092% | -8.057% | -9.389% |
| WIF | 1.319% | -8.369% | -16.819% |
| WLD | -0.223% | -6.765% | -14.085% |
| XLM | -0.877% | -7.031% | -8.360% |
| XPL | -5.551% | -7.954% | -8.262% |
| XRP | 4.490% | -4.924% | -8.848% |
| ZEC | 40.628% | -16.263% | 491.743% |
| ZRO | 24.858% | -10.193% | -6.980% |

Q reproduce las reglas de rebote propuestas, no T/R. Selector ADXdiario<=25→R;>25→M, fijado antes de recopilar esta tanda tras ser exploratorio en la anterior. Usa 1 h,4 h ydiarias solo desde su cierre, as-of hacia atrás ycontroles de prefijo sin futuro. Warmup 200 h, luego 520 h evaluadas; señal 1 h en zona conclose>open, close>midrange, low>stop; intento solo alopen siguiente dentro de zona y RRreal>=2. R7 d/M5 d, barreras fijas, stop primero ante dobletoque, gaps alopen, sin reentrada misma barra, cierrefinal. Costos aditivos 55 bps/lado como el gate, estrés 110 bps. Equity ilustrativo 10,000, riesgo 0.05%, tope activo 20%, una entrada/día y reglas experimentales de pérdidas acotadas por cada serie individual.

No es simulación de 38 posiciones ni del presupuesto global. No incluye profundidad histórica, colas, ticks de cantidad/mínimos ejecutados, revisión 5 cierres/5 R o restricciones de eventos futuros de esta propuesta. Qpuede simular en LIGHTER con medias disponibles, pero no elimina el fallo de calidad de datos del gate. No se rebaja warmup o política para aprobar. Ausencia de fill no es éxito; resultados negativos no se ocultan.

| Activo | Señales enplano | Fills /retQ | DDQ | Fills /ret costo doble |
| --- | --- | --- | --- | --- |
| S | 2 | 0 / 0.00000% | 0.00000% | 0 / 0.00000% |
| SHIB | 2 | 2 / -0.09997% | -0.09997% | 1 / -0.05000% |
| SOL | 2 | 0 / 0.00000% | 0.00000% | 0 / 0.00000% |
| STX | 3 | 0 / 0.00000% | 0.00000% | 0 / 0.00000% |
| SUI | 1 | 0 / 0.00000% | 0.00000% | 0 / 0.00000% |
| TAO | 1 | 0 / 0.00000% | 0.00000% | 0 / 0.00000% |
| TIA | 3 | 0 / 0.00000% | 0.00000% | 0 / 0.00000% |
| TON | 3 | 1 / -0.05000% | -0.05106% | 1 / -0.05000% |
| TRUMP | 0 | 0 / 0.00000% | 0.00000% | 0 / 0.00000% |
| TRX | 2 | 2 / -0.09997% | -0.09997% | 0 / 0.00000% |
| UNI | 4 | 0 / 0.00000% | 0.00000% | 0 / 0.00000% |
| VIRTUAL | 4 | 1 / -0.05000% | -0.06499% | 1 / -0.05000% |
| WIF | 2 | 0 / 0.00000% | 0.00000% | 0 / 0.00000% |
| WLD | 5 | 1 / -0.05000% | -0.05575% | 1 / -0.05000% |
| XLM | 5 | 2 / -0.05301% | -0.10415% | 1 / -0.01551% |
| XPL | 1 | 1 / -0.05000% | -0.05000% | 1 / -0.05000% |
| XRP | 1 | 0 / 0.00000% | 0.00000% | 0 / 0.00000% |
| ZEC | 1 | 0 / 0.00000% | 0.00000% | 0 / 0.00000% |
| ZRO | 0 | 0 / 0.00000% | 0.00000% | 0 / 0.00000% |

## Dos libros y límites de ejecución

Profundidad=asks hasta 10 bps del mejorask, participación máxima 1%; para ejemplos se toma el menor tope de ambos libros. No promediar un spread fallido con uno válido. El volumen 24 h USD es aproximación precio típico×volumenbase de 24 barras Kraken, no volumen CoinGecko auditado. Liquidez en la entrada no garantiza salida enstress; órdenes límite pueden no llenar.

| Activo | HoraUTC inicial /contraste | Spread bps inicial /contraste | Tope1%USD inicial /contraste | Vol24hUSD aprox. | Horas sinvol. |
| --- | --- | --- | --- | --- | --- |
| S | 18:02:00 / 22:37:54 | 21.436 / 42.283 | 4.09 / 22.65 | 81493 | 0.00% |
| SHIB | 18:02:10 / 22:37:56 | 6.153 / 4.132 | 63.48 / 94.00 | 215437 | 0.00% |
| SOL | 18:02:18 / 22:37:57 | 1.975 / 0.999 | 6025.26 / 5699.90 | 13392716 | 0.00% |
| STX | 18:02:26 / 22:37:58 | 9.812 / 6.649 | 36.89 / 16.10 | 408420 | 0.00% |
| SUI | 18:02:34 / 22:37:59 | 2.183 / 1.102 | 852.82 / 931.53 | 5483705 | 0.00% |
| TAO | 18:02:42 / 22:38:00 | 3.815 / 7.577 | 621.31 / 608.36 | 3394646 | 0.00% |
| TIA | 18:02:50 / 22:38:01 | 3.661 / 5.527 | 27.20 / 21.61 | 594333 | 0.00% |
| TON | 18:02:57 / 22:38:02 | 8.193 / 8.254 | 23.10 / 12.68 | 589305 | 0.00% |
| TRUMP | 18:03:05 / 22:38:03 | 11.758 / 5.947 | 167.15 / 47.30 | 206320 | 0.00% |
| TRX | 18:03:13 / 22:38:04 | 0.030 / 0.425 | 946.76 / 806.54 | 1040236 | 0.00% |
| UNI | 18:03:21 / 22:38:05 | 4.086 / 3.397 | 465.28 / 696.48 | 2018788 | 0.00% |
| VIRTUAL | 18:03:29 / 22:38:07 | 1.615 / 4.914 | 40.14 / 84.04 | 272243 | 0.00% |
| WIF | 18:03:37 / 22:38:08 | 11.099 / 11.167 | 22.24 / 32.13 | 227621 | 0.00% |
| WLD | 18:03:45 / 22:38:09 | 15.839 / 9.172 | 155.16 / 315.77 | 1982293 | 0.00% |
| XLM | 18:03:53 / 22:38:10 | 0.652 / 1.074 | 623.40 / 470.59 | 3844396 | 0.00% |
| XPL | 18:04:01 / 22:38:11 | 26.954 / 27.739 | 22.78 / 25.24 | 321170 | 0.00% |
| XRP | 18:04:09 / 22:38:12 | 0.309 / 0.388 | 4429.78 / 5497.62 | 23220737 | 0.00% |
| ZEC | 18:04:17 / 22:38:13 | 8.880 / 2.789 | 1101.77 / 424.93 | 18350824 | 0.00% |
| ZRO | 18:04:25 / 22:38:14 | 17.894 / 18.524 | 104.01 / 38.59 | 1384665 | 0.00% |

[Stop loss Kraken](https://support.kraken.com/articles/7699391647892-stop-loss-orders), actualización 06-10-2026, consulta 26-10-2026 UTC: el disparo genera una orden a mercado y puede llenar peor que elstop, con fees taker. La protección es una orden independiente; tras una salida por otro motivo cancelar remanentes. El Lab no transmite órdenes ni vigila continuamente MDL. No dividir órdenes para eludir capacidad o reiniciar presupuesto.

## Reglas del plan y niveles de investigación

Soporte=min 20 barras 4 h; techoQ=soporte+0.5 ATR1 h. M: stop=soporte−ATR4 h, target=EMA50 d, máximo 5 d; R: stop=min 10 d−0.25 ATR4 h, target=Bollinger superior diaria, máximo 7 d. Precios redondeados hacia abajo al tick. Selector y fórmulas se congelaron antes de datos nuevos. Barreras de medias/Donchian intermedias pueden impedir llegar al target; no hay salida implícita por tocarlas que contradiga el RR mostrado.

**Aclaración algebraica posterior a observar datos:** el protocolo requiere RR>=2 en el precio real de entrada dentro de zona. Su intersección esE<=((1−C)*(T+2 S))/(3*(1+C)). El techo admisible es min(techoQ, techo RR2), sin alterarS/T o expandir la zona; si el techo RR2 queda bajo soporte no existe entrada válida. SOL/ZEC tenían RRligeramente<2 en el techo bruto pero una subzona inferior válida. No se presenta esta aclaración de visualización como preregistro anterior a datos; el diagnóstico congelado ya comprueba RR alopen real y no cambió ningúnfill. No se buscó otro parámetro para mejorar rentabilidad.

Niveles en USD, estáticos de research; **no órdenes listas para ejecutar tras esperar al 29**. Al activarse untrigger, recoger dataset/libro nuevos, recalcular la misma fórmula y crear unaProposal nueva. Cambios de cuenta, política, datos o propuesta requieren hashes y dos revisiones nuevas. No usar aprobación histórica para niveles actuales.

| Activo /tipo | Zona soporte–techo admisible | TechoQ bruto | Stop /target | RR /estrés | Horizonte | Decisión |
| --- | --- | --- | --- | --- | --- | --- |
| S/M | 0.0461–0.0463 | 0.0463 | 0.0448 / 0.0435 | -1.646 / -1.514 | 5d | DESCARTAR CONFIGURACIÓN |
| SHIB/M | 0.000004756–0.000004773 | 0.000004773 | 0.000004679 / 0.000005261 | 2.965 / 1.907 | 5d | SECUNDARIO CONDICIONADO |
| SOL/M | 98.51–98.88 | 98.93 | 96.93 / 106.09 | 2.009 / 1.207 | 5d | PRINCIPAL CONDICIONADO |
| STX/M | 0.2928–0.2949 | 0.2949 | 0.2833 / 0.3298 | 2.129 / 1.561 | 5d | SECUNDARIO CONDICIONADO |
| SUI/R | 0.8989–0.9041 | 0.9041 | 0.898 / 1.1611 | 15.342 / 9.038 | 7d | SECUNDARIO CONDICIONADO |
| TAO/R | 242.408–243.7756 | 243.7756 | 241.0766 / 301.0734 | 10.120 / 6.387 | 7d | SECUNDARIO CONDICIONADO |
| TIA/M | 0.5155–0.5199 | 0.5199 | 0.4976 / 0.4987 | -0.961 / -0.968 | 5d | DESCARTAR CONFIGURACIÓN |
| TON/M | 1.155–1.16 | 1.16 | 1.131 / 1.397 | 5.359 / 3.854 | 5d | SECUNDARIO CONDICIONADO |
| TRUMP/R | 1.617–1.625 | 1.625 | 1.611 / 2.003 | 11.260 / 6.817 | 7d | SECUNDARIO CONDICIONADO |
| TRX/R | 0.328279–0.328566 | 0.328566 | 0.327113 / 0.335856 | 0.719 / -0.002 | 7d | DESCARTAR CONFIGURACIÓN |
| UNI/M | 6.5078–6.5543 | 6.5543 | 6.3137 / 7.2609 | 2.025 / 1.451 | 5d | PRINCIPAL CONDICIONADO |
| VIRTUAL/M | 0.6051–0.6079 | 0.6079 | 0.5927 / 0.6941 | 3.625 / 2.530 | 5d | SECUNDARIO CONDICIONADO |
| WIF/M | 0.175–0.1759 | 0.1759 | 0.1708 / 0.2074 | 4.195 / 3.061 | 5d | SECUNDARIO CONDICIONADO |
| WLD/R | 0.4308–0.4344 | 0.4344 | 0.4266 / 0.5894 | 11.916 / 8.323 | 7d | SECUNDARIO CONDICIONADO |
| XLM/M | 0.165886–0.16656 | 0.16656 | 0.16329 / 0.19 | 4.225 / 2.829 | 5d | PRINCIPAL CONDICIONADO |
| XPL/R | 0.0706–0.071 | 0.071 | 0.0701 / 0.0909 | 11.342 / 7.389 | 7d | DESCARTAR CONFIGURACIÓN |
| XRP/R | 1.2533–1.25875 | 1.25875 | 1.24841 / 1.45518 | 7.522 / 4.393 | 7d | PRINCIPAL CONDICIONADO |
| ZEC/R | 1117.29–1126.97 | 1128.05 | 1037.4 / 1343.52 | 2.000 / 1.670 | 7d | POSPUESTO NU7 |
| ZRO/M | 1.637–1.654 | 1.654 | 1.571 / 1.659 | -0.131 / -0.265 | 5d | DESCARTAR CONFIGURACIÓN |

En los descartes las cifras solo hacen auditable el fallo; no son instrucciones alternativas. No se cambianstop/target para conseguirratio o tamaño. Para LIT existe además incertidumbre crítica de canje/derecho vigente antes de cualquier ejecución; para LIGHTER el mínimo de historia impide el gate. ZEC permanece pospuesto aunque alcance el filtro aritmético.

Activación y gestión:

1. Verificar evento/calendario, moneda ycuenta, señal y precio, elegibilidad regional y que no haya otro piloto abierto. La prioridad solo decide entre propuestas igualmente válidas; no obliga aesperar unactivo indefinidamente.
2. Rechazo 1 h conlow>stop, close>open, close>(high+low)/2 yclose dentro[soporte, techo admisible]. El toque solo no es señal. En la siguiente barra, un único intento con precio ejecutable dentro de zona y límite<=techo; si abre fuera o no llena inmediatamente, cancelar remanente y esperar otra señal. No perseguir.
3. Recalcular RRreal>=2, costos efectivos, cash, exposición, profundidad, spread<=20 bps, mincantidad/mincost y ticks. Si los costos se acercan al escenario doble, varios planes dejan de ser válidos; no reducirlos artificialmente para pasar.
4. Stop estructural ytarget fijos sobre la cantidad comprada, sin parciales, trailing, promedio a la baja ni agregar exposición. El cambio de ADX después del fill no cambia deM aR. Horizonte 5/7 d desdefill, salida temporal al cumplirse aunque no alcance RR nominal. Un incidente verificado que destruya la tesis exige cierre supervisado/registro; no esperar que un indicador lo absorba.
5. Invalidación antes de entrada por pérdida del stop/base, noticia material contraria, fallo devenue o riesgo. Durante eltrade, mantener protección ycapacidad de supervisar; si el operador no puede vigilar/reconciliar no abrir. Los gaps pueden exceder la pérdida prevista.
6. Datos de mercado<120 s, cuenta<300 s, revisión<3600 s, plan<3600 s ydesviación máxima de entrada 1%. Un escenario que apunta a precio lejano no exime la comprobación. Este informe no esReview operativa niREADY; falta Claude real sobre el mismohash.

## Riesgo, tamaño y presupuesto compartido

Referencia de capital 50,000 ya confirmada; moneda ysaldo actual no inferidos. Máximos 3%MDL/6%MDD; operativos 2%/4%; reserva 20% del MDL operativo(0.4%equity inicial deldía), sinconsumir colchón. Máximoordinario 0.25%portrade, riesgoagregado stops 0.50%, bruto 50% yporactivo 20%. Elpiloto añade máximo 0.05%, una posición global, una entrada/día UTC, pausa diaria 0.15%, pérdidasacumuladas 0.50%,20 cierres/30 días desdeprimerfill oinvalidación, lo primero; revisar 5 cierres o 5 R netos perdidos. Ganancias no renuevan automáticamente presupuesto.

Esas reglas extra requieren control humano: no se implementó unmonitor automático y no se cambiaronflags o límites del Lab. Son compartidas entre 70 filas, ambas IAs y todas las tandas; no sumar propuestas o tamaños. Riesgos/órdenes pendientes ytenencias deben reconciliarse en la misma moneda conconversiones explícitas. MDD respecto amax(capital inicial, pico reconciliado); no reiniciaralias, base, diario olockout para eludir pérdidas.

ParaE, S, T, C=.0055/lado:

`pérdida_unidad = E-S+(E+S)*C`

`RR_neto = (T-E-(T+E)*C)/pérdida_unidad`

`riesgo_permitido = min(0.0005*equity, remanenteMDL_reserva, remanenteMDD_reserva, remanente_stops, remanente_piloto)`

`q = floor_precision(min(riesgo_permitido/pérdida_unidad, exposición_disponible/E, cash/(E*(1+C)), tope_profundidad/E))`

Rechazar si q está bajo mínimo o q*E bajo mínimo monetario. Pérdida prevista alstop no es garantía defill. Ejemplo normalizado de 10,000 USD hipotéticos, sin posiciones/órdenes y riesgo máximo 5 USD, solo comparación. No representa una cuenta ni se suman filas:

| Activo apto deprecio | Cantidad ilustrativa | NotionalUSD | RiesgoUSD previsto | Restricción dominante |
| --- | --- | --- | --- | --- |
| SHIB | 13299175.74513 | 63.477 | 1.9415 | profundidad |
| SOL | 1.65182501 | 163.332 | 5.0000 | riesgo0.05% |
| STX | 54.61168409 | 16.105 | 0.8072 | profundidad |
| SUI | 312.27457 | 282.327 | 5.0000 | riesgo0.05% |
| TAO | 0.93184 | 227.160 | 5.0000 | riesgo0.05% |
| TON | 10.93453 | 12.684 | 0.4549 | profundidad |
| TRUMP | 29.11044 | 47.304 | 0.9257 | profundidad |
| UNI | 16.05785967 | 105.248 | 5.0000 | riesgo0.05% |
| VIRTUAL | 66.03385 | 40.142 | 1.4398 | profundidad |
| WIF | 126.41012 | 22.236 | 0.8857 | profundidad |
| WLD | 357.17776 | 155.158 | 4.4774 | profundidad |
| XLM | 983.44372489 | 163.802 | 5.0000 | riesgo0.05% |
| XRP | 207.21626498 | 260.833 | 5.0000 | riesgo0.05% |
| ZEC | 0.04927368 | 55.530 | 5.0000 | riesgo0.05% |

## Incertidumbre y cierre de investigación

Críticos para ejecución: identidad/región ymoneda/costos/cuenta reconciliada, posiciones/órdenes/flujos/baseline/pico, datos/propuesta vigentes, dos revisiones reales del mismohash ygate. No marcarlos verificados por inferencia. Datos insuficientes para elgate o un producto fuera de alcance no se vuelven válidos por consenso. Estos faltantes no paralizan cerrar elresearch.

Materiales: ventaja desconocida, muestras/selección adaptativa, ejecuciónhistórica aproximada, salidaenstress, concentraciónholders, emisiones/adopción/ingresos no auditados yprobabilidad de alcanzar targets remotos. Se aceptan por Codex solo para el diseño experimental pequeño ycon restricciones explícitas; Claude debe aceptar o rechazar por separado esas mismas incertidumbres. Un nivel con RR alto no permite asignar probabilidad alta. Faltantes específicos se explican en cada ficha.

Menores para esta decisión: API opcional de actividad no disponible odesglose secundario que no cambia la tesis/sizing. No convertir ausencia de unaAPI gratuita en rechazo automático. Las noticias no se conocen al 100%; no se inventó un catalizador o ausencia de todo incidente. Antes deoperar, revisar eventos/incidentes nuevos yprecios reales.

Punto de cierre: cubiertas identidad, técnico/estadístico, economía/tokenómica, fuentesprimarias contradictorias, referencias ydiagnóstico pertinente, doslibros, costos, eventos ygestión. Se hicieron búsquedas dirigidas para LIGHTER/LIT, denominación TON, fees/recompras de UNI/OP/LDO/PENDLE/SUI/PUMP, emisiones TIA/NEAR/TAO y NU7. Fuentes genéricas adicionales no cambiarían materialmente los planes. Se decide conservar, descartar oesperar untrigger/evento, sin exigir información perfecta o rondas indefinidas.

## Revisión propia de Codex y trazabilidad

**Aprobación condicional del diseño, abstención de aprobar ejecución.** Se conservan los principales ysecundarios indicados con evidencia adversa visible; los casos descartados/pospuestos permanecen así pese a sus narrativas o beneficios históricos. No se finge revisión de Claude ni READY. La hipótesis de rebote 5/7 d, señal causal, entrada limitada, stop estructural, target ybarreras, costos, sizing, invalidación yseguimiento son congruentes bajo incertidumbre aceptada. Esa aceptación no asegura valor esperado positivo.

No se ha leído el estudio Claude antes de fijar esta lista ysu hash. Los especialistas aportaron investigación factual autorizada yno firman como una IA distinta. La comparación posterior debe usar mismos instrumentos, moneda, cutoff ycostos o mostrar las diferencias, sin alterar retrospectivamente esta propuesta para imitarla. Elegir la mejor hipótesis no equivale a probar qué IA tiene razón antes de observar resultados registrados prospectivamente.

Verificación del Lab en su base congelada:70 tests offline yruff aprobados. Los diagnósticos pasaron disponibilidad temporal/prefijos, gaps, dobletoque, siguiente barra, costos, riesgo máximo ycontabilidad. Compatibilidad: pandas/NumPy emiten deprecaciones detimedelta en scripts de sesión; se limitaron sus avisos, sin silenciarerrores, cambiarTLS o alterar resultados. Se limpióSSLKEYLOGFILE del proceso por ruta ambiental inaccesible, conservando verificaciónTLS.

Replay exacto requiere snapshots/scripts locales; estos documentos no contienen todos los insumos. Consultas repetidas aAPI no reproducen unlibro histórico. Reproducción conceptual: resolveruniverso→collectenrich→dossiers→T/R congeladas→Qcausal→doslibros→análisisprimario→riesgo/revisión. `lab backtest` es otrareferencia EMA yno sustituye estasreglas. No se llamódecide con cuenta sintética ni se modificópolítica para obtenerPASS. Las fuentes nuevas usanGET público y PublicClient con timeout 25 s, retries máximos 3 ymetadata; probe XYZ100 de especialista fue metadatosPOST de sololectura, sin órdenes ni credenciales de trading.

HashesDataset canónicos SHA256 ylimitaciones permiten auditar versiones; el hash deeste informe figura enconclusiones. Publicación porrama/PR nueva, sinforcepush, identidadjsforeroc 80-debug ypreservación dearchivos remotos; los resultados se verifican antes de afirmar publicación.

| Activo | DatasetSHA256 | Calidad1h/4h/d |
| --- | --- | --- |
| S | `ca7027bd7f5a9aecba09cee4536f0b48ec1c223031959acb9948432eb539b6ba` | PASS / PASS / PASS |
| SHIB | `9ebf0f7362f70dc98717e268b977ccf0c8d69b670561bf5bd7a6738a0d4ccfec` | PASS / PASS / PASS |
| SOL | `f7f4d66bae5e0614ace628e09fdd0c62f742771e36421af3c98eed321d0acf5a` | PASS / PASS / PASS |
| STX | `1d83c1333cf1c20850a81dc5a7c39cd68947a45ebb0a7bbbc9eb063d0122b020` | PASS / PASS / PASS |
| SUI | `4ff8a63bb3db5a611be7b4f79bccbbee2305612fbd3f699950154f5a240801b6` | PASS / PASS / PASS |
| TAO | `e7d52338dc85c721c84c3413b45d36a6e7ff4ebddd2a89b3f5e0f91764ad09ca` | PASS / PASS / PASS |
| TIA | `34ce95b49aca6c8bdec3b715e9fc0d2b0cca8be0784fa07188dc298e17f8523d` | PASS / PASS / PASS |
| TON | `0fa77bd5fd09d3396662b3b07a376748a88ca2aef1ab2895c52d43125e46381c` | PASS / PASS / PASS |
| TRUMP | `9151bf98ff9a0874181091a062689a81a49145508e023258540220ca0e1d2a91` | PASS / PASS / PASS |
| TRX | `779ecb70743236ff03dd389803d859ea634a7874eafdb4cd59219a8312d3be0b` | PASS / PASS / PASS |
| UNI | `e76da059ee2ed0274fdec8f42313ae69e521986277520b7f99ee620bbd6bd43f` | PASS / PASS / PASS |
| VIRTUAL | `9f1475e8be2ed89298c647996293a3f710bafa7277f210720562b9fe761fc432` | PASS / PASS / PASS |
| WIF | `351203d3efa9d1704c2052a09576c1cabdfa1cb17a79c8d2bf60fbec0e480fa2` | PASS / PASS / PASS |
| WLD | `2a3109a33897c875a1e914c6da9da1d9e357a1586131452b2a0bcff4604bd642` | PASS / PASS / PASS |
| XLM | `a3d8097b1937939f53996ab51b7fde8db965f2fefbeb3aa186d065920a086cc2` | PASS / PASS / PASS |
| XPL | `87ce9bfcd058d76b0de747b3416660e4906dbe1ed1aa66b03852d2ff011de23a` | PASS / PASS / PASS |
| XRP | `55903efe539b1aecbaddefd8ba7cf7f82896fbf5f319837668efe453dac75344` | PASS / PASS / PASS |
| ZEC | `03d33f678e4de0533cfd6e792fc519451b597322748e9e1b89cbd32fddcf02b2` | PASS / PASS / PASS |
| ZRO | `cd8bfc48a805d710a5e9ca3e746d0458eed258c0721f3cf7d8ccd8fb39b1980c` | PASS / PASS / PASS |

Excel SHA256:`b1d475c71ad6de7c33f534a5bb854227851ecbfdb36a393b130c8d0a351b211c`.

Protocolo previo SHA256:`72dfd138cc43bbde6f301d6c4a9691435512c9551c57ebee345e73da220eeb92`. Aclaración posterior del techo RR2 SHA256:`9ae7cd6da8ab83977c19c399d455b1f853fac92fa2b8fbf59018c769dac2086d`.

Manifiesto SHA256:`265195220f816af845a53eebbbf94f125562fc838649f3343c68e32e5065f252`. Cuenta ycredenciales excluidas.
