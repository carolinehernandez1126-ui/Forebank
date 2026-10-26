# Cobertura de 70 filas y comparación Codex–Claude

**Codex · 26-10-2026, America/Bogota.** Se cubren las 70 filas originales; no todas son tokens spot elegibles. Esta es mi comparación de documentos publicados por Claude, no su revisión ni una aprobación conjunta. Informes propios congelados el 26oct a las 22:46:12 UTC, antes de descargar los seis documentos de Claude a las 22:47:45 UTC. Se usó el commit `c72ea661241eabb103b038102ea16523a0e98d5f`. No ejecuté su código ni modifiqué sus archivos.

## Juicio concreto para decidir qué propuesta revisar primero

**No hay base para declarar qué IA ganará más dinero. Sí hay diferencias útiles de calidad y de diseño.** Pondría **PUMP, con la estructura de entrada/stop/objetivo de Claude, como primer expediente de convergencia a revisar**, reduciendo el riesgo a mi piloto 0.05%, esperando a después del FOMC y exigiendo una señal/mercado vigentes. Es una preferencia de congruencia y punto de acuerdo, no una ventaja estimada ni orden.

La tesis discrecional de Claude para NEAR también merece contraste específico: mi regla Q no encaja allí porque su objetivo de media queda por debajo de entrada, lo cual descarta esa regla, **no demuestra que NEAR sea una mala oportunidad bajo otro diseño**. No cambiaré el informe independiente para fingir que propuse sus niveles. SOL/XRP son las alternativas propias más claras por ejecución en las últimas 40 filas; LTC/LINK/XLM/UNI siguen como candidatos condicionados de sus informes. Los planes anteriores de BTC/ETH/BCH requieren refresco al mismo corte antes de compararlos con estos últimos.

Claude aporta selección por fuerza relativa y contexto de derivados, que mi primera regla homogénea cubría peor; sus planes NEAR/PUMP son más específicos para esos rangos. Codex aporta mayor detalle de filtro de precio real, costo/estrés, procedencia por hash y presupuesto experimental global más pequeño. Ninguna de esas fortalezas acredita beneficio futuro. El objetivo es escoger una hipótesis defendible y controlar pérdidas, no votar por nombre o confianza verbal.

**ZEC queda pospuesto en mi criterio**, aunque Claude lo propone. No aceptaría que subir un stop al precio bruto de entrada se describa como eliminar el riesgo de NU7. **PENGU y ONDO se posponen tras la revisión cruzada**: mi primer texto no trataba suficientemente riesgos materiales de negocio/contexto. La adenda en el cuarto estudio hace esta corrección trazable; no cuento esos dos como alternativas activables ahora.

## Qué se puede comparar y qué no

Claude 4/5 toma libros aproximadamente 12:40/12:55 UTC; los nuevos datasets Codex se obtuvieron alrededor 18 UTC y los segundos libros después. Spreads/profundidad cambian: diferencias en elegibilidad no prueban un error de una IA. Claude usa un filtro adicional de volumen mediano 30 d>=250 k USD; mi política se apoya en mínimos/spread/profundidad del Lab y señala capacidad minúscula, sin convertir ese umbral extra en regla del propietario.

Claude combina dos vías: C1T v 1.1 sigue en paper y sin señal, mientras sus dos últimos estudios proponen operaciones discrecionales. No atribuyo a los trades discretos el rendimiento de C1T ni digo que Claude se niegue a todo piloto por falta de backtest ganador. Mis referencias T/R tampoco validan directamente Q. Horarios, horizontes y salidas distintos impiden comparar sus porcentajes simulados como una competición controlada.

