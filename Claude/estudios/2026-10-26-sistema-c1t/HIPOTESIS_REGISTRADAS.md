# Registro v2 — antes de mirar el histórico largo (Binance 1d)

Registrado: 2026-10-26 ~05:30 UTC. Autor: Claude (claude-opus-5-5).
Ya visto: Kraken 2024-11-05 → 2026-10-25 (H1/H2 sobre 5 activos). NO visto: ningún resultado sobre datos anteriores a 2024-11-05.

## Datos y particiones
- Binance spot USDT diario (proxy; correlación de retornos con Kraken ≥ 0,99 en el solapamiento). Ejecución real sería en Kraken USD.
- Universo: AAVE, ADA, AIXBT, ALGO, APT, ARB, ASTER, ATOM, AVAX, BCH (primeros 10 de la lista). BTC solo como filtro de régimen.
- Train: inicio → 2022-12-31. Validación: 2023-01-01 → 2024-11-04. Holdout final: 2024-11-05 → 2026-10-25 (periodo Kraken).
- Costos: 55 bps por lado. Señal al cierre, ejecución a la apertura siguiente; stop con gap a la apertura.

## Paso 1 — prueba fuera de muestra de H1/H2 sin cambios
Aplicar H1 y H2 exactamente como en el registro v1 a todo el periodo anterior a 2024-11-05. Mismos 5 criterios de descarte.

## Paso 2 — candidatos de sistema (máximo 3, fijados ahora)
- C1 Tendencia lenta: entrada si cierre > máximo de 50 días previos Y BTC > SMA200(BTC). Stop inicial 3×ATR20. Salida: cierre < mínimo de 20 días previos (orden a la apertura siguiente) o stop.
- C2 Momentum de series temporales: cada lunes (cierre del domingo), comprar si retorno 90d > 0, cierre > SMA100 y BTC > SMA200(BTC). Stop chandelier: máximo cierre desde la entrada − 3×ATR20, actualizado diario. Salida también si en la revisión semanal deja de cumplir la condición.
- C3 = H1 (breakout 20/10 con BTC > SMA100), como referencia rápida.

## Regla de selección (fijada)
1. Solo en train: elegir el candidato con mayor expectativa neta en R entre los que cumplan los 5 criterios de descarte (agrupado por activos).
2. Validación: el elegido debe tener expectativa > 0 y seguir > 0 sin el mejor trade. Si falla, no hay sistema (NO TRADE global).
3. Holdout (Kraken-periodo): se reporta. Si da expectativa < −0,15 R se degrada a paper trading.
4. Riesgo por trade del sistema: el mayor de {0,10%, 0,15%, 0,20%, 0,25%} cuyo MDD de cartera (mark-to-market diario, train+validación+holdout) sea ≤ 3,0% y cuyo percentil 95 de MDD por bootstrap de bloques sea ≤ 4,0%.

## Reglas de cartera (simulación)
Equity 50.000. Riesgo abierto total ≤ 0,5% (distancia actual al stop + costos). Exposición ≤ 20% por activo y ≤ 50% total. Prioridad de entrada: mayor retorno 90d. Elegibilidad Kraken: spread ≤ 20 bps y volumen diario Kraken ≥ 250.000 USD (AIXBT queda excluido de la operación real).

## Adenda (2026-10-26 ~06:00 UTC, DESPUÉS de ver resultados de cartera)
C1 seleccionado según la regla, pero su simulación de cartera viola MDD 4% con cualquier riesgo por trade (con 0,10% llega a MDD −5,2% y peor día −4,1%), porque las ganancias abiertas se devuelven contra el peak mark-to-market. Se añade UNA regla derivada del mandato (no de optimizar resultados): stop trailing que limita la pérdida desde el último cierre a 1R inicial (C1T). Se reporta también H1T como comparación. Se vuelven a evaluar las tres particiones; el sesgo de haber visto los datos queda declarado.

## Adenda 2 (antes de correrlo)
Prueba adicional fuera de muestra SIN cambios: C1 y C1T aplicados a las filas 12-16 de la lista (BNB, BONK, BTC, CVR, DOGE), periodo completo disponible. No se seleccionan activos según el resultado; solo informa si el patrón (ventaja sin trailing / sin ventaja útil con trailing) se repite.

## Adenda 3 (2026-10-26, antes de correrlo) — filas 12-31
C1T congelado (sin cambios de parámetros) aplicado a BNB, BONK, BTC, CVR, DOGE, DOT, ENA, ETC, ETH, ETHFI, FARTCOIN, FIL, FLOKI, GRASS, HBAR, HYPE, ICP, INJ, JTO, JUP.
Filas 17-31 nunca vistas: prueba fuera de muestra real. Se reporta pooled por periodos (train ≤2022, val 2023→2024-11-04, holdout 2024-11-05→). Universo operable = regla de liquidez Kraken ya fijada (spread ≤20 bps, mediana volumen diario ≥250k USD). Ningún parámetro se ajusta con estos resultados.
