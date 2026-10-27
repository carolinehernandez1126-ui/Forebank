# Comparativa Matemática y de Backtests: Laboratorio Claude vs. Laboratorio Codex

- **Autor:** Gemini (Interventor y Calificador Financiero Independiente)
- **Fecha:** 2026-10-26 (America/Bogota) / 2026-10-27 UTC
- **Modelo de Costos del Laboratorio (`src/research_lab/risk.py`):** Comisión *taker* `40 bps` (`0.0040`) + *slippage* `15 bps` (`0.0015`) por lado = **`55 bps` (`0.55%`) por lado / `110 bps` (`1.10%`) ida y vuelta**.

---

## 1. Comparación de Sistemas Cuantitativos (Backtests con Costos Reales)

| Sistema / Prueba | Laboratorio | Universo y Periodo | Operaciones (`Trades`) | Tasa de Acierto (`Win Rate`) | Expectativa Media por Trade ($R$) | Expectativa sin el Mejor Trade | Profit Factor ($\text{PF}$) | Retorno Acumulado ($R$) | Peor Día Simulado (`MDL` máx. `2.0%`) | Drawdown Máx. (`MDD` máx. `4.0%`) |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Regla `Q`** (Soporte 20d + Vela 1h, Stop `min(low, S20) - 0.25 ATR`) | **Codex** | 61 activos spot en Kraken (`520 h`: 4–26 oct 2026) | **32** (`2` ganadas / `30` perdidas / `0` *targets*) | **`6.25%`** | **`-0.8416 R`** | `-0.8944 R` | **`0.05`** | **`-26.9307 R`** | `-0.50%` (tope 2 pos.) | No reportado en cartera |
| **Hipótesis `H1`** (Ruptura 20d, `BTC > SMA100`, Stop `2.5 ATR`) | **Claude** | 4 activos lote 1 (`2025–2026`, régimen bajista) | **22** | `14.00%` | `-0.6000 R` | `-0.6800 R` | `0.14` | `-13.2000 R` | — | `-14.0 R` *(Descartada)* |
| **Hipótesis `H1` Fuera de Muestra** (Sin cambiar parámetros) | **Claude** | 9 activos (`2018 – nov 2024`, datos no vistos) | **125** | — | **`+0.6100 R`** | **`+0.4700 R`** | `> 1.80` | **`+76.2500 R`** | — | `-20.0 R` |
| **Hipótesis `H2`** (Pullback `RSI(3) < 20` sobre `SMA100`) | **Claude** | 9 activos (`2018 – nov 2024`, fuera de muestra) | **145** | `40.00%` (lote 1) | `-0.0020 R` | `-0.0200 R` | `~1.00` | `-0.2900 R` | — | *(Descartada)* |
| **Sistema `C1` Puro** (Ruptura 50d, `BTC > SMA200`, Stop `3 ATR_20`, salida 20d) | **Claude** | 15 activos fuera de muestra (`2018–2026`, nunca vistos) | **106** | — | **`+1.1300 R`** | **`+0.8700 R`** | **`3.31`** | **`+119.7800 R`** | `-4.10%` ❌ (en lote 1) | `-5.20%` ❌ (excede `4%`) |
| **Sistema `C1` Validación** (Fuera de muestra) | **Claude** | 15 activos no vistos (`2023 – nov 2024`) | **33** | — | **`+2.0500 R`** | **`+1.4400 R`** | **`5.24`** | **`+67.6500 R`** | — | — |
| **Sistema `C1T v1.1`** (`C1` + Trailing Stop de `1 R` máximo) | **Claude** | 15 activos fuera de muestra (`2018–2026`) | **169** | — | **`+0.2200 R`** | **`+0.1500 R`** | **`1.54`** | **`+37.1800 R`** | **`-0.56%`** ✔ | **`-1.73%`** ✔ (`p95 = -3.22%`) |
| **Sistema `C1T v1.1` en Holdout Reciente** (Mercado bajista/lateral) | **Claude** | 15 activos fuera de muestra (`nov 2024 – oct 2026`) | **67** | — | **`+0.0300 R`** | `-0.0500 R` | **`1.07`** | **`+2.0100 R`** | **`-0.56%`** ✔ | **`-1.73%`** ✔ |
| **Cartera Completa `C1T v1.1`** (`0.10%` riesgo/trade, 24 activos) | **Claude** | 24 activos elegibles (`2018–2026`, *mark-to-market*) | **284** | — | **`+0.2900 R`** (en 13 act.) | Positivo | **`> 1.50`** | **`+0.98%` anual** (`Sharpe 0.83`) | **`-0.56%`** ✔ | **`-1.73%`** ✔ (`p95 = -3.22%`) |

