# Comprobación de preparación

Fecha de la sesión: 2026-10-25, America/Bogota. **Estado: listo para iniciar investigación y diseño de estrategias con Codex y Claude.** La habilitación de una operación concreta sigue requiriendo sus verificaciones de cuenta, mercado y revisión dual.

## Verificado desde GitHub

- Código completo integrado en Forebank, commit `f3e89de984ca61368fabaf461ef689ac11b37271`; 61 archivos de implementación/documentación verificados por hash, preservando el historial, el archivo Codex y los archivos originales del repositorio.
- [GitHub Actions aprobado](https://github.com/carolinehernandez1126-ui/Forebank/actions/runs/40269345762): jobs Linux y Windows finalizados con success. Se instalaron las dependencias y el paquete desde el repositorio y pasaron lint, pytest, demo y verificación de contratos.
- La última verificación local ejecutó 70 pruebas con éxito. La integración no publica claves, snapshots de cuenta, caches ni payloads de proveedores.
- [Guía común de inicio](START_RESEARCH.md) disponible para las dos IAs.

## Verificado localmente en esta sesión

- 70 pruebas offline aprobadas; lint correcto; JSON Schema consistente con los modelos; pip sin dependencias rotas.
- Demo sintética, dossier de datos reales y backtest de referencia ejecutados.
- Claves locales presentes y funcionales: CoinGecko Demo devolvió ETH; FRED devolvió 30 observaciones de cada serie DFF, DGS10, DTWEXBGS y VIXCLS.
- Descarga real ETH/USD de Kraken en 1h/4h/1d y TVL de Ethereum de DefiLlama. La colección enriquecida no emitió warnings.
- GitHub autenticado como jsforeroc80-debug con escritura en carolinehernandez1126-ui/Forebank.
- Lista de activos leída del Excel existente sin modificar el original. El mapeo por identificador y elegibilidad es la primera tarea de investigación; no se debe asumir que cada nombre equivale a una moneda spot válida.

Las comprobaciones de datos son pruebas de funcionamiento, no recomendaciones para ETH ni validación de una estrategia de inversión. Los payloads y claves permanecen fuera del repositorio.

## Preparación para dos entornos

Ambas IAs necesitan la misma versión de código, contratos y propuestas. Para ejecutar conectores en otro entorno se configuran allí las claves; nunca se publican para que otra IA las lea desde GitHub. Si comparten este workspace, pueden usar el mismo `.env` local sin exponerlo en outputs.

## Qué no impide iniciar research

La cuenta aún no reconciliada, la moneda definitiva pendiente y la ausencia de revisiones de trades concretos no impiden recopilar evidencia y diseñar estrategias. Sí impiden declarar una propuesta lista para ejecución. Ninguna prueba técnica representa una aprobación de Claude.
