# Opinión actual de Codex sobre Forebank

Fecha: **2026-10-25**, America/Bogota. Autor: **Codex**. Estado: **criterio de trabajo vigente**, sin recomendación sobre un activo concreto.

## Valoración

El laboratorio es una base funcional para adquirir datos, reproducir análisis y estructurar decisiones auditables, y está listo para comenzar la investigación con ambas IAs. La última verificación local es de 70 pruebas aprobadas. El código está publicado y la CI en Linux/Windows aprobó instalación, lint, pytest, demo y contratos. CoinGecko, FRED, Kraken y DefiLlama respondieron en una colección real sin warnings. Estos hechos comprueban funcionamiento; no demuestran una ventaja de inversión ni validan el rendimiento de una estrategia.

Considero adecuado separar los techos máximos del mandato —MDL 3% y MDD 6%— de los umbrales operativos —2% y 4%— y reservar riesgo para posiciones y órdenes pendientes. Sobre 50.000, los máximos nominales iniciales son 1.500 y 3.000; los operativos son 1.000 y 2.000. La reserva inicial adicional es 200 y el riesgo por trade se limita inicialmente a 125, sujeto a liquidez y al resto del presupuesto. La moneda USD sigue siendo provisional.

## Investigación y toma de decisiones

Una investigación útil no requiere conocer toda la información del mercado. Debe cubrir los factores capaces de cambiar la tesis, el tamaño, la ejecución o la pérdida prevista; contrastar afirmaciones materiales y buscar evidencia contraria. Cuando más búsquedas resulten redundantes, corresponde cerrar el alcance, explicar por qué hay información suficiente y decidir.

Aceptaría una propuesta con incertidumbre residual si está identificada, tiene consecuencias comprensibles y mitigaciones proporcionales, y ambas IAs la aceptan de manera independiente. Un faltante que impida calcular el riesgo o ejecutar válidamente sigue bloqueando. El consenso no transforma datos deficientes en hechos ni demuestra rentabilidad.

La congruencia importa más que acumular indicadores: tesis, horizonte, señal, reglas de entrada/salida, invalidación, costos, tamaño y evidencia empírica deben describir el mismo sistema. Un backtest EMA no valida una propuesta con otras reglas. Una muestra corta no debe presentarse como prueba de robustez.

## Límites que afectan la decisión actual

- No hay todavía una propuesta real de inversión ni una revisión real de Claude. No emito una aprobación de trading en este documento.
- El estado vivo de cuenta, la moneda definitiva y fees requieren verificación antes de ejecutar. La lista de activos ya se puede leer; mapear identificadores y comprobar elegibilidad es el primer trabajo de research, sin sustituciones automáticas de tickers ambiguos.
- El control de riesgo actual se ejecuta al invocarse; no vigila continuamente el equity. El operador debe supervisar el MDL y los stops.
- El código, pruebas, contratos y guías están integrados en el repositorio. Si Claude usa otro entorno, debe instalar el paquete y configurar allí sus claves de manera privada; el repositorio no distribuye secretos.

Evidencia de preparación: [reporte](../docs/READINESS.md), [CI aprobada](https://github.com/carolinehernandez1126-ui/Forebank/actions/runs/40269345762), código validado en commit `f3e89de984ca61368fabaf461ef689ac11b37271`.

## Siguiente trabajo útil

Revisar el universo de activos, contrastar la implementación con Claude, formular hipótesis concretas y evaluar cada sistema con datos pertinentes y costos realistas. Al cerrar la investigación, emitir un resumen detallado de trading o un descarte razonado, indicando qué condición justificaría reconsiderarlo.
