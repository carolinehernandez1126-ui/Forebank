# Estudio final de trading: AAVE, ADA, AIXBT, ALGO y APT

**Autor y revisor: Codex. Sesión iniciada el 25-10-2026, America/Bogota.** Datos reales Kraken, `synthetic=false`. Investigación independiente respecto de Claude: no se consultó su estudio ni se atribuye su aprobación. Versión pública saneada: porcentajes y capital hipotético; sin cuenta, credenciales, saldos, cachés ni conversaciones.

## 1. Decisión

**NO TRADE en los cinco activos en el corte analizado. Riesgo nuevo recomendado: 0%.** Ambas estrategias diarias están inactivas; la evidencia empírica es insuficiente y AIXBT falla liquidez. Esta decisión se sostiene aunque se reconcilie la cuenta. Mantener disponible el efectivo destinado a estas nuevas compras; no se presume una cuenta íntegramente en cash ni se instruyen ventas de posiciones existentes.

AAVE queda primero para seguimiento, ALGO segundo; ADA y APT requieren reconstruir tendencia; AIXBT se excluye de ejecución bajo la liquidez observada. Es prioridad de investigación, no ranking de retornos esperados. T y R quedan documentados para observación en papel; se rechaza su despliegue real actual.

Alcance: Kraken Pro, capital propio, spot long-only, sin apalancamiento y ejecución humana. BTC es solo referencia contextual, no un sexto activo seleccionado. No se modelan staking, préstamos, cortos o derivados. Los precios usan punto decimal y USD como moneda del par, sin confirmar moneda de cuenta. Las cotizaciones publicadas son históricas, no órdenes vigentes.

**Cierre de investigación UTC:** `2026-10-26T05:05:04.271243+00:00`. Mercado congelado: 26-10-2026 04: 47: 22–04: 47: 48 UTC; contraste adicional del libro: 04: 53: 41–04: 53: 46 UTC. No existe aprobación ejecutable. [Conclusiones y hash](CONCLUSIONES.md).

## 2. Universo e identidad

Selección literal de primeras cinco filas no vacías: `archivos_de_apoyo/lista_activos.xlsx`, hoja **Lista de activos**, rango **A2: A6**. Kraken AssetPairs confirmó base, quoteUSD, estado online, tick y mínimos. CoinGecko se resolvió por identidad y contratos, no solo ticker.

| Orden | Activo | Par Kraken | ID CoinGecko | Identidad | Tick / mínimo unidades |
| --- | --- | --- | --- | --- | --- |
| 1 | AAVE | AAVEUSD | aave | ERC20 Ethereum | 0.01 / 0.03 |
| 2 | ADA | ADAUSD | cardano | Nativa Cardano | 0.000001 / 20 |
| 3 | AIXBT | AIXBTUSD | aixbt | Token Base | 0.00001 / 200 |
| 4 | ALGO | ALGOUSD | algorand | Nativa Algorand | 0.00001 / 41 |
| 5 | APT | APTUSD | aptos | 0x1:: aptos_coin:: AptosCoin | 0.0001 / 6 |

