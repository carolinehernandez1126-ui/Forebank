# Conclusiones — A32:A51

**Codex · 26 de octubre de 2026, America/Bogota.** Veinte filas revisadas en orden, diecinueve datasets spot reales y un producto fuera del alcance. **Prioridad: LTC → LINK.** Alternativas secundarias vigentes: PUMP, POL, PENDLE, OP, MON, RENDER, KAITO, MOODENG. PENGU y ONDO quedan pospuestos tras la revisión cruzada; la adenda del estudio explica fuentes y límites.

SP se registra como producto índice perpetuo, sin simular spot. LIGHTER queda bloqueado por solo 70 velas diarias, por debajo del mínimo vigente. LIT es Litentry legado, un activo distinto de Lighter, y falla ejecución.

No hay compra inmediata. Esperar rechazo de soporte confirmado al cierre de una hora, precio válido en la siguiente barra, RR neto ≥2 y límites de ejecución. Primera reconsideración: **29 de octubre, 00:00 UTC**, tras comprobar el comunicado FOMC y recoger datos nuevos. No dejar órdenes con los precios históricos del informe. Cuenta reconciliada, moneda/fees efectivos, revisión real de Claude y gate vigente siguen pendientes. No existe READY ni se enviaron órdenes.

| Principal | Zona USD | Stop | Target | RR neto / doble costo | Horizonte máximo |
| --- | --- | --- | --- | --- | --- |
| LTC | 55.05–55.29 | 54.1 | 59.83 | 2.181 / 1.368 | 5 días |
| LINK | 11.22675–11.28142 | 11.17366 | 13.69507 | 9.843 / 6.029 | 7 días |

Se permite un **piloto real con ventaja estadística desconocida**. No se exige un backtest ganador; se preservan sus pérdidas y limitaciones. Los targets remotos y stops estrechos pueden producir ratios grandes sin demostrar valor esperado positivo. LTC y LINK se priorizan por ejecución y congruencia; el diagnóstico de LINK pierde un stop y el doble costo invalida el ratio de LTC.

Máximo propuesto **0.05% del equity por trade**, una posición experimental global y una entrada nueva por día UTC. Pausa por pérdida diaria de 0.15%, pérdidas acumuladas de 0.50%, 20 cierres o 30 días desde el primer fill, lo primero que ocurra; revisión tras 5 cierres o pérdida neta de 5 R. Presupuesto compartido entre las 70 filas y ambas IAs, sin reinicio por tanda. Permanecen MDL/MDD operativos de 2%/4%, techos de 3%/6%, reserva y límites de exposición. El overlay adicional requiere supervisión humana; no se implementó un monitor automático.

**Revisión propia: aprobación condicional del diseño, abstención de aprobar ejecución.** La hipótesis de rebote de 5/7 días, entrada limitada, stop estructural, target, costos, tamaño, invalidación y seguimiento se explican en el [estudio detallado](ESTUDIO_FINAL.md). No se atribuye aceptación de incertidumbre o aprobación a Claude. Una fuente adicional genérica no cambiaría las decisiones; se cierra la investigación con triggers concretos.

Verificación: 56/57 series de calidad; 12 filtros aritméticos/calidad/ejecución aprobados, que no equivalen a órdenes. Referencias T/R y diagnóstico Q separados, dos libros por activo, fuentes primarias y control de contradicciones. Base del Lab: 70 pruebas offline y ruff aprobados. Datos y scripts quedan locales; un replay exacto requiere esos insumos. Solo se publican los resultados finales.

SHA256 del estudio: `46b23ff7e9808dfaeb2b6c93d98eec8b95667119e3825543a1817fb780f5227f`. La comparación con Claude debe mostrar diferencias de instrumento, fecha, costos, señal y riesgo; no se establece un ganador por número de ideas o confianza verbal.

La lista independiente se congeló antes de leer Claude. Hash de aquella versión: `dba6dec01d48e2501532cab489282637474f4e811f6996a323bfa5504920ac69`. Esta edición conserva el cuerpo histórico con una adenda visible y prevalente, sin cambiar cálculos o elevar riesgo.
