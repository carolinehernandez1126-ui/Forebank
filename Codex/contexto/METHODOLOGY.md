# Método de investigación

## 1. Definir la hipótesis antes de optimizar

Registrar activo, venue, horizonte, argumento económico, reglas de entrada/salida, criterios de invalidación, parámetros que se probarán, costos, métricas y un holdout final intacto. Registrar también hipótesis descartadas. El resultado puede ser no operar.

No exigir conocimiento total. La investigación debe ser exhaustiva dentro del horizonte y cerrar cuando nuevas fuentes no cambien materialmente la decisión. Ver docs/DECISION_STANDARD.md: gaps críticos bloquean; materiales pueden aceptarse con mitigación y acuerdo explícito. Un resultado razonado bajo incertidumbre no equivale a certeza ni obliga a operar.

## 2. Calidad y universo

Configurar identificadores inequívocos en config/assets.toml. CoinGecko ID no es un ticker; Kraken utiliza identificadores legacy como XBTUSD/XXBTZUSD. El registro AssetPairs gobierna mínimos, precisión, tick y estado. La moneda de cuenta debe coincidir explícitamente con el quote; USD no equivale a USDT/USDC.

Se usan timestamps UTC conscientes de zona y solo velas cerradas. Detectar duplicados, gaps, desorden, datos futuros, faltantes, precios inválidos y falta de historial. No forward-fill silencioso: Kraken puede omitir periodos sin trades. Documentar exclusiones de activos y sesgo de supervivencia.

El endpoint público OHLC es una ventana corta, no un histórico completo. Con 720 horas, una prueba solo cubre alrededor de un mes. Importar CSV oficial, varios regímenes y periodos de estrés antes de atribuir significancia.

## 3. Técnico

Implementado: SMA/EMA 20/50/200, RSI14 suavizado exponencial, MACD12/26/9, ATR14, ADX14 aproximado con suavizado exponencial, Bollinger20, Donchian20, OBV, VWAP móvil20, VWAP diario UTC y z-score de volumen. Revisar tendencia en 1h/4h/1d por defecto.

El warm-up exponencial difiere del seed SMA exacto de algunas plataformas Wilder; no exigir coincidencia al último decimal con Kraken. El VWAP se aproxima con precio típico y volumen de velas, no con ticks; el VWAP de una vela diaria carece de detalle intradía. Donchian incluye la vela cerrada actual; una regla de ruptura ejecutada durante esa vela debe usar el canal desplazado.

No existe una lista universal de «todos los indicadores necesarios»: añadir una característica solo si prueba una hipótesis fuera de muestra y no duplica información. No sumar RSI/MACD/medias como si fueran evidencias estadísticamente independientes.

## 4. Fundamental y eventos

CoinGecko proporciona un resumen agregado y DefiLlama TVL de cadena; estos conectores no completan una tesis por sí solos. Ambas IAs deben investigar fuentes primarias sobre utilidad, captura de valor, emisiones, supply circulante/total, concentración, desbloqueos, ingresos, adopción, seguridad, gobernanza y catalizadores. Identificar qué métricas aplican: BTC no se valora como un token DeFi.

Registrar fecha de publicación y consulta; distinguir noticia, anuncio, ejecución y rumor. Un mercado agregado en USD no sustituye al spread Kraken. FRED actual sirve de contexto; datos revisados no pueden entrar en un backtest histórico sin vintage/fecha de disponibilidad.

## 5. Estadístico y empírico

El dossier incluye retornos, volatilidad anualizada (mercado cripto 365,25 días), VaR/CVaR histórico por vela al 95%, drawdown histórico, asimetría, curtosis y autocorrelación lag1. Son descripciones de la muestra, no garantías ni distribuciones normales asumidas. La correlación multiactivo alinea timestamps comunes, no rellena observaciones ausentes.

El baseline EMA long/flat:

1. Selecciona entre cuatro combinaciones EMA únicamente en una ventana previa de entrenamiento.
2. Aplica la combinación a una ventana de test posterior, sin solapamiento entre tests.
3. Usa señal del cierre anterior y entrada/salida en la apertura siguiente; el último cierre liquida para marcar cada fold.
4. Descuenta comisiones y slippage por cada lado, sin apalancamiento.
5. Reinicia a cash en cada fold y compone retornos fuera de muestra.
6. Genera bootstrap por bloques contiguos con semilla fija para mostrar sensibilidad al orden de los retornos.

El baseline no tiene stops, no simula órdenes límite, paths intrabar, funding, cola ni impacto. No demuestra cumplimiento MDL. Sus resultados no pueden reutilizarse como backtest de una propuesta que tenga otras reglas. No se implementa todavía un simulador completo de estrategias arbitrarias.

Antes de promover una estrategia evaluar: amplitud de muestra, operaciones, regímenes adversos, benchmark cash/buy-and-hold, sensibilidad a costos y parámetros, número total de intentos, holdout intacto y paper trading. Si una verificación no puede completarse, registrar su impacto como gap y decidir si bloquea, exige otra modalidad/menor riesgo o es aceptable. No presentar una validación ausente como realizada ni exigir conocimiento imposible. Los intervalos del bootstrap no son una probabilidad calibrada de ganar.

## 6. Propuesta y evaluación posterior

Fijar entrada, cantidad, stop, target, horizonte en tesis, caducidad, invalidación y riesgos de eventos. El sizing se valida por separado. Evaluar propuesta, revisión dual, fills reales, slippage, fees, PnL neto y excursiones adversas; comparar con el plan sin reescribirlo después del resultado. Mantener resultados ganadores y perdedores en el mismo registro.

Proposal v2 agrega horizonte explícito, cierre de búsqueda, suficiencia, alternativas, escenarios, reglas, seguimiento y matriz de faltantes. El resumen de trading debe explicar congruencia entre cada elemento: régimen/tesis → señal → horizonte → invalidación/stop → target → sizing/costos → validación → ejecución. Un formato largo sin esa cadena no constituye una estrategia congruente.
