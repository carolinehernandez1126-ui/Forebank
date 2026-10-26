# Conclusiones — siguientes veinte activos

**Codex · 26 de octubre de 2026, America/Bogota.** Investigación independiente de Claude. Universo del Excel, A12:A31: BNB, BONK, BTC, CRV, DOGE, DOT, ENA, ETC, ETH, ETHFI, FARTCOIN, FIL, FLOKI, GRASS, HBAR, HYPE, ICP, INJ, JTO y JUP. El propietario confirmó que «CVR» de A15 significa CRV (Curve). No se alteró el Excel ni se saltaron filas. Siguiente activo pendiente: A32, KAITO.

**Decisión: conservar BTC → ETH → HYPE → DOGE como candidatos principales de compra condicionada.** Alternativas secundarias: INJ, CRV, ENA, HBAR, BONK, FLOKI y ETHFI. BNB no alcanza RR neto 2; DOT/FIL/ICP/JTO/JUP tienen stops incompatibles con el soporte; ETC/FARTCOIN fallan ejecución; GRASS falla ejecución y objetivo. Se descartan esas configuraciones, sin prohibir permanentemente los activos.

No hay compra inmediata ni señal al corte. Esperar un rechazo de soporte confirmado al cierre de una vela de una hora, precio válido en la siguiente barra y RR neto ≥ 2. Primera reconsideración: **29 de octubre, 00:00 UTC**, tras comprobar el comunicado FOMC de la reunión 27–28 de octubre y actualizar los datos. No dejar órdenes esperando desde hoy con estas cotizaciones. El [estudio detallado](ESTUDIO_FINAL.md) explica fuentes, contraevidencia, fórmulas, actualización de niveles, gestión y revisión propia.

| Candidato | Zona de entrada USD | Stop | Target | RR neto base | Horizonte máximo |
| --- | --- | --- | --- | --- | --- |
| BTC | 79120.8–79303.6 | 78936.4 | 84731.0 | 3.657 | 7 días |
| ETH | 2279.8–2288.08 | 2246.53 | 2462.66 | 2.233 | 5 días |
| HYPE | 74.33–74.69 | 72.93 | 81.76 | 2.414 | 5 días |
| DOGE | 0.074668–0.0749482 | 0.0734556 | 0.0845546 | 3.781 | 5 días |

Se admite un **piloto real con ventaja estadística no demostrada**; no se exige un backtest ganador. Contraevidencia: BTC y DOGE perdieron en el diagnóstico de las reglas específicas; ENA obtuvo una ganancia pequeña. Hay referencias T/R con holdout positivo y una o dos operaciones, sin demostrar ventaja. HYPE solo dispone de 271 velas diarias: no admite warmup de 200, desarrollo y holdout de 120. Su resultado completo positivo no es OOS válido. Duplicar costos lleva los ratios de BTC/ETH/HYPE por debajo de 2. Los ratios altos de HBAR/ETHFI no son probabilidades de éxito ni prioridad automática.

Riesgo del piloto propuesto: **máximo 0.05% del equity por trade**, una posición experimental simultánea y una entrada nueva por día UTC. Pausa por pérdida diaria de 0.15%, pérdidas acumuladas de 0.50%, 20 cierres o 30 días desde el primer fill, lo primero que ocurra; revisión temprana tras 5 trades o pérdida neta de 5 R. Presupuesto compartido entre todas las tandas, sin reiniciarlo por activo o IA. Se mantienen MDL/MDD operativos de 2%/4%, máximos de 3%/6%, reserva y límites de exposición. No se cambió la política para aprobar. Los contadores adicionales del piloto requieren supervisión manual; el Lab no los vigila automáticamente.

**Revisión propia: aprobación condicional del diseño; abstención de aprobar ejecución.** Cuenta, moneda, fees, reconciliación, hashes nuevos, aceptación de incertidumbre por ambas IAs y motor de riesgo vigente siguen siendo requisitos críticos. No existe firma de Claude ni READY; no se enviaron órdenes. USD es la cotización de mercado utilizada, sin confirmar moneda ni saldo actual de la cuenta.

Verificación: 20 datasets reales, 60 series de calidad, 40 referencias T/R, 20 diagnósticos causales, dos libros por activo y fuentes primarias. Las 70 pruebas offline del Lab, ruff y controles específicos de causalidad, gaps, doble toque, costos y PnL pasaron. Solo se publican el estudio y las conclusiones. Datos y scripts de sesión quedan locales para preservar el aislamiento y el alcance pedido. Un replay exacto requiere esos snapshots; los dos documentos no contienen todos los insumos.

Estudio SHA256: `8e0e321dc63d04180140f8de9e6f32538cf3c35a9956249e52643697f9d48c52`. Esta revisión narrativa corresponde al informe; no reemplaza una Review operativa de Proposal, dataset, política y cuenta vigentes.
