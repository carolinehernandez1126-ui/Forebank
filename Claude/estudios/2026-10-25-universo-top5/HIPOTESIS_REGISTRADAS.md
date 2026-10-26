# Hipótesis registradas por Claude antes de backtests

Registrado: 2026-10-26 ~05:00 UTC. Autor: Claude (claude-opus-5-5).
Ya se había visto: snapshot actual (precios, SMAs, liquidez, retornos). NO se había corrido ningún backtest de reglas.

Universo: AAVE/USD, ADA/USD, AIXBT/USD, ALGO/USD, APT/USD (Kraken spot). Datos: 720 velas diarias Kraken (2024-11-05 → 2026-10-25).
Costos: 40 bps fee + 15 bps slippage por lado (config/lab.toml). Stops se ejecutan al precio de stop menos slippage, o a la apertura si hay gap por debajo.
Resultados en múltiplos de R (riesgo inicial incluyendo costos), así el sizing de 0,25% por trade es independiente del activo.

## H1 — Tendencia / breakout diario con filtro de régimen BTC
- Entrada: cierre diario > máximo de los 20 días previos Y BTC cierre > SMA100 de BTC. Compra a la apertura siguiente.
- Stop inicial: entrada − 2,5 × ATR14. Salida: cierre < mínimo de los 10 días previos (trailing), o stop.
- Racional: momentum de series temporales en cripto (Liu & Tsyvinski 2021); el filtro BTC evita comprar breakouts en mercado bajista general.

## H2 — Pullback en tendencia alcista (mean reversion de corto plazo)
- Condición: cierre > SMA100 y RSI(3) < 20. Compra a la apertura siguiente.
- Stop: entrada − 2 × ATR14. Target: entrada + 2,5 × riesgo. Salida por tiempo a los 10 días.

## Criterios de descarte (aplican a cada hipótesis, pooled sobre los activos elegibles)
1. Expectativa neta ≤ 0 R por trade después de costos → descartar.
2. Menos de 20 trades en total → evidencia insuficiente; no operar con tamaño completo (máx. paper trading).
3. Si al quitar el mejor trade la expectativa pasa a ≤ 0 → descartar (dependencia de un outlier).
4. Si la expectativa cambia de signo entre la primera y la segunda mitad de la muestra → no robusta; solo paper trading.
5. Max drawdown simulado > 8 R secuenciales → incompatible con MDD operativo 4% (= 16 R a 0,25%) con margen de seguridad → reducir riesgo a la mitad o descartar.

## Elegibilidad de activos (antes de estrategia)
- Spread actual > 20 bps (max_spread_bps) o mediana de volumen diario Kraken < 250.000 USD → no elegible para operar; se puede seguir estudiando.
