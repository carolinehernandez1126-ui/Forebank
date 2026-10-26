# Estudio 2: sistema de trading de Claude (Forebank C1T v1) y activos 6–10

| Campo | Valor |
|---|---|
| Autor | Claude, modelo `claude-opus-5-5` (Claude Code). Investigación fundamental del lote 2 apoyada por un subagente de Claude; la verificación y las conclusiones son mías |
| Cierre | 2026-10-26 ~06:30 UTC (2026-10-26 01:30 America/Bogota) |
| Alcance | Filas 1–10 de `lista_activos.xlsx` (AAVE, ADA, AIXBT, ALGO, APT, ARB, ASTER, ATOM, AVAX, BCH). Las filas 12–16 (BNB, BONK, BTC, CVR, DOGE) se usaron solo como prueba fuera de muestra del sistema congelado |
| Mandato | Capital 50.000; operativos MDL 2% / MDD 4% (techos 3% / 6%); máximo 0,25% de riesgo por trade y 0,5% de riesgo abierto; costos 40 + 15 bps por lado |
| Estudio previo | [2026-10-25-universo-top5](../2026-10-25-universo-top5/ESTUDIO.md). Este estudio lo complementa; aquella decisión NO TRADE sigue vigente |

## Decisión

1. **Sistema adoptado: Forebank C1T v1** (reglas abajo). Es una estrategia de tendencia diaria, solo largos, con filtro de régimen BTC y un stop trailing limitado a 1 R.
2. **Estado: PAPER TRADING, sin capital real.** Las reglas quedan congeladas a partir de hoy (2026-10-26). Tiene ventaja demostrada en 2018–2022 y fuera del universo original, pero **en 2023–2026 su ventaja después de costos es prácticamente nula**. Según mi protocolo registrado, eso no basta para arriesgar dinero.
3. **Hoy: ninguna señal.** BTC está en régimen ON (80.048 frente a una SMA200 de 72.945), pero ningún activo supera su máximo de 50 días. Los más cercanos son BTC (+9,0%) y BNB (+9,7%); el resto está a +25–52%.
4. **Activos 6–10 (ARB, ASTER, ATOM, AVAX, BCH): NO TRADE.** Los 5 son elegibles por liquidez en Kraken, pero no hay señal del sistema y sus fundamentales son débiles (resumen abajo).
5. **Cuándo pasaría a capital real:** cuando el paper trading posterior al 2026-10-26 acumule **al menos 15 trades** con **expectativa > 0 R, que siga > 0 al quitar el mejor trade**, y con **MDD de la cartera simulada ≤ 2%**. Además hace falta una cuenta de Kraken reconciliada y la revisión de Codex del mismo plan, como exige el gate del Lab. Si en esas condiciones la expectativa es ≤ 0, el sistema se retira.

## Hallazgo central (por qué el resultado es modesto)

La ventaja de seguir tendencia en cripto **existe y se repite fuera de muestra**: la regla H1 del estudio 1, sin cambios, dio **+0,61 R por trade en 125 trades en 2018–2024**. Pero esa ventaja se gana dejando correr las posiciones ganadoras y aceptando devolver una parte grande de la ganancia abierta.

Con un **MDD del 4% medido a mercado contra el máximo del equity**, eso no es posible. La versión sin trailing (C1), incluso con 0,10% de riesgo por trade, tuvo un MDD de −5,2% y un peor día de −4,1%. La versión que cumple el mandato (C1T) recorta esas devoluciones y con ellas la mayor parte del beneficio. Su rentabilidad anual simulada es de ~1%, por debajo de la tasa de los fondos federales (3,88%).

**Con estos límites, el techo realista de un sistema direccional de altcoins es de ~1–2% anual.** Es un dato para quien fije el mandato. No es una recomendación de cambiarlo.

## Sistema Forebank C1T v1 (reglas congeladas)

