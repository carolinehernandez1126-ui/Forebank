# Plan de Inversión Completo y Guía de Ejecución Manual en Kraken Pro

- **Autor:** Gemini (Interventor y Calificador Financiero Independiente) — Basado en la propuesta ganadora del **Laboratorio Claude** con las salvaguardas macro y de liquidez de la Interventoría y del **Laboratorio Codex**.
- **Fecha:** 2026-10-26 (America/Bogota) / 2026-10-27 UTC
- **Cuenta y Modalidad:** Kraken Pro — Operación **100% Manual**, **Spot Long-Only (solo compras al contado, sin apalancamiento ni margen)**.
- **Capital Total de la Cuenta (`Equity`):** **`\$50,000.00 USD`**

---

## 1. Presupuesto Global de Riesgo y Distribución del Capital

Para garantizar matemáticamente que **jamás se violen los límites de cierre de cuenta** (`3.00%` de pérdida diaria = `\$1,500.00 USD` y `6.00%` de drawdown acumulado = `\$3,000.00 USD`), la distribución del capital de `\$50,000.00 USD` es la siguiente:

| Concepto del Portafolio | Monto en USD | % sobre Capital (`\$50,000`) | Función Financiera |
| :--- | :---: | :---: | :--- |
| **Efectivo en Reserva de Protección (`Cash USD`)** | **`\$48,883.50 – \$49,296.75 USD`** | **`97.77% – 98.59%`** | Blindaje absoluto contra caídas de mercado; garantiza que el `MDD` del `6%` sea imposible de alcanzar en este ciclo. |
| **Capital Invertido en Posición 1 (`NEAR/USD` — Escenario Diurno Estándar)** | **`\$826.50 USD`** *(o `\$413.25 USD` en liquidez nocturna)* | **`1.65%`** *(o `0.83%`)* | Compra spot en soporte estructural del líder de fuerza relativa a 90 días (`+172%`). |
| **Capital Invertido en Posición 2 (`PUMP/USD` — Tamaño Mínimo por Profundidad)** | **`\$290.00 USD`** | **`0.58%`** | Compra spot en soporte del único activo con fuerza relativa positiva vs. BTC a 30 días (`+6.0%`). |
| **Exposición Bruta Total en Activos (`Notional Total`)** | **`\$1,116.50 USD`** *(o `\$703.25 USD`)* | **`2.23%`** *(o `1.41%`)* | Más del `97.7%` del patrimonio permanece en dólares (`USD`) sin riesgo de mercado. |
| **Riesgo Máximo Si `NEAR/USD` Toca Stop-Loss (incluyendo comisiones y *slippage*)** | **`\$80.00 USD`** *(o `\$40.00 USD`)* | **`0.16%`** *(o `0.08%`)* | Por debajo del tope del Lab de `0.25%` (`\$125.00 USD`) por operación. |
| **Riesgo Máximo Si `PUMP/USD` Toca Stop-Loss (incluyendo comisiones y *slippage*)** | **`\$35.02 USD`** | **`0.07%`** | Ajustado al tope del `1%` de la profundidad de libro de Kraken a `10 bps` (`\$29,000 USD`). |
| **PÉRDIDA MÁXIMA TOTAL SI AMBAS POSICIONES FALLAN EL MISMO DÍA** | **`\$115.02 USD`** *(o `\$75.02 USD`)* | **`0.23%`** *(o `0.15%`)* | **Consume apenas el `7.67%` del límite diario de cierre (`\$1,500`) y el `3.83%` del drawdown máximo (`\$3,000`).** |
| **GANANCIA NETA ESPERADA SI AMBAS POSICIONES LLEGAN A TARGET (después de costos)** | **`+\$253.89 USD`** *(o `+\$165.12 USD`)* | **`+0.51%`** *(o `+0.33%`)* | Relación Recompensa/Riesgo Neta combinada de **`2.21 a 1`** libre de comisiones y *slippage*. |

---

## 2. Calendario y Condición Previa Obligatoria Antes de Abrir Cualquier Posición

