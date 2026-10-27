# Registro de Interventoría Financiera de Gemini

Esta carpeta conserva los dictámenes oficiales de interventoría financiera, matemática, estadística y macroeconómica, así como las calificaciones comparativas y los planes de inversión y ejecución manual en Kraken Pro elaborados por **Gemini** (Interventor y Calificador Independiente del Laboratorio Forebank).

Reglas de este registro: [PROTOCOLO_REGISTRO.md](PROTOCOLO_REGISTRO.md). Opinión vigente: [OPINION_ACTUAL.md](OPINION_ACTUAL.md).

## Dictámenes y estudios de interventoría

| Fecha (America/Bogota) | Estudio | Activos Evaluados | Elección Ganadora | Decisiones de Inversión Aprobadas | Estado |
|---|---|---|---|---|---|
| 2026-10-26 | [estudios/2026-10-26-interventoria-70-activos/ESTUDIO.md](estudios/2026-10-26-interventoria-70-activos/ESTUDIO.md) | 70 activos (`lista_activos.xlsx`: 5 estudios de Claude vs. 5 tandas de Codex) | **Laboratorio Claude (`88.05 / 100`)** sobre Laboratorio Codex (`81.95 / 100`), integrando el bloqueo macro pre-FOMC de Codex | **1. `NEAR/USD`:** Compra límite post-FOMC en `4.4000`, Stop `4.0200`, Target `5.4000` ($\text{RR}_{\text{neto}} = 2.22$, riesgo `0.08%–0.16%` = `\$40–\$80 USD`).<br>**2. `PUMP/USD`:** Compra límite post-FOMC en `0.004000`, Stop `0.003560`, Target `0.005100` ($\text{RR}_{\text{neto}} = 2.18$, riesgo `0.07%` = `\$35 USD`).<br>**3. `ZEC/USD`:** Pospuesta hasta después del *hard fork* `NU7` (5 nov 2026).<br>**4. Resto (67 activos):** `NO TRADE` / `ESPERAR` / `EVITAR`. | Vigente |

## Archivos del estudio vigente (`2026-10-26-interventoria-70-activos`)

- [ESTUDIO.md](estudios/2026-10-26-interventoria-70-activos/ESTUDIO.md): Dictamen integral de interventoría financiera, matemática, estadística y macroeconómica.
- [COMPARATIVA_MATEMATICA_Y_BACKTESTS.md](estudios/2026-10-26-interventoria-70-activos/COMPARATIVA_MATEMATICA_Y_BACKTESTS.md): Comparación numérica exacta de los backtests cuantitativos (`C1`, `C1T v1.1` vs. Regla `Q`) y de la geometría de costos/barreras de las operaciones propuestas.
- [PLAN_INVERSION_Y_EJECUCION_MANUAL_KRAKEN.md](estudios/2026-10-26-interventoria-70-activos/PLAN_INVERSION_Y_EJECUCION_MANUAL_KRAKEN.md): Plan operativo completo paso a paso (montos exactos en USD y unidades, cómo abrir las órdenes manuales en Kraken Pro, configuración de Stop-Loss, Take-Profit, reglas de cancelación y control de `MDL 3% / MDD 6%`).
- [auditoria_cuantitativa_61_activos.json](estudios/2026-10-26-interventoria-70-activos/auditoria_cuantitativa_61_activos.json): Datos estructurados de la auditoría empírica de la regla `Q` en 61 activos, cálculos de barrera estocástica y lecturas de liquidez de Kraken en vivo.