AAVE Ethereum:`0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9`. AIXBT Base:`0x4F9Fd6Be4a90f2620860d680c0d4d5Fb53d1A825`, contrastado con [contratos oficiales](https://docs.aixbt.tech/resources/tokenomics). El ID antiguo `aixbt-by-virtuals` devolvió404; el registro actual identifica `aixbt`. Se excluyeron homónimos y variantes Binance-Peg. El par CEX no implica compatibilidad de depósitos en todas las redes; no se hicieron transferencias.

Cada activo: 720 velas 1h, 720 velas 4h, 720 diarias, salvo AIXBT: 612 diarias desde21-02-2025. Los demás comienzan05-11-2024. Última diaria: apertura25-10-2026 00: 00 y cierre26-10 00: 00 UTC; última1h: apertura03: 00 y cierre04: 00 UTC; última4h: apertura00: 00 y cierre04: 00 UTC. Las15 series aprobaron continuidad, orden, duplicados, antigüedad y longitud del Lab. No se rellenaron huecos ni se usaron otras bolsas.

[OHLC Kraken](https://docs.kraken.com/api-reference/market-data/get-ohlc-data) limita la ventana a unas720 entradas y entrega una vela final mutable, que se excluyó. La ausencia de huecos no garantiza transacciones efectivas: AIXBT tiene horas con volumen cero. Su inicio concuerda con el [listado oficial del21-02-2025](https://blog.kraken.com/product/asset-listings/aixbt-odos-and-toshi-are-available-for-trading). La ventana no representa todos los ciclos.

## 3. Macro y eventos

FRED se usa como contexto actual, nunca como filtro retrospectivo con datos revisados:

| Serie | Fecha observada | Valor | Limitación |
| --- | --- | --- | --- |
| [DFF](https://fred.stlouisfed.org/series/DFF) | 22-10-2026 | 3.88% | No rendimiento disponible de cash |
| [DGS10](https://fred.stlouisfed.org/series/DGS10) | 22-10-2026 | 4.96% | Tipo nominal, no predicción cripto |
| [DTWEXBGS](https://fred.stlouisfed.org/series/DTWEXBGS) | 16-10-2026 | 121.4048 | +3.4921 puntos frente a 08-09; dato rezagado |
| [VIXCLS](https://fred.stlouisfed.org/series/VIXCLS) | 22-10-2026 | 19.03 | +3.19 puntos frente a 11-09; mide renta variable |

Interpretación: dólar más firme en esa comparación y sensibilidad a tasas aconsejan cautela; no prueban causalidad ni predicen caída. BTC diario cerró80048.5, bajo EMA 50 80763.22 y sobre EMA 200 76268.22, RSI 41.65: corrección dentro de estructura mayor mixta. No se añadió este filtro al backtest después de ver resultados.

La [Reserva Federal](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm) agenda FOMC **27–28 de octubre de 2026**. Overlay prospectivo propuesto: no abrir nuevas posiciones esos dos días UTC; reconsiderar desde el primer cierre diario posterior al28, una vez publicado y leído el comunicado y normalizada la liquidez. El calendario no fija aquí una hora. No forma parte del backtest ni supone ventas automáticas.

## 4. Técnico multihorizonte

Se calcularon SMA/EMA 20/50/200, RSI 14, MACD12/26/9, ATR 14, ADX 14, Bollinger 20/2, Donchian 20, OBV, VWAP20 móvil, VWAP de sesión UTC y z-score de volumen 20. Se agrupan en tendencia, momentum, volatilidad y participación; no son votos independientes. ADX mide fuerza, no dirección. RSI bajo no basta para comprar. VWAP de una vela diaria no proporciona estructura intradía; OBV absoluto no se compara entre tokens.

### Diario

| Activo | Cierre | EMA 20 | EMA 50 | EMA 200 | RSI 14 | ATR/cierre | ADX 14 | Hist.MACD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AAVE | 136.19 | 152.078612 | 147.195277 | 126.279284 | 35.50 | 7.14% | 21.07 | -3.390404 |
| ADA | 0.204022 | 0.224523 | 0.225424 | 0.238323 | 34.87 | 6.81% | 23.17 | -0.003406 |
| AIXBT | 0.01815 | 0.01975 | 0.020443 | 0.024986 | 36.22 | 6.35% | 28.90 | -0.00011 |
| ALGO | 0.10481 | 0.112347 | 0.109799 | 0.105447 | 40.21 | 7.90% | 27.15 | -0.001933 |
| APT | 0.7017 | 0.778611 | 0.750481 | 0.894189 | 40.95 | 11.92% | 27.46 | -0.017681 |

### Contexto táctico4h y1h; no sustituye reglas diarias

| Activo | Cierre4h/1h | EMA 20_4h | EMA 50_4h | EMA 200_4h | RSI 4h/1h | EMA 50_1h | VWAP20_4h | Zvol4h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AAVE | 134.16 | 140.382738 | 146.367911 | 151.905464 | 28.39 / 35.23 | 138.326286 | 139.972872 | 0.19 |
| ADA | 0.201474 | 0.208614 | 0.215321 | 0.227594 | 29.77 / 34.05 | 0.206566 | 0.208306 | -0.39 |
| AIXBT | 0.01813 | 0.018725 | 0.01908 | 0.020277 | 34.90 / 39.64 | 0.018602 | 0.018509 | -0.62 |
| ALGO | 0.10325 | 0.105478 | 0.108578 | 0.112136 | 38.98 / 41.86 | 0.104698 | 0.104953 | 1.09 |
| APT | 0.6899 | 0.724609 | 0.757658 | 0.769952 | 30.86 / 37.14 | 0.712811 | 0.722775 | 0.02 |

### Desempeño del subyacente y rangos diarios

| Activo | 7d | 30d | 90d | Bollinger inferior | Mínimo / máximo20d |
| --- | --- | --- | --- | --- | --- |
| AAVE | -10.38% | -11.36% | 39.15% | 134.28737 | 133.83 / 187.61 |
| ADA | -7.69% | -21.15% | 31.21% | 0.196854 | 0.200301 / 0.282499 |
| AIXBT | -1.63% | -25.28% | 6.64% | 0.017523 | 0.01788 / 0.02328 |
| ALGO | -5.56% | -9.94% | 31.01% | 0.102588 | 0.10082 / 0.1443 |
| APT | -10.65% | -19.52% | 18.53% | 0.696362 | 0.6875 / 1.1 |

**AAVE. Observación:** EMA 50d>EMA 200d y cierre>EMA 200d, pero cierre bajo EMA 20/50; en 4h/1h domina caída, RSI 4h28.39. **Hipótesis:** recuperación si regresa demanda. **Contraevidencia:** MACD diario negativo y bajo VWAP20d; soporte133.83/133.32 no garantiza suelo. **Conclusión:** esperar; no comprar sobreventa4h con una regla validada en diario.

**ADA. Observación:** bajo EMA 20/50/200d, -21.15% a 30d. **Hipótesis:** rebote técnico posible. **Contraevidencia:** EMA 50d<EMA 200d y debilidad táctica. **Conclusión:** descartar compra inmediata; liquidez no cambia régimen.

**AIXBT. Observación:** debajo de medias diarias, -25.28% a 30d, negociación discontinua. **Hipótesis:** noticias pueden provocar saltos. **Contraevidencia:** saltos no equivalen a fills replicables; spread excesivo y poca profundidad. **Conclusión:** excluir ejecución; señales menos confiables por precios poco negociados.

**ALGO. Observación:** EMA 50d>EMA 200d, pero cierre algo bajo EMA 200d; histograma MACD4h positivo sugiere desaceleración bajista. **Contraevidencia:** medias tácticas y momentum diario débiles. Se conserva esta evidencia mixta. **Conclusión:** segunda prioridad para observar; mejora aislada no habilita compra.

**APT. Observación:** bajo tres medias diarias y ATR/cierre11.92%. **Hipótesis:** alivio de oferta podría apoyar medio plazo. **Contraevidencia:** alta volatilidad, beta y profundidad variable. **Conclusión:** no anticipar suelo por tokenomics.

## 5. Fundamentos y valoración

CoinGecko aporta agregados multivenue, no precio ejecutable Kraken ni estados auditados. TVL es capital medido en protocolos, sensible a precio/metodología; no equivale a ingresos o valor del token.

### Oferta y capitalización

| Activo | MCAP USD millones | FDV proveedor millones | Circulante/máximo | Precio×máximo millones |
| --- | --- | --- | --- | --- |
| AAVE | 2077.65 | 2153.46 | 96.48% | 2151.84 |
| ADA | 7632.03 | 9142.49 | 83.48% | 9139.09 |
| AIXBT | 18.18 | 18.18 | 100.00% | 18.18 |
| ALGO | 939.21 | 939.21 | 90.74% | 1035.06 |
| APT | 616.47 | 844.73 | 42.07% | 1465.30 |

ALGO: FDV proveedor=MCAP por su convención de oferta total; queda9.26% frente al máximo, no dilución cero. APT: MCAP/FDV proveedor72.98%, circulante/máximo42.07%; denominadores distintos. La última columna es cálculo al precio agregado, no precio justo ni pronóstico.

### AAVE

La [documentación](https://www.aave.com/docs/ecosystem/aave) describe gobernanza y recompras con ingresos: presupuesto anualUSD50 millones, rango semanal ajustableUSD250mil–1.75 millones. Tokens a reserva, no quema; presupuesto no significa dividendo ni compras efectivas esta semana. Es un vínculo económico relativo más directo, condicionado a gobernanza y sostenibilidad.

DefiLlama: TVL USD 17523.26 millones; préstamos USD 12150.25 millones en campo separado, sin sumarlos. `dailyRevenue`: USD 146435 a 24h y USD 4972440 a 30d. Resumen sin metodología detallada: no se llama beneficio neto ni se anualiza perpetuamente para valorar. [Protocolo](https://api.llama.fi/protocol/aave), [ingresos](https://api.llama.fi/summary/fees/aave?dataType=dailyRevenue).

Catalizador:[mercados Sentora en V4 anunciados22-10-2026](https://aave.org/blog/sentora-aave-launch). Confirma despliegue, no adopción rentable. Riesgos:[contratos, oráculos, collateral, liquidaciones, puentes y gobernanza](https://www.aave.com/docs/resources/risks). Juicio: mérito para seguir, insuficiente para contradecir timing o justificar buy/hold con MDD 6%.

### ADA

[Cardano](https://cardano.org/what-is-ada/) describe moneda nativa y delegación; [gobernanza](https://cardano.org/governance/) contempla DReps, pools y comité constitucional. Spot Kraken no incorpora automáticamente staking; no se contabiliza rendimiento.

Circulante/máximo83.48%. [TVL Cardano](https://api.llama.fi/v2/historicalChainTvl/Cardano): USD 57.50 millones, -15.99% a 30d; precio y flujos pueden explicarlo, no demuestra abandono de usuarios. MCAP/TVL no es P/E ni comparación homogénea con AAVE.

Tesis favorable: utilidad, seguridad y gobernanza ofrecen opcionalidad de adopción. Contraargumentos: competencia L1, incentivos y captura incierta de valor. Falta serie homogénea de usuarios económicos, fees orgánicos y concentración para traducir actividad a precio justo. Juicio: esperar confirmación.

### AIXBT

[Términos oficiales](https://docs.aixbt.tech/resources/tokenomics): 600000 tokens dan acceso Holder sujeto a límites; excluyen equity, votos, dividendos, reparto de ingresos/beneficios, rescate y valor garantizado. El [producto](https://docs.aixbt.tech/) ofrece información/alertas/API; no convierte al token en acción de empresa de IA.

La [web](https://aixbt.tech/) advierte sobre información de IA y declara tokens del equipo y comisiones ligadas a negociación: conflicto económico; rankings no son evidencia independiente. Oferta máxima 100% circulante según proveedor reduce esa fuente de dilución, sin eliminar concentración, ventas grandes, contratos o puentes. Juicio: utilidad sin flujo exigible y mala liquidez pesan más que caída desde máximos.

### ALGO

[Utilidad oficial](https://algorand.co/technology/the-algo): transacciones/consenso, máximo10000 millones. [Recompensas](https://algorand.co/staking-rewards) requieren participación específica; no se imputan al spot.

[Informe de agosto, publicado10-09-2026](https://algorand.co/blog/august-2026-algo-insights-report): 677000 wallets activas mensuales,+29.6%; TVL USD 67 millones,+4.7%, pero TVL en ALGO-1.7% y stablecoins-2.3%. Evidencia mixta de mes previo; wallets no son personas. [DefiLlama posterior](https://api.llama.fi/v2/historicalChainTvl/Algorand): USD 32.23 millones,-9.59% a 30d. No concatenar sin reconciliar definiciones.

Tesis: crecimiento de uso puede apoyar demanda. Contraargumento: fees reducidos, incentivos y competencia pueden impedir captura suficiente. Juicio: observar recuperación; tres trades de R no validan el sistema.

### APT

[Actualización18-02-2026](https://aptosnetwork.com/currents/aptos-tokenomics-update): reformas de oferta y fin en octubre2026 del ciclo de cuatro años de inversores/core. No elimina emisiones o distribuciones comunitarias. Distinguir propuesta de parámetros posteriores.

[Dashboard actualizado26-10-2026](https://aptosnetwork.com/apt-supply): máximo2100 millones, tasa2.6% ajustable, emisiones~1.5 millones/mes y quemas~171900; resumen indica emisión neta positiva~1.4 millones. No es deflacionario. Restar valores redondeados no equivale a contabilidad exacta. No se asume yield para comprar spot.

[TVL Aptos](https://api.llama.fi/v2/historicalChainTvl/Aptos): USD 42.57 millones,-15.13% a 30d. Tesis: menor presión de ciertos desbloqueos y crecimiento de uso. Contraargumentos: dilución, competencia y tokenomics sin conciliación transacción a transacción. Calendarios secundarios discrepan; no se afirma fecha/hora/cantidad exacta del próximo desbloqueo. Juicio: catalizador potencial, sin entrada defendible.

## 6. Estadística y dependencia

Retornos simples cierre a cierre. Volatilidad=desviación muestral×raíz de 365.25 en diario. VaR95 histórico=pérdida del percentil5; CVaR=pérdida media de cola inferior. Describen muestra, sin normalidad ni garantía futura. Drawdown siguiente: subyacente100% invertido, no sistema dimensionado.

| Activo | N | Vol.anual | VaR95_1d | CVaR95_1d | MDD subyacente | Peor día | Exceso curtosis | Autocorr.1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AAVE | 719 | 97.00% | 6.99% | 10.27% | -84.10% | -19.30% | 3.37 | -0.027 |
| ADA | 719 | 101.27% | 6.18% | 9.67% | -88.34% | -24.50% | 49.26 | -0.003 |
| AIXBT | 611 | 130.82% | 9.51% | 13.84% | -92.93% | -34.55% | 3.39 | 0.024 |
| ALGO | 719 | 96.79% | 6.98% | 9.59% | -84.81% | -18.19% | 6.20 | 0.072 |
| APT | 719 | 91.32% | 7.13% | 10.53% | -96.49% | -22.57% | 3.76 | 0.048 |

Colas fuertes y pequeña autocorrelación lineal diaria. No prueba eficiencia perfecta ni ausencia de cualquier ventaja; impide inferir una de la simple persistencia. ADA registra un día+72.28%, que contribuye a curtosis extrema; no se depuró por resultar incómodo ni se extrapola.

Pearson diario: 611 retornos comunes alineados por UTC:

|  | AAVE | ADA | AIXBT | ALGO | APT |
| --- | --- | --- | --- | --- | --- |
| AAVE | 1.000 | 0.692 | 0.572 | 0.652 | 0.666 |
| ADA | 0.692 | 1.000 | 0.582 | 0.706 | 0.670 |
| AIXBT | 0.572 | 0.582 | 1.000 | 0.607 | 0.640 |
| ALGO | 0.652 | 0.706 | 0.607 | 1.000 | 0.704 |
| APT | 0.666 | 0.670 | 0.640 | 0.704 | 1.000 |

Spearman también es positivo: ADA/ALGO0.786 y AAVE/ADA0.746. Referencia BTC: 719 retornos horarios comunes:

| Activo | Corr.BTC1h | BetaBTC1h | Horas sin volumen |
| --- | --- | --- | --- |
| AAVE | 0.675 | 1.808 | 0.00% |
| ADA | 0.778 | 2.003 | 0.00% |
| AIXBT | 0.409 | 1.309 | 35.69% |
| ALGO | 0.462 | 1.586 | 0.00% |
| APT | 0.631 | 2.295 | 0.14% |

AIXBT puede parecer menos correlacionado por precios poco actualizados, no por diversificación económica. Se suman pérdidas a stops sin crédito de diversificación. Repartir nombres no convierte una exposición pasiva en compatible con MDD máximo6%.

## 7. Sistemas predefinidos y evaluación empírica

Protocolo congelado antes de recopilar estos datasets y mirar resultados. **Diez ensayos declarados: dos sistemas×cinco activos**, sin optimización. Universo fijado por usuario, pero con posible supervivencia de activos actuales. Últimas120 velas reservadas para una única evaluación después de definir reglas; no es validación externa ciega ni mercado independiente.

### T: continuación de tendencia, hasta 20 días

Cierre t: EMA 50>EMA 200, cierre>EMA 200 y cierre>máximo de highs t-20 a t-1, excluyendo la vela de señal. Entrada al open t+1; rechazar distancia absoluta desde cierre t>ATR 14(t). Stop=mínimo entre low de últimas10 velas terminadas en t y entrada−2ATR14(t). Target=entrada+3×distancia al stop. Salir por stop/target, en apertura posterior a cierre<EMA 50 o al transcurrir20 intervalos diarios desde entrada.

Congruencia: compra solo con régimen y ruptura; stop combina estructura/volatilidad y después se dimensiona. Coherente como hipótesis, resultados insuficientes. Mantener una pérdida por fe fundamental contradice este sistema.

### R: reversión, hasta 10 días

Cierre t: RSI 14<30 y cierre<Bollinger inferior20/2. Entrada siguiente con mismo filtro de gap. Stop=entrada−2ATR14(t); target=entrada+2.5×distancia al stop. Salida en apertura posterior a cierre>=SMA 20, al transcurrir10 intervalos, o stop/target.

**Limitación de congruencia: la salida SMA 20 puede llegar antes del target nominal2.5R.** RR nominal neto>=2 no garantiza recorrido hasta ese target antes de la salida más próxima. R se rechaza para despliegue hasta resolver esa salida en una hipótesis nueva y validarla; no se retocó para mejorar este holdout.

### Simulación

Indicadores causales del Lab, warm-up 200 velas; stop-gap al open adverso; si stop y target se tocan en la misma vela, stop primero. No reentrada en vela de salida. Liquidación al close final con costos. Cada ventana reinicia cash y fuerza cierre independiente; desarrollo+holdout no tiene que sumar resultado continuo. En ADA/APT el corte de operaciones cambia resultados.

Riesgo por entrada0.25% del equity, exposición por activo 20%, fee40 bps y slippage15 bps por lado, fills multiplicativos y RR nominal neto>=2. Comparadores: cash 0% y buy/hold 20%+cash 80%, con costos de entrada/salida. No se presume interés sobre saldo Kraken.

Simulaciones individuales, **no cartera combinada**. No modelan libros históricos, mínimos/ticks históricos, órdenes concurrentes, disponibilidad jurisdiccional ni MDL intradía. Fills AIXBT especialmente optimistas. Agregar fricciones no rescata un sistema que ya no muestra ventaja. La referencia EMA del Lab se ejecutó como benchmark adicional1h/4h/1d; no valida T/R.

### Desarrollo y holdout

Desarrollo: 24-05-2025–27-06-2026, 400 velas; AIXBT: 09-09-2025–27-06-2026, 292 velas. Holdout común:**28-06-2026–25-10-2026, 120 velas**. Fechas corresponden a apertura UTC. Retorno/MDD se expresan sobre equity simulado individual.

| Activo/sistema | Trades dev | Ret.dev | MDD dev | Trades OOS | Ret.OOS | MDD OOS | R medio OOS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AAVE/T | 4 | -0.6078% | -0.7253% | 1 | -0.1313% | -0.2660% | -0.5250 |
| AAVE/R | 4 | 0.0167% | -0.3037% | 0 | 0.0000% | 0.0000% | n/a |
| ADA/T | 1 | -0.1265% | -0.1910% | 0 | 0.0000% | 0.0000% | n/a |
| ADA/R | 10 | -0.5181% | -0.8328% | 0 | 0.0000% | 0.0000% | n/a |
| AIXBT/T | 0 | 0.0000% | 0.0000% | 0 | 0.0000% | 0.0000% | n/a |
| AIXBT/R | 3 | -0.0516% | -0.2792% | 1 | 0.0074% | -0.1315% | 0.0296 |
| ALGO/T | 0 | 0.0000% | 0.0000% | 0 | 0.0000% | 0.0000% | n/a |
| ALGO/R | 3 | 0.2808% | -0.1349% | 0 | 0.0000% | 0.0000% | n/a |
| APT/T | 0 | 0.0000% | 0.0000% | 0 | 0.0000% | 0.0000% | n/a |
| APT/R | 5 | -0.3047% | -0.6004% | 1 | 0.1247% | -0.0277% | 0.4987 |

### Ventana continua elegible tras warm-up

| Activo/sistema | Trades | Retorno | MDD | Acierto | PF | R medio | Exposición barras |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AAVE/T | 5 | -0.7382% | -0.8556% | 0.0% | 0.000 | -0.5922 | 14.81% |
| AAVE/R | 4 | 0.0167% | -0.3037% | 50.0% | 1.033 | 0.0180 | 5.38% |
| ADA/T | 1 | -0.1265% | -0.1910% | 0.0% | 0.000 | -0.5060 | 3.65% |
| ADA/R | 10 | -0.3429% | -0.8328% | 40.0% | 0.626 | -0.1368 | 15.58% |
| AIXBT/T | 0 | 0.0000% | 0.0000% | n/a | n/a | n/a | 0.00% |
| AIXBT/R | 4 | -0.0442% | -0.2792% | 75.0% | 0.607 | -0.0441 | 10.68% |
| ALGO/T | 0 | 0.0000% | 0.0000% | n/a | n/a | n/a | 0.00% |
| ALGO/R | 3 | 0.2808% | -0.1349% | 66.7% | 9.992 | 0.3743 | 5.00% |
| APT/T | 0 | 0.0000% | 0.0000% | n/a | n/a | n/a | 0.00% |
| APT/R | 5 | -0.1720% | -0.6004% | 60.0% | 0.656 | -0.1370 | 6.54% |

Cero operaciones significa inactividad, no validación exitosa. PF cercano a 10 de ALGO-R nace de tres trades de desarrollo y ninguno OOS. APT-R gana 0.1247% OOS con una operación, aunque ventana continua negativa. AIXBT-R gana 0.0074% con una operación y falla ejecución actual. No se asignan probabilidades de éxito.

### Costos e incertidumbre

Sensibilidad: doblar fee/slippage a 80/30 bps por lado. Bootstrap del holdout por bloques 10 barras, 2000 muestras, semilla 42. Solo combinaciones activas:

| Activo/sistema | Ret.base | Ret.doble costo | Bootstrap p05 | p50 | p95 |
| --- | --- | --- | --- | --- | --- |
| AAVE/T | -0.1313% | -0.1374% | -0.4702% | -0.1090% | 0.1553% |
| AIXBT/R | 0.0074% | -0.0049% | -0.2132% | -0.0381% | 0.0000% |
| APT/R | 0.1247% | 0.1026% | -0.0085% | 0.0000% | 0.2744% |

El remuestreo mezcla pocos días activos y muchos ceros; no corrige escasez de operaciones, cambio de régimen, selección o iliquidez. Percentiles no equivalen a intervalo de rentabilidad futura ni probabilidad calibrada. El pequeño beneficio AIXBT desaparece con doble costo.

### Buy/hold20% del equity, cada activo aislado

| Activo | Retorno OOS | MDD OOS | Ret.ventana elegible |
| --- | --- | --- | --- |
| AAVE | 8.693% | -8.682% | -9.492% |
| ADA | 7.828% | -7.921% | -14.599% |
| AIXBT | -0.219% | -7.779% | -16.950% |
| ALGO | 4.052% | -6.585% | -10.725% |
| APT | 3.948% | -6.274% | -17.396% |

Cada comparador tiene 80% cash y es una cuenta separada, no cinco posiciones sumables. Todos superaron 6% de drawdown OOS. Retornos positivos de algunos no justifican inversión pasiva bajo el mandato. Drawdown observado en backtest no es pérdida aceptable para la cuenta real.

## 8. Liquidez y ejecución

Profundidad=sumatoria asks hasta 10 bps desde mejor ask; orden máxima 1% de esa profundidad. No es1% del volumen diario ni todo el libro.

| Activo | Bid/ask04: 47 UTC | Spread bps | Prof.ask10 bps USD | Tope1% USD | Vol24h Kraken estim.USD |
| --- | --- | --- | --- | --- | --- |
| AAVE | 134.57 / 134.58 | 0.74 | 31979.93 | 319.80 | 774660 |
| ADA | 0.203029 / 0.20308 | 2.51 | 83725.45 | 837.25 | 2235514 |
| AIXBT | 0.01816 / 0.01823 | 38.47 | 132.25 | 1.32 | 5534 |
| ALGO | 0.10361 / 0.10362 | 0.97 | 14316.54 | 143.17 | 587106 |
| APT | 0.6977 / 0.6983 | 8.60 | 1080.74 | 10.81 | 217396 |

Volumen 24h estimado con volumen base×precio típico de velas, no notional auditado trade a trade ni volumen global. Segunda observación unos seis minutos después:

| Activo | Hora UTC | Bid/ask | Spread bps | Tope1% USD |
| --- | --- | --- | --- | --- |
| AAVE | 04: 53: 41 | 135.13 / 135.19 | 4.44 | 636.92 |
| ADA | 04: 53: 42 | 0.203797 / 0.203878 | 3.97 | 571.07 |
| AIXBT | 04: 53: 43 | 0.01823 / 0.0183 | 38.32 | 0.44 |
| ALGO | 04: 53: 45 | 0.10392 / 0.10396 | 3.85 | 153.54 |
| APT | 04: 53: 46 | 0.7006 / 0.7011 | 7.13 | 78.40 |

AIXBT excede spread 20 bps en ambas. Mínimo 200 tokens×0.01823=USD 3.646, frente a tope USD 1.322; después mínimoUSD3.66 frente a topeUSD0.437. No hay cantidad admisible; no se afloja política.

APT pasa spread pero capacidad cambia USD 10.81→78.40; AAVE también varía mucho. Son fotografías, no distribución de liquidez ni fill garantizado. Refrescar libro antes del sizing. Una entrada límite puede no llenar; un stop a mercado sufre slippage. [Mecánica stop loss Kraken](https://support.kraken.com/articles/7699391647892-stop-loss-orders).

## 9. Riesgo y diseño prospectivo

Máximos **MDL 3%/MDD 6%**, operativos **2%/4%**, máximo trade 0.25%, riesgo adicional conjunto 0.50%, exposición bruta 50% y activo 20%. Reserva20% del MDL operativo, inicialmente 0.40% del equity diario. No son presupuestos a consumir.

MDD contra mayor entre capital inicial y pico reconciliado; los pisos suben al ganar, no bajan para tolerar pérdidas. MDL incluye patrimonio total, PnL no realizado, costos, órdenes y flujos. Reinicio interno00: 00 UTC, no regla atribuida a Kraken Pro. Brecha intradía mantiene bloqueo aunque recupere. Stops no aseguran límites ante gaps.

Eventual piloto posterior: presupuesto menor, hasta 0.10% por trade/0.20% conjunto, subordinado a cuenta y todos los límites. No habilita piloto hoy ni cambia política. Riesgo aprobado en este corte: 0%. No repartir capital en cinco partes iguales.

Para compra, C=(fee+slippage)/10000=0.0055 por lado:

```text
riesgo_unitario=E-S+(E+S)*C
beneficio_target=T-E-(T+E)*C
RR_neto_target=beneficio_target/riesgo_unitario
q<=min(presupuesto/riesgo_unitario, espacio_exposicion/E,
       cash_disponible/[E*(1+C)],0.01*profundidad_10bps/E)
```

Cantidad hacia abajo a precisión; stop hacia abajo y target arriba al tick; recalcular RR/riesgo tras redondeo. Cumplir mínimos. Justificar invalidación antes de dimensionar; no estrechar stop para aumentar tamaño.

### Ejemplo aritmético; NO plan ejecutable

Base **hipotética 10000 USD**, presupuesto 10(0.10%), libro inicial congelado. Geometría R: stop 2ATR, target 5ATR, redondeada. No hay señal, validación, cuenta u orden asignada; RR al target no representa expectativa con salida temprana. No copiar esta tabla a Kraken.

| Activo | Referencia E | S ilustrativo | T ilustrativo | RR target | Cantidad tope | NotionalUSD | RiesgoUSD | Resultado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AAVE | 134.58 | 115.12 | 183.23 | 2.251 | 0.47999961 | 64.60 | 10.00 | Señal ausente |
| ADA | 0.20308 | 0.175272 | 0.2726 | 2.238 | 334.57196335 | 67.94 | 10.00 | Señal ausente |
| AIXBT | 0.01823 | 0.01592 | 0.024 | 2.217 | 72.54398 | 1.32 | 0.18 | NO cumple ejecución |
| ALGO | 0.10362 | 0.08706 | 0.145 | 2.272 | 567.89980430 | 58.85 | 10.00 | Señal ausente |
| APT | 0.6983 | 0.531 | 1.1164 | 2.345 | 15.47672188 | 10.81 | 2.69 | Señal ausente |

No sumar filas como cartera propuesta. Cuenta ficticia sin posiciones y libro instantáneo; el motor requiere cuenta real completa. Reducir tamaño no subsana falta de ventaja. Las verificaciones account/policy permanecen pendientes.

## 10. Seguimiento, triggers y caducidad

**No introducir órdenes nuevas con este estudio.** Las alertas siguientes reabren evaluación; no son entradas aprobadas ni un sistema distinto validado retrospectivamente.

| Activo | Decisión | Alerta de mejora | Máximo20d al corte | Invalidación de recuperación |
| --- | --- | --- | --- | --- |
| AAVE | Esperar; prioridad 1 | Cierre4h recupera EMA 20≈140.38; luego146–152 | 187.61 | Pérdida133.83/133.32 y luego EMA 200d≈126.28 deteriora tesis; no promediar |
| ADA | Esperar | 4h sobre 0.208614; luego0.225424/0.238323 diarias | 0.282499 | Nuevo mínimo bajo 0.200301 refuerza descarte |
| AIXBT | Excluir ejecución | Primero spread<=20 bps y profundidad compatible con mínimo; después señal | 0.02328 | Liquidez deficiente mantiene exclusión aunque suba |
| ALGO | Esperar; prioridad 2 | Recuperar EMA 200d≈0.105447 y EMA 20_4h≈0.105478 | 0.1443 | Pérdida diaria0.10082 debilita recuperación |
| APT | Esperar | Recuperar0.724609_4h; luego0.750481/0.894189 diarias | 1.1 | Pérdida0.6875 y profundidad escasa impiden anticipar suelo |

T exige además EMA 50>EMA 200 y cierre>EMA 200. Máximo20d es móvil, se recalcula, no se fija en la cifra de tabla. R exige RSI diario<30 y cierre bajo Bollinger inferior; ninguno cumple. Una señal nueva permite registro en papel y revisión de evidencia; no habilita operar este informe.

Escenario favorable: recuperación de medias, ruptura y mejor demanda/libro; reevaluar T sin cambiar reglas y respetando FOMC. Adverso: extensión bajista/spread creciente; continuar sin compras, cancelar borradores no vigentes. Lateral: costos altos frente a recorrido; esperar sin inventar scalping. Sin probabilidades subjetivas.

Cadencia sugerida: tras cierre diario00: 00 UTC; 4h solo alertas. Próxima actualización de velas: 27-10-2026 00: 00 UTC, dentro del periodo sin nuevas aperturas por FOMC. Tras evento: leer comunicado, refrescar mercado/noticias y tesis. Los niveles se retiran al siguiente cierre diario o evento material, lo primero. No hay monitor o aviso automático programado.

Para propuesta real futura: investigación antes del snapshot final; cuenta y libro nuevos; entry/stop/target/cantidad/hash congelados; revisiones reales Codex+Claude de misma versión; gate vigente. Máxima antigüedad de mercado 120s y cuenta300s según política; no ampliar para forzar aprobación. Entrada con límite/precio máximo y sin perseguir gaps; proteger cantidad realmente llenada, registrar parcial y cancelar remanente vencido. Nunca ampliar stops o promediar pérdidas. Sin supervisión de cuenta, no iniciar. Órdenes existentes desconocidas requieren reconciliación; no se infieren de este estudio.

Una corrección futura de R exige protocolo nuevo, muestra futura y revisiones; este holdout ya fue observado.

## 11. Faltantes y cierre razonado

| Severidad | Faltante | Impacto y mitigación | Aceptación de Codex |
|---|---|---|---|
| Crítico ejecución | Moneda/equity/posiciones/órdenes/flujos/peak/baseline no reconciliados | No sizing ni presupuesto MDL/MDD real; requiere snapshot confirmado | No para operar; no impide NO TRADE |
| Crítico ejecución | Fees efectivos y verificaciones operativas pendientes | Costo altera RR/riesgo; conservar supuestos hasta confirmar | No para aprobación real |
| Crítico ejecución | No revisión Claude de misma propuesta ni snapshot vigente | No hay consenso ni READY; documento no los suple | No aceptado |
| Crítico AIXBT | Spread y mínimo incompatibles con profundidad | No cantidad admisible; solo datos nuevos lo resuelven | No aceptado |
| Material deployment | Pocos trades OOS, sin portafolio ni MDL intrabar validado | No inferir ventaja/seguridad; observación en papel | Aceptado para NO TRADE, no para desplegar |
| Material | Concentración, actividad económica orgánica y recompras efectivas sin reconciliación completa | Limita valoración/catalizadores; no proyectar retornos | Aceptado para esperar; contrastar si una nueva tesis depende de ello |
| Material APT | Calendario exacto remanente sin conciliar | No operar fecha/cantidad supuesta; revisar issuer/ledger antes de event trade | Aceptado para NO TRADE |
| Material | Sin profundidad histórica/ejecución durante noticias | Slippage fijo subestima riesgo; libro solo capacidad instantánea | Aceptado para descarte, no garantía de fills |
| Menor este corte | Developer_data nulo/APIs de sentimiento ausentes | No cambia señales ni ejecución; no inventar scores | Aceptado; sin nuevas keys necesarias |

Aceptación exclusivamente de Codex para este NO TRADE; no implica aceptación de Claude o ejecución. Kraken público, CoinGecko Demo, DefiLlama, FRED y fuentes primarias cubrieron dimensiones relevantes. No se necesitan nuevas keys para sostener esta decisión.

**Cierre:**se cubrieron técnico, fundamental, estadístico, liquidez, costos, macro y contraevidencia. Ronda dirigida aclaró ID AIXBT, FDV, tokenomics APT y variación del libro. Más sentimiento o precisión de valoración no cambiaría señales inactivas, validación débil y falla AIXBT. Se decide con información suficiente, sin exigir perfección. Reabrir por señal nueva, cambio material fundamental/liquidez o propuesta defendible; verificar cuenta cuando esa propuesta exista.

## 12. Revisión independiente de Codex

**Identidad:**sesión Codex autora del expediente; versión exacta del modelo no expuesta, no inventada. Independiente respecto de Claude, cuyo estudio no se leyó. Es revisión del propio expediente, no auditoría externa ni segunda firma.

**Veredicto:**rechazar nuevas compras y despliegue real T/R; aceptar cierre y seguimiento en papel. `uncertainty_accepted`: sí para NO TRADE y limitaciones explícitas, no para propuesta real. `strategy_coherence_confirmed`: T coherente como hipótesis pero insuficiente; R con limitación entre target nominal y salida temprana. No existe aprobación de trade con ambos campos válidos.

Comprobé identidad/quote/status, velas cerradas, causalidad, breakout excluyendo señal, entrada siguiente, costos bilaterales, stops/gaps/doble toque, partición, operaciones reales, correlación sin diversificación, umbrales inferiores al mandato, tick/mínimos/profundidad, fuentes y contraargumentos. Los fundamentos no sustituyen timing; indicadores comparten información.

Objeciones para aprobar: escasa actividad OOS; sin cartera/MDL intradía probado; salida R temprana; AIXBT sin cantidad; cuenta/costos pendientes; sin revisión Claude sobre misma propuesta. No se llama `decide` con trade, cuenta o firma inventados para producir WAIT decorativo: este es veredicto de investigación sin propuesta ejecutable. Cuando exista, deberán usarse contratos/gate del Lab.

**Congruencia final:**no comprar concuerda con mandato, señales, costos y evidencia. AAVE puede merecer seguimiento por vínculo económico, sin entrada hoy. Un trade ganador o cero operaciones no validan rentabilidad. Se acepta incertidumbre para tomar esta decisión concreta, no para prometer resultados.

## 13. Trazabilidad y verificación

Worktree/venv/base/cachés/outputs exclusivos; sin modificaciones Claude, órdenes Kraken ni APIs de modelos. Base del Lab:

`a2c4f006983a4ae15bbc35d07e38f8e55e6c160f`. SHA256 Excel:`b1d475c71ad6de7c33f534a5bb854227851ecbfdb36a393b130c8d0a351b211c`. SHA256 protocolo previo:`0010401ea9e5cdad0963ca739eca4fe4d37f319f3867c9f1cf01f5e20ee77e08`.

| Dataset | SHA256 canónico Lab | SHA256 bytes JSON |
| --- | --- | --- |
| AAVE | c5fc5a80a43510da4f422789902fecde52f46414352706bdcd4d470d9062a96c | 3a72d7e1f05aff5c41f44796c5726fa09360148fedaa27dd93fc251f7dd50371 |
| ADA | 566115b6c68904687641e53d995a0d65787e9fab6ceb9c9cf3c84a695063b856 | efbc8f12e70d1a1789272ec6ea1932e8c663b88b574bfe9fd7eb22688239fd6e |
| AIXBT | 26b5043aa0ced21ad16b553ccbc6f95cdc229b6776d29fc7fbaeb85ee00753bc | 4f37e082bfb5812034b1ead757ee58f4a597228f74196271f9cb337711c89280 |
| ALGO | 4df10e63170189fd4ccb49df0d80ad8a30047444b09fd43646c585e7b8074e14 | 2138d2a659d36060fdfefdd1f75a7bcc3663b1005705546dd175953150406735 |
| APT | 5fb419714e6c403f88189194919141bc242c6ea7ded14830a7985f6e102a54da | 3944a1f172ca949e9dd99391cf16757335aa925bbb8bdc2161d33005e1a80365 |

Canónico y bytes difieren por serialización; no por contenido económico. Canónico es el del dossier. Procedencia local: URL, parámetros sin claves, fetched_at original, body_sha256. Caché no rejuvenece fecha.

Reproducción metodológica: commit base, requirements-lock e instalación editable; cinco identificadores; collect enriquecido y analyze en 60/240/1440; reglas sección7, warm-up 200 y split N-120. Recolección actual da otra ventana/hash. **Hashes no reconstruyen payloads perdidos.** Snapshots y simulador de sesión quedan en entorno aislado para auditoría autorizada, fuera de publicación por alcance solicitado. Reproducir exactamente requiere esos snapshots; el código base no incluye el simulador específico T/R. Aquí se publican reglas/métricas suficientes para reconstruir el método, sin afirmar reproducción exacta solo desde GitHub.

Verificaciones: 70 pruebas Lab aprobadas; ruff src/tests aprobado; checks específicos de entrada causal, no anticipación en ejecución, stop primero, gap adverso, costos, exposición y contabilidad PnL. No certifican ventaja. Primer pytest tuvo11 errores de permisos en temporales compartidos; repetición con temporales exclusivos pasó70/70. No se cambió Lab para alterar resultados.

Solo se comparten este estudio y conclusiones. No hay cuenta verificada, orden o monitor oculto.


### Huellas adicionales del expediente local

| Artefacto local no publicado | SHA256 bytes |
|---|---|
| private/strategy_study.py | `cf4da9922c65885307a0c0d989e1f374a347b22b94059695d033ab0c7f810392` |
| outputs/strategy-study.json | `8d5aae9fa391f28dea770f4e62a9f83ee7d7bc37da97615485df0c2ace8262b3` |
| outputs/manifest.json | `0cf4ef54333d07bd3b2ea847a5f420db115a7f4317ad0ea69794797e5f2b6bb8` |
| data/market-recheck.json | `7c6f862150aee68c9a61fc9dac91cf9d2dcec840450151cffd3496d374a53642` |

## 14. Registro de fuentes

Todas las páginas web citadas se consultaron **26-10-2026 UTC**. Hora individual no archivada; se informa día UTC y publicación si existe. Endpoints sí conservan fetched_at exacto. Documentación sin fecha=s/f; consulta actual no es publicación actual.

| Fuente citada | Publicación/observación | Sustenta | Limitación |
|---|---|---|---|
| Kraken AssetPairs/OHLC/Depth | Snapshot04: 47, recheck04: 53 UTC | Instrumentos, velas, libro | No libros históricos/fills futuros |
| CoinGecko registro/mercados/detalles | Recolección sesión; last_updated proveedor | Identidad, oferta, MCAP, FDV | Agregados y convenciones distintas |
| DefiLlama Aave/fees | Snapshot sesión, fecha propia TVL | TVL/dailyRevenue | No estados auditados |
| DefiLlama cadenas | Último dato26-10-2026 00 UTC | TVL/cambio30d | No usuarios ni ingresos token |
| FRED | Observaciones16/22-10-2026 | Contexto macro | Rezago/revisiones; no backtest con vintages |
| Fed calendario | Calendario2026; s/f | FOMC 27–28 octubre | No decisión/hora futura |
| Aave token/riesgos | Documentación viva; s/f | Recompras/gobernanza/riesgos | Emisor; presupuesto no ejecución |
| Aave Sentora | 22-10-2026 | Lanzamiento V4 curado | No prueba adopción/rentabilidad |
| Cardano token/gobernanza | s/f | Utilidad/organización | Sin valoración económica |
| AIXBT docs/web | s/f | Contratos/acceso/derechos/conflicto | Emisor, sin estados auditados |
| Kraken listado AIXBT | 21-02-2025 | Inicio negociación | No profundidad actual |
| Algorand token/staking | s/f | Utilidad/oferta/recompensas | No yield automático CEX |
| Algorand informe agosto | 10-09-2026 | Actividad mixta | Mes previo; wallets no personas |
| Aptos tokenomics | 18-02-2026 | Reforma/ciclo inversores-core | Propuestas no todas implementadas |
| Aptos dashboard | Actualizado26-10-2026 | Oferta/emisiones/quemas | Redondeos/gobernanza/dinámico |
| Kraken stop loss | Documentación viva; s/f | Mecánica stop | Sin precio garantizado |

Hechos primarios se contrastan con mercado/ejecución; no aseguran infravaloración, catalizadores sin descontar o cumplimiento de pérdidas máximas en mercados discontinuos.