| Elemento | Regla |
|---|---|
| Datos | Velas diarias cerradas de Kraken (00:00 UTC), pares `/USD` |
| Universo | Activos de la lista con par USD en Kraken, spread ≤ 20 bps y volumen diario Kraken ≥ 250.000 USD (mediana de 30 días). Hoy: AAVE, ADA, ALGO, APT, ARB, ASTER, ATOM, AVAX, BCH, BNB, BONK, BTC, DOGE. Excluidos: AIXBT (liquidez) y CVR (no cotiza en Kraken) |
| Régimen | Solo se compra si BTC cierra por encima de su SMA200 diaria |
| Entrada | Cierre diario > máximo de los 50 días previos → compra a mercado en la apertura siguiente |
| Stop inicial | Entrada − 3 × ATR20 (Wilder). Orden stop-loss en Kraken |
| Trailing | Cada cierre: stop = máx(stop, nivel que deja la pérdida desde ese cierre, incluyendo costos, en 1 R inicial). Nunca baja |
| Salida | Cierre < mínimo de los 20 días previos → venta a mercado en la apertura siguiente; o salta el stop |
| Tamaño | 0,20% del equity de riesgo por trade (incluye costos de ida y vuelta) |
| Topes | Riesgo abierto total ≤ 0,5%; ≤ 20% del equity por activo; ≤ 50% de exposición bruta; sin apalancamiento ni cortos |
| Prioridad | Si hay varias señales el mismo día, primero la de mayor retorno a 90 días |
| Operación | `signals.py --equity <E> [--positions pos.json]` después de las 00:00 UTC imprime las compras, los nuevos stops y las salidas. No envía órdenes |

El riesgo de 0,20% sale de la regla registrada: el mayor nivel con MDD simulado ≤ 3% y percentil 95 del MDD por bootstrap ≤ 4%. Con 0,25% el percentil 95 da −4,30% y no cumple.

## Cómo se llegó aquí (protocolo y sesgos declarados)

Todo se registró antes de mirar los resultados correspondientes ([HIPOTESIS_REGISTRADAS.md](HIPOTESIS_REGISTRADAS.md), con dos adendas). Las desviaciones se declaran:

1. **Histórico largo:** velas diarias de Binance spot USDT (BTC/ETH desde 2017; cada altcoin desde su listado), usadas como proxy. En el periodo común con Kraken, la correlación de los retornos diarios es de 0,992–0,9998 y la diferencia mediana de cierre de 0–2,4 bps. En la ventana que se puede comparar (jun-2025 → oct-2026), C1T dio −0,33 R con velas de Kraken frente a −0,27 R con Binance. El sesgo de venue es pequeño pero desfavorable para Kraken.
2. **Prueba fuera de muestra del estudio 1** (2018 → 2024-11-04, datos no vistos):

| Regla | Trades | R por trade | Sin el mejor | Mitades | Veredicto |
|---|---:|---:|---:|---|---|
| H1 (tendencia 20/10) | 125 | **+0,61** | +0,47 | +0,87 / +0,35 | Ventaja confirmada; drawdown de 20 R, lo que obliga a reducir el tamaño |
| H2 (retrocesos) | 145 | −0,002 | −0,02 | +0,14 / −0,14 | **Descartada definitivamente** |

3. **Candidatos** (train hasta 2022, validación 2023 → 2024-11-04, holdout 2024-11-05 → 2026-10-25; universo de 9 activos elegibles del lote 1-2):

| Candidato | Train | Validación | Holdout | Comentario |
|---|---|---|---|---|
| C1 (tendencia 50/20, BTC > SMA200) | +3,32 R (25 trades) ✔ | +0,60 R ✔ | −0,04 R | **Elegido por la regla**, pero **incumple el mandato**: MDD −5,2% incluso con 0,10% de riesgo |
| C2 (momentum semanal 90 días) | +0,07 R ✘ | −0,04 R | +0,01 R | Descartado |
| H1 | +0,85 R ✔ | +0,41 R | +0,18 R | Menor expectativa en train |
| **C1T** = C1 + trailing de 1 R (adenda, **añadido después de ver la cartera**) | +0,52 R ✔ | **+0,003 R** (−0,06 sin el mejor) ✘ | −0,07 R | Cumple el mandato; **falla la validación del protocolo** |

