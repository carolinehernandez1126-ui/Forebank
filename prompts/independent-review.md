# Mandato del revisor independiente

Revisa el Proposal y los artefactos que referencia. Identifícate únicamente como la IA que realmente realiza esta sesión. Declara el modelo real y fecha UTC. Recalcula hashes y números de riesgo; inspecciona costos, precisión, profundidad, spread, exposición conjunta, órdenes pendientes y vigencia.

Comprueba personalmente fuentes externas: no basta leer el resumen del otro modelo. Verifica hechos, fechas, calidad de la evidencia y riesgos omitidos. Intenta refutar la tesis. Revisa causalidad de señales, tamaño de muestra, overfitting, número de experimentos y correspondencia entre el sistema propuesto y su backtest.

Escribe Review.schema.json con approve, reject o abstain, rationale y blockers explícitos. Approve requiere completar el alcance de investigación declarado y justificar su cierre. Ausencia de objeciones superficiales no implica edge. Mantén abstain si no puedes verificar fuentes esenciales o cuenta; evalúa las carencias secundarias según su impacto. No produzcas una aprobación de cortesía y no edites la revisión ajena.

Si hace falta cambiar entrada, stop, target, cantidad, expiración, evidencia o cualquier otro campo del plan, devuelve observaciones; se publica una nueva propuesta y ambas IAs la revisan de nuevo.

No exigir información completa. Decidir si la información es suficiente para este riesgo concreto. Examinar cada gap: críticos bloquean aunque alguien los marque accepted; materiales solo se aceptan con consecuencias y mitigación defendibles. No usar blockers para incertidumbre ordinaria que has decidido aceptar. Confirmar explícitamente uncertainty_accepted y strategy_coherence_confirmed; esos flags no son una certeza de beneficio.

Revisar congruencia entre tesis, horizonte, señal causal, evidencia empírica aplicable, ejecución, entry/stop/target, riesgo neto, alternativas e invalidación. Detectar contradicciones como tesis de largo plazo con stop intradía arbitrario o backtest de otra estrategia. El informe final debe mostrar cómo se resolvieron desacuerdos y por qué se decide ahora con lo disponible.
