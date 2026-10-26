# Estándar de decisión y resumen detallado

## Mandato

Investigar exhaustivamente y después decidir con información suficiente. La incertidumbre no desaparece; se hace visible, se gestiona y se revisa. Evitar tanto aprobar por intuición sin sustento como buscar indefinidamente un dataset perfecto.

## Cadena de razonamiento obligatoria

| Eslabón | Qué debe explicar el expediente |
|---|---|
| Observaciones | Qué se midió, fuente, fecha, calidad, alcance y faltantes |
| Interpretación | Régimen de mercado y explicación económica; hechos vs hipótesis |
| Contraevidencia | Qué cuestiona la tesis y por qué la cambia o no |
| Alternativas | Operar ahora, esperar una condición concreta, otra configuración o cash |
| Estrategia | Reglas causales y horizonte consistentes con la tesis |
| Validación | Qué se probó realmente, muestra, costos, sesgos y límites |
| Ejecución | Tipo de orden descrito, entrada, stop, target, tamaño, expiración y fills parciales |
| Riesgo | Pérdida agregada, MDL/MDD operativos vs techos, liquidez y colchones |
| Invalidación | Qué hecho o precio demostraría que la tesis dejó de aplicar |
| Seguimiento | Cuándo comprobar la tesis y qué obliga a cerrar, cancelar o revisar |

No justificar un stop únicamente por el tamaño deseado de la posición: justificar invalidación y después dimensionar. No combinar la tesis de un horizonte con parámetros de otro sin explicar la relación. No atribuir a un sistema resultados de un backtest con reglas distintas.

## Cerrar la investigación

Después de cubrir las dimensiones pertinentes y contrastar contradicciones, evaluar si información adicional probablemente cambiaría la decisión. Si no, documentar el corte y decidir. Si sí, identificar la información concreta y si es obtenible a tiempo; buscarla o escoger una alternativa condicionada/descartada. Nunca prometer conocimiento del 100% ni convertir cada incógnita en un bloqueo.

ResearchConclusion contiene la justificación de suficiencia y cada gap indica severity, impact, mitigation y accepted. Aprobar con gaps materiales aceptados está permitido. Un crítico sigue bloqueado; no se soluciona escribiendo accepted=true. La clasificación es juicio de investigación auditado por ambas IAs, no una garantía de verdad.

## Entregable final

`decide` genera JSON del gate y Markdown detallado. El documento debe permitir a un tercero reconstruir la decisión sin leer el chat: qué se analizó, qué se descartó, qué se desconoce, por qué se decide ahora y cómo cada regla del trade responde a la tesis. Conservar revisiones y desacuerdos, limitaciones y fuentes.

No fabricar un trade para rellenar la plantilla ni forzar consenso. Una decisión de no operar debe tener motivo concreto y, cuando aplique, una condición verificable para reconsiderarla. El reporte no sustituye la vigilancia del operador ni extiende la vigencia de los inputs.
