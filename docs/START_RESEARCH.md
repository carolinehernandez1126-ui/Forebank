# Inicio coordinado de investigación

## Alcance

El Lab suministra datos y análisis; Codex y Claude investigan y revisan por separado. Las claves FRED y CoinGecko se mantienen en `.env` local. Si Claude corre en otro equipo/entorno, allí se instalan las dependencias y se configuran sus claves por un canal privado. Clonar GitHub no copia secretos.

Capital confirmado: 50.000; máximos MDL 3%, MDD 6%; operativos 2%/4% y reserva adicional. La moneda y el estado actual de cuenta no se deducen del capital nominal. No volver a preguntar parámetros ya informados.

## Instrucción para ambas IAs

> Lee AGENTS.md, CLAUDE.md (si eres Claude), docs/STATUS.md, docs/RISK.md, docs/DECISION_STANDARD.md y docs/COLLABORATION.md. Usa archivos_de_apoyo/lista_activos.xlsx como universo de entrada; confirma identificadores, moneda, venue y elegibilidad spot antes de consultar cada activo. No sustituyas un ticker ambiguo ni un producto no compatible por otro de nombre parecido. Investiga técnico, fundamental y estadístico con el Lab y fuentes primarias web. Cierra la investigación cuando exista información suficiente; registra desconocidos, contraevidencia y alternativas. Diseña estrategias congruentes y propuestas bajo los límites operativos. Escribe tu propia revisión y nunca la de la otra IA. Genera un resumen detallado de trading que explique cómo se llegó a cada decisión. Si no hay una oportunidad defendible, descarta o define un trigger concreto. No ejecutes órdenes ni verifiques una cuenta por inferencia.

## Primera sesión

1. Actualizar el repositorio e instalar Python 3.12 y requirements-lock.txt; instalar el paquete editable y ejecutar `lab demo`.
2. Resolver el universo por identificadores exactos. `config/assets.toml` contiene BTC/ETH/SOL para las pruebas de conectividad, no la selección final del universo. Registrar mapeos, ambigüedades, pares no listados y productos fuera del alcance spot; investigar por web cuando corresponda, sin habilitar trades inválidos.
3. Recoger datos con `collect --enrich`, generar dossier, validar calidad y registrar qué backtest aplica a las reglas propuestas. No usar la estrategia EMA de referencia para validar otro sistema.
4. Preparar investigación antes del snapshot final de mercado/cuenta. Luego congelar propuesta, hashes, entradas y vencimiento; ambas IAs revisan esa versión.
5. `decide` emite JSON y resumen Markdown. Una cuenta no reconciliada bloquea ejecución, pero no impide investigar, descartar activos o diseñar hipótesis.

## Antes de una ejecución manual

Confirmar moneda, fees efectivos y snapshot vigente de cuenta con posiciones, órdenes pendientes y baseline diario. Las dos revisiones deben ser reales y la decisión estar vigente. El Lab actual no vigila continuamente el MDL; el operador debe supervisarlo. Estos requisitos no deben retrasar el inicio de la investigación.
