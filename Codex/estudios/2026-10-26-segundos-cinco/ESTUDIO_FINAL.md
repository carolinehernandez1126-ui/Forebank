# Estudio final — segunda tanda: ARB, ASTER, ATOM, AVAX y BCH

**Codex | 26-10-2026, America/Bogota.** Investigación y revisión propias, independientes respecto de Claude; su estudio no se leyó. Mercado real Kraken, `synthetic=false`. Solo se publican este estudio y sus conclusiones; cuenta, claves, scripts de sesión y snapshots quedan fuera de Git. Datos públicos en USD no confirman la moneda de la cuenta.

## 1. Decisión detallada

**Conservar tres planes experimentales de compra condicionada: BCH primero, AVAX segundo y ASTER tercero.** ARB queda en observación y ATOM se pospone hasta aclarar su actualización de red. No hay compra inmediata al precio del snapshot: los tres candidatos están por encima de sus zonas de entrada. No se compran por perseguir el mercado.

Estos planes pueden convertirse en pilotos reales con ventaja estadística no demostrada. No se exige OOS positivo ni un backtest ganador; sí tesis coherente, precio/stop/target razonados, incertidumbre aceptada por ambas IAs y riesgo válido. La recomendación se basa en estructura y escenarios, no en rentabilidad probada. BCH destaca por colchón de costos; AVAX por profundidad; ASTER por estructura lateral y vínculo de recompras, con menor capacidad y mayor riesgo de oferta.

Los tres planes se excluyen entre sí en esta primera tanda del piloto: **una sola posición experimental simultánea**. No se suman cantidades como cartera. La cuenta/costos reales y la firma de Claude siguen pendientes; no existe READY ni orden enviada. Los activos de la primera tanda no fueron trades perdedores: no se ejecutaron.

Corte principal: 26-10-2026, aproximadamente 11:50–11:51 UTC. Libros contrastados a las 11:54:30–11:54:34 UTC. El informe es un expediente de research; las cotizaciones son históricas, no una aprobación vigente. [Conclusiones y hash del documento](CONCLUSIONES.md).

## 2. Selección e identificación

Se tomaron las siguientes cinco filas, sin saltos: `archivos_de_apoyo/lista_activos.xlsx`, hoja **Lista de activos**, rango **A7: A11**. Corresponden a las posiciones6–10 del universo, después de AAVE/ADA/AIXBT/ALGO/APT. No se eligieron por su rendimiento observado.

| Fila | Activo | Kraken spot USD | ID CoinGecko | Identidad | Tick / mínimo unidades |
| --- | --- | --- | --- | --- | --- |
| 7 | ARB | ARBUSD | arbitrum | Arbitrum One ERC20 | 0.0001 / 25 |
| 8 | ASTER | ASTERUSD | aster-2 | Aster BEP20 BNB Chain | 0.00001 / 7 |
| 9 | ATOM | ATOMUSD | cosmos | Cosmos Hub, uatom | 0.0001 / 3 |
| 10 | AVAX | AVAXUSD | avalanche-2 | Moneda nativa Avalanche | 0.001 / 0.5 |
| 11 | BCH | BCHUSD | bitcoin-cash | Moneda nativa Bitcoin Cash | 0.01 / 0.018 |

Todos los pares estaban online y quoteUSD. Aunque AssetPairs ofrece margen en algunos, aquí se considera únicamente compra spot sin apalancamiento. La elegibilidad regional de la cuenta debe confirmarse; online internacional no la demuestra.

