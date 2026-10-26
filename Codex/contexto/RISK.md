# Política de riesgo para capital propio

## MDL: distinción necesaria

El usuario confirmó Kraken Pro con capital propio y **capital 50.000, MDL máximo 3%, MDD máximo 6%**. Se adoptan umbrales operativos menores, autorizados por su instrucción de dejar colchón. El artículo oficial de [Maximum Daily Loss](https://support.kraken.com/articles/maximum-daily-loss-mdl-explained) describe Kraken Prop; estos porcentajes son el mandato interno del propietario, no una atribución de reglas de Prop a su cuenta.

USD permanece provisional hasta confirmar la moneda; las cantidades siguientes son unidades de cuenta sobre una base de 50.000. `policy_verified=false` conserva el estado pendiente de moneda/costos y bases operativas, sin desconocer los parámetros ya confirmados. No representa una cuenta reconciliada en vivo.

| Regla interna | Default |
|---|---:|
| Capital de referencia confirmado | 50.000 |
| MDL máximo del mandato | 3% = 1.500 al inicio |
| MDL operativo sobre equity de apertura | 2% = 1.000 al inicio |
| Riesgo nuevo por trade | 0,25% del equity actual |
| Riesgo total adicional a stops | 0,50% del equity actual |
| Exposición bruta spot | 50% del equity |
| Exposición por activo | 20% del equity |
| MDD máximo del mandato | 6% = 3.000 al inicio |
| MDD operativo | 4% = 2.000 al inicio |
| Reserva del presupuesto MDL operativo | 20% = 200 al inicio |
| Reward/risk después de costos | 2,0 mínimo |
| Reinicio diario | 00:00 UTC, interno |
| Comisión / slippage por lado | 40 / 15 bps, supuestos verificables |

El reinicio 00:00 UTC corresponde a las 19:00 del día anterior en Bogotá. Es una elección interna editable, no una regla atribuida a Kraken.

Riesgo nuevo por trade: hasta **125** sobre equity de 50.000; riesgo adicional conjunto a stops: hasta **250**. Los topes por exposición, liquidez y presupuesto disponible pueden reducirlos. La reserva deja inicialmente 800 de espacio diario antes de reservar riesgo abierto, aunque el stop operativo diario esté en 1.000. No se intenta agotar esos importes.

Para drawdown se adopta una base conservadora: **el mayor entre capital inicial y peak equity reconciliado**, con ambos floors sobre esa base. Inicialmente son 48.000 operativo y 47.000 máximo. Si se gana capital, los pisos suben; no se relajan tras pérdidas. Este criterio es interno y explícito, no una definición de MDD del exchange.

## Estado de cuenta

`private/account.json` debe reflejar la cuenta de trading completa, en la misma moneda de cotización que la propuesta. No hay conversión FX automática.

- `day_start_equity`: valor de mercado de la cuenta al instante exacto del reinicio, incluyendo tenencias y PnL no realizado.
- `equity`: equity actual después de comisiones, pérdidas/ganancias realizadas, no realizadas y otros cargos. No restar nuevamente los mismos cargos.
- `net_external_flows_today`: depósitos menos retiros desde el reinicio. El ajuste evita que un depósito o retiro se confunda con rendimiento.
- `peak_equity`: máximo comparable para drawdown. Mantener una serie ajustada por flujos; ante movimientos de capital se exige reconciliación de la base, no suponer que las cifras antiguas son comparables.
- `free_cash`: efectivo realmente utilizable, descontadas reservas de órdenes. No es el saldo total si existen tenencias.
- `positions`: **todas** las posiciones y órdenes pendientes, con valor bruto y riesgo **adicional desde la valoración actual hasta el stop**, incluyendo costos de salida. Una orden pendiente incluye el riesgo desde su entrada. Evitar contar una orden de salida protectora como otra compra.
- `protected`: confirmar que la posición/orden dispone de protección operativa; una posición sin ella bloquea nuevas compras.
- `verified`, `reconciled`: solo true después de confirmación del propietario sobre los datos reales.
- `daily_lockout`: bloqueo persistente declarado por el operador si se alcanzó el límite en cualquier momento.

El ejemplo de 50.000 refleja el mandato de capital, pero su reparto completo en cash y timestamp son placeholders; no prueban el equity ni las posiciones actuales. El software no puede detectar posiciones omitidas. El estado vence a los 300 s por defecto.

## Fórmulas

Para una compra spot, sean `E0` equity de apertura diaria, `E` equity actual, `F` flujos netos, `d` MDL operativo, `b` reserva, `Ropen` riesgo adicional conjunto y `C=(fee_bps+slippage_bps)/10000`:

```text
Eajustado = E - F
floor_diario = E0 × (1-d)
floor_diario_maximo = E0 × (1-0,03)
reserva = E0 × d × b
base_drawdown = max(capital_inicial, peak_equity)
floor_drawdown = base_drawdown × (1-0,04)
floor_drawdown_maximo = base_drawdown × (1-0,06)
riesgo_unitario = entrada - stop + (entrada + stop) × C

presupuesto = min(
    E × riesgo_por_trade,
    Eajustado - floor_diario - reserva - Ropen,
    E × riesgo_total - Ropen,
    E - floor_drawdown - reserva - Ropen,
    Eajustado - floor_diario_maximo - reserva - Ropen,
    E - floor_drawdown_maximo - reserva - Ropen
)

q_max = floor_a_precision(min(
    max(0,presupuesto) / riesgo_unitario,
    espacio_exposición_bruta_y_activo / entrada,
    free_cash / (entrada × (1+C)),
    profundidad_asks_a_10bps × participación_máxima / entrada
))

RR_neto = (target - entrada - (target+entrada) × C) / riesgo_unitario
```

El cálculo de costos usa una aproximación conservadora de primer orden. Se exige `stop < entrada < target`, cantidad <= q_max, tick real, precisión y mínimos de Kraken. La profundidad es una fotografía, no liquidez asegurada. La política no concede crédito por correlaciones: supone que todos los stops se pierden juntos.

Ejemplo: E0=50.000, E=49.300, MDL operativo=2%, reserva=200 y Ropen=75 deja solo 25 unidades monetarias de presupuesto diario para el trade nuevo. Dos IAs aprobando una operación no crean más presupuesto. Los operativos deben ser estrictamente inferiores a los máximos; Pydantic rechaza igualdad o inversión de los umbrales y configurar un techo mayor que el mandato de 3%/6%.

## Bloqueos

Se bloquean propuesta vencida, inputs futuros, velas abiertas o con gaps, pocas observaciones, datos sintéticos, moneda diferente, spread/exposición/tamaño excesivos, ausencia de verificaciones, instrumento no online, referencias hash diferentes y revisiones faltantes o disidentes.

`min_bars` y `required_intervals` forman parte de la política y su hash: por defecto se exigen al menos 250 velas en 1h/4h/1d. Quitar un timeframe o bajar el historial exige una política diferente y nuevas revisiones; el motor no acepta menos de 201 velas para sus indicadores de 200 periodos.

Si el Lab observa equity ajustado <= floor diario, deja un lockout en SQLite para ese alias de cuenta y día. Una brecha del drawdown máximo deja un bloqueo de cuenta que no se reinicia al día siguiente; requiere detenerse y revisar la política con el propietario, no un bypass automático. El operador también debe registrar cualquier brecha observada fuera del Lab. No eliminar la base ni cambiar de alias para eludir el bloqueo. La ausencia de vigilancia continua significa que un descenso y recuperación entre consultas puede pasar inadvertido.

## Límites prácticos

Un stop no garantiza precio; gaps, deslizamiento, interrupciones y ejecución humana pueden superar el modelo. El Lab no es un freno del exchange. Las cifras de fee deben reflejar el par y tier real; por defecto se presupone costo por ambos lados. La rentabilidad histórica no valida el MDL, y el backtest de referencia no simula stops ni drawdown diario intrabar.

Kraken describe el stop loss como una orden que se activa a mercado; el colchón cubre parte del riesgo de ejecución, sin garantizar un fill en el precio del stop. Fuente: [Stop loss orders](https://support.kraken.com/articles/7699391647892-stop-loss-orders).

Para inversiones mantenidas varios días, toda tenencia sigue marcada a mercado y consume riesgo diario. Cualquier ampliación a cortos/margen/derivados exige modelar liquidación, collateral, financiación y riesgo de cuenta por separado.
