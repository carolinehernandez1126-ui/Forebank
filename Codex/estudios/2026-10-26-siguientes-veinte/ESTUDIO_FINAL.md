# Estudio final de Codex — siguientes veinte activos

**26 de octubre de 2026, America/Bogota · Investigación propia e independiente.** Universo: Excel A12:A31, posiciones 11–30. Corrección humana expresa: A15 «CVR» significa **CRV, Curve**; se conserva el Excel original. Mercado real Kraken, `synthetic=false`. Publicación limitada al estudio final y conclusiones, sin conversaciones, secretos ni información de cuenta. Claude desarrolla su investigación por separado; aquí no se leyó su estudio ni se emite una firma en su nombre.

## 1. Decisión y alcance

**Conservar cuatro candidatos principales de retroceso: BTC → ETH → HYPE → DOGE**, en ese orden de preferencia entre propuestas simultáneamente válidas. Conservar siete alternativas subordinadas: INJ, CRV, ENA, HBAR, BONK, FLOKI y ETHFI. Las otras nueve configuraciones se descartan por geometría, costos o ejecución. Ningún activo tiene entrada activa en el corte observado. Once filtros aritméticos aprobados no son once recomendaciones de comprar hoy ni una cartera de once posiciones.

Se admite un **piloto real con ventaja estadística desconocida**, riesgo máximo propuesto 0.05% de equity, una posición experimental global simultánea y una entrada nueva al día UTC. No se exige un backtest ganador, significancia o rentabilidad fuera de muestra para permitir ese piloto. Sí se exige una hipótesis falsable, ejecución viable y aceptación real de la incertidumbre por Codex y Claude, además de cuenta y motor de riesgo válidos. El resultado no acredita rentabilidad futura.

La prioridad favorece ejecución y objetivos menos remotos; no se seleccionó el mayor resultado histórico ni el ratio nominal más alto. BTC/ETH tienen los mejores libros de esta tanda. HYPE añade una tesis de actividad de protocolo con historial Kraken corto y oferta pendiente. DOGE tiene buen libro, pero tesis más dependiente de flujos especulativos y estructura diaria débil. Son candidatos alternativos: una sola oportunidad puede utilizar el presupuesto compartido con las tandas anteriores.

**Fecha más temprana para reconsiderar nuevas entradas: 29-10-2026, 00:00 UTC**, después de comprobar la publicación del comunicado FOMC y condiciones estables. Es una restricción de evento elegida para este piloto, no una regla de Kraken ni una promesa de entrada ese día. La Fed publica reunión 27–28 octubre; no se anticipa el resultado. [Calendario oficial FOMC](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm), consulta 26-10-2026 UTC, página vigente sin fecha de publicación individual para esa reunión.

No existe READY: faltan cuenta reconciliada, moneda/fees efectivos y revisión real de Claude sobre la misma propuesta vigente. Los snapshots ya son históricos para ejecución. El estudio concluye y permite preparar decisiones; esos faltantes no justifican investigar indefinidamente. [Conclusiones y hash de este informe](CONCLUSIONES.md).

## 2. Selección, identificadores y límites de los datos

Se siguió el orden original, sin saltar activos por su rendimiento. Hoja «Lista de activos», archivo `archivos_de_apoyo/lista_activos.xlsx`. BNB, BONK, BTC, CRV, DOGE, DOT, ENA, ETC, ETH, ETHFI, FARTCOIN, FIL, FLOKI, GRASS, HBAR, HYPE, ICP, INJ, JTO y JUP. La siguiente fila pendiente es A32, KAITO. No se ha investigado aquí esa siguiente tanda.

Todos los instrumentos estaban online, spot y cotizados en USD en el registro público. Esa disponibilidad no certifica elegibilidad regional ni saldo del operador. No se usan las posibilidades de margen que la API pueda listar. Las denominaciones Bitcoin/XBT y Dogecoin/XDG son alias del mismo activo. JUP se identifica como Jupiter de Solana, no otro proyecto homónimo. Los activos nativos no se sustituyen por versiones wrapped.

| Fila | Activo | Par Kraken exacto | ID CoinGecko | Identidad | Tick / mínimo unidades |
| --- | --- | --- | --- | --- | --- |
| 12 | BNB | BNBUSD | binancecoin | Nativo BNB Chain | 0.01 / 0.007 |
| 13 | BONK | BONKUSD | bonk | Solana SPL | 0.000000001 / 1300000 |
| 14 | BTC | XXBTZUSD | bitcoin | Bitcoin nativo; alias XBT | 0.1 / 0.00006 |
| 15 | CRV | CRVUSD | curve-dao-token | Curve ERC 20 Ethereum | 0.00001 / 15 |
| 16 | DOGE | XDGUSD | dogecoin | Dogecoin nativo; alias XDG | 0.0000001 / 50 |
| 17 | DOT | DOTUSD | polkadot | Polkadot nativo | 0.0001 / 3.9 |
| 18 | ENA | ENAUSD | ethena | Ethena ERC 20 Ethereum | 0.0001 / 20 |
| 19 | ETC | XETCZUSD | ethereum-classic | Ethereum Classic nativo | 0.001 / 0.6 |
| 20 | ETH | XETHZUSD | ethereum | Ethereum nativo | 0.01 / 0.002 |
| 21 | ETHFI | ETHFIUSD | ether-fi | ether.fi ERC 20 Ethereum | 0.0001 / 7 |
| 22 | FARTCOIN | FARTCOINUSD | fartcoin | Solana SPL | 0.0001 / 30 |
| 23 | FIL | FILUSD | filecoin | Filecoin nativo | 0.001 / 5 |
| 24 | FLOKI | FLOKIUSD | floki | Ethereum/BSC, mismo proyecto | 0.00000001 / 180000 |
| 25 | GRASS | GRASSUSD | grass | Solana SPL | 0.0001 / 7 |
| 26 | HBAR | HBARUSD | hedera-hashgraph | Hedera nativo | 0.00001 / 55 |
| 27 | HYPE | HYPEUSD | hyperliquid | Hyperliquid nativo | 0.01 / 0.06 |
| 28 | ICP | ICPUSD | internet-computer | Internet Computer nativo | 0.001 / 1.5 |
| 29 | INJ | INJUSD | injective-protocol | Injective nativo | 0.001 / 0.7 |
| 30 | JTO | JTOUSD | jito-governance-token | Jito governance Solana | 0.00001 / 9 |
| 31 | JUP | JUPUSD | jupiter-exchange-solana | Jupiter Solana | 0.00001 / 15 |

| Token | Contrato de identidad; no instrucción de depósito |
| --- | --- |
| BONK | `DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263` |
| CRV | `0xd533a949740bb3306d119cc777fa900ba034cd52` |
| ENA | `0x57e114b691db790c35207b2e685d4a43181e6061` |
| ETHFI | `0xfe0c30065b384f05761f15d0cc899d4f9f9cc0eb` |
| FARTCOIN | `9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump` |
| FLOKI | `ETH:0xcf0c122c6b73ff809c693db761e7baebe62b6a2e; BSC:0xfb5b838b6cfeedc2873ab27866079ac55363d37e` |
| GRASS | `Grass7B4RdKfBCjTKgSqnXkqjwiGvQyFbuSCUJr3XXjs` |
| JTO | `jtojtomepa8beP8AuQc6eXt5FriJwfFMwQx2v2f9mCL` |
| JUP | `JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN` |

