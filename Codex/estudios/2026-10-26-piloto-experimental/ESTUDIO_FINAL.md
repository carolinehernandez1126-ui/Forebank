# Revisión final V2: decisiones con ventaja no demostrada y piloto limitado

**Codex — 26 de octubre de 2026, America/Bogota.** Revisión metodológica solicitada por el propietario. Sustituye el criterio restrictivo de despliegue del [estudio anterior](../2026-10-25-primeros-cinco/ESTUDIO_FINAL.md); no cambia ni borra sus resultados históricos. Únicamente Codex emite esta revisión; no se leyó ni se suplanta el estudio de Claude.

## 1. Corrección de criterio

**No se exigirá rentabilidad positiva fuera de muestra, significancia estadística ni un backtest ganador como condición universal para proponer un piloto real.** Una hipótesis económica y operativa razonada puede ser elegible aun con ventaja estadística desconocida. La falta de prueba deja incertidumbre material: se declara, se acepta expresamente por ambos revisores para esa propuesta y se limita el capital que puede perderse mientras se aprende.

Mi informe anterior dio demasiado peso a una validación que la ventana y el número de operaciones difícilmente podían ofrecer. El motor del Lab no tenía una regla de Sharpe, PF o retorno OOS mínimo; la barrera era mi interpretación. La corrijo sin inventar una ventaja o convertir pérdidas observadas en algo irrelevante. No se modifica el código de riesgo ni se relajan sus límites.

Tampoco es correcto afirmar que el sobreajuste anula inevitablemente todos los backtests. La búsqueda repetida y selección de parámetros producen falsos positivos; un único holdout tampoco lo resuelve siempre. Esa es la advertencia de [Bailey, Borwein, López de Prado y Zhu, versión del 27-02-2015](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf), no una demostración de imposibilidad de toda estrategia. Fuente primaria consultada el 26-10-2026 UTC; no estima la probabilidad de sobreajuste de nuestro Lab.

Distingo tres situaciones:

| Situación | Tratamiento |
|---|---|
| Ventaja no demostrada o muestra pequeña | Puede aceptarse para un piloto limitado con hipótesis concreta; no bloqueo universal |
| Evidencia adversa pertinente | Debe explicarse por qué sigue teniendo sentido el intento; limitar riesgo no borra esa evidencia |
| Costos, geometría, liquidez o datos críticos incompatibles | Descartar esa entrada específica; ninguna aprobación estadística o humana crea capacidad de ejecución |

Gestionar riesgo limita el daño; no crea expectativa positiva. Si W y L son resultados netos de ganancia/pérdida, E=pW−(1−p)L. Con W=2L la tasa de equilibrio simplificada es 1/3, pero aquí p es desconocida y las salidas temporales/gaps alteran los resultados. Un RR grande no prueba que se alcance el target con frecuencia suficiente. Si no existiera ventaja bruta, pagar costos empeoraría la expectativa; nuestra postura es ventaja desconocida, no rentabilidad negativa conocida y aceptada como negocio sostenible.

## 2. Política de piloto que propongo

**Se permite considerar capital real experimental; no se exige una fase indefinida en papel como requisito absoluto.** Para cada propuesta concreta siguen siendo necesarios cuenta válida, revisión real de ambas IAs y gate vigente. El usuario puede aceptar incertidumbre sin que eso equivalga a confirmar saldos o firmar por Claude.

| Regla adicional de piloto | Propuesta de Codex |
|---|---:|
| Riesgo inicial por trade, incluyendo costos | Hasta 0.05% del equity actual |
| Posiciones del piloto simultáneas | Una |
| Nuevas entradas del piloto | Máximo una por día UTC; cero es válido |
| Pérdida diaria del piloto | Pausa al alcanzar 0.15% de su equity base de inicio diario |
| Presupuesto de pérdida acumulada | Hasta 0.50% de la base reconciliada al iniciar el piloto |
| Revisión de procedimiento | A 5 trades cerrados o 5R de pérdida neta acumulada, lo primero |
| Fin de la primera tanda | 20 trades cerrados, 30 días desde primera entrada, presupuesto agotado o invalidación material, lo primero |
| Reposición de presupuesto / aumento de tamaño | No automáticos; nunca para recuperar pérdidas |

