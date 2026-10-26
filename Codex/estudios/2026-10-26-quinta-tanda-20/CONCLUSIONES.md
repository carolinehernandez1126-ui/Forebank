# Conclusiones — A52:A71

**Codex · 26 de octubre de 2026, America/Bogota.** Veinte filas revisadas en orden, diecinueve datasets spot reales y un producto fuera del alcance. **Prioridad: SOL → XRP → XLM → UNI.** Alternativas secundarias: SUI, TAO, SHIB, VIRTUAL, WLD, WIF, TON, TRUMP, STX.

XYZ100 se registra como perpetuo, sin simular spot. ZEC tiene una subzona aritméticamente válida, pero el piloto se pospone hasta verificar NU7 y normalización del mercado.

No hay compra inmediata. Esperar rechazo de soporte confirmado al cierre de una hora, precio válido en la siguiente barra, RR neto ≥2 y límites de ejecución. Primera reconsideración: **29 de octubre, 00:00 UTC**, tras comprobar el comunicado FOMC y recoger datos nuevos. No dejar órdenes con los precios históricos del informe. Cuenta reconciliada, moneda/fees efectivos, revisión real de Claude y gate vigente siguen pendientes. No existe READY ni se enviaron órdenes.

| Principal | Zona USD | Stop | Target | RR neto / doble costo | Horizonte máximo |
| --- | --- | --- | --- | --- | --- |
| SOL | 98.51–98.88 | 96.93 | 106.09 | 2.009 / 1.207 | 5 días |
| XRP | 1.2533–1.25875 | 1.24841 | 1.45518 | 7.522 / 4.393 | 7 días |
| XLM | 0.165886–0.16656 | 0.16329 | 0.19 | 4.225 / 2.829 | 5 días |
| UNI | 6.5078–6.5543 | 6.3137 | 7.2609 | 2.025 / 1.451 | 5 días |

Se permite un **piloto real con ventaja estadística desconocida**. No se exige un backtest ganador; se preservan sus pérdidas y limitaciones. Los targets remotos y stops estrechos pueden producir ratios grandes sin demostrar valor esperado positivo. SOL solo cumple en una subzona inferior al techo bruto: 98.51–98.88 USD. Es una intersección algebraica del requisito de RR, sin mover stop/target ni alterar fills históricos, aclarada después de observar los datos. UNI apenas supera RR2 al costo base; XRP/XLM deben remontar barreras y el diagnóstico de XLM es adverso.

Máximo propuesto **0.05% del equity por trade**, una posición experimental global y una entrada nueva por día UTC. Pausa por pérdida diaria de 0.15%, pérdidas acumuladas de 0.50%, 20 cierres o 30 días desde el primer fill, lo primero que ocurra; revisión tras 5 cierres o pérdida neta de 5 R. Presupuesto compartido entre las 70 filas y ambas IAs, sin reinicio por tanda. Permanecen MDL/MDD operativos de 2%/4%, techos de 3%/6%, reserva y límites de exposición. El overlay adicional requiere supervisión humana; no se implementó un monitor automático.

**Revisión propia: aprobación condicional del diseño, abstención de aprobar ejecución.** La hipótesis de rebote de 5/7 días, entrada limitada, stop estructural, target, costos, tamaño, invalidación y seguimiento se explican en el [estudio detallado](ESTUDIO_FINAL.md). No se atribuye aceptación de incertidumbre o aprobación a Claude. Una fuente adicional genérica no cambiaría las decisiones; se cierra la investigación con triggers concretos.

Verificación: 57/57 series de calidad; 14 filtros aritméticos/calidad/ejecución aprobados, que no equivalen a órdenes. Referencias T/R y diagnóstico Q separados, dos libros por activo, fuentes primarias y control de contradicciones. Base del Lab: 70 pruebas offline y ruff aprobados. Datos y scripts quedan locales; un replay exacto requiere esos insumos. Solo se publican los resultados finales.

SHA256 del estudio: `d6c62c84f74b5e3b02566ac49f9ab78018f3ec766471dd5ce0272d8f37db8ddf`. La comparación con Claude debe mostrar diferencias de instrumento, fecha, costos, señal y riesgo; no se establece un ganador por número de ideas o confianza verbal.