Los contratos se contrastaron con el registro de plataformas CoinGecko, la red listada por Kraken y documentación del proyecto cuando estaba disponible. La coincidencia de símbolo sola no bastó. Son identificadores de investigación, no una auditoría de contratos ni rutas de depósito. ICP usa el ledger canister `ryjl3-tyaaa-aaaaa-aaaba-cai`; INJ se estudia en su red nativa, no como el antiguo ERC 20. BNB y HYPE también son nativos aunque un agregador ofrezca direcciones de otras representaciones. [Lista de activos Kraken](https://support.kraken.com/articles/360000678446-cryptocurrencies-available-on-kraken) y [registro CoinGecko](https://api.coingecko.com/api/v3/coins/list?include_platform=true), consulta 26-10-2026 UTC, registros dinámicos sin fecha editorial. No queda CVR ambiguo después de la corrección humana.

Recopilación principal: **26-10-2026,12:28:41.958774–12:31:22.852373 UTC**. Segundo libro:12:33 UTC, hora individual en tabla de liquidez. Se conservan 720 velas cerradas 1 h y 720 de 4 h para cada activo. Diarias:720 salvo BNB 552, FARTCOIN 641, GRASS 637, HBAR 473, HYPE 271. Calidad 60/60 aprobada, sin warnings de adquisición. Última 1 h abre 11 UTC/cierra 12 UTC; última 4 h abre 08 UTC/cierra 12 UTC; última diaria abre 25 oct/cierra 26 oct 00 UTC. El precio diario y el de 1 h pueden diferir sin contradicción.

Se excluyó la vela abierta. La documentación OHLC de Kraken anuncia un máximo de 720 entradas recientes y una última entrada mutable; no permite reconstruir historia ilimitada con `since`. En las respuestas archivadas revisadas de BTC se observaron 721 filas incluyendo la mutable: se retuvieron 720 cerradas. El conteo usado procede del payload real, aunque difiere del máximo anunciado en la documentación. Se confirmó que la última 1 h de 12 UTC, la 4 h de 12 UTC y la diaria del 26 oct fueron descartadas; no hay uso de esas velas abiertas. No se rellenaron días con otra bolsa ni se mezclaron precios CoinGecko con velas Kraken. [Documentación OHLC Kraken](https://docs.kraken.com/api-reference/market-data/get-ohlc-data), consulta 26-10-2026 UTC, sin fecha editorial visible. Calidad formal no significa estacionariedad, ausencia de manipulación ni capacidad de ejecución histórica.

## 3. Lectura técnica conjunta

Se calcularon SMA/EMA 20/50/200, RSI 14, MACD 12/26/9, ATR 14, ADX 14, Bollinger 20/2, Donchian 20, OBV, VWAP 20/VWAP de sesión UTC y z-score de volumen 20 en 1 h/4 h/1 d. Se agrupan en tendencia, momentum, volatilidad y participación: EMA/RSI/MACD no son tres confirmaciones independientes. ADX expresa fuerza, no dirección. VWAP/OBV dependen de este venue; no describen todo el mercado. No añadir indicadores hasta obtener una votación favorable.

La clasificación automática «up» del Lab se basa en medias; no implica que el cierre supere EMA 200. Se muestran los niveles para evitar ocultar esa diferencia. FIL, ICP y JUP conservan alguna estructura de medias favorable con precio debilitado; ETH está cerca de EMA 200 d. El rebote intradía de CRV o GRASS tampoco basta para afirmar continuación diaria.

Precios USD. RSI 1 h/4 h/d y ADX d permiten valorar horizonte; cierre 1 h es referencia de mercado cerrado, no el ask de una orden.

| Activo | Cierre 1 h | Cierre d | EMA 20 d | EMA 50 d | EMA 200 d | RSI 1 h /4 h /d | ADX d |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BNB | 742.33 | 737.71 | 740.555826394876 | 733.480221734532 | 690.268566899582 | 56.6 / 54.8 / 48.2 | 23.2 |
| BONK | 0.000002998 | 0.000003002 | 0.000003179933 | 0.000003229974 | 0.000004508971 | 47.9 / 44.9 / 42.7 | 18.3 |
| BTC | 80281.8 | 80048.5 | 82042.9586152327 | 80763.22191520766 | 76268.21958649733 | 51.6 / 43.2 / 41.6 | 17.6 |
| CRV | 0.35316 | 0.34353 | 0.359903544741 | 0.348333206518 | 0.306678340366 | 64.3 / 49.1 / 45.7 | 10.9 |
| DOGE | 0.0771473 | 0.0768086 | 0.082242544536 | 0.084554618204 | 0.091294249916 | 52.7 / 44.2 / 33.5 | 26.6 |
| DOT | 1.0234 | 1.0274 | 1.126953084421 | 1.103003206525 | 1.181587930552 | 48.2 / 36.6 / 37.7 | 16.6 |
| ENA | 0.2055 | 0.2067 | 0.205662299128 | 0.196452459817 | 0.160270026554 | 52.9 / 57.2 / 50.3 | 20.0 |
| ETC | 7.518 | 7.478 | 8.002822651006 | 8.071228154458 | 8.361300467252 | 50.4 / 42.2 / 35.9 | 33.1 |
| ETH | 2330.47 | 2326.5 | 2450.633444353915 | 2462.660549266299 | 2317.315906749067 | 50.2 / 42.2 / 34.1 | 28.5 |
| ETHFI | 0.6323 | 0.6209 | 0.672300082213 | 0.657492373703 | 0.571075895112 | 60.7 / 48.1 / 40.8 | 15.5 |
| FARTCOIN | 0.1258 | 0.1242 | 0.149677706122 | 0.157932953444 | 0.185667934466 | 52.7 / 37.2 / 31.3 | 22.7 |
| FIL | 0.917 | 0.918 | 1.030850978998 | 0.991244182533 | 0.960636326682 | 49.2 / 36.4 / 39.7 | 19.8 |
| FLOKI | 0.00002278 | 0.00002278 | 0.00002474479 | 0.000025332786 | 0.000028376628 | 45.2 / 39.8 / 36.5 | 28.8 |
| GRASS | 0.7165 | 0.719 | 0.650875892476 | 0.576186237635 | 0.457163924211 | 59.9 / 61.9 / 58.0 | 31.0 |
| HBAR | 0.07735 | 0.07741 | 0.084971996754 | 0.085773902719 | 0.087880343415 | 52.1 / 42.9 / 35.7 | 21.6 |
| HYPE | 77.22 | 76.27 | 80.93460594212 | 81.764151453465 | 67.499585219025 | 57.7 / 50.3 / 35.9 | 27.2 |
| ICP | 2.607 | 2.625 | 2.921336061834 | 2.904849799074 | 2.744139321888 | 48.6 / 37.8 / 36.4 | 20.1 |
| INJ | 7.769 | 7.867 | 7.983968986424 | 7.343343864286 | 5.970256983138 | 53.0 / 46.8 / 50.2 | 22.4 |
| JTO | 0.42624 | 0.4222 | 0.476608407625 | 0.496863775725 | 0.539048483067 | 54.2 / 42.3 / 37.9 | 10.1 |
| JUP | 0.28133 | 0.28066 | 0.310062873697 | 0.295823187945 | 0.246880736488 | 49.5 / 37.8 / 40.9 | 21.1 |

| Activo | MACD hist. d | ATRd/cierre | Vol.zd | VWAP 20 4 h | Soporte 20 4 h | Resistencia 20 4 h |
| --- | --- | --- | --- | --- | --- | --- |
| BNB | 0.228826463934 | 2.69% | -0.14 | 739.052486425887 | 717.21 | 749.64 |
| BONK | -0.000000012424 | 8.03% | -0.18 | 0.000003143654 | 0.000002924 | 0.000003359 |
| BTC | -345.497277318248 | 2.59% | -1.18 | 80471.15488262687 | 79120.8 | 81942.7 |
| CRV | -0.001689139916 | 8.34% | -1.30 | 0.353123459943 | 0.33646 | 0.37186 |
| DOGE | -0.000440122197 | 5.18% | -0.81 | 0.077254165544 | 0.074668 | 0.0805826 |
| DOT | -0.018189765308 | 8.24% | -1.63 | 1.091469782908 | 1.0015 | 1.2003 |
| ENA | -0.001158569635 | 10.30% | -0.26 | 0.200144048981 | 0.1838 | 0.2133 |
| ETC | -0.054490781357 | 5.29% | -0.88 | 7.609433597567 | 7.391 | 7.916 |
| ETH | -11.490865158655 | 3.98% | -1.22 | 2345.441910427532 | 2279.8 | 2414.63 |
| ETHFI | -0.009232371425 | 9.90% | -1.06 | 0.628693234315 | 0.5979 | 0.6694 |
| FARTCOIN | -0.002826957566 | 10.85% | -0.54 | 0.131953010857 | 0.1193 | 0.1484 |
| FIL | -0.027960606799 | 10.31% | -1.34 | 0.933323456743 | 0.897 | 0.997 |
| FLOKI | -0.000000216182 | 6.44% | -0.29 | 0.000023665501 | 0.00002252 | 0.00002489 |
| GRASS | -0.005569820996 | 11.10% | 0.63 | 0.679125414286 | 0.6078 | 0.7384 |
| HBAR | -0.001287573752 | 6.90% | -1.43 | 0.077744000544 | 0.07484 | 0.08165 |
| HYPE | -0.527242069989 | 4.96% | -1.37 | 76.690615387357 | 74.33 | 78.85 |
| ICP | -0.057257532001 | 7.74% | -1.31 | 2.682652640553 | 2.556 | 2.79 |
| INJ | -0.109979531962 | 9.97% | -1.09 | 7.739133366663 | 7.415 | 8.312 |
| JTO | -0.007380386947 | 11.09% | -1.15 | 0.430396062905 | 0.41208 | 0.4662 |
| JUP | -0.006155652488 | 9.25% | -0.92 | 0.29177495841 | 0.2735 | 0.31538 |

La mayoría de altcoins está corrigiendo frente a sus medias diarias. El diseño explora comprar un rechazo verificable de soporte, no promediar pérdidas ni asumir que RSI bajo obliga al rebote. GRASS presenta fuerza relativa, pero una vuelta a EMA 50 situada por debajo de la entrada propuesta no puede ser un objetivo long. En varios tokens el mínimo 10 d está por encima del soporte 4 h: esa incongruencia invalida el stop calculado aunque el ratio numérico parezca excelente.

## 4. Estadística, dependencia y condiciones macro

Retornos 7/30/90 d entre cierres Kraken. Volatilidad anualizada con 365 días, Va R 95/CVa R 95 empíricos de un día en la muestra diaria disponible. No son límites de pérdida ni pronósticos gaussianos; curtosis, saltos y dependencia hacen peligroso extrapolarlos. El MDD de precio usa toda la historia disponible de cada activo, de distinta longitud. No confundirlo con MDD del sistema o de la cuenta.

| Activo | 7 d | 30 d | 90 d | Vol.anuald | Va R 95 d | CVa R 95 d | MDD precio muestra | Beta BTC 1 h / correl. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BNB | 2.08% | -5.06% | 30.39% | 47.3% | 3.80% | 5.54% | -58.3% | 0.89 / 0.82 |
| BONK | 2.18% | -19.90% | 1.59% | 120.0% | 8.83% | 12.11% | -95.8% | 2.09 / 0.70 |
| BTC | -2.38% | -4.81% | 25.67% | 44.4% | 3.51% | 4.98% | -53.1% | 1.00 / 1.00 |
| CRV | -2.87% | -3.24% | 65.59% | 108.3% | 8.21% | 11.78% | -85.4% | 1.58 / 0.48 |
| DOGE | -3.23% | -22.40% | 9.22% | 87.7% | 6.17% | 9.86% | -85.2% | 1.55 / 0.82 |
| DOT | -7.97% | -15.27% | 35.51% | 88.6% | 6.52% | 9.50% | -93.0% | 1.76 / 0.57 |
| ENA | 9.83% | -22.87% | 151.77% | 130.3% | 9.80% | 12.49% | -94.4% | 2.21 / 0.59 |
| ETC | -3.50% | -21.14% | 10.21% | 75.9% | 5.42% | 8.29% | -84.3% | 1.50 / 0.71 |
| ETH | -3.36% | -13.56% | 23.02% | 69.7% | 5.17% | 7.87% | -67.6% | 1.23 / 0.89 |
| ETHFI | -8.11% | -13.80% | 52.00% | 122.0% | 9.55% | 13.10% | -90.3% | 2.21 / 0.58 |
| FARTCOIN | -13.69% | -36.83% | 1.97% | 169.6% | 13.34% | 18.36% | -93.6% | 2.38 / 0.69 |
| FIL | -11.90% | -12.40% | 32.28% | 110.2% | 7.13% | 11.16% | -92.2% | 1.91 / 0.52 |
| FLOKI | -2.69% | -21.12% | 10.37% | 104.4% | 7.68% | 11.47% | -92.4% | 1.64 / 0.63 |
| GRASS | 22.18% | 38.24% | 112.09% | 144.4% | 10.62% | 15.34% | -93.8% | 2.25 / 0.40 |
| HBAR | -9.30% | -19.04% | 13.70% | 76.8% | 5.52% | 7.96% | -77.9% | 1.47 / 0.50 |
| HYPE | -3.30% | -17.47% | 36.07% | 84.4% | 6.09% | 8.20% | -30.0% | 1.25 / 0.66 |
| ICP | -9.42% | -17.76% | 25.06% | 99.2% | 7.68% | 10.55% | -86.8% | 1.66 / 0.56 |
| INJ | -9.73% | -3.85% | 66.71% | 104.5% | 8.10% | 11.54% | -92.0% | 2.05 / 0.57 |
| JTO | -4.44% | -26.42% | -25.20% | 118.8% | 8.88% | 11.94% | -94.0% | 2.12 / 0.60 |
| JUP | -3.01% | -17.82% | 54.70% | 104.1% | 7.79% | 11.31% | -90.0% | 1.99 / 0.59 |

La correlación/beta con BTC se estimó sobre 719 retornos 1 h comunes; la matriz diaria conjunta usa 270 observaciones, limitada por HYPE. Son medidas retrospectivas e inestables, no coberturas. BONK/ENA muestran beta elevada; poseer varios tokens de Solana/DeFi no elimina el factor cripto. La regla de un piloto global evita sumar exposiciones correlacionadas bajo nombres distintos. Autocorrelación lag 1, asimetría y curtosis están en los dossiers; no se interpretaron p-values ni se estimaron probabilidades de éxito a partir de tan pocas operaciones.

Las cuatro series FRED son contexto contemporáneo, no features históricas del backtest: no se dispone aquí de vintages para demostrar qué valor se conocía cada día.

| Serie | Última fecha observada | Valor | Comparación con inicio de muestra |
| --- | --- | --- | --- |
| DFF | 2026-10-22 | 3.88 | 2026-09-23: 3.88 → Δ0.0000 |
| DGS 10 | 2026-10-22 | 4.96 | 2026-09-11: 4.96 → Δ0.0000 |
| DTWEXBGS | 2026-10-16 | 121.4048 | 2026-09-08: 117.9127 → Δ3.4921 |
| VIXCLS | 2026-10-22 | 19.03 | 2026-09-11: 15.84 → Δ3.1900 |

Fuentes de esas observaciones: [DFF](https://fred.stlouisfed.org/series/DFF), [DGS 10](https://fred.stlouisfed.org/series/DGS10), [dólar amplio DTWEXBGS](https://fred.stlouisfed.org/series/DTWEXBGS), [VIXCLS](https://fred.stlouisfed.org/series/VIXCLS); consulta API 26-10-2026 UTC, fecha de observación en tabla; fecha exacta de publicación/vintage no verificada. VIX es volatilidad implícita de acciones estadounidenses, no de cripto. Tipos/dólar más exigentes y reunión FOMC próxima son contraevidencia para comprar correcciones indiscriminadamente; la relación causal con cada token no está estimada.

La pausa 27–28 octubre limita exposición al evento; no sustituye stops ni significa que el mercado será seguro el 29. No se exige saber la decisión de la Fed antes de diseñar el plan. No se modeló sorpresa monetaria, probabilidades de recorte, posicionamiento institucional ni liquidaciones de derivados. Ese contexto no autoriza añadir derivados al alcance.

## 5. Fundamentales comparables y límites de valoración

Capitalización y FDV provienen de CoinGecko, no de cuentas auditadas del proyecto. FDV usa la metodología del proveedor y no siempre máximo teórico; por ello no se calcula descuento mecánico al valor justo. Un token no es automáticamente una acción ni tiene derecho a las comisiones de su protocolo. Valores en millones USD; capturados junto al dataset 26-10-2026 UTC, valores de oferta dinámicos.

| Activo | Capitalización MUSD | FDV MUSD | Circulante | Total informado |
| --- | --- | --- | --- | --- |
| BNB | 97557.54 | 97557.54 | 131511669.93 | 131511666.83 |
| BONK | 264.01 | 264.01 | 87994317971913.55 | 87994317971913.55 |
| BTC | 1614166.30 | 1614184.69 | 20103596 | 20103825 |
| CRV | 554.26 | 851.21 | 1581655914 | 2429060384.5891476 |
| DOGE | 12083.02 | 12084.88 | 156461052863.23425 | 156485122860.16907 |
| DOT | 1743.90 | 1743.91 | 1709147832.0604138 | 1709155111.2168295 |
| ENA | 2776.53 | 3106.61 | 13406250000 | 15000000000 |
| ETC | 1198.90 | 1198.90 | 158822869.6169818 | 158823301.0281818 |
| ETH | 284504.78 | 284504.78 | 122164245.28340018 | 122164245.28340018 |
| ETHFI | 637.23 | 637.23 | 998535999 | 998535999 |
| FARTCOIN | 125.75 | 125.75 | 999914464.423245 | 999914464.423245 |
| FIL | 765.72 | 1787.10 | 838487227 | 1956934063 |
| FLOKI | 220.52 | 220.52 | 9642395243758.873 | 9642395243758.873 |
| GRASS | 506.31 | 723.83 | 699492325 | 1000000000 |
| HBAR | 3447.80 | 3889.03 | 44327157617.85491 | 50000000000 |
| HYPE | 17250.85 | 74084.86 | 222445714.07414138 | 955307079.4341414 |
| ICP | 1456.33 | 1456.33 | 558158637.614198 | 558158637.614198 |
| INJ | 775.85 | 775.85 | 100000000 | 100000000 |
| JTO | 229.86 | 428.40 | 536562686.5 | 1000000000 |
| JUP | 935.91 | 1934.63 | 3319369204.37 | 6861485982.001763 |

[CoinGecko coins/markets](https://docs.coingecko.com/reference/coins-markets) y las fichas por ID de la sección 2 sustentan los agregados; consulta 26-10-2026 UTC, sin publicación estática. No se deduce un calendario de desbloqueos de la razón circulante/máximo. BNB conserva en el agregador un máximo de 200 M que no representa sus monedas efectivamente pendientes tras quemas. FLOKI tiene representaciones en dos cadenas: el máximo agregado no se interpreta como dilución económica adicional automática. Las cifras se preservan como reportadas y se priorizan reglas de emisión de fuentes oficiales para la tesis.

Como contraste de actividad se consultó DeFiLlama. Es un agregador secundario, útil para tamaño y composición, no una auditoría ni prueba de captura de valor por el token. TVL no equivale a ingresos, usuarios pagadores, caja distribuible o valor intrínseco. Seis protocolos devuelven TVL; sus scopes y timestamps no son idénticos.

| Protocolo | TVL USD | Timestamp del dato UTC |
| --- | --- | --- |
| Curve DEX | 1165710147.00 | 2026-10-26 T 11:34:23+00:00 |
| Ethena | 5020480869.55 | 2026-10-26 T 11:01:35+00:00 |
| ether.fi | 4867438952.55 | 2026-10-26 T 11:36:35+00:00 |
| Hyperliquid | 8163450860.00 | 2026-10-26 T 11:50:35+00:00 |
| Jito | 1057607068.44 | 2026-10-26 T 11:43:47+00:00 |
| Jupiter | 1738281904.04 | 2026-10-26 T 11:50:35+00:00 |

| Métrica de fees, scope proveedor | 24 h USD | 30 d USD | Limitación |
| --- | --- | --- | --- |
| hype-fees | 1693683.00 | 76922662.00 | perps/HIP 3/builders y componentes adicionales; no todo va al holder |
| jup-fees | 37258.00 | 2002056.00 | plataforma Ultra, no todo Jupiter |
| etherfi-fees | 371047.00 | 12032162.00 | metodología no informada en respuesta; no beneficio neto |
| ena-fees | 6.35 | 16423477.38 | 24 h 6.35 es anomalía/no comparable; no inferir colapso |

Endpoints consultados 26-10-2026 UTC: [Curve](https://api.llama.fi/protocol/curve-dex), [Ethena](https://api.llama.fi/protocol/ethena), [ether.fi](https://api.llama.fi/protocol/ether.fi), [Hyperliquid](https://api.llama.fi/protocol/hyperliquid), [Jito](https://api.llama.fi/protocol/jito), [Jupiter](https://api.llama.fi/protocol/jupiter); fees [Hyperliquid](https://api.llama.fi/summary/fees/hyperliquid-perps?dataType=dailyFees), [Jupiter Ultra](https://api.llama.fi/summary/fees/jupiter-aggregator?dataType=dailyFees), [ether.fi](https://api.llama.fi/summary/fees/ether.fi?dataType=dailyFees), [Ethena](https://api.llama.fi/summary/fees/ethena?dataType=dailyFees). Fuentes dinámicas sin fecha editorial. La metodología de Hyperliquid incluye desde 27 agosto una parte de rendimientos de reserva AQA v 2; no se rotula todo como trading puro. La llamada de fees Curve respondió HTTP 400: faltante menor para este piloto, suplido conceptualmente por documentación de distribución de fees; no se fabricó cero ni se obtuvo una valoración por múltiplos.

## 6. Dossier interpretado, activo por activo

Todas las fuentes primarias de esta sección se consultaron el **26-10-2026 UTC**. «s/f» significa que la página no muestra una fecha editorial verificable; no se inventa. Afirmación del emisor ≠ verificación independiente de solvencia o ingresos. Los números técnicos de cada párrafo proceden del snapshot Kraken de la sección 2. Hipótesis y conclusiones siguientes son juicio de Codex, no declaraciones del proyecto.

### 1. BNB

**Observaciones fundamentales y límite de la fuente.** La 37.ª quema oficial, publicada 19-10-2026, informa 1,646,196.44 BNB retirados y 131,512,085 BNB restantes al momento de esa publicación. Auto-Burn busca reducir la oferta hacia 100 M; no es un dividendo sobre utilidades del exchange. [Anuncio BNB Chain](https://www.bnbchain.org/en/blog/37th-bnb-burn). El agregado de mercado posterior da una oferta ligeramente distinta; no se fuerza igualdad entre momentos. Hay utilidad de gas y una política de quema, pero el precio continúa expuesto a uso de la red, gobernanza y concentración del ecosistema. La quema no demuestra demanda incremental ni rentabilidad del próximo trade.

**Observaciones de mercado.** Cierre 1 h 742.33 USD; RSI diario 48.2, ADX 23.2; retorno 30 d-5.06%,90 d 30.39%. Soporte 4 h 717.21; EMA 20 d 740.555826394876, EMA 50 d 733.480221734532. Son datos, no un pronóstico.

**Hipótesis, contraevidencia y decisión.** El día conserva medias favorables pero el impulso inmediato no justifica perseguir precio. La vuelta de soporte hacia banda superior produce RR neto 1.749, inferior al mínimo 2. Se descarta esta configuración; esperar una estructura nueva, no bajar el stop o alejar el target para fabricar el ratio. Mantener cash es preferible a convertir la quema en señal de compra.

### 2. BONK

**Observaciones fundamentales y límite de la fuente.** El documento del proyecto caracteriza un token comunitario de Solana y excluye derechos societarios/dividendos/reparto de beneficios en sus términos. [BONK Paper](https://bonkcoin.com/BONK-Paper.pdf), s/f verificable para la versión descargada. No se utilizó su distribución inicial como mapa actual de grandes holders. La hipótesis económica es atención/liquidez del ecosistema; no se dispone de flujos auditados que permitan un DCF. Concentración real de tenedores y calidad del volumen son faltantes materiales aceptables solo con tamaño pequeño y horizonte acotado.

**Observaciones de mercado.** Cierre 1 h 0.000002998 USD; RSI diario 42.7, ADX 18.3; retorno 30 d-19.90%,90 d 1.59%. Soporte 4 h 0.000002924; EMA 20 d 0.000003179933, EMA 50 d 0.000003229974. Son datos, no un pronóstico.

**Hipótesis, contraevidencia y decisión.** Las tres escalas muestran debilidad de tendencia; se estudia un rebote de rango, no acumulación estructural. Es alternativa especulativa: el tope observado de participación reduce el notional ilustrativo a unos 48 USD, aun cuando el presupuesto de riesgo permitiría más. El objetivo queda por encima de EMA 20/50 d; esas barreras pueden frustrar el recorrido. El pequeño OOS positivo R no eleva prioridad.

### 3. BTC

**Observaciones fundamentales y límite de la fuente.** Bitcoin tiene emisión limitada por sus reglas de consenso y seguridad PoW; poseer BTC no equivale a tener un flujo de caja empresarial. [FAQ Bitcoin](https://bitcoin.org/en/faq), s/f. La utilidad monetaria y amplitud del mercado respaldan su elección como vehículo líquido; no fijan valor justo ni fecha del rebote. El riesgo de custodia y de precio sigue existiendo pese a la escasez programada. No se añadió una narrativa de ETF, reservas estatales o flujos institucionales que no hubiera sido comprobada.

**Observaciones de mercado.** Cierre 1 h 80281.8 USD; RSI diario 41.6, ADX 17.6; retorno 30 d-4.81%,90 d 25.67%. Soporte 4 h 79120.8; EMA 20 d 82042.9586152327, EMA 50 d 80763.22191520766. Son datos, no un pronóstico.

**Hipótesis, contraevidencia y decisión.** Es primera opción de esta tanda por libro y geometría, con corrección de corto plazo sobre una estructura diaria relativamente más resistente que varias altcoins. El target de banda superior exige recuperar antes EMA 50 d≈80763 y EMA 20 d≈82043; no es ganancia asegurada. La referencia T pierde en holdout y el diagnóstico nuevo pierde un stop. Se acepta esa contraevidencia para un piloto muy pequeño, condicionado al rechazo del soporte y al evento.

### 4. CRV

**Observaciones fundamentales y límite de la fuente.** Curve genera fees por intercambios e intereses de crvUSD; su distribución está vinculada a veCRV y mecanismos específicos. Los contratos llamados «burner» convierten activos para distribuirlos, lo que no significa que todo CRV sea quemado. [Documentación fees Curve](https://knowledge.curve.finance/developer/fees/overview), s/f. Comprar CRV spot no otorga automáticamente el rendimiento de una posición bloqueada veCRV. Existen riesgos de contratos, incentivos, competencia y emisiones; TVL por sí sola no valora el token.

**Observaciones de mercado.** Cierre 1 h 0.35316 USD; RSI diario 45.7, ADX 10.9; retorno 30 d-3.24%,90 d 65.59%. Soporte 4 h 0.33646; EMA 20 d 0.359903544741, EMA 50 d 0.348333206518. Son datos, no un pronóstico.

**Hipótesis, contraevidencia y decisión.** La recuperación 4 h y la posición relativa de medias diarias hacen defendible explorar un rebote de soporte. Es secundaria: EMA 50 d≈0.3483 y EMA 20 d≈0.3599 son barreras antes del objetivo 0.39332, el spread inicial/contraste y profundidad cambian, y el tamaño debe usar la menor capacidad observada hasta refrescarla. Dos trades T en holdout fueron negativos; no ocultarlos detrás del mejor resultado R histórico.

### 5. DOGE

**Observaciones fundamentales y límite de la fuente.** La documentación oficial describe una emisión anual aproximadamente constante de 5,000 M de monedas, sin un tope absoluto; la inflación porcentual disminuye con la base de oferta. [Dogecoin inflation](https://dogecoin.com/dogepedia/faq/dogecoin-inflation/), s/f. La actividad comunitaria y transferencias pueden sostener interés; no son flujo contractual para el holder. No se atribuye adopción por compañías o celebridades sin fuente primaria actual. El riesgo principal del piloto es que el interés especulativo y la correlación con BTC no permitan recuperar medias.

**Observaciones de mercado.** Cierre 1 h 0.0771473 USD; RSI diario 33.5, ADX 26.6; retorno 30 d-22.40%,90 d 9.22%. Soporte 4 h 0.074668; EMA 20 d 0.082242544536, EMA 50 d 0.084554618204. Son datos, no un pronóstico.

**Hipótesis, contraevidencia y decisión.** Candidato principal por ejecución, con prioridad inferior a BTC/ETH/HYPE por su debilidad diaria y tesis más especulativa. La estrategia es retorno parcial a EMA 50 d, con EMA 20 d≈0.08224 intermedia, no continuación alcista confirmada. El diagnóstico de reglas específicas registra dos stops y−0.09997% sobre equity hipotético. No se cambia la regla para borrar esas pérdidas; una entrada futura necesita un rechazo nuevo y costos vigentes.

### 6. DOT

**Observaciones fundamentales y límite de la fuente.** La política monetaria cambió: la wiki oficial informa referéndum 1710 implementado enenero 2026, techo 2,100 M y reducciones escalonadas de emisión vinculadas a la brecha al techo, con primera fecha 14-03-2026. [DOT, Polkadot Wiki](https://wiki.polkadot.com/learn/learn-dot/), s/f de la edición consultada. La descripción antigua de inflación ilimitada no se aplica como si siguiera intacta. Staking/coretime añaden utilidad potencial; el piloto spot no cobra recompensas por staking. Menor emisión no sustituye demanda de uso.

**Observaciones de mercado.** Cierre 1 h 1.0234 USD; RSI diario 37.7, ADX 16.6; retorno 30 d-15.27%,90 d 35.51%. Soporte 4 h 1.0015; EMA 20 d 1.126953084421, EMA 50 d 1.103003206525. Son datos, no un pronóstico.

**Hipótesis, contraevidencia y decisión.** Precio y medias indican corrección. El stop R 1.0047 queda por encima del soporte 4 h 1.0015: entrar en un retest podría implicar ruptura del supuesto antes de alcanzar el soporte. Se descarta la geometría aunque el cociente nominal sea grande y R holdout pequeño positivo. El stop de un nuevo diseño deberá quedar bajo una estructura válida y requerirá otra revisión, sin ajustar retrospectivamente este estudio.

### 7. ENA

**Observaciones fundamentales y límite de la fuente.** ENA es gobernanza de Ethena, con decisiones sobre estrategias, riesgos y distribución sujeta a mecanismos del protocolo; no constituye un cupón automático por comprar spot. [ENA oficial](https://docs.ethena.fi/overview/ena.md), s/f. La descripción actual del respaldo USDe incluye estrategias y contrapartes más amplias que una cobertura perpetua única. [Riesgos Ethena](https://docs.ethena.fi/protocol-overview/risks), s/f: financiación, custodia, exchange y respaldo siguen siendo relevantes. ENA no e s USDe ni s USDe; sus riesgos y retornos no son intercambiables. No se verificó un calendario exacto de emisiones futuras.

**Observaciones de mercado.** Cierre 1 h 0.2055 USD; RSI diario 50.3, ADX 20.0; retorno 30 d-22.87%,90 d 151.77%. Soporte 4 h 0.1838; EMA 20 d 0.205662299128, EMA 50 d 0.196452459817. Son datos, no un pronóstico.

**Hipótesis, contraevidencia y decisión.** Secundaria por volatilidad/beta, contraparte económica indirecta y fecha de desbloqueos no verificada. El rebote previo 7 d no elimina la caída 30 d. La banda superior 0.2362 queda más allá de varias medias y la resistencia 4 h; se opera una hipótesis de rango de 7 d, no carry estable. El diagnóstico específico tiene una ganancia pequeña y el agregado 24 h de fees es anómalo: ninguno permite afirmar una ventaja o colapso del negocio.

### 8. ETC

**Observaciones fundamentales y límite de la fuente.** La política ECIP 1017 contempla reducciones de 20% del premio cada 5 M de bloques y límite aproximado 210.7 M. [Ethereum Classic, sound money](https://ethereumclassic.com/why-classic/sound-money), s/f de la página; política histórica desde 2017. La escasez y continuidad PoW no garantizan uso ni seguridad económica frente a otras redes. No se calculó una tasa de hash actual ni se certificó ausencia de riesgo de reorganización. ETC no es una participación en Ethereum ni comparte automáticamente su demanda.

**Observaciones de mercado.** Cierre 1 h 7.518 USD; RSI diario 35.9, ADX 33.1; retorno 30 d-21.14%,90 d 10.21%. Soporte 4 h 7.391; EMA 20 d 8.002822651006, EMA 50 d 8.071228154458. Son datos, no un pronóstico.

**Hipótesis, contraevidencia y decisión.** Se descarta por ejecución, aun con RR teórico 2.727. El primer libro permite solo≈3.018 USD al 1%, inferior al mínimo 0.6 ETC; el segundo mejora profundidad pero spread≈21.15 bps supera 20. La debilidad técnica añade cautela, pero la razón decisiva es operativa y cuantificada. Reconsideración exige dos verificaciones actuales con spread y mínimo válidos; no fragmentar órdenes para eludir el límite.

### 9. ETH

**Observaciones fundamentales y límite de la fuente.** Tras PoS, emisión y quema de la comisión base determinan la oferta neta: no existe deflación garantizada en toda ventana. [Emisión tras The Merge](https://ethereum.org/roadmap/merge/issuance/), s/f de actualización. Sus ejemplos históricos de ETH por día no se presentan como producción actual. Uso como gas/collateral y amplitud del ecosistema aportan una tesis de demanda, con competencia, fees variables y riesgos de contratos. Comprar ETH spot no equivale a hacer staking ni incorpora ese rendimiento en el trade.

**Observaciones de mercado.** Cierre 1 h 2330.47 USD; RSI diario 34.1, ADX 28.5; retorno 30 d-13.56%,90 d 23.02%. Soporte 4 h 2279.8; EMA 20 d 2450.633444353915, EMA 50 d 2462.660549266299. Son datos, no un pronóstico.

**Hipótesis, contraevidencia y decisión.** Segunda opción por libro profundo. Está cerca de EMA 200 d≈2317.32 y por debajo de EMA 20/50 d; se propone retorno parcial a EMA 50, no la confirmación de tendencia que aún falta en 4 h. Target 2462.66 enfrenta EMA 20 d≈2450.63 antes de llegar. RR 2.233 base baja a 1.338 con doble costo, por lo que un empeoramiento de ejecución hace fallar el plan sin mover stop/target. Holdout T fue negativo; el diagnóstico nuevo no llenó.

### 10. ETHFI

**Observaciones fundamentales y límite de la fuente.** El programa oficial describe recompras con fees de retirada semanales y parte de ingresos mensuales, con distribución a sETHFI. No todo token recomprado se quema ni recibe ese flujo un holder spot automáticamente. [ether.fi buyback program](https://etherfi.gitbook.io/gov/ethfi-buyback-program), s/f. ETHFI no es ETH ni el token líquido de stakinge ETH. El programa depende de actividad, gobernanza y ejecución; los fees agregados y TVL no acreditan beneficios auditados para el tenedor sin bloquear.

**Observaciones de mercado.** Cierre 1 h 0.6323 USD; RSI diario 40.8, ADX 15.5; retorno 30 d-13.80%,90 d 52.00%. Soporte 4 h 0.5979; EMA 20 d 0.672300082213, EMA 50 d 0.657492373703. Son datos, no un pronóstico.

**Hipótesis, contraevidencia y decisión.** Alternativa de capacidad muy baja: el tope conservador ronda 20.86 USD y hay 1.39% de horas sin volumen en esta muestra. RR nominal 11.18 surge de stop cercano/target remoto, no de un alto valor esperado. EMA 50 d≈0.65749 y EMA 20 d≈0.6723 son obstáculos antes de 0.7574. No debe desplazar a BTC/ETH por su ratio ni por un único trade T positivo en holdout. Exige aceptar explícitamente esa incertidumbre y el tamaño minúsculo.

### 11. FARTCOIN

**Observaciones fundamentales y límite de la fuente.** Se verificó el token de Solana y su disponibilidad pública Kraken, evitando activos de nombre similar. [Redes y activos Kraken](https://support.kraken.com/articles/360000678446-cryptocurrencies-available-on-kraken), registro dinámico. No se encontró en las fuentes primarias verificadas un derecho contractual a ingresos ni estados financieros auditados que fundamentaran valorar este token como una empresa. Eso registra una limitación de evidencia; no demuestra que ninguna utilidad pueda existir. La hipótesis sería atención/flujo de mercado, con riesgo reflexivo y de concentración.

**Observaciones de mercado.** Cierre 1 h 0.1258 USD; RSI diario 31.3, ADX 22.7; retorno 30 d-36.83%,90 d 1.97%. Soporte 4 h 0.1193; EMA 20 d 0.149677706122, EMA 50 d 0.157932953444. Son datos, no un pronóstico.

**Hipótesis, contraevidencia y decisión.** Se descarta esta configuración por spread del segundo libro≈31.77 bps, pese al ratio numérico elevado. La estructura de medias es débil y la banda superior está lejos, atravesando varias resistencias. El diagnóstico histórico es negativo y no incluye libros: no se usa para justificar que hoy podría ejecutarse. Reconsiderar únicamente con spread real<=20 y una tesis/tamaño explícitos, sin presuponer liquidez por el volumen global.

### 12. FIL

**Observaciones fundamentales y límite de la fuente.** Filecoin coordina almacenamiento y pruebas; los proveedores usan FIL como collateral y pueden sufrir penalizaciones por fallos, mientras los clientes pagan por servicios. [Documentación Filecoin](https://docs.filecoin.io/getting-started/what-is-filecoin), s/f. Capacidad almacenada, capacidad ofertada y demanda orgánica pagadora son magnitudes distintas. Un holder spot no recibe automáticamente el margen económico del proveedor. No se estimaron aquí crecimiento de clientes pagadores ni ingresos netos con una serie primaria suficiente.

**Observaciones de mercado.** Cierre 1 h 0.917 USD; RSI diario 39.7, ADX 19.8; retorno 30 d-12.40%,90 d 32.28%. Soporte 4 h 0.897; EMA 20 d 1.030850978998, EMA 50 d 0.991244182533. Son datos, no un pronóstico.

**Hipótesis, contraevidencia y decisión.** El precio está por debajo de EMA 20/50/200 d aunque el clasificador de medias conserve otra etiqueta. El stop R 0.900 está por encima de soporte 0.897, incoherente con comprar el retest de ese soporte. Se descarta sin modificar parámetros. La brecha FDV/capitalización advierte diferencias de oferta reportada, pero no permite fechar ventas futuras. La alternativa es esperar una nueva base, no comprar por una narrativa de almacenamiento.

### 13. FLOKI

**Observaciones fundamentales y límite de la fuente.** El whitepaper presenta un conjunto de aplicaciones, entre ellas juego, herramientas DeFi, bot, educación y marketplace. [Floki whitepaper](https://docs.floki.com/floki-whitepaper), s/f de edición consultada. Esa cartera de productos no verifica por sí sola usuarios orgánicos, beneficios netos ni un derecho económico de FLOKI sobre todos los productos asociados. TokenFi no se confunde con FLOKI. Las representaciones Ethereum/BSC se reconocen sin sumar dos veces la misma exposición; no se realiza una auditoría del bridge.

**Observaciones de mercado.** Cierre 1 h 0.00002278 USD; RSI diario 36.5, ADX 28.8; retorno 30 d-21.12%,90 d 10.37%. Soporte 4 h 0.00002252; EMA 20 d 0.00002474479, EMA 50 d 0.000025332786. Son datos, no un pronóstico.

**Hipótesis, contraevidencia y decisión.** Se mantiene únicamente como alternativa especulativa M. Las tres escalas muestran debilidad; se busca rechazo y recuperación hacia EMA 50 d. La profundidad impone notional≈31.16 USD y 4.58% de horas sin volumen limita la lectura de indicadores. La pequeña ganancia R holdout es una única operación y pertenece a otra regla. Ni volumen global ni el nombre del ecosistema justifican subir tamaño.

### 14. GRASS

**Observaciones fundamentales y límite de la fuente.** La tokenómica oficial asigna 300 M a comunidad,228 M a fundación,252 M a inversores tempranos y 220 M a contribuidores, con cliffs/vesting para las categorías correspondientes. [Grass tokenomics](https://grass-foundation.gitbook.io/grass-docs/introduction/grass-tokenomics.md), s/f. El uso declarado de datos/ancho de banda para IA no establece por sí mismo ingresos auditados o reparto al holder. El calendario gráfico de la fuente no permitió confirmar un monto exacto del próximo desbloqueo; calendarios secundarios consultados discrepan. No se publica un número como si fuera un evento confirmado.

**Observaciones de mercado.** Cierre 1 h 0.7165 USD; RSI diario 58.0, ADX 31.0; retorno 30 d 38.24%,90 d 112.09%. Soporte 4 h 0.6078; EMA 20 d 0.650875892476, EMA 50 d 0.576186237635. Son datos, no un pronóstico.

**Hipótesis, contraevidencia y decisión.** Presenta fuerza relativa y tendencia intradía más favorable, pero el plan M resulta inválido: target EMA 50 d 0.5761 queda por debajo de entrada 0.6141 y stop 0.5797. Además, ambos libros superan 20 bps de spread. Se descarta, sin inventar una estrategia de momentum a posteriori para salvarlo. Esperar aclaración del calendario y una geometría nueva; no basta con que el precio esté subiendo.

### 15. HBAR

**Observaciones fundamentales y límite de la fuente.** HBAR se utiliza para servicios de Hedera, cuya arquitectura y gobernanza se describen por la organización; los anuncios empresariales no prueban por sí solos demanda pagadora recurrente. [Cómo funciona Hedera](https://hedera.com/learning/how-hedera-works/), s/f. La documentación de tesorería describe 50,000 M de oferta preemitida y su distribución; no se usa una proyección antigua como circulante actual. [Hedera treasury report](https://hedera.com/blog/introducing-the-hedera-treasury-management-report/), documento histórico, no calendario vigente certificado.

**Observaciones de mercado.** Cierre 1 h 0.07735 USD; RSI diario 35.7, ADX 21.6; retorno 30 d-19.04%,90 d 13.70%. Soporte 4 h 0.07484; EMA 20 d 0.084971996754, EMA 50 d 0.085773902719. Son datos, no un pronóstico.

**Hipótesis, contraevidencia y decisión.** Secundario. El objetivo de banda superior exige remontar EMA 20/50/200 d≈0.085–0.088 desde una estructura debilitada, por lo que el ratio 14.39 no lo convierte en la mejor opción. El stop está cerca del soporte y de las oscilaciones intradía; el beneficio remoto podría no alcanzarse en 7 d. La liquidez permite solo≈119 USD en el ejemplo y reduce el riesgo efectivo respecto al máximo. No se presupone yield de staking en la tesis.

### 16. HYPE

**Observaciones fundamentales y límite de la fuente.** La documentación describe distribución de fees entre comunidad, HLP, fondo de asistencia y deployers; el fondo convierte ingresos en HYPE y el texto consultado describe la quema de esos HYPE. [Hyperliquid fees](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees), s/f. No todo fee bruto es caja distribuida al holder. Actividad de su exchange y utilidad de la red aportan vínculo económico, pero existen riesgo de plataforma/gobernanza y una gran diferencia entre circulante/total reportados. No se predice una fecha o magnitud exacta de unlock sin confirmación.

**Observaciones de mercado.** Cierre 1 h 77.22 USD; RSI diario 35.9, ADX 27.2; retorno 30 d-17.47%,90 d 36.07%. Soporte 4 h 74.33; EMA 20 d 80.93460594212, EMA 50 d 81.764151453465. Son datos, no un pronóstico.

**Hipótesis, contraevidencia y decisión.** Tercer candidato, con libro suficiente para piloto y target EMA 50 d 81.76, por encima de EMA 20 d 80.93 que actúa como barrera. Solo 271 diarias Kraken: después del warmup quedan 71; no existe un holdout 120 con desarrollo suficiente bajo el protocolo. Su T histórico positivo es descriptivo, no OOS. La prioridad se mantiene por ejecución/tesis, con esa carencia material expresamente aceptable solo a riesgo pequeño y sin ampliar horizonte.

### 17. ICP

**Observaciones fundamentales y límite de la fuente.** La economía de Internet Computer combina emisión de recompensas a nodos/votantes y quema de ICP convertido a ciclos de cómputo y otras fees. [Economía de red ICP](https://docs.internetcomputer.org/concepts/network-economics/), s/f. No implica oferta neta siempre decreciente ni ingresos automáticos de staking en una posición spot. La hipótesis de demanda depende de uso real de cómputo; no se verificó aquí una serie de ingresos de clientes que permita descontar caja para el token.

**Observaciones de mercado.** Cierre 1 h 2.607 USD; RSI diario 36.4, ADX 20.1; retorno 30 d-17.76%,90 d 25.06%. Soporte 4 h 2.556; EMA 20 d 2.921336061834, EMA 50 d 2.904849799074. Son datos, no un pronóstico.

**Hipótesis, contraevidencia y decisión.** La corrección deja el precio por debajo de las medias diarias, y el stop R 2.558 supera soporte 4 h 2.556. La geometría falla y se descarta aunque el ratio computado sea 22.16. Dos stops del diagnóstico y T negativo en holdout son contraevidencia, pero no la razón única del descarte. Una estructura distinta tendría que definirse y revisarse de nuevo, sin reinterpretar el stop actual como válido.

### 18. INJ

**Observaciones fundamentales y límite de la fuente.** El sitio oficial presenta INJ como token nativo de utilidad/gobernanza, con mecanismos de recompras/quemas y afirma oferta plenamente circulante sin futuros vestings internos. [INJ oficial](https://injective.com/inj), s/f. Ausencia de unlock interno no significa ausencia de toda emisión de protocolo futura ni deflación neta garantizada. Los contadores dinámicos de la web no se tomaron como cifras auditadas. Uso del exchange/red y gobernanza son mecanismos plausibles de demanda, con competencia y actividad cíclica.

**Observaciones de mercado.** Cierre 1 h 7.769 USD; RSI diario 50.2, ADX 22.4; retorno 30 d-3.85%,90 d 66.71%. Soporte 4 h 7.415; EMA 20 d 7.983968986424, EMA 50 d 7.343343864286. Son datos, no un pronóstico.

**Hipótesis, contraevidencia y decisión.** Es la alternativa secundaria mejor posicionada por estructura diaria y libro, pero su objetivo R 9.181 exige romper EMA 20 d≈7.984 y resistencias antes de completarse. RR 7.768 no estima la probabilidad de ese recorrido. Los cinco intentos del diagnóstico no llenaron por geometría/gap, y T holdout pierde; no se sustituye el target para exhibir un backtest mejor. Si ninguna opción principal activa señal, puede proponerse piloto INJ con revisión explícita de esas barreras.

### 19. JTO

**Observaciones fundamentales y límite de la fuente.** JTO gobierna decisiones del ecosistema Jito; la documentación describe oferta 1,000 M y vesting para categorías de equipo/inversores. [Jito governance token](https://www.jito.network/docs/governance/the-jito-governance-token-jto/), s/f de edición. JitoSOL, el token líquido de staking, es un producto distinto: su rendimiento no se adjudica a JTO spot. Las métricas de adopción históricas citadas en páginas de lanzamiento no se presentaron como cifras actuales. TVL y actividad MEV no son dividendos contractuales a JTO.

**Observaciones de mercado.** Cierre 1 h 0.42624 USD; RSI diario 37.9, ADX 10.1; retorno 30 d-26.42%,90 d-25.20%. Soporte 4 h 0.41208; EMA 20 d 0.476608407625, EMA 50 d 0.496863775725. Son datos, no un pronóstico.

**Hipótesis, contraevidencia y decisión.** Se descarta el plan R: stop 0.41221 por encima del soporte 0.41208, target 0.57408 muy alejado y capacidad conservadora≈7.44 USD. No confundir el ratio grande con una oportunidad: la tesis de retest falla antes de discutir probabilidad. La debilidad diaria y oferta futura son contraevidencia adicional. Aguardar base nueva y libro vigente, sin replicar trades de JitoSOL como si fueran JTO.

### 20. JUP

**Observaciones fundamentales y límite de la fuente.** Una propuesta oficial del foro, publicada 13-02-2026 por Kash, discute emisiones netas cero, aplazar asignaciones y financiar recompras. [Propuesta Net Zero Emissions](https://discuss.jup.ag/t/proposal-net-zero-emissions/39948). Se registra como **propuesta**, no se declara ejecutada sin voto/implementación comprobados. Los datos de fees Ultra cubren un producto, no todos los ingresos Jupiter. JUP de Solana no equivale a una participación garantizada en el beneficio agregado del exchange/agregador.

**Observaciones de mercado.** Cierre 1 h 0.28133 USD; RSI diario 40.9, ADX 21.1; retorno 30 d-17.82%,90 d 54.70%. Soporte 4 h 0.2735; EMA 20 d 0.310062873697, EMA 50 d 0.295823187945. Son datos, no un pronóstico.

**Hipótesis, contraevidencia y decisión.** La configuración R se descarta: stop 0.27372 queda por encima del soporte 4 h 0.2735. El target 0.37659 cruza EMA 50 d≈0.2958 y EMA 20 d≈0.3101; un único T holdout positivo no corrige la geometría ni valida esa nueva regla. El diagnóstico específico registra un stop. Esperar estructura coherente y claridad de emisión si se replantea; no usar titulares de «cero emisiones» como certeza de oferta futura.

## 7. Referencias estadísticas congeladas: T y R

Se reutilizaron dos familias de referencia sin optimizarlas para estos activos. **T:** EMA 50 d>EMA 200 d, cierre>EMA 200 d y ruptura del máximo de las 20 velas previas, excluida la actual. Entrada al open siguiente; no entrar si el gap frente al cierre supera ATR 14. Stop=min(mínimo 10 d incluido día de señal, entrada−2 ATR); target=entrada+3 R. Salida por stop/target, cierre bajo EMA 50 confirmado al open siguiente o 20 días.

**R:** RSI 14<30 y cierre bajo banda Bollinger inferior 20/2; entrada al open siguiente con el mismo filtro de gap; stop=entrada−2 ATR; target=entrada+2.5 R. Salir por stop/target, recuperación de SMA 20 al open siguiente o 10 días. Esa salida anticipada puede impedir alcanzar el target nominal: no se confunde con los nuevos pilotos M/R de la sección 10.

En ambas referencias: costo 40 bpsfee+15 bpsslippage por lado; simulador compone ambos factores, ligeramente distinto de la suma conservada por el motor de riesgo. RR neto nominal mínimo 2, riesgo 0.25% por operación y exposición máxima 20%, capital hipotético sin saldo de cuenta. Stops primero ante doble toque, gap adverso al open, no reentrada en la barra de salida, liquidación forzada al final de ventana y contabilidad de Pn L contrastada. No hay profundidad histórica ni cola de órdenes. Son referencias, no simulación exacta de la cuenta ni de los pilotos 0.05%.

Warmup 200 diarias. Para 19 activos: desarrollo hasta antes de las últimas 120, holdout cronológico 28-06 a 25-10-2026; cada segmento comienza plano. El tramo continuo elegible atraviesa el corte sin reiniciarse y no es la suma de los segmentos. En HYPE solo 71 barras elegibles: no se reduce el warmup ni se inventa desarrollo/OOS. Su muestra completa es descriptiva. El holdout se inspeccionó durante la selección secuencial; **no se proclama validación independiente**.

Las tablas muestran todas las 40 referencias de esta tanda, no solo las ganadoras. DD=drawdown de equity simulado. «Sin partición» significa no disponible, no cero. T y R están inactivos al corte en los 20 activos.

| Activo /familia | N desarrollo | Ret desarrollo | N holdout | Ret holdout | DD holdout | Ret continuo elegible | N continuo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BNB/T | 1 | 0.6336% | 1 | -0.1316% | -0.1651% | 0.5011% | 2 |
| BNB/R | 5 | -0.3848% | 0 | 0.0000% | 0.0000% | -0.3848% | 5 |
| BONK/T | 2 | -0.2517% | 0 | 0.0000% | 0.0000% | -0.2517% | 2 |
| BONK/R | 5 | 0.1505% | 2 | 0.0700% | -0.1545% | 0.2206% | 7 |
| BTC/T | 4 | -0.4851% | 1 | -0.0766% | -0.1070% | -0.5614% | 5 |
| BTC/R | 6 | -0.3288% | 0 | 0.0000% | 0.0000% | -0.3288% | 6 |
| CRV/T | 1 | 0.2206% | 2 | -0.3479% | -0.3963% | -0.1281% | 3 |
| CRV/R | 4 | 0.1031% | 0 | 0.0000% | 0.0000% | 0.1031% | 4 |
| DOGE/T | 1 | -0.1525% | 0 | 0.0000% | 0.0000% | -0.1525% | 1 |
| DOGE/R | 6 | -0.2190% | 0 | 0.0000% | 0.0000% | -0.3152% | 6 |
| DOT/T | 0 | 0.0000% | 0 | 0.0000% | 0.0000% | 0.0000% | 0 |
| DOT/R | 9 | -0.0978% | 1 | 0.0563% | -0.0747% | 0.0420% | 9 |
| ENA/T | 2 | -0.2826% | 1 | 0.0295% | -0.2306% | -0.2532% | 3 |
| ENA/R | 4 | 0.1893% | 0 | 0.0000% | 0.0000% | 0.1893% | 4 |
| ETC/T | 1 | -0.2112% | 0 | 0.0000% | 0.0000% | -0.2112% | 1 |
| ETC/R | 5 | -0.1924% | 0 | 0.0000% | 0.0000% | -0.1924% | 5 |
| ETH/T | 3 | 0.4924% | 1 | -0.1853% | -0.1853% | 0.3062% | 4 |
| ETH/R | 5 | -0.2985% | 0 | 0.0000% | 0.0000% | -0.2985% | 5 |
| ETHFI/T | 2 | -0.1727% | 1 | 0.1884% | -0.2182% | 0.0154% | 3 |
| ETHFI/R | 1 | 0.1750% | 0 | 0.0000% | 0.0000% | 0.1750% | 1 |
| FARTCOIN/T | 0 | 0.0000% | 0 | 0.0000% | 0.0000% | 0.0000% | 0 |
| FARTCOIN/R | 4 | -0.0612% | 0 | 0.0000% | 0.0000% | -0.0612% | 4 |
| FIL/T | 0 | 0.0000% | 0 | 0.0000% | 0.0000% | 0.0000% | 0 |
| FIL/R | 3 | -0.0878% | 0 | 0.0000% | 0.0000% | -0.0878% | 3 |
| FLOKI/T | 0 | 0.0000% | 0 | 0.0000% | 0.0000% | 0.0000% | 0 |
| FLOKI/R | 3 | 0.2125% | 1 | 0.1686% | -0.0526% | 0.3972% | 3 |
| GRASS/T | 0 | 0.0000% | 2 | -0.3179% | -0.3340% | -0.3179% | 2 |
| GRASS/R | 1 | 0.1531% | 0 | 0.0000% | 0.0000% | 0.1531% | 1 |
| HBAR/T | 0 | 0.0000% | 0 | 0.0000% | 0.0000% | 0.0000% | 0 |
| HBAR/R | 2 | 0.0624% | 0 | 0.0000% | 0.0000% | 0.2238% | 3 |
| HYPE/T | sin partición | n/d | sin partición | n/d | n/d | 0.5436% | 3 |
| HYPE/R | sin partición | n/d | sin partición | n/d | n/d | 0.0000% | 0 |
| ICP/T | 0 | 0.0000% | 1 | -0.1874% | -0.2335% | -0.1874% | 1 |
| ICP/R | 3 | 0.2436% | 0 | 0.0000% | 0.0000% | 0.2436% | 3 |
| INJ/T | 0 | 0.0000% | 1 | -0.0947% | -0.1240% | -0.0947% | 1 |
| INJ/R | 5 | 0.0282% | 0 | 0.0000% | 0.0000% | 0.0282% | 5 |
| JTO/T | 0 | 0.0000% | 0 | 0.0000% | 0.0000% | 0.0000% | 0 |
| JTO/R | 3 | 0.0479% | 0 | 0.0000% | 0.0000% | 0.0479% | 3 |
| JUP/T | 0 | 0.0000% | 1 | 0.1445% | -0.1508% | 0.1445% | 1 |
| JUP/R | 3 | -0.1264% | 0 | 0.0000% | 0.0000% | -0.1264% | 3 |

Seis combinaciones tienenholdout positivo: BONK-R, DOT-R, ENA-T, ETHFI-T, FLOKI-R, JUP-T. Sus muestras son de una o dos operaciones; no se afirma que ningún backtest pueda ganar, ni que ganar una ventana pruebe una ventaja. En HYPE, T continuo gana≈0.5436% con 3 operaciones; no tiene partición OOS válida. Periodos sin operaciones y bootstrap degenerado en cero describen inactividad, no robustez.

Para los holdouts con actividad se repitió costo 80/30 bps por lado y bootstrap por bloques 10 días,2000 réplicas, semilla 42. Intervalo 5–95% del retorno de la serie resampleada, no intervalo de una probabilidad de ganancia ni corrección por selección múltiple. Con 1–2 trades puede ser especialmente poco informativo.

| Activo /familia con actividad holdout | N base /doble costo | Ret base /doble costo | Bootstrap p 05 /p 50 /p 95 |
| --- | --- | --- | --- |
| BNB/T | 1 / 1 | -0.1316% / -0.1410% | -0.3350% / -0.1360% / 0.0143% |
| BONK/R | 2 / 2 | 0.0700% / 0.0447% | -0.1338% / 0.0690% / 0.3512% |
| BTC/T | 1 / 1 | -0.0766% / -0.0889% | -0.2081% / -0.0768% / 0.0210% |
| CRV/T | 2 / 2 | -0.3479% / -0.3558% | -0.5876% / -0.2253% / 0.0000% |
| DOT/R | 1 / 1 | 0.0563% / 0.0355% | -0.0967% / 0.0000% / 0.1071% |
| ENA/T | 1 / 1 | 0.0295% / 0.0208% | -0.2917% / 0.0333% / 0.4335% |
| ETH/T | 1 / 1 | -0.1853% / -0.1894% | -0.4316% / -0.1831% / 0.0000% |
| ETHFI/T | 1 / 1 | 0.1884% / 0.1659% | -0.0936% / 0.1847% / 0.5804% |
| FLOKI/R | 1 / 1 | 0.1686% / 0.1396% | -0.0149% / 0.0000% / 0.3623% |
| GRASS/T | 2 / 2 | -0.3179% / -0.3219% | -0.7239% / -0.2981% / -0.0168% |
| ICP/T | 1 / 1 | -0.1874% / -0.1905% | -0.4605% / -0.1790% / 0.0000% |
| INJ/T | 1 / 1 | -0.0947% / -0.0993% | -0.2288% / -0.0934% / 0.0000% |
| JUP/T | 1 / 1 | 0.1445% / 0.1312% | -0.0073% / 0.1438% / 0.3824% |

Benchmark: comprar 20% del patrimonio y mantener 80% cash sin interés, con los mismos costos inicial/final. No es la asignación recomendada ni una cartera simultánea de 20 activos; cada fila es un experimento individual. Cash sin operaciones retorna 0 en la convención, sin modelar interés, inflación o riesgo de custodia.

| Activo | Buy/hold 20% retorno holdout | DD holdout | Ret continuo elegible |
| --- | --- | --- | --- |
| BNB | 6.229% | -2.715% | -5.273% |
| BONK | -5.684% | -12.650% | -17.165% |
| BTC | 6.417% | -2.132% | -5.247% |
| CRV | 15.489% | -5.474% | -11.300% |
| DOGE | 0.430% | -6.014% | -13.249% |
| DOT | 4.967% | -6.673% | -15.535% |
| ENA | 33.239% | -14.532% | -8.949% |
| ETC | 0.840% | -5.653% | -11.975% |
| ETH | 9.282% | -5.080% | -1.787% |
| ETHFI | 15.694% | -7.634% | -9.959% |
| FARTCOIN | -0.851% | -12.681% | -17.728% |
| FIL | 5.013% | -7.595% | -13.653% |
| FLOKI | 0.804% | -6.503% | -15.530% |
| GRASS | 8.896% | -10.953% | -0.328% |
| HBAR | 1.312% | -10.916% | -5.162% |
| HYPE | n/d | n/d | 6.515% |
| ICP | 4.242% | -8.025% | -10.062% |
| INJ | 13.395% | -5.348% | -7.931% |
| JTO | -9.713% | -10.175% | -15.847% |
| JUP | 5.474% | -7.650% | -10.034% |

En 13 de los 19 holdouts el benchmark 20% buy/hold supera el techo 6% de MDD en valor absoluto; en HYPE la ventana completa descriptiva también lo supera. Es evidencia contra comprar y mantener con esa exposición sin control, no prohibición matemática de un piloto mucho menor. Los filtros de riesgo no garantizan que gaps no atraviesen un límite.

**Selección múltiple:** hay 40 nuevas familias T/R y 38 comparaciones de desarrollo/holdout disponibles; sumadas a las 20 referencias de las primeras 10 filas,60 familias revisadas en 30 activos. También existen propuestas exploratorias de las tandas anteriores y 20 configuraciones nuevas. No se ha contado cada decisión de diseño como un ensayo independiente ni se ha corregido estadísticamente una selección adaptativa compleja. Orden fijo del Excel reduce cherry-picking del universo, pero no elimina selección de estrategias o de candidatos. La conclusión es ventaja desconocida, no validación por exclusión.

## 8. Diagnóstico específico de los nuevos pilotos

El protocolo previo congeló la familia Q: retest de mínimo 20 barras 4 h, rechazo 1 h, objetivo EMA 50 d(tipo M) o Bollinger superior diaria(tipo R). **El selector preciso ADX d<=25→R; >25→M se fijó después de observar el régimen**, antes de calcular y filtrar los ratios; es una decisión exploratoria, no una regla validada por preregistro anterior a datos. No se probó cuál variante daba mayor beneficio para elegirla. En cada punto histórico se eligió el tipo usando únicamente ADX de la última diaria cerrada, sin imponer al pasado el régimen de hoy.

Se alinearon datos 1 h con 4 h y diario mediante as-of hacia atrás, disponibles desde su cierre real. Tras 200 h de warmup se evaluaron 520 barras 1 h:04-10-2026,20 UTC a 26-10-2026,11 UTC. Señal al cierre dentro de la zona, close>open, close por encima del centro high-low ylow>stop. Intento al open siguiente solo dentro de zona y con RR neto>=2; no se presume fill posterior si la apertura quedó fuera. Stops/targets fijados al entrar; R 7 d, M 5 d; gaps al open, doble toque adverso, sin reentrada misma barra.

Riesgo 0.05%, tope activo 20%, costos aditivos 55 bps por lado como el gate; contraste 110 bps. Cada activo se simula por separado con equity ilustrativo 10,000: **no son veinte pilotos simultáneos ni una simulación conjunta del presupuesto global**. Una entrada/día, pausa tras pérdida diaria 0.15% y presupuesto de pérdidas 50 unidades/20 operaciones están en este diagnóstico; la reconciliación de cuenta y supervisión global continúan siendo requisitos reales. No modela profundidad histórica, cantidad mínima/tick de cantidad ejecutada, colas ni la revisión de 5 trades/5 R. Se redondearon los niveles de precio al tick. Limitaciones de ejecución histórica se aceptan como materiales, no se presentan fills simulados como realizables.

Esta muestra de unas 22 jornadas fue vista al diseñar las hipótesis: no es OOS independiente. Se preserva el resultado adverso y se rechaza usar cero actividad como éxito. Gaps, siguiente barra, doble toque, costos, tope de riesgo, disponibilidad de intervalos superiores, prefijos sin futuro y contabilidad pasaron controles específicos.

| Activo | Señales en plano | Fills base | Ret base | DD base | Fills doble costo | Ret doble costo |
| --- | --- | --- | --- | --- | --- | --- |
| BNB | 0 | 0 | 0.00000% | 0.00000% | 0 | 0.00000% |
| BONK | 1 | 0 | 0.00000% | 0.00000% | 0 | 0.00000% |
| BTC | 2 | 1 | -0.05000% | -0.05000% | 0 | 0.00000% |
| CRV | 3 | 0 | 0.00000% | 0.00000% | 0 | 0.00000% |
| DOGE | 2 | 2 | -0.09997% | -0.13181% | 0 | 0.00000% |
| DOT | 1 | 1 | -0.05000% | -0.05000% | 1 | -0.05000% |
| ENA | 4 | 1 | 0.03231% | -0.01550% | 1 | 0.02443% |
| ETC | 2 | 0 | 0.00000% | 0.00000% | 0 | 0.00000% |
| ETH | 1 | 0 | 0.00000% | 0.00000% | 0 | 0.00000% |
| ETHFI | 5 | 0 | 0.00000% | 0.00000% | 0 | 0.00000% |
| FARTCOIN | 1 | 1 | -0.05000% | -0.06679% | 1 | -0.05000% |
| FIL | 1 | 1 | -0.05000% | -0.05000% | 1 | -0.05000% |
| FLOKI | 1 | 0 | 0.00000% | 0.00000% | 0 | 0.00000% |
| GRASS | 3 | 0 | 0.00000% | 0.00000% | 0 | 0.00000% |
| HBAR | 2 | 0 | 0.00000% | 0.00000% | 0 | 0.00000% |
| HYPE | 3 | 0 | 0.00000% | 0.00000% | 0 | 0.00000% |
| ICP | 3 | 2 | -0.09997% | -0.11007% | 2 | -0.09997% |
| INJ | 5 | 0 | 0.00000% | 0.00000% | 0 | 0.00000% |
| JTO | 0 | 0 | 0.00000% | 0.00000% | 0 | 0.00000% |
| JUP | 1 | 1 | -0.05000% | -0.05000% | 1 | -0.05000% |

BTC pierde un stop; DOGE pierde dos; ENA tiene una ganancia pequeña. Entre los descartados de hoy, DOT/FIL/ICP/JUP pudieron tener geometría válida en otros momentos y luego perder: que hoy se descarten no borra sus fills históricos. El diagnóstico no promueve ENA por ganar ni veta BTC por perder. Es contraevidencia relevante para mantener tamaño mínimo y no confundir un rebote plausible con un valor esperado estimado positivo.

## 9. Ejecución: dos libros por activo

Profundidad compradora utilizable=asks hasta 10 bps del mejor ask; participación máxima 1% de esa profundidad. Se usa el menor tope de los dos snapshots solo para dimensionar ejemplos conservadores; antes de operar se requiere libro nuevo. Un libro no es capacidad garantizada: puede cancelarse, y la salida bajo estrés puede ser peor. Los pares/mínimos provienen de [AssetPairs Kraken](https://api.kraken.com/0/public/AssetPairs), consultas 26-10-2026 UTC, registro dinámico.

Volumen 24 h USD es una aproximación Kraken deprecio típico×volumen base de las últimas 24 barras 1 h, no volumen auditado ni CoinGecko global. Horas sin volumen sobre 720 h. Las horas exactas son UTC del 26 octubre.

| Activo | Hora inicial /contraste | Spread inicial /contraste bps | Tope 1% inicial /contraste USD | Vol 24 h Kraken USD aprox. | Horas sin volumen |
| --- | --- | --- | --- | --- | --- |
| BNB | 12:28:46 / 12:33:01 | 0.135 / 0.135 | 277.49 / 389.39 | 1219980 | 0.00% |
| BONK | 12:28:55 / 12:33:02 | 6.660 / 3.335 | 53.85 / 48.12 | 362816 | 0.00% |
| BTC | 12:29:03 / 12:33:03 | 0.012 / 0.012 | 57029.91 / 79094.12 | 107191139 | 0.00% |
| CRV | 12:29:11 / 12:33:04 | 9.911 / 14.481 | 66.82 / 239.19 | 559387 | 0.00% |
| DOGE | 12:29:19 / 12:33:05 | 0.013 / 0.013 | 1139.24 / 1090.02 | 1607026 | 0.00% |
| DOT | 12:29:27 / 12:33:06 | 0.978 / 0.979 | 92.25 / 69.21 | 481952 | 0.00% |
| ENA | 12:29:35 / 12:33:08 | 4.816 / 4.865 | 459.22 / 268.18 | 4048930 | 0.00% |
| ETC | 12:29:43 / 12:33:09 | 14.522 / 21.150 | 3.02 / 13.11 | 78137 | 0.69% |
| ETH | 12:29:51 / 12:33:10 | 0.043 / 0.043 | 19292.04 / 24903.08 | 44242728 | 0.00% |
| ETHFI | 12:29:59 / 12:33:11 | 12.486 / 18.806 | 20.86 / 22.68 | 40933 | 1.39% |
| FARTCOIN | 12:30:07 / 12:33:12 | 15.873 / 31.771 | 36.04 / 370.89 | 527381 | 0.00% |
| FIL | 12:30:15 / 12:33:13 | 10.935 / 10.947 | 118.86 / 40.60 | 312153 | 0.00% |
| FLOKI | 12:30:23 / 12:33:14 | 17.475 / 17.498 | 37.27 / 31.16 | 31923 | 4.58% |
| GRASS | 12:30:31 / 12:33:15 | 24.869 / 27.663 | 100.15 / 73.39 | 877620 | 0.00% |
| HBAR | 12:30:39 / 12:33:16 | 2.569 / 1.285 | 134.20 / 119.14 | 730796 | 0.00% |
| HYPE | 12:30:47 / 12:33:18 | 1.290 / 2.581 | 1319.38 / 1454.90 | 4406773 | 0.00% |
| ICP | 12:30:55 / 12:33:19 | 7.666 / 7.660 | 33.39 / 50.45 | 473833 | 0.00% |
| INJ | 12:31:03 / 12:33:20 | 6.453 / 6.435 | 250.46 / 239.19 | 2571472 | 0.00% |
| JTO | 12:31:11 / 12:33:21 | 6.305 / 1.630 | 7.44 / 7.63 | 60710 | 0.00% |
| JUP | 12:31:19 / 12:33:22 | 17.045 / 17.412 | 69.31 / 56.55 | 326269 | 0.00% |

Fallos observados: ETC mínimo 0.6 unidades no cabe en el tope inicial y su segundo spread supera 20 bps; FARTCOIN segundo spread 31.77 bps; GRASS ambos≈24.87/27.66 bps. No se promedian spreads para convertir un fallo en PASS. ETHFI/FLOKI muestran horas sin negociación y límites de tamaño especialmente pequeños. Tampoco se usa profundidad global de otra bolsa para sustituir estos libros.

[Stop loss Kraken](https://support.kraken.com/articles/7699391647892-stop-loss-orders), actualizado 06-10-2026 y consultado 26-10-2026 UTC: al dispararse genera ejecución a mercado con fees taker y puede llenar peor que el stop. Las órdenes protectoras son independientes; tras una salida alternativa hay que cancelar la protección sobrante. La capacidad de stop de este plan no es una garantía del máximo MDL/MDD. No se añaden órdenes automáticas desde el Lab.

## 10. Plan de trading condicionado y escenarios descartados

Todos los niveles son **precios de investigación en USD**, no cotizaciones vigentes ni órdenes que se dejan esperando desde hoy hasta el 29. E representa techo de entrada, no una compra al precio actual. Soporte=min 20 velas 4 h; E=soporte+0.5 ATR 1 h. Tipo M: stop=soporte−ATR 4 h, target=EMA 50 d; tipo R: stop=mínimo 10 d−0.25 ATR 4 h, target=Bollinger superior diaria. E/stop/target se redondean hacia abajo al tick. No se mueven para hacer pasar RR.

Estos niveles se conservan como escenario congelado. Tras el evento, recoger dataset/libro actuales y recalcular la misma fórmula; si cambian niveles, hashes o tesis, generar una **nueva propuesta y dos revisiones**, no ejecutar con aprobación histórica. La transición M/R se decide al diseñar la nueva propuesta; no se cambia objetivo o stop de una posición abierta cuando cambie ADX.

### Diez reglas de activación, gestión e invalidación

1. Después de la pausa FOMC, confirmar comunicado publicado, mercado accesible y cuenta reconciliada en la misma moneda. Si falta un requisito crítico, no abrir; no ampliar búsqueda para suplirlo.
2. Seleccionar entre propuestas válidas por prioridad y disponibilidad de señal; no esperar BTC indefinidamente si otro candidato válido activa. Nunca mantener más de un piloto global simultáneo, incluidas otras tandas.
3. Con velas cerradas, exigir rechazo 1 h: low>stop, close dentro de[soporte, E], close>open y close>(high+low)/2. Si el soporte pierde el stop antes de confirmar, cancelar el escenario. El toque intrabar solo no es entrada.
4. Intento único en la siguiente barra 1 h, con límite de compra ejecutable que no exceda E y precio dentro de zona. Si abre fuera, no perseguir y no asumir fill intrabar. Si no hay fill inmediato, cancelar el remanente y esperar una nueva señal cerrada; no encadenar intentos para consumir profundidad.
5. Al precio real, recalcular RR neto>=2, tamaño y cash incluyendo costos. Spread<=20 bps y participación<=1% asks 10 bps, mínimos/ticks válidos. Confirmar también salida plausible y que una actualización de libro no cambió materialmente los supuestos. Una modificación exige renovar evidencia y revisiones.
6. Stop fijo de invalidación de precio, no stop de dinero elegido para agrandar posición; colocar protección sobre cantidad efectivamente comprada y supervisarla. Target fijo, sin parciales, promedios a la baja, trailing o añadir exposición. Fees reales mayores reducen tamaño o bloquean RR; no se reduce el costo configurado solo para pasar.
7. M: salir como máximo a 120 h; R: a 168 h desde fill, en el primer momento operativo al cumplirse. Si stop/target no llegó, el cierre temporal puede tener ganancia menor al RR nominal o pérdida. Barreras intermedias se aceptan como riesgo, no se añade una salida implícita antes del target que contradiga el RR publicado.
8. Cancelar antes de entrada si se invalida la estructura, surge un incidente verificado que destruye la tesis, falla venue o límite de riesgo. Durante una posición, un incidente crítico exige salida/supervisión extraordinaria por el operador y registro; un stop/target no resuelve indisponibilidad del exchange.
9. Máximo una entrada nueva/día UTC; registrar también intentos/fills parciales y pérdidas. Pausa del piloto si pérdida del día>=0.15%, pérdidas acumuladas>=0.50%,20 trades cerrados o 30 días desde primer fill, lo primero que ocurra. Revisar tras 5 cierres o 5 R netos de pérdida; no aumentar tamaño para recuperar.
10. Aplicar gate con hashes nuevos, datos de mercado<120 s, cuenta<300 s, revisión<3600 s y plan<3600 s, conforme a config. Desviación máxima de entrada 1%; estar hoy a más de 1% de un precio futuro de escenario no autoriza ignorar ese filtro. Un READY caducado no se ejecuta. Si el balance/política/dataset/propuesta cambia, revisar de nuevo.

### Cuatro candidatos principales

Ninguno tiene señal al corte. RR es beneficio al target dividido por pérdida al stop, ambos con costos; no esperanza matemática. Sensibilidad duplica costos sin desplazar barreras.

| Prioridad | Activo /tipo | Zona entrada USD | Stop | Target | RR neto | RR doble costo | Máximo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | BTC/R | 79120.8–79303.6 | 78936.4 | 84731 | 3.657 | 1.719 | 7 d |
| 2 | ETH/M | 2279.8–2288.08 | 2246.53 | 2462.66 | 2.233 | 1.338 | 5 d |
| 3 | HYPE/M | 74.33–74.69 | 72.93 | 81.76 | 2.414 | 1.581 | 5 d |
| 4 | DOGE/M | 0.074668–0.0749482 | 0.0734556 | 0.0845546 | 3.781 | 2.513 | 5 d |

BTC: soporte 79120.8 y stop 78936.4, estrecho frente al ruido diario; se exige rechazo 1 h en lugar de compra ciega del soporte. La extensión al target 84731 pasa por EMA 50/20 d, y el doble costo deja RR 1.719: no es robusto a cualquier ejecución. ETH: stop 2246.53 bajo base 2279.8 y buffer ATR 4 h; target 2462.66 enfrenta recuperación de medias y es sensible a costos. HYPE: stop 72.93 bajo 74.33; target 81.76 obliga a recuperar EMA 20 d; oferta y muestra corta limitan convicción. DOGE: stop 0.0734556 bajo 0.074668; target 0.0845546 implica rebote dentro de estructura bajista, con atención especulativa y dos pérdidas diagnósticas como contraevidencia.

No se exige que el estrés de costo doble mantenga RR 2 para toda hipótesis: es un escenario adverso revelado, no el costo real confirmado. BTC/ETH/HYPE lo incumplen; por ello no son candidatos a operar si los costos efectivos y tolerancia de slippage se acercan a ese escenario. El gate utiliza costos realistas verificados, nunca los mínimos convenientes.

### Siete alternativas subordinadas

Si no hay señal principal y una alternativa sí tiene todos los controles, puede someterse a revisión conjunta sin abrir un presupuesto adicional. HBAR/ETHFI y otros ratios grandes requieren especial cautela por barreras/target remoto. Son hipótesis exploratorias de 7 d salvo FLOKI 5 d; no objetivos de inversión de largo plazo.

| Activo /tipo | Zona entrada | Stop | Target | RR neto /doble costo | Tope conservador notional USD |
| --- | --- | --- | --- | --- | --- |
| INJ/R | 7.415–7.477 | 7.351 | 9.181 | 7.768 / 5.260 | 239.19 |
| CRV/R | 0.33646–0.3385 | 0.32535 | 0.39332 | 3.023 / 2.287 | 66.82 |
| ENA/R | 0.1838–0.1859 | 0.1725 | 0.2362 | 3.121 / 2.633 | 268.18 |
| HBAR/R | 0.07484–0.07516 | 0.07448 | 0.09774 | 14.390 / 8.890 | 119.14 |
| BONK/R | 0.000002924–0.00000294 | 0.00000278 | 0.000003586 | 3.187 / 2.576 | 48.12 |
| FLOKI/M | 0.00002252–0.00002259 | 0.0000221 | 0.00002533 | 3.366 / 2.254 | 31.16 |
| ETHFI/R | 0.5979–0.6005 | 0.5937 | 0.7574 | 11.178 / 7.121 | 20.86 |

Los targets R son escenarios extremos de rango reciente. Para ETHFI/HBAR no hay evidencia suficiente para estimar la probabilidad de alcanzarlos dentro de 7 d; asumir un ratio alto no compensa eso estadísticamente. Se mantienen como alternativas de baja prioridad con riesgo reducido por profundidad, no como selección por mayor RR. La falta de probabilidad calibrada se acepta como material en el piloto, no se rellena con una tasa de acierto inventada.

### Nueve configuraciones rechazadas

Se muestran sus cifras para hacer auditable el descarte, **no como órdenes alternativas**. Un ratio se vuelve irrelevante si S>=soporte o T<=E. No se realizó una segunda búsqueda de parámetros para salvarlas.

| Activo | Soporte /E /stop /target | RR aritmético | Motivo |
| --- | --- | --- | --- |
| BNB | 717.21 / 719.28 / 703.04 / 769.56 | 1.749 | RR 1.749<2 al costo base |
| DOT | 1.0015 / 1.0071 / 1.0047 / 1.2658 | 18.285 | stop>=soporte: invalida retest |
| ETC | 7.391 / 7.411 / 7.281 / 8.071 | 2.727 | mínimo no cabe primer libro y spread segundo>20 |
| FARTCOIN | 0.1193 / 0.12 / 0.1183 / 0.176 | 18.060 | spread segundo>20 |
| FIL | 0.897 / 0.901 / 0.9 / 1.227 | 28.820 | stop>=soporte |
| GRASS | 0.6078 / 0.6141 / 0.5797 / 0.5761 | -1.087 | target<entrada y ambos spreads>20 |
| ICP | 2.556 / 2.567 / 2.558 / 3.424 | 22.159 | stop>=soporte |
| JTO | 0.41208 / 0.4147 / 0.41221 / 0.57408 | 21.873 | stop>=soporte |
| JUP | 0.2735 / 0.27498 / 0.27372 / 0.37659 | 22.915 | stop>=soporte |

Decisión específica de espera: BNB requiere nueva relación de precios con RR>=2; DOT/FIL/ICP/JTO/JUP requieren soporte/stop coherentes en un diseño nuevo, no más noticias; ETC/FARTCOIN requieren libros que cumplan todos los límites; GRASS requiere además resolver la incertidumbre del calendario de oferta y un objetivo long por encima de entrada. No son vetos permanentes a los activos.

## 11. Sizing, límites y presupuesto global

Mandato de referencia 50,000, **moneda todavía no confirmada para la cuenta**. MDL máximo 3%, MDD máximo 6%; operativos 2%/4%, colchón adicional 20% del MDL operativo. Esos máximos son techos, no presupuesto a consumir. Spotlong-only sin leverage. Límite ordinario por trade 0.25%, riesgo agregado de stops 0.50%, exposición bruta 50% y por activo 20%. Para este experimento se propone 0.05% máximo, inferior al ordinario; el operador debe imponerlo aunqueconfig mantenga 0.25%. No se editó la política para obtener PASS.

La reserva diaria equivale a 0.4% de equity inicial del día, dejando espacio operativo menor que 2% antes de descontar pérdidas y riesgo ya comprometido. El MDD se mide respecto amax(capital inicial, pico reconciliado), incluidos flujos conforme al diario; no reiniciar cuenta/base para eludir un breach. Un lockout intradía persiste ese día. Deben incluirse posiciones, órdenes pendientes, cash y pérdidas latentes en moneda única, con conversiones explícitas verificadas si existen.

Con E de entrada, S stop, T target, C=(fees+slippage)/10000 por lado:

`pérdida_por_unidad = E-S+(E+S)*C`

`beneficio_al_target = T-E-(T+E)*C`

`RR_neto = beneficio_al_target / pérdida_por_unidad`

`riesgo_permitido = min(0.0005*equity, remanenteMDL_reserva, remanenteMDD_reserva, remanente_stop_global, remanente_presupuesto_piloto)`

`q = floor_precisión(min(riesgo_permitido/pérdida_por_unidad, exposición_disponible/E, cash/(E*(1+C)), tope_profundidad/E))`

Verificar q>=mínimo yq*E>=mínimo USD; si no, no operar. La fórmula representa pérdida prevista con costos al stop, no garantiza el fill antegap. El gate añade verificaciones de política/cuenta, hashes, dirección, frescura y consenso. Las cifras de ejemplo no prueban que una cuenta real cumpla ninguna de ellas.

**Ejemplo normalizado de 10,000 USD hipotéticos**, sin posiciones ni órdenes y únicamente para comparar capacidad, usando costos 55 bps y menor profundidad observada. No es saldo ni moneda de la cuenta real. Riesgo máximo 5 USD/trade; no sumar filas. El límite a 0.05% sobre referencia 50,000 serían 25 unidades de la moneda de cuenta, condicionado a su verificación; profundidad/cash/remanentes pueden reducirlo mucho.

| Activo | Cantidad ilustrativa | Notional USD | Pérdida prevista USD alstop | Motivo de límite |
| --- | --- | --- | --- | --- |
| BTC | 0.00404033 | 320.413 | 5.0000 | riesgo 0.05% |
| ETH | 0.07519887 | 172.061 | 5.0000 | riesgo 0.05% |
| HYPE | 1.94408046 | 145.203 | 5.0000 | riesgo 0.05% |
| DOGE | 2165.60756185 | 162.308 | 5.0000 | riesgo 0.05% |
| INJ | 24.0901163 | 180.122 | 5.0000 | riesgo 0.05% |
| CRV | 197.41081816 | 66.824 | 3.3167 | profundidad |
| ENA | 325.28364 | 60.470 | 5.0000 | riesgo 0.05% |
| HBAR | 1585.12031 | 119.138 | 2.3825 | profundidad |
| BONK | 16366275.82837 | 48.117 | 3.1335 | profundidad |
| FLOKI | 1379151.28069231 | 31.155 | 1.0148 | profundidad |
| ETHFI | 34.73834 | 20.860 | 0.4644 | profundidad |

El presupuesto 0.50% de pérdidas acumuladas del experimento, el máximo diario 0.15% y un solo piloto se comparten entre las 30 filas ya estudiadas y propuestas futuras; **no se renuevan con cada tanda, activo, IA o informe**. Ganancias no reabren automáticamente ese presupuesto. La regla de revisión temprana no eleva tamaño. Este overlay es una propuesta de gestión manual del piloto; el Lab actual no mantiene un monitor de fills ni aplica automáticamente esos contadores de experimento.

Antes de ejecutar, el operador debe poder registrar cadafill/fee, órdenes pendientes, valuación intradía, baseline/pico y órdenes protectoras. Si no puede vigilar una posición durante el horizonte, no abrirla. Supervisión no significa retirar stops; si el exchange o conexión falla, registrar contingencia y reducir riesgo tan pronto sea operativo. Ninguna fórmula vuelve inviolable un MDD frente a un salto de mercado.

## 12. Incertidumbre, faltantes y punto de cierre

No se investigó buscando 100% de información. Se cubrieron identidad/red,60 series multitemporales, estadística/correlaciones, tokenómica y captura de valor, actividad cuando disponible,40 referencias T/R, diagnóstico de las 20 reglas, costos, dos libros, macro/evento y gestión. Se buscaron contradicciones materiales: quema BNB más reciente, cambio monetario DOT, recompra sETHFI distintas de burn, derechos veCRV frente a CRVspot, propuesta JUP no ejecutada por inferencia y alcance de fees HYPE/Jupiter.

Tras resolver esos puntos, una fuente adicional genérica sobre el sector no cambia la tesis o el tamaño recomendado. Se cierra la investigación con decisiones y triggers concretos. Refrescar mercado/cuenta al activar no es otra ronda indefinida de búsqueda. No existe garantía de haber detectado todas las noticias, incidentes o cambios intradía posteriores al corte.

| Faltante | Clase | Impacto y tratamiento |
| --- | --- | --- |
| Moneda, fees efectivos, holdings, órdenes, flujos, pico y baseline cuenta | Crítico ejecución | No READY hasta reconciliación y verificación expresa; capital/máximos ya confirmados no se vuelven a pedir |
| Revisión real Claude mismo hash y gate vigente | Crítico ejecución | Codex no la suplanta; cambio de propuesta/datos requiere dos revisiones nuevas |
| Snapshots actuales al activarse el escenario | Crítico ejecución | Datos aquí históricos; refrescar y respetar TTL, no reutilizar aprobación vencida |
| Ventaja/probabilidad calibrada y nueva OOS independiente | Material | Se acepta solo experimental 0.05%, presupuesto global, cierre y revisión; no se exige backtest ganador |
| HYPE solo 271 diarias | Material | Sin partición 120 traswarmup 200; no sustituir venue ni reducir requisitos retrospectivamente |
| Profundidad/salida histórica, intrabar, colas | Material | Diagnósticos aproximados, libro nuevo, menor tamaño; gaps pueden exceder pérdida prevista |
| Concentraciónholder, oferta/unlocks exactos de varios tokens | Material | No monetizar una fecha no verificada; para GRASS esperar claridad, para otros aceptar incertidumbre explícita o posponer |
| Ingresos auditados/captura exacta de valor y calendarización de fees | Material | No DCF ni dividendos imputados; TVL/fees solo contexto de actividad |
| Vintages FRED/noticias completamente exhaustivas | Material acotado | No entran en backtest; operador revisa incidentes/evento antes de activar |
| Fees Curve HTTP 400/API opcional o onchaincompleto | Menor para estas tesis | Documentación primaria y metadatos de faltante; no veto automático ni valorinventado |

Las carencias materiales no quedan aprobadas por publicar este documento. Codex acepta explícitamente, **para diseño de piloto pequeño**, ventaja desconocida, muestra corta/selección adaptativa, fuentes de oferta/ingresos incompletas, costos variables y ejecución histórica aproximada. Claude debe aceptar o rechazar esas mismas incertidumbres con argumento propio sobre el mismo expediente. Consenso no puede convertir un faltante crítico en aceptable.

## 13. Revisión independiente de Codex

**Opinión final propia: APROBACIÓN CONDICIONAL DEL DISEÑO DE PILOTO, ABSTENCIÓN DE APROBACIÓN DE EJECUCIÓN.** Recomiendo conservar BTC/ETH/HYPE/DOGE para el primer candidato que active todos los requisitos, con prioridad indicada si coinciden señales; alternativas secundarias documentadas y nueve configuraciones descartadas. No afirmo una ventaja probada ni que deba operarse el 29 a cualquier precio.

Congruencia comprobada: tesis de rebote limitada a 5/7 d, señales confirmadas al cierre, stop por estructura, target distinto para M/R, barreras intermedias explícitas, costos y sizing verificables, diagnóstico específico separado de T/R, eventos e invalidación, una sola exposición experimental y seguimiento global. Rechazo elevar techos por falta de oportunidades y rechazar todo piloto solo por no pasar OOS. La contraevidencia de BTC/DOGE se conserva y se acepta a riesgo pequeño, no se atribuye una rentabilidad futura a su liquidez.

Objeciones que mantienen prudencia: los targets R de HBAR/ETHFI son ambiciosos; varios ratios se apoyan en stops estrechos; el costo duplicado afecta BTC/ETH/HYPE; HYPE carece de holdout válido; historias de oferta/ingresos son parciales. Las alternativas más débiles no tienen el mismo grado de convicción ni prioridad que los cuatro principales. Un nuevo incidente verificado puede invalidar esta opinión aunque la fórmula siga dando RR 2.

Con autorización del propietario se añadió una auditoría por un agente de Codex, solo lectura y sin acceso a estudios de Claude o datos privados de cuenta. Contrastó los 20 ratios, ticks, mínimos,11 geometrías válidas, nueve descartes ylos 13/19 benchmarks con MDD superior al 6%; también revisó las afirmaciones primarias materiales de BNB/HYPE. No encontró un error material que obligara a cambiar la lista principal. Señaló la discrepancia 720/721 del payload, aquí aclarada, y ratificó que liquidez/prioridad no demuestran rentabilidad esperada. El stop BTC está aproximadamente 0.46% bajo E y los costos pesan mucho en su pérdida prevista. Esta auditoría refuerza la trazabilidad, pero no constituye una segunda firma de IA distinta ni aprobación operativa.

Esta revisión es narrativa del expediente de investigación. **No es una Review aprobatoria del schema para una Proposal operativa con cuenta/hash vigente.** No se llamódecide con cuenta ficticia ni se marcaronpolicy_verified/account.verified/reconciled. No se atribuye revisión o aprobación a Claude. Su colaboración siguiente debe contrastar este estudio sin copiar la conclusión, determinar aceptación material y revisar la propuesta fresca cuando haya señal.

Alternativas consideradas:20%buy/hold independiente implica MDD excesivo en varios activos; efectivo preserva presupuesto hasta señal; no se crean cortos ni derivados para compensar. Entrar al ask actual viola zona/ratio en estos escenarios. Paper indefinido no es requisito universal: se permite piloto real limitado una vez superados los controles críticos.

## 14. Trazabilidad, reproducción y verificación

Base del Lab: `a2c4f006983a4ae15bbc35d07e38f8e55e6c160f`; este trabajo añade investigación, no modifica conectores/motor/política ni la sesión Claude. Los scripts de sesión, cache y snapshots se conservan localmente fuera de Git por el alcance de publicación solicitado. **Repetir consultas públicas no reproduce exactamente un snapshot histórico**; para replay exacto se necesita el archivo local cuyo hash se publica. Estos dos documentos permiten auditar métodos/resultados, pero no incluyen por sí solos todos los insumos de replay.

Procedimiento: resolver Excel/identidad; collect de cada spot con metadata y fundamentales; analyze 1 h/4 h/1 d; simulación T/R del protocolo previo; contraste fundamental web; segundo libro; fórmula Q y diagnóstico causal; revisión narrativa y control de publicación. APIs con timeout, retry acotado y procedencia del PublicClient. No se usaron llamadas a APIs de modelos ni agentes automáticos de trading. No se modificó el Excel para corregir CRV.

Para nueva captura, registrar cada activo/ID/chain exacto en config temporal aislado y usar el CLI del repo:

```text
lab --db data/aislado.sqlite collect --asset BTC/USD --assets-file config/assets.toml --enrich --output data/BTC-nuevo.json
lab analyze --dataset data/BTC-nuevo.json --output outputs/BTC-nuevo-dossier.json
```

Elconfig estándar solo contiene ejemplos; para los otros 19 hay que declarar el mapeo de la sección 2 sin alterar el trabajo concurrente. `lab backtest` es baseline EMA y **no sustituye** los simuladores T/R o Q aquí definidos. Su reproducción requiere implementar las reglas descritas o disponer de los scripts de sesión locales. Antes de operación, usar Proposal/Review/RiskPolicy/Account del repo, renovar hashes y pasar risk-check/decide con ambas revisiones reales; no crear una cuenta sintética para conseguir READY.

Comprobación del entorno de esta tanda: **70 pruebas offline aprobadas y `ruff check src tests` sin errores**. Se retiró del proceso la variable de entorno SSLKEYLOGFILE que apuntaba a una ruta no autorizada, conservando TLSverificado y sin cambiar el Lab. Los diagnósticos privados mostraron avisos de deprecación pandas/Num Py al sumar timedeltas; finalizaron correctamente y sus controles de causalidad/contabilidad pasaron. Es una deuda de compatibilidad de scripts de sesión, no evidencia de rentabilidad.

Fuentes dinámicas y consultas: Kraken OHLC/Depth/AssetPairs, CoinGecko mercados/coins, FREDseries, DeFiLlama TVL/fees, y fuentes primarias enlazadas junto a cada afirmación. Fecha de publicación editorial se indica donde se verificó; en API se conserva fecha de observación/fetched_at. Noticiasnoauditadas, marketing y propuestas de foro se tratan como evidencia limitada, no instrucciones. No se ejecutaron textos de páginas ni se siguieron instrucciones insertadas en respuestas API.

Hashes SHA 256 canónicos de Dataset — incluyen cotización, velas, fundamentales y metadata según serialización del Lab:

| Activo | SHA 256 Dataset | Diarias |
| --- | --- | --- |
| BNB | `57ff56ad4a510d8248bdf14caf20c8de3a8f64adf123b3d3cc3daae6f5db5e59` | 552 |
| BONK | `d388dc30422bd374916acd52bc2cb04e05181e3ab84bc90658c2f65e91408677` | 720 |
| BTC | `510cb8083ac9554f50a983738cebe1b08c18d3590127ff88b0013cc359f8e074` | 720 |
| CRV | `d3e828b460610dc3b1948c95e4458d43af2e2ee64049eeb89cbb4910046a8e66` | 720 |
| DOGE | `8f5272452a6807818ea6edd89a293cd49a27ac70e2cf867868d5d27b7a0cd3f8` | 720 |
| DOT | `a21a260533cb7eb820a2284370a437bfa71b72d04b3417e3a3629c735d0d38e8` | 720 |
| ENA | `70e60b9240e4d5fd7cbc8a80dbef580374b382ad6b8efddd872b6581cb1257ad` | 720 |
| ETC | `c6aae9a6b6b75d3aa121a7fed3c5343d90512149f4ed50df19410b458c9feb7c` | 720 |
| ETH | `a5f860c1e02b03e1df920ee72c6bdfd7e5d680eeb0807638fcf0a1f18071284d` | 720 |
| ETHFI | `d1dd2a2017b95d11207fefdba0e0528dbca255e5705f377fe944c307f22cdf1a` | 720 |
| FARTCOIN | `9c1e98463ba7d484a2158b4a8580512f6201a7ec90b02f420e8b8343f6d07248` | 641 |
| FIL | `336fb053309f4dad45227fb10fdcd61938ea611a5d9009dfdcccb7597e6b659c` | 720 |
| FLOKI | `e0c9c95a0d7d4daae0e22bc7c4abec208f7aa4889b11f19e98961667dcbe3cce` | 720 |
| GRASS | `0aeee4d506ca5c23fc77a91b1b427c5f86e6756f2819f776a7f4aaa1429b90cc` | 637 |
| HBAR | `650e5637019d563f987153b81a3002c5c9b730a363189c2e0b0c10e77bba3878` | 473 |
| HYPE | `f6d043869a0e1ffaa3939b014f9360331ee910cb8b5150b7cd97ab2343d93ddf` | 271 |
| ICP | `b0c68dbb29c6d5f47c1e851721bfb7659334176b341ad3ba528b3e8ab56bf328` | 720 |
| INJ | `b7beec14f4a42e468a7fac63ad7345c090bc3d9bdeebed247363acfaefccdb5a` | 720 |
| JTO | `300bb25cbaff4075416e83eeac7239e8edee63ba598b332cebd6cfd623dbee34` | 720 |
| JUP | `a80d5bcf74238778b04b64a377d52138693a6326e3b9f200910c590872188ea9` | 720 |

Excel SHA 256:`b1d475c71ad6de7c33f534a5bb854227851ecbfdb36a393b130c8d0a351b211c`.

Protocolo previo SHA 256:`6eb1dba8fc6fd56bc238016f6e92e74ff7ec61de8474fb06f4a52d89d967576b`. Incluye la corrección CVR→CRV autorizada antes de recopilar mercado. No incluye como preregistrado el umbral ADX 25 elegido después.

Manifiesto de recolección SHA 256 del archivo local:`7259dae3be75f2d746d7ec05704dde6a4f53f824f45d1a5f39b69106ad9ec49f`.

La validación final comprueba hashes 20/20, calidad 60/60, instrumentos/mínimos, ticks, geometría de los 11 candidatos, descarte de los 9 fallidos, causalidad y contrapruebas, ausencia de secretos y enlaces locales. Los máximos/flags de cuenta siguen intactos. Publicación prevista en rama/PR nueva sobre el main remoto existente comojsforeroc 80-debug, sin force-push y con solo estos dos documentos; el resultado de esa publicación se informa en la entrega y en el estado local.