| Dimensión | Codex vigente | Claude publicado | Implicación |
| --- | --- | --- | --- |
| Mandato común | Spot USD provisional, manual, MDL 2/MDD 4, max 3/6 | Mismo mandato declarado | Sin cuenta vigente ni consenso no hay autorización |
| Riesgo por trade de las propuestas recientes | Piloto máximo 0.05% | NEAR 0.20%, PUMP≈0.07%, ZEC≈0.11% | Todos bajo 0.25% ordinario; diferencias son de exposición, no prueba de incumplimiento delmandato |
| Riesgo conjunto | Un único piloto global; acumuladas 0.50% con pausas | Hasta 0.38% si llenan las tres, bajo 0.50% agregado | No mezclar/ejecutar simultáneamente ambos catálogos |
| Horizonte | Qmáximo 5/7 d | Discrecional 1–3 semanas; vigencia de entrada hasta 2 nov | Comparar barreras/tiempo o crear hipótesis armonizadas nuevas |
| FOMC | Sin nuevas aperturas 27–28 oct; reconsiderar 29 oct | Límites pueden llenar durante anuncio; sin compra a mercado | Un límite no elimina selección adversa y gap |
| Costos | 55 bps/lado +estrés 110 | 55 bps/lado en ratios declarados | Verificar tier/par/fee real y recalcular al fill |
| Derivados | No adquiridos en mi regla Q; faltante acotado | Binancefunding, OI yratios de cuentas | Contexto de otro venue/contrato, no evidencia de spot Kraken ni tres votos independientes |
| Validación | Kraken propio, muestra pública corta; Qdiagnóstico sin OOSindependiente | C1T largo Binance USDT proxy ycontraste Kraken, sesgos declarados | Más historia no elimina sesgos; mantener metodologías separadas |
| Probabilidades | Sin probabilidad calibrada ni EV positivo declarado | Subjetivas y marcadas como tales | No usar sus EV de escenario como frecuencia observada |
| Reglas de órdenes | Sin transmisión; precio/refresco/revisiones antes de colocar | Documenta límites, no prueba envío real | Fecha 2 nov es escenario, no READYválido por una semana |

El ratio de cuentas long/short no mide por sí mismo tamaño nocional o posición neta de todo el mercado. Funding/OI/ratio del mismo venue pueden compartir causa y no se suman como evidencia independiente. [Definiciones Binance](https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data), consulta 26-10-2026 UTC, documentación dinámica. Su uso como contexto es válido; sustituir con ello un libro spot Kraken no lo sería. No se recomiendan derivados ni se ejecutó ninguna consulta de cuenta.

## Planes de Claude recalculados, sin ejecutarlos

Se recalculó con la misma aproximación aditiva del gate 55 bps/lado. Los precios son los publicados por Claude, no nuevos asks. Tabla normalizada a **riesgo 25 USD hipotéticos** para comparar 0.05% de una referencia 50,000 USD, sin confirmar moneda/saldo real. Qmáxima todavía debe reducirse por cash/libro/mínimos/exposición y remanentes. No se afirma que esos precios estén disponibles.

| Origen de tesis | Entrada | Stop | Objetivo | RRneto recalculado | Cantidad a riesgo 25 USD | Notional USD |
| --- | --- | --- | --- | --- | --- | --- |
| Claude NEAR | 4.4 | 4.02 | 5.4 | 2.2193 | 58.64277169 | 258.03 |
| Claude PUMP | 0.004 | 0.00356 | 0.0051 | 2.1802 | 51912.45483616 | 207.65 |
| Claude ZEC | 1130 | 1035 | 1370 | 2.1163 | 0.23384702 | 264.25 |

