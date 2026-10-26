# 02 — Capital, límites y decisión bajo incertidumbre

Autor: Codex. Fecha de registro: 2026-10-25 (America/Bogota). Estado: vigente. Enlaces adaptados a las copias documentales.

## Respuesta

Ya quedó incorporado en el código y en las instrucciones de ambas IAs.

Para el capital de **50.000**:

| Control | Máximo absoluto | Límite operativo |
|---|---:|---:|
| MDL | 3% — 1.500 | **2% — 1.000** |
| MDD | 6% — 3.000 | **4% — 2.000** |

Además, configuré una reserva inicial de **200**, riesgo máximo por trade de **125** y riesgo conjunto abierto de **250**. Los límites de liquidez y exposición pueden reducir esos tamaños. El MDD se calcula conservadoramente desde el mayor entre capital inicial y pico reconciliado. USD continúa como moneda provisional.

Las IAs deberán investigar exhaustivamente, justificar cuándo la información resulta suficiente y decidir con lo disponible. Podrán aceptar faltantes materiales con mitigaciones explícitas; los críticos bloquearán la operación.

Cada decisión genera ahora un **resumen detallado de trading** con análisis, fuentes, contraargumentos, alternativas, incertidumbre, conclusión, reglas de ejecución, riesgo e invalidación. Ambas revisiones deben confirmar la congruencia de la estrategia.

Quedó documentado en el [estándar de decisión](../contexto/DECISION_STANDARD.md) y actualizado para [Claude](../contexto/CLAUDE.md).

**Validación: 70 pruebas aprobadas**, además de lint y contratos JSON.
