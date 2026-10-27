# Opinión Actual de Interventoría (Gemini)

- **Fecha de actualización:** 2026-10-26 (America/Bogota) / 2026-10-27 UTC
- **Capital bajo mandato:** `\$50,000.00 USD` (Ejecución 100% manual en Kraken Pro, spot *long-only*, sin apalancamiento)
- **Límites duros de terminación:** Pérdida Diaria Máxima (`MDL`) = **`3.00%` (`\$1,500.00 USD`)** | Drawdown Acumulado Máximo (`MDD`) = **`6.00%` (`\$3,000.00 USD`)**
- **Límites operativos internos (`config/lab.toml`):** `MDL` = **`2.00%` (`\$1,000.00 USD`, neto `\$800.00 USD` tras reserva del 20%)** | `MDD` = **`4.00%` (`\$2,000.00 USD`)** | Riesgo máximo por operación = **`0.25%` (`\$125.00 USD`)** | Riesgo abierto total máximo = **`0.50%` (`\$250.00 USD`)**

## 1. Calificación Oficial de los Laboratorios

1. **Laboratorio Claude — `88.05 / 100` (GANADOR EN VIABILIDAD FINANCIERA Y SELECCIÓN DE ACTIVOS):**
   - Su sistema cuantitativo `C1T v1.1` demostró expectativa positiva fuera de muestra (`169` trades, `+0.22 R/trade`, `PF = 1.54`, `+37.18 R` acumulados) y preservación de capital en el mercado bajista/lateral `2024–2026` (`67` trades, `+0.03 R/trade`, `PF = 1.07`, peor día `-0.56%`, `MDD = -1.73%`).
   - Sus propuestas discrecionales ganadoras (`NEAR/USD` y `PUMP/USD`) sitúan el stop a `8.64%` y `11.00%` bajo soportes estructurales de rango (`0.78x–0.82x ATR_14` diario), logrando que la fricción de Kraken (`1.10%` ida y vuelta) represente solo el **`8.9%–10.9%` del riesgo unitario**, con ratios netos $\text{RR}_{\text{neto}} = 2.22\text{ y }2.18$.
2. **Laboratorio Codex — `81.95 / 100` (GANADOR EN GOBERNANZA DE RIESGO `MDL/MDD` Y DISCIPLINA MACRO):**
   - Su regla cuantitativa `Q` (rebote horario en soporte de 20 días) queda **descartada para operar capital real** tras comprobar que en los 61 activos spot evaluados (`520 h`) produjo **32 operaciones, 30 pérdidas, 0 aciertos de *target* (`0/32`), `6.25%` de tasa de acierto y `-26.93 R` acumulados (`-0.8416 R/trade`)**, debido a stops microscópicos (`0.16x–0.54x ATR` diario) donde entre el **30.8% y el 70.3% del riesgo se pierde en comisiones y *slippage***.
   - Se incorpora de forma obligatoria la **regla de gobernanza macro de Codex**: prohibición de mantener órdenes límite pasivas abiertas durante la reunión del FOMC (`27–28 de octubre de 2026`).

## 2. Resumen del Plan de Inversión Aprobado

- **Ventana de veda:** `27 y 28 de octubre de 2026` (`100%` en liquidez `USD`, `0` órdenes abiertas durante el anuncio del FOMC).
- **Activación de órdenes manuales:** Desde el **jueves 29 de octubre de 2026 (`00:00 UTC`)**, sujeto a que `BTC/USD` mantenga cierre diario `>= 76,000 USD`.
- **Posición 1 (`NEAR/USD`):** Entrada límite `4.4000 USD` | Stop-Loss `4.0200 USD` | Take-Profit `5.4000 USD` | Monto en horario diurno (profundidad ask 10 bps `>= \$85,000`): **`187.84 NEAR` (`\$826.50 USD` de inversión, riesgo máximo `\$80.00 USD` = `0.16%`)**; en horario nocturno de baja liquidez: **`93.92 NEAR` (`\$413.25 USD` de inversión, riesgo máximo `\$40.00 USD` = `0.08%`)**.
- **Posición 2 (`PUMP/USD`):** Entrada límite `0.004000 USD` | Stop-Loss `0.003560 USD` | Take-Profit `0.005100 USD` | Monto: **`72,500 PUMP` (`\$290.00 USD` de inversión, riesgo máximo `\$35.02 USD` = `0.07%`)**.
- **Riesgo máximo combinado:** **`\$75.02 USD` (`0.15%`) a `\$115.02 USD` (`0.23%`)**, dejando intacto más del **92% del límite diario (`MDL 3% = \$1,500`)** y más del **96% del límite acumulado (`MDD 6% = \$3,000`)**.
