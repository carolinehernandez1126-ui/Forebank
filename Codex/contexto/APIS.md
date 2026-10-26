# APIs, claves y cobertura

Revisión de documentación: 2026-10-25. Planes, disponibilidad regional y cuotas pueden cambiar; consultar el dashboard del proveedor antes de ampliar la frecuencia. No se requiere contratar datos para comenzar.

## Necesarias para comenzar

**Ninguna clave es obligatoria.** Kraken público permite construir el dataset técnico y la demo es offline. Para enriquecer el análisis recomiendo obtener estas dos claves gratuitas y ponerlas en `.env`:

| Variable | Alta oficial | Información | Limitaciones |
|---|---|---|---|
| `COINGECKO_DEMO_API_KEY` | [CoinGecko API](https://www.coingecko.com/en/api/pricing) | Precio agregado, market cap, FDV, supply, ATH, volúmenes | Demo, cuotas/historia según plan; no es precio ejecutable Kraken |
| `FRED_API_KEY` | [FRED API key](https://fred.stlouisfed.org/docs/api/api_key.html) | DFF, DGS10, DTWEXBGS, VIXCLS | Series con rezagos y revisiones; cada colaborador usa su clave |

CoinGecko publica cifras de cuota distintas entre algunas páginas de soporte y precios. La implementación usa 3,1 s entre llamadas al mismo host y cache de una hora; **no presupone una cuota mensual o por minuto garantizada**. Confirmar la cuota efectiva de la cuenta. La clave viaja en header, no en el manifiesto.

## Conectores implementados

| Fuente | Endpoints usados | Autenticación | Cache local |
|---|---|---|---|
| Kraken | `/0/public/AssetPairs`, `/OHLC`, `/Depth` | Pública | 1 h / 30 s / 5 s |
| CoinGecko Demo | `/api/v3/coins/markets` | Header `x-cg-demo-api-key` | 1 h |
| DefiLlama libre | `/v2/historicalChainTvl/{chain}` | Ninguna | 1 h |
| FRED | `/fred/series/observations` | `api_key` en query, excluida de metadatos | 1 h |

El cliente tiene timeout de 25 s, hasta tres intentos para red/429/5xx, pausas acotadas, allowlist de hosts, solicitudes GET y rechazo de endpoints privados de Kraken. TLS se valida con un contexto SSL del sistema, que admite autoridades locales administradas sin desactivar validación. No hace fallback silencioso a datos vencidos. Una falla de Kraken impide crear el dataset; una fuente de enriquecimiento faltante se anota en warnings. Las respuestas originales quedan localmente con hash y fecha de adquisición.

Kraken entrega hasta 720 velas recientes y añade la vela en curso. Se elimina siempre esa última vela. `since` no permite recuperar un histórico anterior a ese límite. Para investigación seria descargar [OHLCVT oficial](https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data) y usar `import-csv`. Los ZIP pueden ser grandes: la aplicación no los descarga automáticamente. Verificar checksum, par e intervalo.

No se debe tratar TVL como valoración fundamental suficiente de una moneda: TVL puede incluir exposición al precio, doble conteo según metodología y activos que no generan valor para el token. El adaptador actual es por cadena, no análisis de ingresos por protocolo.

## Fuentes para investigar sin añadir claves

- Sitio y documentación del proyecto, repositorios oficiales, gobernanza, exploradores de bloques y anuncios oficiales. Verificar token/contrato/red exactos.
- Banco central, reguladores y calendarios oficiales para eventos macro. Usar fechas y horas explícitas.
- Kraken anuncios y estado del servicio para listados, interrupciones y cambios operativos.
- Documentación pública de DefiLlama para posibles extensiones de TVL por protocolo, fees/revenue y stablecoins. Verificar qué endpoints siguen siendo libres antes de implementarlos.

El laboratorio no raspa noticias indiscriminadamente ni guarda artículos completos. Los agentes consultan la web y registran citas breves, claims y limitaciones en la propuesta. Si un endpoint requiere pago o cambia de licencia, registrar el faltante.

## Integraciones futuras, no implementadas

- Kraken privado **solo lectura**: balances, trades, ledger, open orders, fees reales. Antes de integrarlo hace falta modelar holdings spot, órdenes y reconciliación; no basta consultar balance. No crear permisos de órdenes/retiros. El MVP usa un estado manual.
- ALFRED vintages para macro point-in-time. Las observaciones FRED actuales sirven como contexto actual; no introducirlas retrospectivamente en backtests como si hubieran sido conocidas entonces.
- Datos de desbloqueos, actividad on-chain, fees/revenue por protocolo y calendarios de eventos: comenzar con fuentes primarias; elegir APIs gratuitas solo después de conocer los activos.
- Búsqueda/noticias programática: las sesiones de ambas IAs ya pueden investigar web. No es necesario adquirir una API de búsqueda para este MVP.
- APIs de OpenAI/Anthropic: únicamente si se pide orquestación desatendida más adelante. Requieren presupuesto, gestión de secretos, trazas y autenticación de los revisores. No están incluidas ni son gratuitas por disponer de cuentas de chat.

## Distribución

Mantener payloads completos y cuentas en local. Publicar métricas derivadas y resúmenes con atribución; comprobar derechos de redistribución de cada fuente antes de subir datasets. `.env`, `private/`, `data/` y `outputs/` no entran a Git. Cada colaborador crea sus propias claves.