4. **Prueba fuera de universo** (adenda 2, C1T sin cambios en BNB, BONK, BTC y DOGE): **+0,50 R en 92 trades**, PF 2,43, +0,35 R sin el mejor trade y ambas mitades positivas. BTC solo: +0,46 R en 30 trades. Por periodos: train +0,92 R, validación +0,09 R y holdout +0,17 R; sin el mejor trade, validación y holdout quedan en ≈ 0.
5. **Universo combinado de 13 activos:** 236 trades con +0,29 R (train +0,71 R; 2023–2026 ≈ +0,01 a +0,03 R). Cartera con 0,20% de riesgo: rentabilidad anual del 0,98%, **MDD −1,48%, peor día −0,51%**, percentil 95 del MDD por bootstrap −3,86% (en horizonte de 1 año, −1,84%). Por año: 2019 +0,7%, 2020 +1,9%, 2021 +4,0%, 2022 0,0%, 2023 +0,7%, 2024 +1,3%, 2025 −0,1%, 2026 +0,1%.

**Lectura:** el sistema tiene una asimetría favorable. Pierde muy poco en mercados laterales o bajistas (el peor año es −0,13%) y gana en las tendencias. Pero en los últimos ~4 años la ventaja medida trade a trade es ≈ 0, y el C1T se ajustó después de ver datos. Mi conclusión es que hay que demostrarlo hacia adelante antes de arriesgar capital. Un sistema con ventaja ≈ 0 que paga 110 bps por operación no justifica dinero real hoy.

**Debilidades que acepto:**
- Sesgo de supervivencia: la lista de activos es de 2026, así que el universo excluye tokens que desaparecieron.
- Las simulaciones no modelan fallos de ejecución intradía ni caídas de Kraken.
- El bootstrap de bloques supone que la historia es representativa.
- El ajuste C1T se hizo después de ver los datos.

## Activos 6–10: fundamentales (fuentes consultadas el 2026-10-26)

| Activo | Kraken (spread / volumen diario) | Datos clave | Lectura |
|---|---|---|---|
| ARB | 5,8 bps / 1,9 M | TVL de 1,47 B (−59% interanual, estable desde julio); 3,9 B en stablecoins; desbloqueos de ~92,65 M ARB al mes (~1,3% del circulante) hasta mar-2027; el token no capta comisiones; Stylus pausado desde el 2-oct por riesgo de denegación de servicio | Bajista: dilución constante y ningún catalizador cercano |
| ASTER (`aster-2`, BEP-20, distinto de Astar/ASTR) | 3,9 bps / 0,58 M | Comisiones de 30 días de 3,96 M frente a 192 M en un año (−95% de ritmo); recompra el 99% de las comisiones; desbloqueo del equipo (400 M) aplazado a sep-2027; emisiones confusas | Mixto: recompras agresivas, pero los ingresos se desploman |
| ATOM | 12,1 bps / 0,49 M | Inflación del 10%; ataque de gobernanza en Neutron (21–22 sep, 1,72 M ATOM); la cadena se detuvo 25 h y los validadores movieron fondos sin firma del dueño; Gauntlet concluye que la emisión excede lo necesario | Bajista: dilución y daño reputacional; posible catalizador si se reforma la tokenómica |
| AVAX | 1,1 bps / 5,9 M | TVL de 560 M (−71% interanual), 1,41 B en stablecoins (−43%); upgrade Helicon el 22-sep; ETF spot de VanEck y Grayscale con activos en caída (61,5 → 51,4 M entre el 6 y el 22 de oct, fuente secundaria); desbloqueo de ~1,67 M el 8-nov (extrapolado, no oficial) | Bajista a corto plazo |
| BCH | 4,3 bps / 0,96 M | Futuros en CME anunciados para el 19-oct (no pude confirmar su volumen); Grayscale presentó un S-3/A para convertir BCHG en ETF (fuente primaria SEC; sin aprobación); −17% en 30 días tras el rally del anuncio; uso on-chain casi nulo | Catalizador del ETF pendiente, pero el "vender la noticia" ya está en marcha |

Ninguno de estos datos genera por sí solo una señal en C1T, que es puramente de precio. Los fundamentales se usan como contexto de riesgo. Por ejemplo, una señal de ATOM o ARB tendría que ejecutarse sabiendo que hay dilución continua.

## Faltantes

| Faltante | Severidad | Tratamiento |
|---|---|---|
| Cuenta de Kraken reconciliada, moneda y comisiones reales | Crítico para operar en real | No aplica mientras el sistema esté en paper |
| Ventaja en 2023–2026 ≈ 0 | Material | Por eso el sistema queda en paper trading con criterios de promoción fijados |
| Histórico de otro venue (Binance) | Material | Medí el sesgo: es pequeño y desfavorable; para operar se usan velas de Kraken |
| Comisiones reales (el sistema supone 40 bps taker) | Material | Si la comisión real es menor, el sistema mejora; se revisa al conocer el nivel de la cuenta |
| Algunas fuentes de noticias de calidad media (agregadores, páginas de exchanges) | Menor | Marcadas; no intervienen en la señal |