Son restricciones propuestas para una primera tanda, no defaults ya implementados en la CLI. Sus contadores y pausas requieren diario/supervisión humana mientras no exista implementación específica. Los gaps pueden rebasar el presupuesto; no se prometen pérdidas acotadas con certeza. No borrar el diario o cambiar alias para reiniciar la tanda. La pérdida diaria y la acumulada incluyen PnL realizado/no realizado y costos, ajustados por flujos, de todas las posiciones del piloto. La acumulada se mide neta desde su inicio contra una base reconciliada fija; ganancias o depósitos no reinician el presupuesto. R de cada trade es su pérdida inicialmente presupuestada, incluidos costos: la revisión por 5R usa el resultado neto de los trades en esas unidades, no exige cinco stops idénticos.

Se mantienen intactos MDL/MDD operativos 2%/4%, máximos 3%/6%, reserva, riesgo por trade máximo 0.25%, riesgo adicional conjunto 0.50%, exposiciones y liquidez. Los límites del piloto son adicionales: el patrimonio completo con posiciones ajenas al piloto puede agotar antes la capacidad. Siempre manda el menor presupuesto disponible. En la referencia de capital indicada por el usuario, 0.05% serían 25 unidades de cuenta, no 25 USD confirmados ni un saldo real.

Una racha favorable o 20 operaciones no certifican ventaja ni autorizan escalar. Se evalúan calidad de ejecución, costos reales, adherencia, errores y evidencia adversa. Mantener tamaño, revisar o cerrar son decisiones válidas. No hay una rentabilidad diaria obligatoria, cuota de operaciones, martingala o promediado de pérdidas.

## 3. Uso del Lab y de los backtests

Los backtests siguen siendo herramientas para detectar fuga temporal, incoherencias, exposición, costos, fragilidad y escenarios. Sus resultados tienen peso, pero no voto de veto automático por ser negativos o inconclusos. Una simulación adversa exige una explicación económica verificable y tamaño acorde, no retocar reglas hasta que aparezca un gráfico ganador.

Los antiguos T/R conservan sus resultados. R mantiene una objeción distinta a la significancia: su salida SMA20 puede anticipar el target con el que se calculó RR. Ese desacople debe corregirse en un diseño nuevo o reflejarse explícitamente; no se arregla eliminando el requisito OOS. El holdout anterior ya fue observado y no volverá a presentarse como una validación nueva intacta.

El registro prospectivo debe incluir la tesis, versión de reglas, fuentes y hashes, decisiones de no entrar, fill/fees/slippage reales, salida, resultado neto y revisión posterior. Una modificación crea versión nueva con sus intentos declarados; las pérdidas anteriores no desaparecen. Se prefiere pocas reglas justificables y una sola hipótesis por tanda a una búsqueda masiva de parámetros.

## 4. Reevaluación concreta de los cinco activos

Se renovaron Kraken OHLC/AssetPairs/Depth mediante el Lab: 26-10-2026, entre 11:36:25 y 11:36:47 UTC. Las 15 series aprobaron calidad y son reales. No se sustituyó venue. Última 1h cerrada a las 11:00 UTC, última 4h a las 08:00 UTC, diaria a las 00:00 UTC. Los fundamentos de la sesión anterior son contexto fechado, no una nueva auditoría on-chain.

Para demostrar la diferencia entre falta de prueba y entrada económicamente mala se congeló **antes del nuevo snapshot** un diseño experimental P1: recuperación táctica horaria hacia EMA20 de 4h. Lo motiva la corrección previa y, para AAVE, su estructura diaria y vínculo económico relativo. No se le atribuye el backtest de T/R. Los demás se midieron para comparar ejecución, sin afirmar tesis fundamental idéntica.