---

## 2. Auditoría Empírica de la Regla `Q` de Codex por Tanda (61 Activos Spot)

Datos extraídos y verificados directamente de los archivos `pilot-specific-diagnostic.json` generados por Codex:

| Tanda de Codex | Activos Spot con Diagnóstico (`520 h`) | Señales Estando Plano (`signals_while_flat`) | Operaciones Ejecutadas (`fills`) | Salidas por Stop (`-1.0 R`) | Salidas por Target (`> 0 R`) | Salidas por Tiempo / Final | Retorno Acumulado ($R$) | Expectativa Media ($R\text{/trade}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Tanda 1 (Filas 2–6)** | 4 (`AAVE, ADA, ALGO, APT`) | 4 | 0 | 0 | 0 | 0 | `0.0000 R` | `0.0000 R` |
| **Tanda 2 (Filas 7–11)** | 5 (`ARB, ASTER, ATOM, AVAX, BCH`) | 10 | 4 | 3 | **0** | 1 (`BCH -0.9275 R`) | **`-3.9275 R`** | `-0.9819 R` |
| **Tanda 3 (Filas 12–31)** | 19 (`BNB` a `JUP`, excl. `CVR`) | 50 | 10 | 8 | **0** | 2 (`ENA +0.6463 R`, `DOT -0.4158 R`) | **`-7.7695 R`** | `-0.7770 R` |
| **Tanda 4 (Filas 32–51)** | 17 (`KAITO` a `RENDER`, excl. `LIT/LIGHTER/SP`) | 42 | 12 | 11 | **0** | 1 (`PENGU +0.7454 R`) | **`-10.2546 R`** | `-0.8546 R` |
| **Tanda 5 (Filas 52–71)** | 16 (`SHIB` a `ZRO`, excl. `S/TON/XYZ100/ZEC`) | 23 | 6 | 5 | **0** | 1 (`TAO -0.0210 R`) | **`-4.9791 R`** | `-0.8299 R` |
| **TOTAL CONSOLIDADO** | **61 activos** | **129 señales** | **32 trades** | **27 stops llenos + 3 parciales (`30` pérdidas)** | **0 (`0.0%`)** | **2 ganancias (`PENGU`, `ENA`)** | **`-26.9307 R`** | **`-0.8416 R`** |

---

## 3. Comparación Matemática de Geometría de Costos y Barreras: Propuestas de Claude vs. Candidatos de Codex

Fórmulas exactas del motor [`evaluate_risk`](file:///c:/Users/CARO/Forebank/src/research_lab/risk.py#L46-L185) con $c = 0.0055$:
- $\text{Entrada Efectiva } E_{\text{eff}} = E(1 + c)$, $\text{Stop Efectivo } S_{\text{eff}} = S(1 - c)$, $\text{Target Efectivo } T_{\text{eff}} = T(1 - c)$
- $\text{Pérdida Unitaria Neta } L_{\text{unit}} = E(1+c) - S(1-c)$, $\text{Recompensa Unitaria Neta } G_{\text{unit}} = T(1-c) - E(1+c)$
- $\Phi_{\text{cost}} = \frac{c(E+S)}{L_{\text{unit}}}$ (Fracción del riesgo unitario consumida exclusivamente por comisiones y *slippage*)
- $P_{\text{RW}} = \frac{E-S}{T-S}$ (Probabilidad de tocar *target* antes que *stop* bajo movimiento browniano sin deriva)
- $p^* = \frac{1}{1 + \text{RR}_{\text{neto}}}$ (Tasa de acierto mínima necesaria para punto de equilibrio neto)

| Activo (Laboratorio) | Entrada ($E$) | Stop ($S$) | Target ($T$) | Distancia Bruta al Stop (`%` y `ATR_14(1d)`) | Distancia Bruta al Target (`%`) | % del Riesgo Consumido en Costos ($\Phi_{\text{cost}}$) | $\text{RR}_{\text{neto}}$ (`≥ 2.0`) | $\text{RR}_{2\times\text{Cost}}$ (`110 bps`/lado) | $P_{\text{RW}}$ (Paseo Aleatorio) | $p^*$ (Breakeven Neto) | Brecha Direccional ($p^* - P_{\text{RW}}$) | $\text{EV}_{\text{RW}}$ ($R$) | $\text{EV}_{\text{Tesis}}$ ($R$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Claude: `NEAR/USD`** *(Aprobada)* | `4.4000` | `4.0200` | `5.4000` | **`8.64%`** (`0.82x ATR`) | **`+22.73%`** | **`10.86%`** ✔ | **`2.2191`** ✔ | **`1.8551`** ✔ | **`27.54%`** | **`31.06%`** | **`+3.52 pp`** ✔ | `-0.1136 R` | **`+0.4486 R`** (`p=45%`) |
| **Claude: `PUMP/USD`** *(Aprobada)* | `0.004000` | `0.003560` | `0.005100` | **`11.00%`** (`0.78x ATR`) | **`+27.50%`** | **`8.63%`** ✔ | **`2.1795`** ✔ | **`1.8691`** ✔ | **`28.57%`** | **`31.45%`** | **`+2.88 pp`** ✔ | `-0.0915 R` | **`+0.3355 R`** (`p=42%`) |
| **Claude: `ZEC/USD`** *(Pospuesta)* | `1130.00` | `1035.00` | `1370.00` | **`8.41%`** (`0.75x ATR`) | **`+21.24%`** | **`11.15%`** ✔ | **`2.1211`** ✔ | **`1.7662`** ✔ | **`28.36%`** | **`32.04%`** | **`+3.68 pp`** ✔ | `-0.1149 R` | **`+0.4045 R`** (`p=45%`) |
| **Codex: `XRP/USD`** *(Regla `Q`)* | `1.3266` | `1.3157` | `1.4910` | **`0.82%`** ❌ (`0.22x ATR`) | `+12.39%` | **`57.16%`** ❌ | `7.5234` | `2.8630` | `6.22%` | `11.73%` | `+5.51 pp` *(ruido 1h)* | `-0.4701 R` | **`-0.8416 R`** |
| **Codex: `BTC/USD`** *(Regla `Q`)* | `79799.9` | `79434.1` | `85354.5` | **`0.46%`** ❌ (`0.16x ATR`) | `+6.96%` | **`70.51%`** ❌ | `3.7483` | `0.8180` ❌ | `6.18%` | `21.06%` | `+14.88 pp` ❌ | `-0.7066 R` | **`-0.8416 R`** |
| **Codex: `LINK/USD`** *(Regla `Q`)* | `8.5559` | `8.4737` | `10.3517` | **`0.96%`** ❌ (`0.24x ATR`) | `+20.99%` | **`53.26%`** ❌ | `9.8403` | `3.9970` | `4.38%` | `9.22%` | `+4.84 pp` *(ruido 1h)* | `-0.5252 R` | **`-0.8416 R`** |
| **Codex: `TRX/USD`** *(Regla `Q`)* | `0.3144` | `0.3090` | `0.3237` | **`1.72%`** (`0.54x ATR`) | `+2.96%` | **`38.86%`** ❌ | **`0.6480`** ❌ | `0.1900` ❌ | `36.73%` | `60.68%` | `+23.95 pp` ❌ | `-0.3946 R` | **`-0.8416 R`** |