ARB canónico: `0x912ce59144191c1204e64559fe8253a0e49e6548`; se excluyó Arbitrage Loop, ticker ARB. ASTER: `0x000Ae314E2A2172a039B26378814C252734f556A`, confirmado en [documentación oficial](https://docs.asterdex.com/usdaster-token/overview); no es Astar/ASTR. AVAX y BCH nativos no son versiones Wormhole o Binance-Peg. El ID `cosmos` se corresponde a Cosmos Hub/ATOM, no a todo el ecosistema Cosmos.

ASTER tiene 371 diarias desde 20-10-2025, coherentes con su [listado Kraken](https://blog.kraken.com/product/asset-listings/aster-is-available-for-trading) de esa fecha. Los otros cuatro tienen720 desde 05-11-2024. Todos: 720 velas1h y720 velas4h. Última1h abierta26-10 a 10:00 y cerrada11:00 UTC; última4h abierta04:00 y cerrada08:00; diaria abierta25-10 y cerrada26-10 00:00 UTC. Las15 series aprobaron continuidad, duplicados, orden, longitud y antigüedad al recopilarse. Se descartó la vela mutable; no se rellenaron huecos ni se mezclaron bolsas.

[OHLC público Kraken](https://docs.kraken.com/api-reference/market-data/get-ohlc-data) limita la ventana disponible. El histórico corto de ASTER limita inferencia; no constituye una prohibición general de piloto. Un fichero sin huecos puede contener horas sin negociación: se miden separadamente.

## 3. Técnico: observaciones multihorizonte

Indicadores calculados por el Lab: SMA/EMA 20/50/200, RSI 14, MACD12/26/9, ATR 14, ADX 14, Bollinger20/2, Donchian20, OBV, VWAP20 móvil/sesiónUTC y z-score de volumen20. Tendencia, momentum y volatilidad comparten información; no son confirmaciones independientes. ADX no marca dirección. VWAP de una diaria no es una medición intradía.

### Estructura diaria

| Activo | Cierre1d | EMA 20 | EMA 50 | EMA 200 | RSI 14 | ATR/cierre | ADX | Hist.MACD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARB | 0.168 | 0.184047 | 0.175754 | 0.145678 | 41.89 | 9.23% | 17.37 | -0.003113 |
| ASTER | 0.69976 | 0.706909 | 0.705678 | 0.699005 | 47.04 | 4.17% | 16.97 | -0.000203 |
| ATOM | 1.6443 | 1.736072 | 1.71347 | 1.787148 | 42.10 | 6.66% | 13.65 | -0.02005 |
| AVAX | 8.918 | 9.722629 | 9.481126 | 9.121527 | 36.30 | 6.69% | 21.66 | -0.184979 |
| BCH | 278.58 | 282.048063 | 277.525421 | 304.404963 | 47.75 | 5.31% | 20.67 | -0.472229 |

### Ejecución táctica: 4h y1h

| Activo | Cierre4h | EMA 20_4h | EMA 50_4h | EMA 200_4h | RSI 4h/1h | EMA 20_1h | VWAP20_4h | Z volumen4h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARB | 0.1689 | 0.171571 | 0.178434 | 0.183198 | 41.89 / 55.51 | 0.168808 | 0.170578 | -0.51 |
| ASTER | 0.70624 | 0.702777 | 0.703957 | 0.70863 | 52.86 / 60.55 | 0.704198 | 0.700138 | -0.44 |
| ATOM | 1.6294 | 1.661356 | 1.700253 | 1.730958 | 40.08 / 50.06 | 1.634921 | 1.728066 | -0.82 |
| AVAX | 8.841 | 8.995848 | 9.301233 | 9.707138 | 37.26 / 53.61 | 8.887752 | 8.961704 | -1.07 |
| BCH | 275.07 | 277.399033 | 278.335893 | 281.061469 | 46.02 / 52.29 | 277.919969 | 278.756518 | 1.44 |

### Rangos y retornos observados

| Activo | 7d | 30d | 90d | Min/max20d | Bollinger1d inferior/superior |
| --- | --- | --- | --- | --- | --- |
| ARB | -10.16% | -25.93% | 118.75% | 0.1622 / 0.2081 | 0.165968 / 0.203552 |
| ASTER | -0.14% | -5.11% | 12.80% | 0.66937 / 0.75515 | 0.684332 / 0.726879 |
| ATOM | -2.67% | -8.29% | 26.65% | 1.6025 / 2.0825 | 1.571749 / 1.975021 |
| AVAX | -8.66% | -16.28% | 39.19% | 8.666 / 11.726 | 8.593422 / 11.342278 |
| BCH | 0.97% | -18.79% | 31.50% | 256.19 / 317.84 | 259.665877 / 300.458123 |

**ARB. Observación:** EMA 50d>EMA 200d y cierre>EMA 200d, pero fuerte corrección mensual y medias4h descendentes. 1h mejora con RSI 55.51 e histograma positivo. **Hipótesis:** recuperación dentro de un rebote de plazo mayor. **Contraevidencia:** precio todavía bajo EMA 50d y fuerte beta BTC; subida90d desde un mínimo no elimina riesgo. **Decisión:** observar recuperación4h de 0.171571 y0.178434 o retesteo0.1622–0.1631. No fijar una compra para forzar ratio: la primera recuperación a EMA 50d deja recorrido limitado con un stop estructural amplio.

**ASTER. Observación:** régimen lateral diario, ADX 16.97, EMA 50d cerca deEMA200d y mejor estabilidad relativa a 30d; recuperación1h/4h. **Hipótesis:** comprar extremo inferior de rango para volver a banda superior diaria. **Contraevidencia:** cerca del techo4h al precio actual, baja profundidad inicial y gran oferta pendiente. **Decisión:** conservar plan de retroceso; no comprar0.71028 cerca de resistencia0.71323.

**ATOM. Observación:** cierre bajo EMA 200d y EMA 50d<EMA 200d; rebote horario débil. **Hipótesis:** mejora por reforma tokenómica. **Contraevidencia:** reformas no finalizadas y riesgo operativo de upgrade. **Decisión:** posponer hasta resultado de gobernanza, red estable y reconstrucción sobre 1.661356/1.700253; no negociar una promesa de reforma como un cambio ya ejecutado.

**AVAX. Observación:** EMA 50d>EMA 200d, pero cierre bajoEMA200d, corrección4h con ADX 35.77 e histograma positivo. **Hipótesis:** rechazo de soporte8.666 y regreso aEMA50d. **Contraevidencia:** es rebote contra tendencia táctica; EMA 200d≈9.1215 obstaculiza antes del target. **Decisión:** piloto condicionado a soporte, no entrada al ask actual.

**BCH. Observación:** mejor comportamiento7d y precio horario sobreEMA200_1h, pero EMA 50d<EMA 200d. **Hipótesis:** rebote desde soporte de rango con destino a banda superior diaria, no continuación alcista estructural. **Contraevidencia:** obstáculos282/288 y media200 diaria304.40; el rango puede romper a la baja. **Decisión:** candidato prioritario en retroceso con invalidación bajo mínimo 10d.

## 4. Fundamental: utilidad, oferta y riesgos

CoinGecko es agregado multivenue; TVL no equivale a ingresos del token ni a valor justo. No se atribuye rendimiento de staking al spot en Kraken.

| Activo | MCAP USD millones | FDV proveedor millones | Circulante/total | Circulante/máximo | Precio×máximo millones |
| --- | --- | --- | --- | --- | --- |
| ARB | 1176.54 | 1707.08 | 68.92% | 68.92% | 1707.17 |
| ASTER | 1782.44 | 5535.25 | 32.20% | 31.36% | 5683.40 |
| ATOM | 885.54 | 885.54 | 100.00% | Sin máximo reportado | n/a |
| AVAX | 3972.88 | 4211.54 | 94.33% | 61.66% | 6444.00 |
| BCH | 5610.94 | 5610.94 | 100.00% | 95.75% | 5859.63 |

FDV=MCAP no demuestra ausencia de dilución: ATOM no tiene máximo reportado y sigue un modelo de emisión; BCH tiene emisión minera remanente. En AVAX el FDV del proveedor usa oferta total, no el techo720 millones. ARB aparece con máximo 10mil millones en el agregador, pero la documentación permite emisión adicional por gobernanza; no es un límite inmutable. ASTER muestra total menor que máximo histórico, consistente con quemas, sin validar una quema concreta desde estas cifras.

### ARB

La [documentación de Arbitrum](https://docs.arbitrum.foundation/concepts/arb-token) define ARB como gobernanza: emisión inicial10mil millones y posibilidad de acuñar hasta 2% anual mediante propuesta constitucional. No se equipara a una acción con flujo de caja exigible. La [página de oferta](https://docs.arbitrum.foundation/token-supply) describe vesting mensual de equipo/inversores, pero sus cifras de circulante están fechadas en2024; no se reutilizan como saldo actual.

El [reporte oficial H1, publicado02-09-2026](https://forum.arbitrum.foundation/t/the-arbitrum-foundation-h1-2026-progress-update/31378), reporta ingresos DAO USD 6.19 millones y patrimonio no nativo USD 125 millones. Son cifras del emisor de un semestre pasado, no ingresos garantizados para holders. TVL Arbitrum USD 1474.25 millones,+1.88% a 30d, según [API DefiLlama](https://api.llama.fi/v2/historicalChainTvl/Arbitrum).

Tesis favorable: escala y diversificación económica del ecosistema. Contraevidencia: valor DAO no implica captura automática del token, dilución y gasto de tesorería, riesgos rollup/puentes/gobernanza. Juicio: merece seguimiento técnico, sin precio justo o dividendos inventados.

### ASTER

La [tokenómica oficial](https://docs.asterdex.com/usdaster-token/tokenomics) describe recompras con 99% de fees diarios, distribución a veASTER y quema equivalente desde reserva hasta una meta de oferta3mil millones. Eso no equivale a quemar dos veces el mismo ingreso ni a yield para un comprador spot. Cambió el esquema lineal de ecosistema por emisiones de staking y declara extensión del cliff de equipo hacia2027; otra línea de la misma página formula ambiguamente el cliff, por lo que no certifico fecha exacta de su próximo unlock. La información viva prevalece como afirmación actual del emisor sobre snippets viejos, sin sustituir auditoría on-chain.

DefiLlama padre Aster: TVL USD 796.95 millones; staking USD 360.90 millones separado, no sumado. `aster-perps/dailyFees`: USD 3.964909 millones a 30d. No se obtuvo `dailyRevenue` (HTTP400), por lo que fees no se llaman beneficios ni se calcula dividendo. [Protocolo](https://api.llama.fi/protocol/aster), [fees](https://api.llama.fi/summary/fees/aster-perps?dataType=dailyFees). El adaptador incluye fees de trading/funding; no es facturación auditada de efectivo.

Tesis: recompra conecta actividad y demanda potencial. Contraevidencia: incentivos inflan actividad, distribución remanente, concentración/contratos y caída de fees; las recompras no fueron reconciliadas transacción a transacción. Se investiga el token spot de una plataforma de derivados; no se opera apalancamiento o perpetuos.

### ATOM

ATOM asegura Cosmos Hub mediante staking/gobernanza; el éxito de cadenas Cosmos no obliga a que usen ATOM o generen ingresos para él. `max_supply=null` no es cero ni un techo. No se proyecta una tasa de inflación exacta sin verificar estado de cadena.

[Resultados de investigación publicados10-07-2026](https://forum.cosmos.network/t/atom-tokenomics-phase-1-outcomes/17146) proponen mejorar incentivos y tratar presión concentrada; movimientos a CEX no equivalen necesariamente a ventas. La [actualización01-10-2026](https://forum.cosmos.network/t/hub-weekly-update-18-october-1-2026/17397) indica recomendaciones de fase2 en revisión, no una reforma implementada.

[Cosmos Labs, 25-09-2026](https://forum.cosmos.network/t/neutron-governance-attack-cosmos-hub-response-and-recovery-update/17369), distingue ataque en Neutron de Hub no explotado, pero documenta pausa coordinada del Hub y transferencia excepcional para recuperación. No se afirma que Kraken perdiera fondos. Es contraevidencia de continuidad/gobernanza.

La [propuesta de upgrade20-10, actualizada23-10](https://forum.cosmos.network/t/gaia-v29-0-0-software-upgrade-update-v29-0-1-recommended/17491) cierra votación27-10 a 12:00 UTC y estima upgrade28-10 a 13:50 UTC si se aprueba; fecha sujeta a bloques y pausa temporal prevista. Tesis de mejora posible, pero menor prioridad de compra hasta verificar evento y estabilidad.

### AVAX

La [documentación Avalanche](https://build.avax.network/docs/primary-network/avax-token) define uso en gas/staking, límite720 millones, quema de fees y emisión de recompensas. Aún lejos del techo puede seguir inflacionario; quemas no significan deflación neta. El máximo circulante efectivo puede reducirse por quemas. No se confunden tasas de consumo del algoritmo con un APY garantizado del usuario.

[Helicon](https://build.avax.network/docs/primary-network/helicon-upgrade) activado22-09-2026 cambia ejecución/gas y parámetros de validación; la reducción de MinConsumptionRate se aplica gradualmente durante90d. Es un cambio efectivo, sin garantizar precio alcista ni yield por comprar en CEX.

TVL cadena USD 560.03 millones,-10.01% a 30d según [API](https://api.llama.fi/v2/historicalChainTvl/Avalanche). Menos TVL puede reflejar precios/flujo, no se atribuye a una causa sin prueba. Tesis: utilidad verificable y eventual rebote de soporte. Contraevidencia: competencia de L1s, captura de demanda de redes nuevas, emisiones y corrección táctica. Profundidad adecuada permite pilotear con riesgo pequeño si se forma el trigger.

### BCH

El [sitio del proyecto](https://bitcoincash.org/) describe dinero de pagos, PoW SHA256, máximo 21 millones y CashTokens. Estos atributos no son equity, yield ni prueba de demanda suficiente. La [especificación BCHN](https://upgradespecs.bitcoincashnode.org/2026-05-15-upgrade/), versión09-01-2026, fija para mayo mejoras de scripting; una especificación o funcionalidad no demuestra adopción económica o revalorización.

Tesis: activo monetario maduro con oferta relativamente más distribuida y estructura de rango negociable. Contraevidencia: competencia BTC/otros medios de pago, seguridad ligada a minería/valor de subsidio, cambios de dificultad, infraestructura y volatilidad. No se verificó una instantánea de hashrate/concentración minera o uso comercial; no se inventa una probabilidad de ataque. Esa limitación se acepta solo para un piloto de corta duración y riesgo bajo, no como certificación de seguridad.

La elección como primer candidato deriva de geometría/precio, simplicidad de tesis y tolerancia de costos. No se atribuye superioridad económica universal a su menor dilución.

## 5. Macro y riesgo de eventos

FRED se usa como contexto del corte, no como filtro histórico con datos revisados.

| Serie primaria | Fecha observada | Valor | Lectura limitada |
| --- | --- | --- | --- |
| [DFF](https://fred.stlouisfed.org/series/DFF) | 22-10-2026 | 3.88% | No es rendimiento de cash Kraken |
| [DGS10](https://fred.stlouisfed.org/series/DGS10) | 22-10-2026 | 4.96% | Tasa nominal larga, no forecast cripto |
| [DTWEXBGS](https://fred.stlouisfed.org/series/DTWEXBGS) | 16-10-2026 | 121.4048 | +3.4921 puntos frente a 08-09; rezago |
| [VIXCLS](https://fred.stlouisfed.org/series/VIXCLS) | 22-10-2026 | 19.03 | +3.19 puntos frente a 11-09; renta variable |

BTC diario de contexto: cierre 80048.5, EMA 5080763.221915, EMA 20076268.219586, RSI 41.65. No amplía el universo ni se añade retrospectivamente al backtest como filtro.

Dólar más firme en esa comparación y tasas elevadas aconsejan reducir exposición, sin causalidad o dirección futura demostrada. [Calendario Fed](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm), actualizado07-10-2026 y consultado26-10 UTC: FOMC 27–28 de octubre. Mantengo el overlay propuesto de no iniciar nuevas posiciones esos dos días UTC; primera reconsideración29-10 tras comunicado publicado y mercado estable. No se inventa hora de decisión ni se atribuye al backtest este overlay. ATOM añade riesgo de upgrade condicionado a votación, coincidente con esa ventana.

## 6. Estadística descriptiva y dependencia

Retornos simples; volatilidad diaria anualizada con raíz365.25, VaR95=percentil5 de pérdida, CVaR95=media de cola inferior. Son históricos, no pérdidas máximas futuras. MDD siguiente es del subyacente100% invertido, no cuenta piloto.

| Activo | N | Vol.anual | VaR95 diario | CVaR95 diario | MDD subyacente | Peor día | Exceso curtosis | Autocorr.1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARB | 719 | 106.92% | 7.93% | 11.30% | -93.81% | -28.87% | 5.64 | 0.025 |
| ASTER | 370 | 83.54% | 6.86% | 10.47% | -66.24% | -25.56% | 9.21 | -0.233 |
| ATOM | 719 | 79.62% | 5.95% | 9.16% | -88.26% | -23.18% | 3.76 | 0.031 |
| AVAX | 719 | 87.29% | 6.71% | 10.22% | -89.11% | -26.96% | 3.82 | 0.033 |
| BCH | 719 | 77.95% | 5.88% | 8.82% | -70.93% | -14.98% | 8.95 | -0.049 |

ASTER muestra autocorrelación negativa en su ventana y curtosis alta; no se convierte en una estrategia de reversión por sí sola. Las distintas fechas de comienzo afectan comparación. Pearson diario sobre 370 retornos comunes:

|  | ARB | ASTER | ATOM | AVAX | BCH |
| --- | --- | --- | --- | --- | --- |
| ARB | 1.000 | 0.447 | 0.555 | 0.608 | 0.466 |
| ASTER | 0.447 | 1.000 | 0.444 | 0.485 | 0.342 |
| ATOM | 0.555 | 0.444 | 1.000 | 0.576 | 0.426 |
| AVAX | 0.608 | 0.485 | 0.576 | 1.000 | 0.519 |
| BCH | 0.466 | 0.342 | 0.426 | 0.519 | 1.000 |

Spearman ARB/AVAX0.737 frente a Pearson0.608: la dependencia no desaparece al cambiar estimador. Frente a BTC, 719 retornos horarios alineados:

| Activo | Corr.BTC1h | BetaBTC1h | Horas sin volumen | Volumen24h Kraken estimadoUSD |
| --- | --- | --- | --- | --- |
| ARB | 0.684 | 2.278 | 0.00% | 1192969 |
| ASTER | 0.593 | 1.051 | 0.14% | 115770 |
| ATOM | 0.511 | 1.493 | 0.00% | 219459 |
| AVAX | 0.703 | 1.804 | 0.00% | 1223228 |
| BCH | 0.697 | 1.554 | 0.00% | 673325 |

El volumenUSD se estima con volumen base×precio típico de velas, no es notional auditado ni volumen global CoinGecko. No se concede descuento por diversificación: se suman riesgos de posiciones/órdenes. La búsqueda secuencial de activos también es selección: diez referencias T/R nuevas, veinte acumuladas entre tandas, además de P1 explorado antes y tres diseños piloto nuevos. No se presenta al candidato escogido como resultado de una única prueba independiente.

## 7. Evidencia histórica, sin veto universal OOS

Se conservó el mismo protocolo T/R antes de ver estos resultados. No se optimizaron parámetros. Los backtests diagnostican riesgo/coherencia; la falta de rentabilidad OOS no prohíbe un piloto. Una muestra de cero trades tampoco lo valida.

T: EMA 50d>EMA 200d, cierre>EMA 200d y ruptura del máximo de las20 velas anteriores, excluyendo señal. Entrada open siguiente, rechazo de gap>ATR 14. Stop=min(low10, entry−2ATR14), target 3R, salida posterior a cierre<EMA 50 o20 días.

R: RSI 14d<30 y cierre<Bollinger inferior20/2. Entrada siguiente, mismo gap; stop 2ATR, target 2.5R, salida posterior a cierre>=SMA 20 o10 días. La salida SMA 20 puede impedir alcanzar el target nominal; se conserva esa limitación y no se usa R como validación de los planes distintos de sección9.

Fee40 bps+slippage15 bps por lado, fills multiplicativos, riesgo 0.25% por entrada simulada, exposición activo 20%, RR nominal neto>=2. Stop primero si ambos niveles se tocan; gap de salida al open adverso, no reentrada misma vela, liquidación final con costos. Ventanas reinician cash y fuerzan cierre propio: resultados desarrollo+OOS pueden no sumar continuo. Simulaciones individuales; sin libros/minimos históricos ni MDL intradía y sin cartera combinada.

Warm-up200d, desarrollo400d para cuatro activos y51d para ASTER; holdout común120d del28-06 al25-10-2026, por fecha de aperturaUTC. ASTER inició datos20-10-2025; su desarrollo empieza08-05-2026. Los demás: 24-05-2025. El holdout se observó una vez con reglas fijas; no equivale a validación externa ciega.

| Activo/sistema | Ndev | Ret.dev | MDD dev | N OOS | Ret.OOS | MDD OOS | R medio OOS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ARB/T | 1 | -0.2500% | -0.2918% | 0 | 0.0000% | 0.0000% | n/a |
| ARB/R | 6 | -0.3879% | -0.5943% | 0 | 0.0000% | 0.0000% | n/a |
| ASTER/T | 0 | 0.0000% | 0.0000% | 0 | 0.0000% | 0.0000% | n/a |
| ASTER/R | 0 | 0.0000% | 0.0000% | 0 | 0.0000% | 0.0000% | n/a |
| ATOM/T | 0 | 0.0000% | 0.0000% | 0 | 0.0000% | 0.0000% | n/a |
| ATOM/R | 5 | 0.8354% | -0.2262% | 2 | -0.1707% | -0.4201% | -0.341 |
| AVAX/T | 1 | 0.0079% | -0.2306% | 0 | 0.0000% | 0.0000% | n/a |
| AVAX/R | 6 | -0.4355% | -0.6485% | 0 | 0.0000% | 0.0000% | n/a |
| BCH/T | 6 | -0.2113% | -0.6993% | 0 | 0.0000% | 0.0000% | n/a |
| BCH/R | 4 | -0.9963% | -1.1146% | 0 | 0.0000% | 0.0000% | n/a |

### Resultado continuo elegible tras warm-up

| Activo/sistema | Trades | Retorno | MDD | PF | R medio |
| --- | --- | --- | --- | --- | --- |
| ARB/T | 1 | -0.2500% | -0.2918% | 0.000 | -1.000 |
| ARB/R | 6 | -0.2266% | -0.5943% | 0.547 | -0.151 |
| ASTER/T | 0 | 0.0000% | 0.0000% | n/a | n/a |
| ASTER/R | 0 | 0.0000% | 0.0000% | n/a | n/a |
| ATOM/T | 0 | 0.0000% | 0.0000% | n/a | n/a |
| ATOM/R | 7 | 0.6633% | -0.4279% | 3.631 | 0.379 |
| AVAX/T | 1 | 0.0079% | -0.2306% | n/a | 0.031 |
| AVAX/R | 6 | -0.4355% | -0.6485% | 0.242 | -0.290 |
| BCH/T | 6 | -0.2113% | -0.6993% | 0.529 | -0.141 |
| BCH/R | 4 | -0.9963% | -1.1146% | 0.000 | -1.000 |

Solo ATOM-R opera en el holdout: dos trades, retorno−0.1707%; el continuo positivo depende del tramo anterior. Al doblar fee/slippage a 80/30 bps, ese holdout no admite entradas por filtro de RR: retorno0 con cero trades, no mejora rentable. Bootstrap de sus retornos, bloques 10, 2000 muestras, seed 42: p05−0.7664%, mediana−0.1274%, p95+0.2666%. No es probabilidad calibrada y la muestra es mínima. Las demás combinaciones no operan OOS; remuestrear ceros no aporta evidencia de ventaja.

Comparador20% buy/hold+80% cash, mismos costos, cada activo en cuenta independiente:

| Activo | Retorno OOS | MDD OOS | Retorno continuo elegible |
| --- | --- | --- | --- |
| ARB | 25.338% | -12.787% | -11.496% |
| ASTER | 2.312% | -3.245% | 0.932% |
| ATOM | 0.601% | -5.093% | -13.217% |
| AVAX | 7.469% | -7.331% | -12.333% |
| BCH | 8.247% | -7.021% | -7.075% |

ARB/AVAX/BCH rebasaron6% de MDD OOS incluso con 80% cash; ASTER/ATOM quedaron debajo en esa ventana, sin garantía futura. No se descartan pilotos pequeños por ello ni se confunde buy/hold con el sistema propuesto.

### Diagnóstico específico de las tres nuevas reglas

Los diseños se construyeron después de ver estructura de mercado y fundamentos: **no están preregistrados antes de ver esos datos, ni tienen validación independiente**. Se realizó además un diagnóstico causal corto con sus propias reglas de entrada/stop/target, sin atribuirles T/R.

Se alinearon velas1h con datos4h/diarios solo desde su cierre, mediante as-of hacia atrás; no usar high/low diarios antes de que cierre el día. Calentamiento200h, 520h evaluadas (04-10 a 19:00 hasta 26-10 a 10:00 UTC). Señal: cierre 1h dentro de zona, positivo respecto al open y por encima del centro high-low, low>stop. Intento único a apertura siguiente, solo dentro de zona y bajo techo de entrada, RR neto>=2 y una entrada/día. Stop/target/time-out fijos; doble toque adverso; riesgo 0.05% y exposición20% de capital hipotético. Costos40/15 bps y sensibilidad80/30.

Resultado: AVAX dos señales, ambas rechazadas históricamente por RR; ASTER/BCH ninguna. Cero fills en las tres y en doble costo, retorno0: **ausencia de validación, no éxito ni motivo automático de rechazo del futuro piloto**. El simulador no presupone fill posterior dentro de vela si el open no cumple, ni profundidad histórica. Esto es un diagnóstico acotado, no prueba de ejecución real completa. Controles de disponibilidad temporal, prefijos sin futuro, gaps, stop primero, costos, precio máximo y contabilidad pasaron.

## 8. Liquidez observada

Profundidad=asks hasta 10 bps del mejor ask; participación máxima1%. Todos pasaron spread<=20 bps y mínimo en ambos snapshots. Esto no demuestra capacidad permanente.

| Activo | Hora inicial UTC | Bid/ask | Spread bps | Prof.10 bps USD | Tope1% USD |
| --- | --- | --- | --- | --- | --- |
| ARB | 11:50:41 | 0.1708 / 0.171 | 11.70 | 8551.36 | 85.51 |
| ASTER | 11:50:51 | 0.70998 / 0.71028 | 4.22 | 4920.27 | 49.20 |
| ATOM | 11:50:58 | 1.6441 / 1.6461 | 12.16 | 12272.60 | 122.73 |
| AVAX | 11:51:06 | 8.951 / 8.954 | 3.35 | 74269.82 | 742.70 |
| BCH | 11:51:14 | 279.12 / 279.29 | 6.09 | 18587.02 | 185.87 |

| Activo | Hora contrasteUTC | Bid/ask | Spread bps | Tope1% USD |
| --- | --- | --- | --- | --- |
| ARB | 11:54:30 | 0.1714 / 0.1715 | 5.83 | 71.94 |
| ASTER | 11:54:31 | 0.71087 / 0.71114 | 3.80 | 222.86 |
| ATOM | 11:54:32 | 1.652 / 1.6542 | 13.31 | 79.74 |
| AVAX | 11:54:33 | 8.969 / 8.972 | 3.34 | 672.28 |
| BCH | 11:54:34 | 279.88 / 280.01 | 4.64 | 299.69 |

La capacidad ASTER cambiaUSD49.20→222.86; para ejemplos se usa el menor de ambas. No se traslada volumen global a Kraken. Un precio límite protege precio de compra pero puede no llenar; [stop loss Kraken](https://support.kraken.com/articles/7699391647892-stop-loss-orders) se activa a mercado y no garantiza precio. No dividir órdenes para eludir participación o reintentar hasta agotar profundidad.

## 9. Planes de piloto: condiciones precisas

**Propuestas de diseño condicional, no órdenes listas para ejecutar.** Spot long-only, sin staking ni apalancamiento. Los precios son referencias congeladas de este estudio; se reemplazan por una propuesta nueva si cambian datos o tesis. Prioridad BCH→AVAX→ASTER es juicio de costos/ejecución y congruencia, no una probabilidad estimada de ganar.

| Prioridad | Activo | Zona de entrada USD | Stop USD | Target USD | RR neto al techo | RR con doble costo | Tiempo máximo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | BCH | 267.27–268.85 | 262.29 | 300.45 | 3.003 | 2.043 | 7 días |
| 2 | AVAX | 8.666–8.704 | 8.504 | 9.481 | 2.298 | 1.482 | 5 días |
| 3 | ASTER | 0.68338–0.68422 | 0.67512 | 0.72687 | 2.105 | 1.128 | 3 días |

### Construcción sin mover el stop para conseguir tamaño

**BCH:** extremo inferior = mínimo 20 barras 4h267.27; techo = soporte+0.5ATR1h, redondeado268.85. Stop = mínimo 10 diarias 263.76−0.25ATR4h, redondeado262.29: pérdida de base reciente invalida el rebote. Target = Bollinger superior diaria300.45, antes deEMA200d304.40. Es recorrido de rango diario, no objetivo inmediato a media20. Barreras282/288 pueden frustrarlo; no se asume que desaparezcan. Sin parciales o cierre automático por tocarlas, para no vender RR de un objetivo que se abandonaría por regla antes. Tiempo máximo 7d; el time-out puede dar resultado menor al RR nominal.

**AVAX:** soporte = mínimo 20 barras 4h8.666; techo = soporte+0.5ATR1h→8.704. Stop = soporte−ATR 4h→8.504, dejando un buffer de volatilidad bajo mínimo reciente. Target = EMA 50 diaria9.481. EMA 200d≈9.1215 y zona 9.30 son barreras intermedias; se acepta el riesgo de no recuperarlas. La tesis es reversión parcial de la corrección, no tendencia4h alcista confirmada. Máximo5d. Con costos duplicados RR baja a 1.48; por tanto precio/costos efectivos requieren verificación estricta antes de aprobar.

**ASTER:** soporte = mínimo 20 barras 4h0.68338; techo = soporte+0.25ATR1h→0.68422. Stop = mínimo 10 diarias 0.67924−0.5ATR4h→0.67512. Target = Bollinger superior diaria0.72687, rango lateral observado. EMA 20/4h y0.71323 obstaculizan antes; no se ocultan ni se cambia target para maquillar un trade con salida temprana. Máximo3d. RR2.105 deja poco margen; doble costo lo baja a 1.13. Menor tamaño, o cancelar si el costo real supera el supuesto. La tesis de recompra no obliga a mantener si el rango rompe.

Las fórmulas vinculan horizonte con soporte/volatilidad/objetivo; se diseñaron una vez, sin búsqueda de parámetros que produzca un backtest positivo. No prueban que ese objetivo sea probable. El presupuesto se calcula después del stop.

### Activación, ejecución e invalidación

1. Para estos tres planes, no activar antes del29-10-2026 00:00 UTC y nunca durante27–28octUTC. Confirmar comunicado Fed publicado; ATOM no participa en esta primera selección. No colocar hoy órdenes que queden expuestas a llenarse en el periodo excluido.
2. Tras llegar a zona, esperar una1h cerrada dentro de ella, con cierre>open y cierre>(high+low)/2, low>stop. Es una señal sencilla de rechazo, no una garantía ni otra confirmación independiente.
3. Recolectar mercado/cuenta nuevos; a inicio de la hora siguiente, entrada límite negociable con precio<=techo y dentro de zona. Si abre bajo zona/stop, encima del techo o no permite fill inmediato aceptable, cancelar intento; no asumir fill intrabar posterior ni perseguir. Cancelar remanente sin llenar. El fill parcial consume su riesgo real; no duplicar la orden para completar presupuesto.
4. Antes de enviar, dos revisiones reales de la misma propuesta/hash y gate vigente. Max desviación de entry respecto a quote1%, mercado120s/cuenta300s y otros vencimientos siguen aplicando. Los planes de research están hoy a más de 1% del ask: **no pasarían el gate con este snapshot y no deben enviarse ahora**.
5. Stop protector por cantidad realmente llenada y target fijos. Salir por stop, target o tiempo máximo; sin ampliar stop, promediar pérdidas, trailing o parciales no modelados. Registrar gap y precio real. Supervisión humana; sin ella no iniciar.
6. Si antes de activar se toca stop, cierra4h bajo el soporte o aparece incidente material, cancelar ese diseño. Si nuevos datos alteran nivel/tesis, crear versión y revisar de nuevo; no mover referencias silenciosamente para conseguir fill.

Los niveles son válidos como hipótesis para observación hasta 02-11-2026 00:00 UTC como máximo. Cada cierre diario y, antes de operar, todo cambio material exige actualización; no son una orden vigente por una semana. El primer checkpoint sugerido es29-10 00:00 UTC, sujeto a comunicado/estabilidad. No hay tarea de monitorización automática programada.

No se requiere un número fijo de días en papel antes de un piloto. Sí se requiere que la oportunidad de precio ocurra y el presupuesto exista. Si no llega a zona, el resultado del plan es no fill, no una obligación de elegir otra entrada.

## 10. Riesgo, tamaño y costos

Mantener máximos del mandato MDL 3%/MDD 6%, operativos 2%/4%, reserva 20% del MDL operativo, máximo por trade 0.25%, riesgo adicional conjunto 0.50%, exposición bruta 50% y activo 20%. USD continúa provisional. MDD se mide contra mayor de capital inicial y peak reconciliado; pisos no se bajan tras pérdidas. MDL incorpora toda la cuenta, posiciones/órdenes, PnL no realizado y flujos. La brecha diaria queda bloqueada aunque luego se recupere.

Para esta primera tanda experimental: **hasta 0.05% por trade, un piloto simultáneo, una entrada/díaUTC**, pausa de pérdida diaria0.15% y presupuesto acumulado0.50% de base inicial reconciliada. Fin al primero de 20 trades, 30d desde primera entrada, presupuesto o invalidación. Revisión intermedia a 5 trades/5R netos perdidos. Son restricciones humanas propuestas y adicionales, no contadores nuevos implementados en el Lab. Las ganancias no autorizan escalado automático ni recarga para recuperar.

Los límites globales incluyen posiciones fuera del piloto; el menor presupuesto disponible manda. Pérdidas del piloto incluyen costos y PnL realizado/no realizado ajustado por flujos. No se borran diario/lockouts. Gaps pueden rebasar riesgo estimado: un stop no garantiza MDL/MDD.

Con C=(fee+slippage)/10000=0.0055 por lado:

```text
riesgo_unitario=E-S+(E+S)*C
beneficio_target=T-E-(T+E)*C
RR_neto_target=beneficio_target/riesgo_unitario
q<=min(presupuesto_disponible/riesgo_unitario,
       espacio_exposicion/E,cash_disponible/[E*(1+C)],
       profundidad_ask_10bps*0.01/E)
```

La expresión es aproximación conservadora de primer orden; los simuladores usan fills/costos multiplicativos. Cantidad hacia abajo a precisión, mínimos de cantidad/notional y tick. Sizing no modifica stop ni toma crédito por correlación. Confirmar tier y sumar costos reales antes de enviar.

### Ejemplo público: cuenta hipotética 10000 USD y riesgo máximo 5

No describe el saldo del propietario. Se usa el menor tope de profundidad de dos libros y techo de entrada de cada plan, no una liquidez garantizada al precio futuro.

| Activo | Cantidad ilustrativa | Notional USD | Riesgo estimado USD | % equity hipotético | Tope notional por libro USD |
| --- | --- | --- | --- | --- | --- |
| BCH | 0.52735551 | 141.78 | 5.000 | 0.0500% | 185.87 |
| AVAX | 16.96963114 | 147.70 | 5.000 | 0.0500% | 672.28 |
| ASTER | 71.91059000 | 49.20 | 1.192 | 0.0119% | 49.20 |

ASTER consume menos presupuesto por liquidez, no se aumenta cantidad para gastar los5. No sumar filas ni aplicar cantidades a otra cuenta. En la referencia nominal del usuario el techo0.05% sería25 unidades de cuenta, pero tamaño real exige moneda, estado y liquidez de ejecución. Ninguna fila es un sizing aprobado.

Los targets son objetivos nominales netos de costos supuestos, no expectativa estadística ni porcentaje de acierto. Los time-outs/gaps pueden producir resultados distintos. BCH conserva RR>=2 incluso duplicando costos, lo que apoya su prioridad relativa; no demuestra una ventaja ni permite usar fees sin verificar.

## 11. Matriz de faltantes y cierre

| Severidad | Faltante | Impacto / mitigación | Aceptación propia de Codex |
|---|---|---|---|
| Crítico para ejecución | Moneda, fees efectivos y cuenta completa reconciliada, baseline/peak/flujos | No calcular presupuesto real o aprobar; confirmar snapshot al preparar propuesta | No aceptado para ejecutar; no bloquea diseñar |
| Crítico para ejecución | Revisión real Claude y propuesta/inputs vigentes | No hay consenso; no atribuir firmas o READY | No aceptado para ejecutar |
| Crítico si ocurre | Precio fuera de zona, RR<2 con costo real, mínimo/profundidad o spread inválidos | Cancelar entrada concreta; no relajar límites | No aceptado |
| Material | Ventaja no demostrada, escasa evidencia y cero fills del diagnóstico corto | Riesgo experimental pequeño, reglas fijas, registro prospectivo, presupuesto finito | Aceptado para considerar estos tres diseños; Claude debe decidir por sí mismo |
| Material | Barreras intermedias y probabilidad de target desconocida | Stops/tiempos definidos; sin vender nominalRR como expectativa; no ampliar exposición | Aceptado para diseño piloto, no promesa de retorno |
| Material ASTER | Emisiones/cliff y recompras no auditados completamente; inconsistencias de texto | No event trade basado en fecha exacta; tamaño muy reducido y revisión de novedades | Aceptado solo para piloto corto condicionado |
| Material ATOM | Upgrade/resultado gobernanza y continuidad | Posponer, comprobar fuente primaria y red estable después del evento | No aceptado para activar ATOM ahora |
| Material BCH | Hashrate/concentración y demanda comercial actuales incompletos | No tesis de seguridad garantizada; piloto breve y bajo riesgo | Aceptado con esa limitación |
| Material | Sin libros históricos, fills parciales o MDL intrabar validados | No inferir capacidad histórica; medir costos/fills reales, control humano | Aceptado para investigación; no garantía de ejecución |
| Menor para este corte | Developer_data nulo, sentimiento/API opcional ausentes | No inventar métricas; nuevas keys no cambiarían estructura o capacidad | Aceptado; no paraliza |

La aceptación pertenece a Codex y a este alcance, no a Claude. Un crítico no se resuelve escribiendo accepted=true. No se pide otra vez capital o máximos ya conocidos.

**Punto de cierre:** universo/contratos, 15 series, fundamentos/tokenomics, eventos, costo/liquidez, dos referencias históricas y diagnóstico específico cubren los impulsores de esta decisión. La ronda de contradicciones separó fees/ingresos Aster, emisión/FDV de los tokens, upgrade ATOM y barreras antes de targets. Más APIs de sentimiento o un histórico perfecto no permitirían comprar fuera de zona ni asegurarían rentabilidad. Se cierran tres planes condicionados y dos decisiones de espera; se reabre por trigger y evidencia material, sin investigación indefinida.

## 12. Revisión independiente de Codex

Sesión Codex autora y revisora de este expediente, independiente respecto de Claude; no auditoría externa. La versión exacta del modelo no está expuesta y no se inventa.

**Veredicto de research:** favorable a considerar un piloto condicionado BCH, seguido de AVAX y ASTER, con ventaja estadística no demostrada y riesgo muy pequeño. ARB en observación; ATOM pospuesto por evento/técnico. Rechazo compra inmediata al snapshot: precio fuera de zona, inputs que vencerán y cuenta/segunda revisión pendientes. Esto no es un veto por falta de OOS positivo.

Acepto expresamente incertidumbre residual y coherencia de estas tres hipótesis de rebote/rango bajo sus horizontes; no apruebo una orden ni completo un Review JSON de una propuesta todavía inexistente. Sus targets tienen barreras intermedias y su rentabilidad es desconocida. R sigue limitado por salida temprana; no se le atribuye validación de estos planes nuevos. Cambiar entry/stop/target/dataset/cuenta/política requiere hash y revisiones nuevas.

Comprobé identidades, moneda/estado de par, velas cerradas y alineación causal, datos no sintéticos, reglas de precio y límites, ticks/mínimos y RR con costos, riesgo agregado sin diversificación, ausencia de órdenes/firma Claude inventadas, contraevidencia y fuentes primarias. Los argumentos técnicos correlacionados no se multiplican como votos. Los resultados adversos se conservan sin optimizar para hacerlos positivos.

El gate no se invoca con cuenta ficticia o firma fabricada para producir un estado decorativo. Cuando se forme señal se creará Proposal bajo schemas, revisión real de cada IA y `risk-check/decide`; el Lab presentará el resumen sobre esa propuesta. Este documento entrega la investigación y planes concretos que permiten llegar a ese paso.

## 13. Procedencia y reproducción

Worktree, venv, cachés y bases locales de Codex separados. No se tocaron resultados de Claude ni se llamó API de modelos o endpoint de órdenes. El Lab base no cambió para producir candidatos. Las fuentes públicas usan timeout25s, throttling, retry máximo 3 y procedencia; faltantes se registran. Secretos solo leídos del .env original en el proceso necesario, sin copiarlos al estudio.

Commit base Lab: `a2c4f006983a4ae15bbc35d07e38f8e55e6c160f`. SHA256 Excel: `b1d475c71ad6de7c33f534a5bb854227851ecbfdb36a393b130c8d0a351b211c`. Protocolo T/R previo al snapshot: `409232dc4e4109f3010a11d426117e890180235e34658dc003649e33934f9f62`. Recopilación: `2026-10-26T11:50:36.900715+00:00`–`2026-10-26T11:51:25.239471+00:00`.

| Dataset real | SHA256 canónico Lab | SHA256 bytes JSON local |
| --- | --- | --- |
| ARB | 9b4aa76f94a8c4ad6f06963da5d7f221d8eaa0510534361b412fa67f194a4316 | 63c1d1fc06d6cb57abc24e7a0f1f699f911bbb2ae3ea512284677b4c1fb5a965 |
| ASTER | 1287dde17e0d585fa27664e3c108cab9ae92fa82616dcdd7c95bf6d3e18dc97b | f7af8727324d01bee100b8bf48ef86bd06034ff1f829cee7f5caa37a153bdc44 |
| ATOM | eb06c923006e3cc20448f581cd39b0133f5389bb9e12b300035e8e3017ada7cd | 473ce2bafd02e7c6e729a78e00d441a67be3f51433bd6439a2e617f1d3b2a9f7 |
| AVAX | 4d2a99ddeb7dc37a6349d751e9e26069563c1316f63a0c23401909f91019d2ce | 4e41b2ae7e611e00d0b4a63e53ea62ed637936c6bf6b208fe6f926972d913505 |
| BCH | d812b5b2aea76c031b6f7207cc173ff2dc4c6954a32e265279d54c3991633f70 | 44e41e1a049e283b888f8c652571e6e15a282d7e04e4db633a6e589bcc579c28 |

| Artefacto local no publicado | SHA256 bytes |
| --- | --- |
| private/backtest_second_five.py | 3c5c920093a6dd4a8593c719ad21133fa1373a8efb6a1fe1fd3fedbdcc8be5d9 |
| private/plan_second_five.py | 01a5117088b7d6ed8e767050821f81531233804da78a662e1ac38a469707a4b6 |
| private/diagnostic_second_five.py | 446a03a3053d611152dc4f6b414f51d1849ca3ccd0a3dd025710041be03249ad |
| outputs/second-five-20261026/strategy-study.json | d5628b46670364e72c6d8783211159a7430cc0a8df865ebc66fdebc4315ab964 |
| outputs/second-five-20261026/conditional-plans.json | 1a39145e6ea19c3b8898486990774dfd4f106f73f0a8b03a8778432bc85d1892 |
| outputs/second-five-20261026/pilot-specific-diagnostic.json | 9d4dc3054e4c5d8e035bca52f175e7dcef9a72f9118f936b8d0ad15e81966603 |

El hash canónico y el de bytes difieren por serialización, no contenido económico. Dossiers usan el canónico. Procedencia conserva URL/parámetros sin claves, fetched_at original y body_sha256; la caché no rejuvenece datos. La repetición del script de límites regeneró el mismo diagnóstico, sin selección de parámetros.

Reproducción metodológica: commit base, requirements-lock y paquete editable; identificadores de sección2, collect enriquecido y analyze para60/240/1440; reglas T/R sección7 y reglas nuevas sección9. Diagnóstico piloto merge-asof solo tras cierres, warm-up200h. Los scripts/snapshots originales se conservan localmente; GitHub por sí solo no reproduce bytes exactos ni contiene el simulador específico. Los hashes no reconstruyen un payload perdido; una nueva consulta genera otra ventana/hash.

La primera ejecución de tests encontró cinco fallos por la ruta de keylog SSL inyectada por el entorno. Se repitió sin esa variable, conservando verificación TLS y sin cambiar el código del Lab. Verificación de esta tanda: 70 pruebas del Lab y ruff aprobados; checks del simulador T/R, alineación multi-timeframe y prefijos sin fuga, pruebas específicas de entrada siguiente, doble toque, gap, techo de precio, costos y riesgo; cinco hashes/15 series y cálculos de planes revisados. Esto comprueba implementación, no ventaja o cumplimiento continuo MDL. No hay código fuente nuevo publicado en esta entrega.

## 14. Fuentes consultadas y límites

Páginas consultadas el **26-10-2026 UTC**. Hora individual de web no archivada; sí fecha UTC. Endpoints conservan hora exacta en su procedencia. s/f indica documentación viva sin publicación estable. Los snippets antiguos que discrepan con una página viva no se usan como estado actual.

| Fuente enlazada en el texto | Publicación / dato | Afirmación / uso | Limitación |
|---|---|---|---|
| Kraken AssetPairs/OHLC/Depth | Sesión11:50–11:54 UTC | Pares, velas, libros y restricciones | No jurisdicción privada o libro futuro |
| Kraken ASTER listado | 20-10-2025 | Inicio de histórico del venue | No capacidad actual |
| CoinGecko registro/markets/detalle | last_updated propio del snapshot | Identidad, oferta, MCAP/FDV | Agregado, convenciones distintas |
| Arbitrum token/oferta | s/f; tabla oferta de 2024 | Gobernanza, emisión, vesting | Tabla vieja no es saldo actual |
| Arbitrum H1 reporte | 02-09-2026 | Ingresos DAO/tesorería de H1 | Emisor, no dividendo holder |
| Aster overview/tokenomics | Documentación viva, s/f | Contrato y reglas declaradas de recompras/emisión | No auditoría de ejecución; texto cliff ambiguo |
| DefiLlama Aster/protocolo/fees | Sesión actual | TVL y fees perps | Revenue no disponible; no beneficio neto |
| DefiLlama Arbitrum/Avalanche | Último día26-10-2026 00 UTC | TVL y cambio30d | Precio/flujo no separados |
| Cosmos fase1/weekly18 | 10-07/01-10-2026 | Investigación de reforma | Propuestas, no cambio aprobado universal |
| Cosmos respuesta Neutron | 25-09, edición29-09-2026 | Ataque externo y pausa/recuperación Hub | No afirma explotación Hub o pérdidas Kraken |
| Cosmos upgradev29 | 20-10, actualización23-10-2026 | Voto27-10/estimación28-10 si aprobado | Horario dependiente de bloques |
| Avalanche token/Helicon | s/f; activación22-09-2026 | Emisión/quema/cambios de parámetros | No prueba retorno o deflación neta |
| BCH sitio/BCHNspec | s/f / versión09-01-2026 | Utilidad/consenso y scripting | No mide adopción/hashrate actuales |
| FRED cuatro series | 16/22-10-2026 | Contexto macro | Rezago/revisiones, no backtest causal macro |
| Fed calendario | Actualizado07-10-2026 | FOMC 27–28octubre | No dirección futura ni hora de comunicado aquí |
| Kraken stop loss | s/f | Mecánica de salida | No precio o pérdida garantizados |

Las fuentes primarias sustentan hechos declarados, no probabilidades de rentabilidad. El análisis y sus contraargumentos explican por qué cada hipótesis es aceptable para considerar un piloto, no por qué sería cierta con seguridad.
