# Archivo de Claude — Forebank

Decisiones finales de Claude en cada estudio de trading, junto con el estudio que las sustenta, para auditoría posterior por los colaboradores del Research Lab.

Repositorio de carolinehernandez1126-ui. Claude publica como jsforeroc80-debug (colaborador). Cada registro indica el modelo real que lo produjo.

## Estudios

| Fecha | Estudio | Activo | Decisión de Claude | Estado |
|---|---|---|---|---|
| 2026-10-25 | [Universo: primeros 5 de la lista](estudios/2026-10-25-universo-top5/ESTUDIO.md) | AAVE, ADA, AIXBT, ALGO, APT | **NO TRADE** en los 5 (AIXBT no elegible por liquidez) | Vigente; complementado por el estudio 2 |
| 2026-10-26 | [Sistema Forebank C1T v1 + activos 6–10](estudios/2026-10-26-sistema-c1t/ESTUDIO.md) | ARB, ASTER, ATOM, AVAX, BCH (sistema sobre 13 activos elegibles) | **Sistema C1T adoptado en PAPER TRADING**; hoy sin señales; NO TRADE en real | Vigente; se promueve a real con ≥ 15 trades en paper, expectativa > 0 sin el mejor trade y MDD ≤ 2% |

## Sistema vigente de Claude

**Forebank C1T v1**: tendencia diaria solo en largos (ruptura del máximo de 50 días si BTC está por encima de su SMA200; stop 3×ATR20 con trailing limitado a 1 R; salida por mínimo de 20 días; 0,20% de riesgo por trade). Reglas congeladas el 2026-10-26. Señales del día: `estudios/2026-10-26-sistema-c1t/signals.py`.

Ver el [protocolo](PROTOCOLO_REGISTRO.md) para el formato de cada estudio.

Estas decisiones son de Claude y no sustituyen a las de Codex. Una operación requiere la aprobación de ambas IAs y el gate de riesgo; un registro aquí no es por sí solo una autorización para operar.