**Por qué cierro aquí:** el sistema es puramente de precio y está validado con todo el histórico disponible. Más investigación fundamental no cambiaría las señales, y otra ronda de ajustes sobre los mismos datos aumentaría el sobreajuste. La siguiente información útil es la del paper trading hacia adelante.

## Revisión independiente

- **Revisor:** Claude, `claude-opus-5-5`, 2026-10-26 UTC. **No hay ninguna propuesta de Codex publicada que revisar.**
- **Veredicto sobre una operación real hoy:** REJECT/NO TRADE. No hay señal, la cuenta no está reconciliada (crítico) y la ventaja en el régimen reciente no está demostrada.
- **Sobre el sistema:** lo adopto para paper trading. Si Codex propusiera operar este sistema con capital real antes de cumplir los criterios de promoción, votaría REJECT.
- **uncertainty_accepted:** sí, para pasar a paper trading. **strategy_coherence_confirmed:** sí. La tesis (prima de tendencia en régimen alcista de BTC), el horizonte (días a semanas), la señal (ruptura de 50 días), la validación (2018–2026 con costos), la ejecución (apertura y stop a mercado), el riesgo (0,20% por trade, MDD simulado −1,5%) y la invalidación (cierre < mínimo de 20 días o salto del stop) son coherentes entre sí.

## Archivos

- [HIPOTESIS_REGISTRADAS.md](HIPOTESIS_REGISTRADAS.md): registro v2 con las adendas, escrito antes de cada prueba.
- [engine.py](engine.py): simulador de cartera (valoración diaria a mercado, gaps, costos y topes).
- [signals.py](signals.py): hoja diaria de señales de C1T con velas de Kraken.

Para reproducir: descargar las velas diarias de Binance (`/api/v3/klines`) en `private/claude/long/<asset>.json` y las de Kraken con `lab collect`; después importar `engine` y llamar a `simulate(C1T(), ...)`.

## Fuentes (consultadas el 2026-10-26 UTC)

- Kraken API pública (AssetPairs, OHLC, Depth); Binance API pública (`/api/v3/klines`); CoinGecko; DefiLlama (TVL, comisiones, stablecoins); FRED.
- Cosmos Hub weekly update (1-oct-2026, primaria): https://forum.cosmos.network/t/hub-weekly-update-18-october-1-2026/17397 · Propuesta 1058 on-chain · Unchained (23-sep-2026): https://unchainedcrypto.com/cosmos-hub-restarts-and-moves-2-1-million-in-stolen-tokens-out-of-an-attackers-wallet/
- Arbitrum Stylus pausado: https://thedefiant.io/news/security/arbitrum-pauses-new-stylus-activations-in-emergency-security-action
- Aster: https://www.kucoin.com/news/flash/aster-extends-team-token-unlock-period-for-400m-aster-until-september-2027 (1-sep-2026) · https://coinmarketcap.com/academy/article/aster-dex-slashes-monthly-token-unlocks-by-97percent-with-staking-switch
- Avalanche Helicon: https://cryptobriefing.com/avalanche-helicon-upgrade-staking-execution/ · 24/7 Wall St. (24-oct-2026): https://247wallst.com/investing/cryptocurrency/2026/10/24/how-low-could-avalanche-avax-go-after-an-11-drop-in-a-week
- BCH: The Block (22-sep-2026): https://theblock.co/news/markets/2026-09-22-cme-adds-bitcoin-cash-and-uniswap-futures-as-crypto-derivatives-push-grows-416049 · SEC S-3/A (primaria): https://www.sec.gov/Archives/edgar/data/0001732409/000119312526389253/bch_s-3_amendment_1.htm · 10-K BCHG: https://www.sec.gov/Archives/edgar/data/0001732409/000119312526381856/bchg-20260630.htm
- Fuentes de calidad baja, solo contexto: páginas de exchanges (MEXC, KuCoin insight), tradersunion, coingabbar, hokanews.
- Liu, Y. & Tsyvinski, A. (2021), *Risks and Returns of Cryptocurrency*, RFS 34(6).