Reglas P1: última 1h cerrada debe superar el máximo de las seis anteriores y EMA20_1h; stop = mínimo de las seis últimas cerradas −0.25ATR14_1h; primer target = EMA20_4h redondeado hacia abajo. No se aleja el target para fabricar RR>=2. La entrada límite no puede superar el ask observado ni el precio que permite RR neto 2 con ese stop/target. No perseguir más de 0.25ATR1h desde cierre de señal; cancelar si se toca stop o un nuevo cierre 1h pierde EMA20, o al cumplir 30 minutos sin fill. Ese plazo es solo un techo: cualquier vencimiento anterior de propuesta, cotización, cuenta o revisión según el gate cancela antes; no extiende la vigencia actual de 120s del mercado ni 300s de la cuenta. Máximo 24 horas de tenencia; al término, salida manual con costos. Sin parciales, trailing ni breakeven. Una propuesta nueva congelaría precios, stop/target y caducidad después de formarse la señal.

Este protocolo fue escrito informado por el estudio anterior; no es una hipótesis descubierta a ciegas ni una estrategia validada. Se comprobó una sola parametrización, sin optimizar para obtener entrada. La tolerancia a incertidumbre permite plantearlo; no exige aceptarlo si falla su geometría.

| Activo | Ask USD | Spread bps | Tope1% profundidad USD | Stop P1 | Primer target P1 | RR neto al ask | Señal P1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AAVE | 135.22 | 0.74 | 598.32 | 133.27 | 139.82 | 0.901 | No |
| ADA | 0.204368 | 5.43 | 888.41 | 0.200191 | 0.208009 | 0.214 | No |
| AIXBT | 0.01819 | 16.51 | 6.53 | 0.01793 | 0.01865 | 0.561 | No |
| ALGO | 0.1048 | 3.82 | 133.80 | 0.1024 | 0.10525 | -0.199 | No |
| APT | 0.697 | 10.05 | 17.02 | 0.682 | 0.7209 | 0.713 | No |

**Resultado:** P1 todavía no activa una compra en ninguno. El motivo ya no es «no pasa OOS»: faltan señal y RR neto mínimo en esta configuración. No se congeló una propuesta ejecutable, no se fabricaron cuenta/revisiones ni se invocó un gate con datos ficticios.

AAVE al ask 135.22, stop 133.27 y primer obstáculo 139.82 ofrece RR neto aproximado 0.901 con fee/slippage 40/15bps por lado. Para RR2 con esas referencias necesitaría entrada <=133.97; un tick arriba da aproximadamente 1.988. **133.97 es un límite algebraico al corte, no una orden recomendada**: no hay señal activa, el precio puede invalidar el stop y las referencias se recalcularían antes de una propuesta nueva. No se cambia target a una media más lejana solo para cumplir el ratio.

ALGO está por encima de EMA20_1h, pero no rompe el máximo de seis horas; el recorrido al primer target 4h no cubre siquiera los costos supuestos. APT/ADA tampoco activan P1. Su utilidad fundamental no cambia esa aritmética.

**Corrección actual de liquidez AIXBT:** spread 16.51bps y tope de profundidad USD6.53 frente a mínimo 200×0.01819=USD3.638. En esta fotografía ya son compatibles; retiro el bloqueo instantáneo atribuido al snapshot anterior. Eso no borra dos libros adversos previos ni 35.69% de horas con volumen cero en la ventana. Se exige nueva lectura al entrar, no exclusión permanente basada en una foto vieja.

FOMC 27–28 de octubre sigue siendo un evento conocido según el [calendario Fed](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm), consultado 26-10-2026 UTC. Mantengo la exclusión propuesta de nuevas aperturas esos dos días; no requisito de rentabilidad histórica. El piloto no obliga a abrir antes del evento.

