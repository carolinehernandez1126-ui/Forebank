# Protocolo de registro de Interventoría (Gemini)

## Qué se guarda

Se conservan exclusivamente:
1. El **dictamen oficial de interventoría financiera, matemática y estadística** sobre los estudios de los laboratorios **Claude** y **Codex**.
2. La **comparativa cuantitativa verificable** de backtests, costos de fricción (`40 bps` comisión + `15 bps` *slippage* por lado), probabilidades de barrera y liquidez real en el libro de órdenes de Kraken (`Ask Depth 10 bps`).
3. El **plan de inversión y guía de ejecución manual en Kraken Pro**, con montos exactos, dimensionamiento de posición (`sizing`), precios de entrada, *Stop-Loss*, *Take-Profit* e interruptores de riesgo.

Nunca se publican secretos, `.env`, claves privadas ni archivos sin sanear de `private/`.

## Formato

Cada intervención de auditoría se almacena en `Gemini/estudios/AAAA-MM-DD-<tema>/` e incluye:
- `ESTUDIO.md`: Dictamen completo de interventoría y calificación ponderada.
- `COMPARATIVA_MATEMATICA_Y_BACKTESTS.md`: Desglose numérico de los resultados de ambos laboratorios.
- `PLAN_INVERSION_Y_EJECUCION_MANUAL_KRAKEN.md`: Manual operativo de ejecución para los operadores humanos en Kraken Pro.
- Archivos `.json` con las métricas reproducibles verificadas por la interventoría.

## Independencia e Integridad

Gemini no altera ni sobreescribe los archivos dentro de `Claude/` ni `Codex/`, preservando intacta la autoría original de cada laboratorio.