> [!IMPORTANT]
> **REGLA 1 — Veda Pre-FOMC (27 y 28 de octubre de 2026):**
> **NO coloques ninguna orden hoy martes 27 ni el miércoles 28 de octubre.** La Reserva Federal (FOMC) anuncia su decisión de tasas el miércoles 28 de octubre a las `14:00 ET` (`18:00 UTC`). Dejar órdenes límite abiertas durante el anuncio expone la cuenta a una caída vertical por sorpresa macroeconómica.
>
> **REGLA 2 — Ventana de Apertura (Desde el jueves 29 de octubre de 2026 a las `00:00 UTC` / miércoles 28 a las `19:00` hora Colombia):**
> Antes de ingresar a Kraken Pro para cargar las órdenes, verifica una sola cifra en el gráfico diario (`1D`) de **`BTC/USD`**:
> - ✅ **Si el último cierre diario de `BTC/USD` es `>= 76,000.00 USD`:** El régimen alcista de medio plazo sigue intacto. Procede a abrir las posiciones según las fichas exactas de la Sección 3.
> - 🛑 **Si `BTC/USD` cerró algún día por debajo de `76,000.00 USD`:** Se activa el **Interruptor Global de Protección**. No abras ninguna posición y mantén el `100%` en `USD`.

---

## 3. Fichas Exactas de las 2 Posiciones Aprobadas

### POSICIÓN 1: `NEAR/USD` (NEAR Protocol contra Dólar Estadounidense)

* **Tesis Financiera y Técnica:** Líder de fuerza relativa en los últimos 90 días (`+172%`), cotizando `+89%` por encima de su media móvil de 200 días (`SMA200`) y consolidando en un rango lateral limpio entre `4.25 USD` y `5.50 USD` con volumen decreciente. El apalancamiento especulativo ya se purgó (*Open Interest* `-11.5%` en 7 días, *funding* neutro `-0.03 bps`) y cuenta con demanda estructural del ETF spot con staking de Bitwise (`NRR`, `~66 M USD` bajo gestión).
* **Niveles de Precio Exactos:**
  - **Precio de Entrada (Orden Límite de Compra / *Limit Buy*):** **`4.4000 USD`** (parte baja del rango de soporte; **no comprar a mercado** si cotiza en `4.55–4.65 USD`).
  - **Precio de Stop-Loss (Orden *Stop-Loss Market*):** **`4.0200 USD`** (`-8.64%` desde la entrada; ubicado por debajo de los mínimos estructurales de `4.25 USD`).
  - **Precio de Take-Profit (Orden *Take-Profit Limit*):** **`5.4000 USD`** (`+22.73%` desde la entrada; justo debajo de la resistencia del rango en `5.45–5.50 USD`).
* **Montos Exactos a Ingresar en Kraken Pro (según liquidez del libro al momento de cargar la orden):**
  - **Opción A — Horario Diurno Estándar (cuando la columna de venta *Ask* entre `4.4000` y `4.4044` suma `>= \$85,000 USD`, habitual entre `08:00` y `17:00` hora Colombia):**
    - **Cantidad de Unidades a Comprar (`Volume`):** **`187.84 NEAR`**
    - **Monto Total de la Compra (`Total / Notional`):** **`\$826.50 USD`** (`1.65%` del capital)
    - **Pérdida Neta Máxima si salta el Stop en `4.0200` (incluyendo `1.10%` de costos):** **`\$80.00 USD`** (`0.16%` del capital)
    - **Ganancia Neta Estimada si llega al Target en `5.4000` (después de costos):** **`+\$177.53 USD`** (`+0.36%` del capital, $\text{RR}_{\text{neto}} = 2.22$)
  - **Opción B — Horario Nocturno / Baja Liquidez (si el libro a `10 bps` tiene entre `\$45,000` y `\$84,000 USD`):**
    - **Cantidad de Unidades a Comprar (`Volume`):** **`93.92 NEAR`**
    - **Monto Total de la Compra (`Total / Notional`):** **`\$413.25 USD`** (`0.83%` del capital)
    - **Pérdida Neta Máxima si salta el Stop en `4.0200` (incluyendo costos):** **`\$40.00 USD`** (`0.08%` del capital)
    - **Ganancia Neta Estimada si llega al Target en `5.4000` (después de costos):** **`+\$88.76 USD`** (`+0.18%` del capital, $\text{RR}_{\text{neto}} = 2.22$)

