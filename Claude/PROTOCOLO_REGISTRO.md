# Protocolo de registro de Claude

## Qué se guarda

Solo la **decisión final de cada estudio de trading y el estudio que la sustenta**. No se guardan respuestas intermedias, pruebas de entorno ni comprobaciones de acceso.

Nunca se publican secretos, `.env`, saldos, posiciones, órdenes reales ni archivos de `private/`. Si el estudio usa datos de cuenta, se publica una versión saneada (porcentajes o unidades normalizadas) y se indica la omisión.

## Formato

Un archivo por estudio: `estudios/AAAA-MM-DD-<activo>-<tema>.md` (fecha America/Bogota). Contenido:

1. **Cabecera:** autor Claude, modelo real, fecha UTC de cierre, activo, horizonte, hash de la propuesta revisada y del dataset.
2. **Decisión:** APPROVE, REJECT, ABSTAIN o NO TRADE, con condiciones y fecha de caducidad.
3. **Estudio:**
   - hipótesis y criterios de descarte, fijados antes de ver resultados;
   - análisis técnico, fundamental y estadístico, y backtest pertinente con sus límites;
   - fuentes consultadas (URL, fecha de consulta UTC, qué afirman, limitación);
   - hipótesis contraria, contraevidencia y escenarios de cola.
4. **Faltantes:** clasificados como crítico, material o menor, con su impacto, mitigación y por qué se acepta la incertidumbre restante.
5. **Plan revisado:** entrada, stop, target, sizing en % de capital, invalidación y seguimiento; coherencia con MDL/MDD operativos (2% / 4%).
6. **Cómo se llegó a la decisión:** resumen del razonamiento y diferencias con Codex, si las hay.

Después de cada estudio se actualiza la tabla de README.md.

## Correcciones

No se borra nada. Si una decisión se revisa (por un plan nuevo, un dato nuevo o un error), se crea un registro nuevo y el anterior se marca como sustituido en el índice.

## Independencia

Claude no edita `Codex/` ni las revisiones de Codex. Si cambia una cifra del plan, ambas revisiones se repiten.
