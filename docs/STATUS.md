# Estado del proyecto

Fecha de entrega: **2026-10-25**, America/Bogota. Versión 0.1.0.

Mandato actualizado por el propietario: capital **50.000**, MDL máximo **3%**, MDD máximo **6%**. Se aplican operativos **2%/4%**, reserva adicional de 20% del MDL operativo y máximo 0,25% por trade. USD permanece provisional; el estado actual de cuenta no está reconciliado por informar el capital nominal.

## Implementado

- Paquete Python instalado en `.venv` y comando `lab`; dependencias probadas fijadas en requirements-lock.txt.
- Contratos Pydantic y JSON Schema para dataset, cuenta, política, propuesta y revisión.
- Kraken público: instrumentos, velas cerradas por timeframe y libro con bid/ask/profundidad.
- Enriquecimiento opcional CoinGecko Demo, DefiLlama TVL de cadena y FRED actual; secretos locales y faltantes explícitos.
- Snapshots/cache y diario SQLite; hashes canónicos y procedencia de fuentes.
- Indicadores técnicos, estadística de retornos/colas y correlaciones alineadas.
- Baseline EMA walk-forward con costos, benchmark cash/buy-and-hold y bootstrap por bloques.
- Importación de histórico OHLCVT Kraken desde CSV verificado por el operador.
- MDL interno, reserva, drawdown, riesgo de posiciones/órdenes pendientes, sizing, exposición, liquidez, mínimos y ticks; checks de calidad/fechas.
- Bloqueo diario persistente si el Lab observa una brecha; bloqueo de drawdown que no reinicia al cambiar el día.
- Gate de dos revisores diferentes, mismo hash, vigencia y ausencia de blockers. Plantillas de revisión en abstención, sin firmas ficticias.
- Propuesta v2 con suficiencia de información, cierre de investigación, horizonte, escenarios, alternativas, congruencia y matriz de gaps. Admite incertidumbre material aceptada; no exige información perfecta.
- Revisiones con aceptación expresa de incertidumbre y confirmación de coherencia; `decide` escribe resumen detallado `.md` además del JSON, aun en WAIT.
- Documentación, mandatos de especialistas, instrucciones AGENTS.md/CLAUDE.md, plantillas de resultados y CI offline Linux/Windows preparada.
- Repositorio Git local inicializado en `main`; destino real confirmado: `carolinehernandez1126-ui/Forebank`. Usuario de trabajo: `jsforeroc80-debug`, colaborador. Se publicó la carpeta Codex en main; la integración del código completo del Lab sigue pendiente.

## Verificado localmente

- **70 pruebas sin red aprobadas**: riesgo, consenso, expiración, cambios de hashes, bloqueo persistente, datos mutables, cache sin secretos, retries, causalidad, costos y demo; ampliadas con límites operativos/máximos, aceptación de incertidumbre y resumen de trading.
- Lint/formato, consistencia de schemas, compilación Python y `pip check`.
- Instalación editable del comando `lab` y demo offline completa.
- Descarga real de **BTC/USD y ETH/USD en Kraken**, análisis 1h/4h/1d y validación de calidad de los tres timeframes.
- Descarga real de TVL Ethereum de **DefiLlama**. En la verificación de preparación posterior, CoinGecko Demo y FRED también respondieron con las claves locales: ETH y las cuatro series macro configuradas, sin warnings.
- Backtest real de la ventana pública BTC y correlaciones BTC/ETH. Estas ejecuciones comprueban funcionamiento, **no validan una estrategia para operar**.
- Los outputs reales permanecen en `data/smoke-*.json` y `outputs/smoke-*`, fuera de Git; ejemplos compartibles son exclusivamente sintéticos.

La validación TLS utiliza el almacén del sistema; no se desactivó verificación de certificados. No se ejecutaron órdenes ni se consultaron cuentas privadas. El workflow remoto de GitHub todavía no se ha ejecutado.

Acceso GitHub probado con GH_TOKEN local: identidad **jsforeroc80-debug**, repositorio **carolinehernandez1126-ui/Forebank**, público y activo, rama principal **main**, permisos de lectura y escritura confirmados por la API (sin administración). La prueba fue solo de lectura; no publicó cambios ni modificó la sesión global. El token no se mostró ni se incorporó al repo.

Publicación posterior autorizada: carpeta **Codex/**, con 20 documentos de respuestas, opinión actual, protocolo de registro y copias de contexto. Commit **e41c4fe93aa77c30ee633e5d741758193e03ab11**, creado como jsforeroc80-debug sobre el historial remoto existente, sin force-push. Se verificaron todos los hashes de los nuevos archivos y la preservación de las 4 entradas existentes del árbol, incluyendo README y lista de activos Excel. No se publicó código del Lab, .env, cuentas, bases de datos ni snapshots privados en esta operación. La revisión documental no detectó enlaces internos rotos ni patrones de credenciales.

## Pendiente del propietario

1. Confirmar moneda y activos seleccionados. El capital y los máximos ya están informados; no volver a solicitarlos. BTC/ETH/SOL son ejemplos de configuración.
2. Verificar costos reales, moneda y bases operativas pendientes. `policy_verified=false` y cuenta de ejemplo no reconciliada mantienen el gate bloqueado; esto no desconoce el mandato de capital/riesgo ya confirmado.
3. Si Claude trabaja en otro entorno, configurar allí de forma privada las claves de datos. Las claves del workspace actual ya se verificaron; no se copian mediante GitHub.
4. Reconciliar `private/account.json` con holdings, órdenes pendientes, flujos y baseline diario.

## Pendiente de investigación / siguiente fase

- Revisión real de Claude del código y metodología; no existe todavía su aprobación.
- Hipótesis elegidas, histórico largo, simulador específico de cada sistema, holdout y paper trading. No hay trades reales recomendados en esta entrega.
- Sincronización de cuenta por API de solo lectura y reconciliación automática.
- Monitor continuo y alertas con control de riesgo intradía. El gate actual solo comprueba al invocarse.
- Registro automatizado de fills/PnL: actualmente se conserva mediante la plantilla de ejecución y reconciliación manual.
- Identidad verificable de agentes, orquestación por APIs y presupuesto de modelos si se solicita una fase desatendida.
- Datos fundamentales especializados por activo, vintages macro y stress tests de ejecución intrabar.

El proyecto es una base funcional de research y revisión, no un sistema probado de rentabilidad ni un mecanismo de control de riesgo aplicado por el exchange.
