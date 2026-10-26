# Entrada de contexto para Claude

Este repositorio fue iniciado por Codex por encargo del propietario. **No se ha simulado ninguna aprobación tuya.** Tu tarea es colaborar como investigador independiente, cuestionar supuestos y revisar planes concretos.

Destino GitHub confirmado: **carolinehernandez1126-ui/Forebank**, repo compartido ya creado por otra usuaria. Autenticarse exclusivamente como **jsforeroc80-debug**, que tiene acceso de colaborador; no usar sebasforero ni pedir credenciales de la propietaria. No crear otro repo ni sobrescribir su historial. El acceso puntual se facilitará por GH_TOKEN local; para colaboradores puede requerirse PAT classic de alcance más amplio, aunque nuestras operaciones se limitan a Forebank. No publicar secretos ni cambiar sesiones globales. Consultar docs/RUNBOOK.md antes de publicar.

## Qué pidió el usuario

Un Lab Research que suministre datos y análisis a Codex y Claude; ambas IAs investigarán activos que el usuario definirá, analizarán técnico/fundamental/estadístico y propondrán sistemas o trades. La decisión requiere ambas IAs y controles de riesgo; colaboradores ejecutan manualmente y consultan resultados en GitHub. Cuenta confirmada: **Kraken Pro con capital propio; capital 50.000; MDL máximo 3%, MDD máximo 6%**. Operar con umbrales inferiores: MDL 2% y MDD 4%, además de reserva. Moneda definitiva, universo, fees y snapshot de cuenta siguen pendientes.

El usuario exige investigación exhaustiva con cierre práctico: nunca habrá información completa. Decidir con evidencia suficiente y explicar qué se desconoce, por qué se acepta y cómo afecta la estrategia. No convertir incertidumbre ordinaria en espera permanente.

## Empieza aquí

1. Leer AGENTS.md y README.md, luego docs/STATUS.md, docs/RISK.md, docs/METHODOLOGY.md y docs/COLLABORATION.md.
2. Ejecutar la demo y tests para verificar el entorno. Inspeccionar schemas/ y src/research_lab/.
3. Revisar especialmente fórmulas de sizing, PnL diario, timestamps, look-ahead, validez de revisiones y límites del modelo de ejecución.
4. Registrar hallazgos concretos en research/ usando REVIEW_TEMPLATE.md; proponer fixes mediante PR. No asumir que la primera implementación está validada para operar.

## Cómo colaborar en una oportunidad

- Leer el mandato de capital/límites ya confirmado; resolver universo/moneda si aún faltan y verificar el snapshot vigente. No volver a pedir el capital ni los techos conocidos.
- Consumir el mismo dataset y propuesta que Codex. Consultar fuentes primarias web de forma independiente; no limitarte a refrendar su resumen.
- Usar prompts/analyst.md y prompts/independent-review.md. Evaluar hipótesis contraria y escenarios de cola.
- Escribir exclusivamente la revisión `reviewer="claude"` con el modelo real, fecha UTC, hash de la propuesta, rationale, fuentes comprobadas y blockers.
- Evaluar una ventaja razonada con evidencia proporcional al horizonte; no exigir certeza ni significancia imposible con la muestra disponible. Registrar debilidades de la validación y limitar el riesgo o descartar según su impacto. Sin cuenta vigente o con un faltante crítico, no aprobar.
- Completar ResearchConclusion y los flags uncertainty_accepted/strategy_coherence_confirmed de tu revisión solo tras evaluarlos realmente. Se puede aprobar con faltantes materiales aceptados y mitigados; los críticos siguen bloqueando.
- Entregar una decisión concreta y resumen detallado de cómo análisis y contraevidencia condujeron a ella. NO TRADE es válido si existe una razón específica, no por exigir el 100% de información.
- Nunca sustituir ni completar la revisión de Codex. Si cambias una cifra del plan hay que repetir ambas revisiones.

## Entregables útiles en tu primera colaboración

Auditoría del motor de riesgo y de los backtests; una hipótesis registrada con criterios de descarte; revisión de faltantes fundamentales y fuentes gratuitas; propuesta de paper trading. El roadmap distingue expresamente monitor continuo, sincronización privada y atribución real de revisiones, que **aún no están implementados**.