---

### POSICIÓN 2: `PUMP/USD` (Pump.fun contra Dólar Estadounidense)

* **Tesis Financiera y Técnica:** Único activo del lote con fuerza relativa positiva frente a Bitcoin en los últimos 30 días (`+6.0%`) y `+99.9%` en 90 días, cotizando `+52%` sobre su `SMA200`. En derivados, los minoristas están ligeramente cortos (`ratio 0.90`), los grandes operadores están largos (`1.98`) y el *Open Interest* bajó `-14.2%` en 7 días. Fundamentalmente genera `\$64.1 M USD` en ingresos mensuales y destina el `50%` de los ingresos netos a recompra y quema de tokens (`~\$20 M USD/mes`).
* **Niveles de Precio Exactos:**
  - **Precio de Entrada (Orden Límite de Compra / *Limit Buy*):** **`0.004000 USD`** (sobre la zona de soporte `0.00380–0.00390 USD`).
  - **Precio de Stop-Loss (Orden *Stop-Loss Market*):** **`0.003560 USD`** (`-11.00%` desde la entrada; por debajo de los mínimos de oscilación de `0.00376 USD`).
  - **Precio de Take-Profit (Orden *Take-Profit Limit*):** **`0.005100 USD`** (`+27.50%` desde la entrada; justo bajo el techo del rango en `0.00520 USD`).
* **Montos Exactos a Ingresar en Kraken Pro:**
  - **Cantidad de Unidades a Comprar (`Volume`):** **`72,500 PUMP`**
  - **Monto Total de la Compra (`Total / Notional`):** **`\$290.00 USD`** (`0.58%` del capital; limitado estrictamente al `1%` de los `\$29,000 USD` de profundidad a `10 bps` en Kraken).
  - **Pérdida Neta Máxima si salta el Stop en `0.003560` (incluyendo `1.10%` de costos):** **`\$35.02 USD`** (`0.07%` del capital)
  - **Ganancia Neta Estimada si llega al Target en `0.005100` (después de costos):** **`+\$76.36 USD`** (`+0.15%` del capital, $\text{RR}_{\text{neto}} = 2.18$)

---

## 4. Paso a Paso: Cómo Abrir las Posiciones y el Stop-Loss Manualmente en Kraken Pro

Dado que ninguna IA puede conectarse a Kraken para enviar órdenes, el operador humano debe seguir exactamente estos **6 pasos en la interfaz web de Kraken Pro (`pro.kraken.com`)**:

### Paso 1: Seleccionar el Par Correcto y Modo Spot (Sin Margen)
1. Inicia sesión en **Kraken Pro** y en el selector de mercado (esquina superior izquierda) busca **`NEAR/USD`** (para la Posición 1) o **`PUMP/USD`** (para la Posición 2).
2. En el panel de orden (derecha), verifica que esté seleccionado **`Spot`** (nunca *Margin* ni *Futures*). Verifica que el botón activo sea **`Buy` (Comprar)**.

### Paso 2: Confirmar el Gatillo Técnico Antes de Enviar la Orden
1. A partir del **29 de octubre de 2026 (`00:00 UTC`)**, observa el precio actual:
   - Si el precio está **por encima de la zona de entrada** (por ejemplo, `NEAR` en `4.55 USD` y `PUMP` en `0.00420 USD`) y `BTC/USD` no ha cerrado ningún día bajo `76,000 USD`, puedes dejar cargada la orden **`Limit`** en `4.4000` (`NEAR`) y `0.004000` (`PUMP`), **o bien** esperar a que el precio toque la banda `4.35–4.42` (`NEAR`) / `0.00395–0.00402` (`PUMP`) y cierre una vela de 1 hora (`1H`) por encima del soporte (`4.25` en `NEAR`, `0.00380` en `PUMP`).
   - **Si antes de llenarse la orden `NEAR` cierra un día por debajo de `4.2500 USD` o `PUMP` cierra un día por debajo de `0.003760 USD`**, **cancela la orden inmediatamente** porque el soporte fue perforado.

