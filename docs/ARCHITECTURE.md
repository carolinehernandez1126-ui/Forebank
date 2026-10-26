# Arquitectura

## Diseño local reproducible

Un paquete Python y una CLI, sin servidor obligatorio. Codex y Claude leen los mismos archivos JSON/Markdown y ejecutan comandos de análisis. Esto evita depender de una API de modelos para el funcionamiento básico.

| Capa | Implementación | Salida |
|---|---|---|
| Contratos | Pydantic, `models.py`, JSON Schema | Validación estricta de campos, tipos, fechas conscientes de zona |
| Adquisición | HTTPX, `providers.py` | Kraken público + enriquecimiento opcional |
| Persistencia | SQLite WAL, `store.py` | Snapshots con hash, cache, diario de eventos |
| Técnica y estadística | NumPy/Pandas, `analytics.py` | Dossier por timeframe, calidad y correlaciones |
| Investigación empírica | `backtest.py` | Walk-forward, costos, bootstrap por bloques |
| Riesgo | `risk.py` | Sizing máximo y bloqueos deterministas |
| Consenso | `decision.py` | Suficiencia bajo incertidumbre, congruencia y `WAIT` / `READY_FOR_MANUAL_EXECUTION` |
| Resumen de trading | `summary.py` | Tesis, análisis, cierre de investigación, alternativas, reglas, riesgo y revisiones en Markdown |
| Interfaz | `cli.py` | Comandos, JSON y Markdown |
| Colaboración | Archivos, Git/PR y plantillas | Hipótesis, revisiones y resultados saneados |

## Trazabilidad

Cada fuente guarda URL sin claves, parámetros públicos, instante de adquisición, hash del body y body local. El cache conserva la fecha original. Cada dataset tiene instrumentos, bid/ask, profundidad cercana, velas cerradas y procedencia. Los estados de cuenta se mantienen aparte.

La propuesta referencia hashes canónicos de dataset, política y cuenta. Cada revisión referencia el hash de la propuesta completa. Cambiar un precio, límite o evidencia invalida ambas revisiones. El hash es SHA-256 de JSON ordenado y normalizado por el modelo: no es el hash de los bytes indentados del archivo.

Proposal v2 requiere un cierre de investigación razonado y la matriz de incertidumbre. Faltantes materiales aceptados y mitigados pueden pasar; críticos o materiales no aceptados bloquean. Ambas revisiones declaran aceptación de incertidumbre y congruencia. El gate no demuestra semánticamente la calidad de esas declaraciones: la investigación y revisión independientes siguen siendo necesarias.

Un hash comprueba que dos participantes usaron el mismo contenido; no prueba que un dato de entrada sea verdadero ni que proceda realmente de quien declara el archivo. La adquisición controlada, la reconciliación y la revisión de fuentes aportan esas comprobaciones.

El diario SQLite es append-only por la interfaz; **no es inmutable frente al propietario del archivo**. No constituye una firma ni un registro remoto inviolable. GitHub puede aportar historial revisado para resultados saneados.

## Fronteras

La aplicación no ejecuta órdenes, no llama a los modelos ni se queda vigilando continuamente la cuenta. La conformidad se calcula al ejecutar `risk-check` o `decide`. La cuenta es una declaración manual del operador. Si no se registran holdings u órdenes, la estimación de riesgo será incompleta. No se atribuye identidad real a una revisión por escribir `reviewer=claude`.

La ejecución manual debe ser con orden y stop protector revisados en la plataforma. Varias propuestas simultáneas no reservan capital automáticamente: tras aceptar una, incluir su orden pendiente en la cuenta antes de evaluar otra. Revalidar después de cualquier fill/cancelación.

## Evolución

1. MVP actual: adquisición pública, análisis, baseline empírico, riesgo y protocolo de revisiones.
2. Próximo: universo y cuenta reales, hipótesis registradas, paper trading y diario de ejecución.
3. Posterior: sincronización privada de lectura y monitor continuo con lockouts persistentes confiables.
4. Si escala: almacén Parquet/DuckDB para grandes históricos, servicio de lectura o MCP, orquestador de agentes con identidad y gastos acotados.

No hace falta desplegar infraestructura cloud para empezar. Ninguna etapa de ejecución automática se incluye por defecto.