## 5. Decisión y revisión independiente de Codex

**Acepto el cambio de mandato: un piloto real puede proponerse con ventaja estadística no demostrada.** La incertidumbre de rentabilidad es material y puede aceptarse expresamente por ambos revisores cuando la tesis y el riesgo lo permitan. Deja de ser una prohibición general o una exigencia de años de validación.

Apruebo como criterio de investigación este presupuesto pequeño y reglas explícitas de aprendizaje. No es una aprobación de orden: P1 no está activo y no hay cuenta o firma Claude verificadas. Mi decisión de esperar esta configuración específica se fundamenta en señal/costos/RR, no en significancia. La falta de certeza no bloquea universalmente; un precio incompatible sí descarta una entrada.

Críticos de ejecución que permanecen: moneda y estado completo de cuenta reconciliados, costos efectivos, datos vigentes y revisión de ambas IAs de la misma propuesta. No se vuelven a pedir capital ni máximos ya informados. No hay un requisito nuevo de API opcional o historial perfecto.

El escalado queda desacoplado del deseo de recuperar dinero: observar adherencia no equivale a probar ventaja, y proteger capital no convierte una tesis débil en rentable. Reabrir por señal formada, cambio de precio que mejore geometría sin destruir tesis o nueva información material; evaluar una propuesta real con ese snapshot, no reutilizar los precios de este documento.

## 6. Trazabilidad

No se modificaron código, schemas, valores de riesgo ni verificaciones de cuenta. Se revisó `decision.py`/`risk.py`: no contienen gate de retorno OOS, Sharpe o PF. El criterio cambiado es de revisión humana/IA. No se ejecutaron órdenes ni APIs de modelos. Trabajo en el worktree separado de Codex, sin leer resultados de Claude.

La validación fue de hashes, calidad de 15 series y álgebra del límite de entrada; no se afirma un backtest nuevo rentable ni nuevas pruebas de código. Las 70 pruebas aprobadas del estudio original siguen siendo su verificación de software; no se presentan como validación económica del piloto. Los costos se mantienen conservadores hasta confirmar el tier.

| Dataset nuevo | SHA256 canónico Lab |
| --- | --- |
| AAVE | 5e061f83e6ae6d3c6549d010beb2902a8f81f76f938ba93f469bd11d3208178b |
| ADA | ad52cac3304a88334c51ba6c8c5725422a9d5c29885dfcec98795edf2ff5b0a2 |
| AIXBT | cab2f9c7c8599378cf9bdc545f6e81a83b069553e72a88f37a2017f10f088372 |
| ALGO | fa4163f2e98d98cbd56889e0e60d6e3b349d8fcd3c35385e9613d498e5ccf697 |
| APT | 9e3b1820427f54657bdbf7c46f2d00c8521f88840cd76ca1a5f055cbacf0be2d |

SHA256 del protocolo previo al nuevo snapshot: `90d71aa45c330625cd5094c0d856c831bdf07bc919fb4494fc4a38e8dd15640d`. SHA256 de la evaluación local: `36c3ba77a71f7f9d78a79dc353fd5c17dfd0a794943ea1b6549b7fe3a401e6d9`. Cierre de esta revisión: `2026-10-26T11:41:03.957307+00:00`.

Snapshots y scripts quedan fuera de Git; reproducir exactamente requiere los originales, no solo hashes. Las reglas y resultados resumidos quedan públicos para contraste. No hay monitor automático; el próximo cierre horario no se evaluará desatendidamente. La próxima propuesta requerirá datos nuevos.

Este documento final y sus conclusiones corrigen el criterio anterior sin transcribir el chat. Las notas en el estudio anterior enlazan aquí; su resultado histórico sigue fechado y preservado. [Conclusiones vigentes](CONCLUSIONES.md).