### Paso 3: Configurar la Orden de Entrada (`Limit Buy`)
1. En **Order Type (Tipo de Orden)** selecciona **`Limit` (Límite)**.
2. En **Limit Price (Precio Límite)** escribe:
   - Para `NEAR/USD`: **`4.4000`**
   - Para `PUMP/USD`: **`0.004000`**
3. En **Quantity / Volume (Cantidad)** escribe:
   - Para `NEAR/USD`: **`187.84`** (horario diurno con buena liquidez) o **`93.92`** (horario nocturno). Verifica que el recuadro `Total` marque **`826.50 USD`** (o **`413.25 USD`**).
   - Para `PUMP/USD`: **`72500`**. Verifica que el recuadro `Total` marque **`290.00 USD`**.

### Paso 4: Adjuntar el Stop-Loss Automático (`Conditional Close` / Cierre Condicional)
> [!CAUTION]
> **NUNCA envíes la orden de compra sin dejar programado el Stop-Loss en el mismo boleto de orden.**

1. En la parte inferior del mismo formulario de orden de Kraken Pro, activa la casilla **`Conditional Close` (Cierre Condicional)** o **`Stop Loss`** vinculada a la compra (`OTO` — *One Triggers the Other*):
   - En **Conditional Order Type** selecciona **`Stop Loss`** (orden Stop-Loss a mercado, para garantizar la salida inmediata si se rompe el nivel).
   - En **Stop Price (Precio de Disparo del Stop)** escribe:
     - Para `NEAR/USD`: **`4.0200`**
     - Para `PUMP/USD`: **`0.003560`**
2. Haz clic en **`Buy NEAR with USD`** / **`Buy PUMP with USD`** y confirma en la ventana emergente que:
   - Es una orden **Spot** (sin apalancamiento).
   - Tiene adjunto el **Conditional Close Stop-Loss** en `4.0200` (`NEAR`) o `0.003560` (`PUMP`).

### Paso 5: Colocar el Take-Profit Una Vez Ejecutada la Compra
1. Tan pronto como la orden límite de compra se ejecute (*Filled*):
   - Verifica en la pestaña **`Open Orders` (Órdenes Abiertas)** que la orden de venta **`Stop Loss`** por el total de las unidades (`187.84 NEAR` o `72,500 PUMP`) haya quedado **activa**.
   - Si tu interfaz de Kraken Pro permite orden combinada **`OCO` (*One-Cancels-the-Other*: Stop-Loss + Take-Profit simultáneos)** al editar o crear la salida, fija el **Take-Profit Limit** en **`5.4000 USD`** (`NEAR`) y **`0.005100 USD`** (`PUMP`).
   - Si utilizas el `Conditional Close` simple (que ocupa el saldo en la orden `Stop Loss`), **mantén siempre prioridad absoluta en la orden física de `Stop Loss` (`4.0200` / `0.003560`)** y configura una alerta en `5.35 USD` (`NEAR`) y `0.00505 USD` (`PUMP`); cuando el precio alcance `5.4000` o `0.005100`, cancela el Stop-Loss y ejecuta la venta en el objetivo.

### Paso 6: Reglas de Gestión, Caducidad y Prohibiciones Durante la Operación
1. **Caducidad de órdenes no ejecutadas:** Si llega el **lunes 2 de noviembre de 2026 a las `00:00 UTC`** (`19:00` del domingo 1 de noviembre en Colombia) y alguna de las dos órdenes límite **no se ha llenado**, **cancélala manualmente** en la pestaña `Open Orders`. (Especialmente crítico en `PUMP`, que tiene desbloqueo estimado hacia el 12 de noviembre).
2. **Prohibición de mover el Stop-Loss hacia abajo:** Una vez abierta la posición, el Stop-Loss en `4.0200` (`NEAR`) y `0.003560` (`PUMP`) **jamás se baja ni se desactiva**.
3. **Salida por tiempo:** Si transcurren **21 días calendario** desde la compra y la posición no ha tocado ni el Stop-Loss ni el Take-Profit, se cierra manualmente a precio de mercado.
4. **Registro en Bitácora:** Anota el ID de orden de Kraken, hora UTC de ejecución, precio promedio real de llenado y comisión pagada en `research/EXECUTION_TEMPLATE.md` para mantener reconciliado el motor de riesgo.
