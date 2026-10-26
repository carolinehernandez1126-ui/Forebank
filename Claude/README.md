# Archivo de Claude — Forebank

Decisiones finales de Claude en cada estudio de trading, junto con el estudio que las sustenta, para auditoría posterior por los colaboradores del Research Lab.

Repositorio de carolinehernandez1126-ui. Claude publica como jsforeroc80-debug (colaborador). Cada registro indica el modelo real que lo produjo.

## Estudios

| Fecha | Estudio | Activo | Decisión de Claude | Estado |
|---|---|---|---|---|
| 2026-10-25 | [Universo: primeros 5 de la lista](estudios/2026-10-25-universo-top5/ESTUDIO.md) | AAVE, ADA, AIXBT, ALGO, APT | **NO TRADE** en los 5 (AIXBT no elegible por liquidez) | Vigente; complementado por el estudio 2 |
| 2026-10-26 | [Sistema Forebank C1T v1 + activos 6–10](estudios/2026-10-26-sistema-c1t/ESTUDIO.md) | ARB, ASTER, ATOM, AVAX, BCH (sistema sobre 13 activos elegibles) | **Sistema C1T adoptado en PAPER TRADING**; hoy sin señales; NO TRADE en real | Vigente; se promueve a real con ≥ 15 trades en paper, expectativa > 0 sin el mejor trade y MDD ≤ 2% (riesgo actualizado por el estudio 3) |
| 2026-10-26 | [Filas 12–31 + C1T v1.1](estudios/2026-10-26-filas-12-31/ESTUDIO.md) | BNB, BONK, BTC, CVR, DOGE, DOT, ENA, ETC, ETH, ETHFI, FARTCOIN, FIL, FLOKI, GRASS, HBAR, HYPE, ICP, INJ, JTO, JUP | **NO TRADE** en los 20 (sin señal). CVR, ETC, ETHFI, FLOKI y GRASS no son elegibles. El universo de C1T pasa a 24 activos con 0,10% de riesgo por trade | Vigente; paper trading |

## Sistema vigente de Claude

**Forebank C1T v1.1**: tendencia diaria solo en largos (ruptura del máximo de 50 días si BTC está por encima de su SMA200; stop 3×ATR20 con trailing limitado a 1 R; salida por mínimo de 20 días). **0,10% de riesgo por trade** y riesgo abierto ≤ 0,5%. Universo de 24 activos elegibles por liquidez en Kraken. Reglas de señal congeladas el 2026-10-26; estado **paper trading**. Señales del día: `estudios/2026-10-26-filas-12-31/signals.py`.

Ver el [protocolo](PROTOCOLO_REGISTRO.md) para el formato de cada estudio.

Estas decisiones son de Claude y no sustituyen a las de Codex. Una operación requiere la aprobación de ambas IAs y el gate de riesgo; un registro aquí no es por sí solo una autorización para operar.
