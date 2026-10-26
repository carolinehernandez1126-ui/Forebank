# Conclusiones V2 — piloto bajo incertidumbre

**Codex, 26-10-2026.** Sustituye el veto general por falta de backtest ganador del estudio anterior.

1. **Se puede proponer un piloto real sin ventaja estadística demostrada.** No se exige OOS positivo, significancia o simulación ganadora como permiso universal. Se requiere una hipótesis razonada, costos/riesgo coherentes y aceptación expresa de la incertidumbre por ambas IAs.
2. Propuesta inicial: riesgo hasta **0.05% por trade**, una posición del piloto y una entrada nueva por día UTC; pausa diaria 0.15% y presupuesto total 0.50%. Revisión a 5 trades o 5R perdidos; fin de tanda a 20 trades/30 días/presupuesto/invalidación, lo primero. Son reglas propuestas con control humano, no contadores nuevos implementados en el Lab.
3. Permanecen MDL/MDD operativos **2%/4%**, máximos **3%/6%**, reserva y todos los límites de cuenta/liquidez. Pérdidas y gaps pueden superar stops; tamaño pequeño no crea rentabilidad. No reiniciar presupuesto, promediar pérdidas o escalar para recuperar.
4. Backtests sirven para diagnóstico y contraevidencia, no para buscar un gráfico que apruebe. Resultados adversos no se ignoran. Ventaja desconocida y expectativa negativa conocida son situaciones diferentes.
5. Nuevo snapshot Kraken **11:36 UTC**: el diseño experimental P1 no tiene señal y no alcanza RR neto 2 en estos cinco. AAVE ask135.22/stop133.27/primer target139.82 da RR~0.901. Esperar esa entrada responde a precio/costos, no a OOS. El techo algebraico133.97 no es orden activa. No se aleja el target para fabricar ratio.
6. AIXBT ahora pasa spread y mínimo/profundidad en la fotografía nueva:16.51bps y USD6.53 de capacidad; se retira el bloqueo instantáneo viejo, manteniendo cautela por libros variables y horas sin negociación.
7. **Revisión de Codex:** acepto el marco de piloto con ventaja no demostrada; no apruebo una orden inexistente ni atribuyo revisión a Claude. Para ejecutar: cuenta y costos confirmados, señal/precios vigentes, dos revisiones del mismo hash y gate. Sin condición indefinida de paper trading.

[Estudio final V2: criterios, protocolo, snapshot, límites, fuentes y revisión](ESTUDIO_FINAL.md).

SHA256 del estudio revisado: `1ac0e63b4c2a38ba601e93cf8ee6b430541604f69a11d25bbb657e018be855d9`.

No se han ejecutado operaciones, cambiado el motor de riesgo o confirmado una cuenta por inferencia. Solo se publican resultados finales y correcciones trazables, sin conversaciones ni información privada.
