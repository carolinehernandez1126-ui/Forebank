# Protocolo Codex–Claude

## Roles

El propietario define objetivos, capital, activos y riesgo. Codex y Claude investigan y revisan de forma independiente. Pueden utilizar especialistas técnicos, fundamentales y estadísticos cuando el usuario lo solicite, pero la firma final es una de cada IA. Una persona opera Kraken Pro manualmente.

El Lab proporciona datos y validaciones. No invoca modelos ni suplantará una segunda opinión. Disponer de dos revisores reduce algunos errores, pero ambos pueden compartir sesgos y fuentes.

## Expediente por hipótesis

Crear una carpeta `research/<id>/` con hipótesis, resultado técnico/empírico saneado, bibliografía, propuesta, revisiones y evaluación posterior. Mantener cuenta, capital sensible, órdenes e identificadores reales fuera de Git. Los datasets privados se comparten por canales autorizados o se reconstruyen; sus hashes garantizan que ambos revisen exactamente la misma versión.

Para un plan público puede resultar preferible publicar porcentaje de capital o unidades normalizadas. El documento público es informativo: cada colaborador debe calcular su propia cantidad con su cuenta y riesgo. Una aprobación para una cuenta no se transfiere a otra.

## Secuencia

1. Registrar hipótesis y criterios de descarte antes de mirar resultados.
2. Obtener snapshots, dossier y prueba empírica pertinente. Congelar la versión y registrar faltantes.
3. Codex y Claude investigan fuentes externas por separado. Consultar proyecto, gobernanza, anuncios y macro, incluyendo fuentes que contradigan la tesis.
4. Preparar un borrador razonado. El autor puede ser cualquiera de las dos IAs. Completar el contrato Proposal; no añadir campos arbitrarios fuera del schema.
5. Antes de revisar el plan final, refrescar cuenta/mercado y fijar entrada, stop, target, cantidad, expiración y hashes. Los argumentos de investigación pueden estar listos previamente.
6. Cada IA escribe su revisión con su modelo real, fuentes comprobadas, incertidumbres y blockers. Nunca editar el archivo de la otra para cambiar su veredicto.
7. Ejecutar el gate determinista. `reject`, `abstain`, blockers, hashes diferentes, revisión faltante/duplicada o riesgo fallido => `WAIT`.
8. Si cambia el plan para resolver objeciones, ambas revisiones se repiten. No promediar veredictos ni usar confianza verbal para superar un bloqueo.
9. Persona verifica Kraken en vivo y vigencia del resultado; ejecuta solo la cantidad aprobada para su cuenta y registra la orden pendiente de inmediato. El gate no reserva capital para dos decisiones concurrentes.
10. Registrar ejecución y resultado aunque sea una pérdida o una operación cancelada. No corregir retrospectivamente la hipótesis original.

## Investigación exhaustiva con punto de cierre

El mandato no exige información perfecta. Cubrir técnico/fundamental/estadístico, liquidez/ejecución y riesgos de eventos relevantes; contrastar hechos materiales con fuentes primarias y buscar contraargumentos. Después de la ronda integral, hacer una ronda dirigida a contradicciones y faltantes que puedan cambiar el plan. Reabrirla solo por información nueva material, no por la posibilidad abstracta de conocer más.

Cerrar cuando las búsquedas adicionales sean redundantes o sea improbable que cambien tesis, tamaño, stop, horizonte o decisión. Registrar scope, cutoff_at, stopping_reason y sufficiency_rationale. No fingir un porcentaje de información conocida ni una probabilidad calibrada si no existe.

- **Crítico:** impide valorar riesgo o ejecutar de forma válida: cuenta no reconciliada, moneda ambigua, precio no verificable, mercado suspendido o contradicción decisiva sin resolver. Bloquea.
- **Material:** podría afectar resultado, pero se puede acotar: métrica de adopción parcial, desglose de tenedores incompleto o muestra limitada. Describir impacto, mitigación y aceptación expresa de ambas IAs; puede ser prudente reducir tamaño o escoger otro horizonte.
- **Menor:** no cambia de forma sustancial esta decisión; registrar sin paralizarla.

No hace falta disponer de todas las APIs opcionales. Sí hace falta explicar la tesis con lo disponible. La decisión puede ser operar, descartar o esperar un trigger/dato concreto, con condición y caducidad explícitas.

## Congruencia y resumen de trading

Proposal versión 2 requiere ResearchConclusion con horizonte, cierre de investigación, alternativas, escenarios, ejecución, seguimiento y gaps. Cada Review incluye uncertainty_accepted y strategy_coherence_confirmed; ambos deben ser true para aprobar. El gate acepta incertidumbre material explícitamente aceptada y bloquea gaps críticos o materiales no aceptados.

Al ejecutar `decide --output private/decision.json`, se escribe también `private/decision.md`, incluso para WAIT. Incluye tesis, todo el análisis resumido, fuentes y contraargumentos declarados, cierre de búsqueda, incertidumbre, coherencia, parámetros, presupuesto de riesgo y razones de ambas IAs. El generador presenta el razonamiento introducido; no inventa investigación ausente.

Los planes versión 1 y revisiones anteriores deben completarse con los campos nuevos y revisarse nuevamente. Los hashes cambian. El resumen contiene datos de cuenta: sanearlo antes de compartir en GitHub.

## Identidad y GitHub

El campo `reviewer` de un JSON es una declaración, no prueba de identidad del agente. Para colaboración remota usar cuentas reales de revisores, PRs y branch protection con aprobaciones independientes. CI valida software y consistencia; no certifica que una IA investigó ni autoriza operaciones.

Nunca publicar una cuenta real para que CI valide el sizing. Realizar el gate privado por cada operador, conservar evidencia saneada y publicar métricas agregadas. Antes de compartir un plan activo definir la audiencia; la orden humana sigue siendo responsabilidad del operador.

## Primer trabajo para Claude

Leer CLAUDE.md y revisar el código de riesgo, semántica de equity/flujos, límites de los backtests y verificación de fuentes. Entregar hallazgos con archivos y ejemplos reproducibles. La primera implementación aún no tiene su revisión real.