**PUMP:** mi objetivo Q 0.00617 desde techo 0.003927 es más remoto que 0.00510 desde 0.00400 de Claude; su stop 0.00356 deja más margen de estructura que mi 0.003748. Prefiero estudiar primero ese recorrido más cercano, aunque da RRmenor. A riesgo 25 USD el notional aproximado 207.65 cabe en los topes históricos observados por Codex; no prueba que quepa en un libro futuro. Su riesgo original≈0.07% era mayor que mi piloto 0.05%, aunque estaba bajo el techo ordinario. Cambiar riesgo, timing o condición de señal crea una **propuesta nueva que requiere dos revisiones nuevas**, no una aprobación implícita de Claude a mi adaptación. [Claude 4](https://github.com/carolinehernandez1126-ui/Forebank/blob/c72ea661241eabb103b038102ea16523a0e98d5f/Claude/estudios/2026-10-26-filas-32-51/ESTUDIO.md).

**NEAR:** el rango con invalidación más amplia es una hipótesis distinta de Q. El mayor impulso relativo y contexto de OI que Claude describe son razones plausibles para priorizar una investigación conjunta, sin que prueben ganancia. No doy por auditados todos sus flujos ETF o incidentes de prensa. La ronda primaria nueva confirma evolución de Chain Signatures, pero no cuantifica ventaja de trading ni verifica por sí misma cada incidente alegado. [NEAR, publicación 23 oct](https://www.near.org/blog/chain-signatures-tee), consulta 26-10-2026 UTC. No abrir solo porque una narrativa reciente es convincente.

**ZEC:** ambos situamos una compra hipotética cerca de 1127–1130 y stop≈1035–1037. La discrepancia es gestión del evento y target. La Fundación confirma NU7 en altura 3,543,405, alrededor 5 nov; una R 7 d desde 29 oct puede cruzarlo. [Zebra 7.0.0](https://zfnd.org/zebra-7-0-0-release/), publicación 22 oct yconsulta 26 oct UTC. El stop bruto en entrada 1130 todavía pierde≈1.10% del notional bajo C=.0055 por lado: para 0.513 ZEC, ≈6.38 USD antes de gap adicional. Breakeven neto en esa aproximación exige precio>=1130*(1+C)/(1−C)≈1142.50. Si el mercado ya está bajo entrada, un stop de venta arriba no da protección diferida; hay que definir cierre/cancelación y no asumir ejecución garantizada. Prefiero posponer ese piloto hasta el upgrade y mercado normal; más tarde los niveles deben recalcularse. [Claude 5](https://github.com/carolinehernandez1126-ui/Forebank/blob/c72ea661241eabb103b038102ea16523a0e98d5f/Claude/estudios/2026-10-26-filas-52-71/ESTUDIO.md).

El valor esperado verbal basado en probabilidades subjetivas 42–45% y dos desenlaces no es rendimiento observado. Claude etiqueta esas probabilidades como subjetivas; el problema sería convertirlas en evidencia calibrada o ignorar salidas temporales, gaps y eventos. No lo hago. Tampoco concluyo que ninguna estrategia pueda obtener OOSpositivo: hay muestras favorables, pero no identifican un ganador fiable.

## Actualizaciones y desacuerdos que cambian la decisión

1. **CVR→CRV:** el propietario corrigió el identificador después del corte de Claude. Su exclusión inicial era razonable ante ambigüedad; ahora Curve debe evaluarse como CRV. Es desfase de información, no punto de superioridad por adivinar un ticker.
2. **SP:** no lo sustituyo por SPX 6900. La fuente primaria de Kraken identifica SP como un perpetuo de S&P 500; si se pretendía otro activo, hace falta identificación explícita. [Anuncio Kraken](https://blog.kraken.com/product/prop/trade-the-sp500),12 ago 2026, consulta 26 oct UTC. Ambos lo excluimos como compra spot disponible, por razones documentadas distintas.
3. **LIGHTER/LIT:** coinciden los dos estudios en distinguir Lighter de Litentry legado yel bloqueo de LIGHTER por 70 diarias. No hay que bajar el mínimo 250 para resolver falta de historia.
4. **PENGU/ONDO:** la información nueva de Claude exige prudencia adicional en misalternativas. El cambio queda en adenda yse posponen; no se transforma toda noticia secundaria enhecho probado. [Adenda cuartoestudio](../2026-10-26-cuarta-tanda-20/ESTUDIO_FINAL.md). Una lista amplia de candidatos también tiene costo de supervisión; no debe operar por inercia.
5. **SOL:** la Fundación confirma Alpenglow mainnet activo 21 oct, así queno es catalizador futuro pendiente. [Actualización oficial](https://solana.com/nl/upgrades/alpenglow), ediciónoct 2026, consulta 26 oct UTC. Eso completa mi dossier deevento sin cambiar stop/target. Claude prefiere confirmación de ruptura por posicionamiento; yo contemplo reversión confirmada en soporte. Son tesis diferentes; comparar el desenlace futuro de una sola no identifica una IA universalmente mejor.
6. **C1T yretorno máximo:** Claude ha investigado una familia de tendencia ydeclara sesgos devenue/selección yajustes posteriores. Es un trabajo empírico más largo que mi diagnóstico Q. Aun así, su estimación de 1–2% anual no es un techo matemático para todo sistema direccional bajo MDL/MDD; es un resultado/juicio de esas reglas ymuestras. No uso ese número para modificar elmandato odecir que otro sistema será rentable.

## Cobertura 70, fila porfila

Leyenda: principal/secundario = diseño condicionado, no READY; descartar = esa configuración; pospuesto = trigger/evento/datoespecífico; fueraalcance = producto sinspot compatible. La columna Claude resume la versión publicada, no la modifica ni la firma. Fuentecódigos A/B/C/D/E se enlazan debajo. Las diferencias de liquidez deben revisarse al mismo instante antes dedecidir.

| Fila | Activo | Codex vigente | Claude reportado | Distinción | Fuente Claude |
| --- | --- | --- | --- | --- | --- |
| 2 | AAVE | WAIT P 1; sin entrada | Sintrade /C1Tpaper | V 2 admite piloto, sinseñal | A |
| 3 | ADA | WAIT P 1; sin entrada | Sintrade /C1Tpaper | V 2 admite piloto, sinseñal | A |
| 4 | AIXBT | WAIT P 1; sin entrada | No elegible:liquidez | V 2 admite piloto, sinseñal | A |
| 5 | ALGO | WAIT P 1; sin entrada | Sintrade /C1Tpaper | V 2 admite piloto, sinseñal | A |
| 6 | APT | WAIT P 1; sin entrada | Sintrade /C1Tpaper | V 2 admite piloto, sinseñal | A |
| 7 | ARB | Observar | Sintrade /C1Tpaper | Tesis/trigger distintos | B |
| 8 | ASTER | Piloto condicionado | Sintrade /C1Tpaper | Tesis/trigger distintos | B |
| 9 | ATOM | Pospuesto evento | Sintrade /C1Tpaper | Tesis/trigger distintos | B |
| 10 | AVAX | Piloto condicionado | Sintrade /C1Tpaper | Tesis/trigger distintos | B |
| 11 | BCH | Principal condicionado | Sintrade /C1Tpaper | Tesis/trigger distintos | B |
| 12 | BNB | Descartar configuración | C1T sin señal /paper | Tendencia 50 d frente a rebote | C |
| 13 | BONK | Secundario condicionado | C1T sin señal /paper | Tendencia 50 d frente a rebote | C |
| 14 | BTC | Principal condicionado | C1T sin señal /paper | Tendencia 50 d frente a rebote | C |
| 15 | CRV (CVR original) | Secundario condicionado | CVR excluido; corrección posterior | Usuario confirmó Curve | C |
| 16 | DOGE | Principal condicionado | C1T sin señal /paper | Tendencia 50 d frente a rebote | C |
| 17 | DOT | Descartar configuración | C1T sin señal /paper | Tendencia 50 d frente a rebote | C |
| 18 | ENA | Secundario condicionado | C1T sin señal /paper | Tendencia 50 d frente a rebote | C |
| 19 | ETC | Descartar configuración | No elegible:liquidez | Regla/lectura delibro distintas | C |
| 20 | ETH | Principal condicionado | C1T sin señal /paper | Tendencia 50 d frente a rebote | C |
| 21 | ETHFI | Secundario condicionado | No elegible:liquidez | Regla/lectura delibro distintas | C |
| 22 | FARTCOIN | Descartar configuración | C1T sin señal /paper | Tendencia 50 d frente a rebote | C |
| 23 | FIL | Descartar configuración | C1T sin señal /paper | Tendencia 50 d frente a rebote | C |
| 24 | FLOKI | Secundario condicionado | No elegible:liquidez | Regla/lectura delibro distintas | C |
| 25 | GRASS | Descartar configuración | No elegible:liquidez | Regla/lectura delibro distintas | C |
| 26 | HBAR | Secundario condicionado | C1T sin señal /paper | Tendencia 50 d frente a rebote | C |
| 27 | HYPE | Principal condicionado | C1T sin señal /paper | Tendencia 50 d frente a rebote | C |
| 28 | ICP | Descartar configuración | C1T sin señal /paper | Tendencia 50 d frente a rebote | C |
| 29 | INJ | Secundario condicionado | C1T sin señal /paper | Tendencia 50 d frente a rebote | C |
| 30 | JTO | Descartar configuración | C1T sin señal /paper | Tendencia 50 d frente a rebote | C |
| 31 | JUP | Descartar configuración | C1T sin señal /paper | Tendencia 50 d frente a rebote | C |
| 32 | KAITO | SECUNDARIO CONDICIONADO | No elegible:liquidez | Comparar mismo corte yregla | D |
| 33 | LDO | DESCARTAR CONFIGURACIÓN | No elegible:liquidez | Comparar mismo corte yregla | D |
| 34 | LIGHTER | DESCARTAR CONFIGURACIÓN | No operable:historia | Historia insuficiente | D |
| 35 | LINK | PRINCIPAL CONDICIONADO | Esperar ruptura | Comparar mismo corte yregla | D |
| 36 | LIT | DESCARTAR CONFIGURACIÓN | No elegible:liquidez | Comparar mismo corte yregla | D |
| 37 | LTC | PRINCIPAL CONDICIONADO | Esperar ruptura | Comparar mismo corte yregla | D |
| 38 | MON | SECUNDARIO CONDICIONADO | Evitar hastaunlock | Comparar mismo corte yregla | D |
| 39 | MOODENG | SECUNDARIO CONDICIONADO | No elegible:liquidez | Comparar mismo corte yregla | D |
| 40 | NEAR | DESCARTAR CONFIGURACIÓN | Compra límite propuesta | Tesis alternativa a Q | D |
| 41 | ONDO | POSPUESTO TRAS REVISIÓN CRUZADA | Esperar | Adenda posterior; pospuesto | D |
| 42 | OP | SECUNDARIO CONDICIONADO | Esperar | Comparar mismo corte yregla | D |
| 43 | PENDLE | SECUNDARIO CONDICIONADO | No elegible:liquidez | Comparar mismo corte yregla | D |
| 44 | PENGU | POSPUESTO TRAS REVISIÓN CRUZADA | Evitar por evento/oferta | Adenda posterior; pospuesto | D |
| 45 | PEPE | DESCARTAR CONFIGURACIÓN | Esperar barrida/posicionamiento | Comparar mismo corte yregla | D |
| 46 | PNUT | DESCARTAR CONFIGURACIÓN | No elegible:liquidez | Comparar mismo corte yregla | D |
| 47 | POL | SECUNDARIO CONDICIONADO | Esperar | Comparar mismo corte yregla | D |
| 48 | POPCAT | DESCARTAR CONFIGURACIÓN | No elegible:liquidez | Comparar mismo corte yregla | D |
| 49 | PUMP | SECUNDARIO CONDICIONADO | Compra límite propuesta | Coincide interés, difieren niveles | D |
| 50 | RENDER | SECUNDARIO CONDICIONADO | Esperar | Comparar mismo corte yregla | D |
| 51 | SP | FUERA DE ALCANCE | Sin spot; no sustituir | Fuera spot | D |
| 52 | S | DESCARTAR CONFIGURACIÓN | No elegible:liquidez | Comparar mismo corte yregla | E |
| 53 | SHIB | SECUNDARIO CONDICIONADO | Esperar | Comparar mismo corte yregla | E |
| 54 | SOL | PRINCIPAL CONDICIONADO | Esperar ruptura/posicionamiento | Comparar mismo corte yregla | E |
| 55 | STX | SECUNDARIO CONDICIONADO | No operable:tamaño | Comparar mismo corte yregla | E |
| 56 | SUI | SECUNDARIO CONDICIONADO | Evitar | Comparar mismo corte yregla | E |
| 57 | TAO | SECUNDARIO CONDICIONADO | Esperar | Comparar mismo corte yregla | E |
| 58 | TIA | DESCARTAR CONFIGURACIÓN | No operable:tamaño | Comparar mismo corte yregla | E |
| 59 | TON | SECUNDARIO CONDICIONADO | Evitar | Comparar mismo corte yregla | E |
| 60 | TRUMP | SECUNDARIO CONDICIONADO | Evitar | Comparar mismo corte yregla | E |
| 61 | TRX | DESCARTAR CONFIGURACIÓN | Esperar | Comparar mismo corte yregla | E |
| 62 | UNI | PRINCIPAL CONDICIONADO | Esperar | Comparar mismo corte yregla | E |
| 63 | VIRTUAL | SECUNDARIO CONDICIONADO | Evitar | Comparar mismo corte yregla | E |
| 64 | WIF | SECUNDARIO CONDICIONADO | Evitar | Comparar mismo corte yregla | E |
| 65 | WLD | SECUNDARIO CONDICIONADO | Evitar | Comparar mismo corte yregla | E |
| 66 | XLM | PRINCIPAL CONDICIONADO | Esperar | Comparar mismo corte yregla | E |
| 67 | XPL | DESCARTAR CONFIGURACIÓN | Evitar | Comparar mismo corte yregla | E |
| 68 | XRP | PRINCIPAL CONDICIONADO | Esperar | Comparar mismo corte yregla | E |
| 69 | XYZ 100 | FUERA DE ALCANCE | Fueraalcance:perpetuo | Fuera spot | E |
| 70 | ZEC | POSPUESTO NU7 | Compra límite propuesta | Discrepa gestión evento | E |
| 71 | ZRO | DESCARTAR CONFIGURACIÓN | Esperar profundidad/ruptura | Comparar mismo corte yregla | E |

A:[Claude/estudios/2026-10-25-universo-top 5/ESTUDIO.md](https://github.com/carolinehernandez1126-ui/Forebank/blob/c72ea661241eabb103b038102ea16523a0e98d5f/Claude/estudios/2026-10-25-universo-top5/ESTUDIO.md); SHA256:`7b0639aaa0054b95216ac35aaeae4d6da675df45ff30a940684343b8eb15d4a1`.

B:[Claude/estudios/2026-10-26-sistema-c 1 t/ESTUDIO.md](https://github.com/carolinehernandez1126-ui/Forebank/blob/c72ea661241eabb103b038102ea16523a0e98d5f/Claude/estudios/2026-10-26-sistema-c1t/ESTUDIO.md); SHA256:`15de4f496ef7b54e18b8e13371a380d0d36767fc69441d407974d98573c8d066`.

C:[Claude/estudios/2026-10-26-filas-12-31/ESTUDIO.md](https://github.com/carolinehernandez1126-ui/Forebank/blob/c72ea661241eabb103b038102ea16523a0e98d5f/Claude/estudios/2026-10-26-filas-12-31/ESTUDIO.md); SHA256:`57b74f61bdba20fa43af37950d3fb0a45b6de96d14b6dd81da22b7b6870aba0b`.

D:[Claude/estudios/2026-10-26-filas-32-51/ESTUDIO.md](https://github.com/carolinehernandez1126-ui/Forebank/blob/c72ea661241eabb103b038102ea16523a0e98d5f/Claude/estudios/2026-10-26-filas-32-51/ESTUDIO.md); SHA256:`ac712a16daed920bff23c9888a9568fddabd5ce5ff3bee9ca2034917ac374eef`.

E:[Claude/estudios/2026-10-26-filas-52-71/ESTUDIO.md](https://github.com/carolinehernandez1126-ui/Forebank/blob/c72ea661241eabb103b038102ea16523a0e98d5f/Claude/estudios/2026-10-26-filas-52-71/ESTUDIO.md); SHA256:`a5ff2bfb7deacfec996982a37235b39a8aa63cc26072d2504ccab3d41e5cca0d`.

Las filas SP/XYZ 100 cuentan como evaluadas, no como backtests spot. Codex dispone de 68 datasets spot entre todas las tandas; LIGHTER no alcanza elgate de historia. En esta sesión:38 datasets nuevos,114 series y 113 aprobadas,26 filtros aritméticos/calidad/liquidez positivos antes deoverlay deeventos ycomparación,25 conservables antes de posponer PENGU/ONDO. No son 26 compras ni 26 ventajas. Las primeras 30 fueron investigadas encortes anteriores; no se refrescó todo eluniverso de forma simultánea en esta entrega.

Se revisaron 134 familias de referencia T/R con tramo completo elegible:68 spots menos LIGHTER, por 2. HYPE carece de partición desarrollo+holdout 120, aunque tiene 71 barras completas traswarmup; LIGHTER no dispone dewarmup 200 diario. Hay 132 familias con partición cronológica válida en 66 activos, sin certificar OOSindependiente. Estas cuentas no incluyen como ensayos independientes cada variación dejuicio ypropuesta exploratoria; la selección múltiple es mayor que un simple número de tests.

## Cómo resolver el desacuerdo con un piloto común

1. Escoger **una sola hipótesis** para revisar al mismo corte de mercado/cuenta, empezando por PUMP si presenta señal y calidad suficiente; si no, no forzar esa elección. Comparar NEAR y SOL/XRP como alternativas, no como posiciones adicionales automáticas.
2. Mantener versión original de cadaidea yregistrar aparte cualquier síntesis. Mismos fees verificados, moneda, presupuesto 0.05%, límites de exposición/participación yvencimiento. Cambiar target, horizonte, señal otiming crea una versiónnueva con dosrevisiones reales; no se promediauna entrada y dos stops por votación.
3. Definirantes del fill qué falsaría cadaidea, evento prohibido, salida temporal ycómo cancelar órdenes pendientes. La ordenlímite se registra como riesgo comprometido tan pronto se coloque; no se ignora por no tenerfill.
4. Medir resultado neto en R y%equity, drawdown intradía/desde pico, pérdida extrema, gaps/slippage, tiempo inmovilizado ycumplimiento de reglas. Registrar también la señal que no ocurrió. Elretorno más alto por un mayor tamaño no demuestra una mejor tesis.
5. Si se lleva un contrafactual del otro plan, etiquetarlo como simulación. Un simple toque deprecio no prueba fill de un límite ni permite fabricar rendimiento; sin libro/colas adecuados ese resultado es incierto. No atribuir a Claude o Codex operaciones que nadie envió.
6. Revisar a 5 cierres o 5 R netos de pérdida, yterminar según presupuesto 0.50%,20 cierres/30 días/invalidación global. Una racha breve tampoco demuestraqué IA tiene razón. No exigimospaperindefinido para admitir elpiloto, ni escalamos trasuna gananciaaislada.

## Trazabilidad y límites finales

Las propuestas se basan en datos históricos, no en un gate vigente. La cuenta/costos reales y ambas revisiones del mismohash siguen críticos. No se han consultado claves privadas Kraken, transmitido órdenes, verificado cuentas por inferencia ni modificado los estudios de Claude. La lectura comparativa es posterior al congelado propio; las fuentes se citan porcommit, no poruna ruta móvil de main.

Este documento es investigación final pública saneada, no un chat archivado ni instrucciones de trading automático. No reprodujo un backtest ajeno ni auditó cada titular secundario de Claude: los puntos no contrastados no se convirtieron en hechos certificados. La adenda corrige mis alternativas donde apareció información material. Pruebas del Lab 70/70 yruff aprobados en la base congelada; validaciones propias dehashes, calidad, ticks, mínimos, geometría ysimulación aprobadas.

Los cuatro informes/conclusiones nuevos yesta comparación son el alcance de publicación. Las respuestas históricas, cuentas, datos yscripts no se añaden alrepo. Los estudios previos de Codex están enlazados porversiones ya publicadas:

[Primera tanda ycriterio V 2](https://github.com/carolinehernandez1126-ui/Forebank/blob/d28bb645857f39c948b3d5356105659de51bee61/Codex/estudios/2026-10-26-piloto-experimental/ESTUDIO_FINAL.md).

[Segunda tanda](https://github.com/carolinehernandez1126-ui/Forebank/blob/3df27f5f1ac740094615d2bbc5e189076de58f57/Codex/estudios/2026-10-26-segundos-cinco/ESTUDIO_FINAL.md).

[Tercera tanda](https://github.com/carolinehernandez1126-ui/Forebank/blob/2b4402b64cf5f0a28e4f30df9df68534121b4602/Codex/estudios/2026-10-26-siguientes-veinte/ESTUDIO_FINAL.md).

| Documento propio congelado antes de Claude | Hash SHA256 original |
| --- | --- |
| 2026-10-26-cuarta-tanda-20 | `dba6dec01d48e2501532cab489282637474f4e811f6996a323bfa5504920ac69` |
| 2026-10-26-quinta-tanda-20 | `d6c62c84f74b5e3b02566ac49f9ab78018f3ec766471dd5ce0272d8f37db8ddf` |

La copia exacta previa a la adenda se conserva localmente; el cuarto estudio publicado muestra la adenda ysu nuevohash. No se afirma que la edición posterior sea ciega a Claude.
