# Fuentes oficiales consultadas

Consulta de documentación: **2026-10-25**, zona del usuario America/Bogota. No son citas de mercado para una operación; cada propuesta exige su propia investigación vigente.

| Fuente | URL | Decisión de diseño |
|---|---|---|
| Kraken: MDL | https://support.kraken.com/articles/maximum-daily-loss-mdl-explained | Es una regla documentada para Kraken Prop; cuenta propia usa política interna |
| Kraken: OHLC | https://docs.kraken.com/api-reference/market-data/get-ohlc-data | Máximo 720, última vela mutable, intervalos válidos |
| Kraken: AssetPairs | https://docs.kraken.com/api-reference/market-data/get-tradable-asset-pairs | Mínimos, tick, precisión, estado y moneda |
| Kraken: histórico OHLCVT | https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data | CSV oficial para historia larga y gaps sin rellenar |
| Kraken: ejemplos públicos | https://support.kraken.com/hc/articles/360000919986-public-endpoint-examples-you-can-try-them-directly-in-a-web-browser- | Datos sin cuenta ni API privada |
| CoinGecko: alta Demo | https://support.coingecko.com/articles/9471335603-user-guide-how-to-sign-up-for-coingecko-demo-api-and-generate-an-api-key | Host Demo y clave por header |
| CoinGecko: precios | https://www.coingecko.com/en/api/pricing | Demo gratuita; confirmar cuotas de cuenta |
| CoinGecko: rate limits | https://support.coingecko.com/articles/5125303456-what-is-the-rate-limit-for-coingecko-api-public-plan | Usar throttling conservador; documentación de cuotas puede diferir |
| DefiLlama: API libre | https://api-docs.defillama.com/llms-free.txt | TVL por cadena sin clave; no extrapolar a endpoints Pro |
| FRED: claves | https://fred.stlouisfed.org/docs/api/api_key.html | Clave individual por usuario |
| FRED: observaciones | https://fred.stlouisfed.org/docs/api/fred/series_observations.html | Series macro y precaución con revisiones/vintages |
| HTTPX: SSL | https://www.python-httpx.org/advanced/ssl/ | Contexto SSL explícito y validación TLS |
| Kraken: stop loss | https://support.kraken.com/articles/7699391647892-stop-loss-orders | Activación a mercado; el colchón no garantiza precio de ejecución |

Las explicaciones y fórmulas del motor de riesgo son decisiones de implementación internas, no reglas atribuidas a los proveedores. Las fuentes no ofrecen una garantía de rentabilidad ni sustituyen los términos efectivos de la cuenta.
