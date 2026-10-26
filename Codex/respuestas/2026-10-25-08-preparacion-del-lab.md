# 08 — Verificación de preparación del Lab

Autor: Codex. Fecha: 2026-10-25 (America/Bogota). Estado: vigente al registrarse. Conclusión: listo para iniciar investigación y diseño de estrategias; no representa aprobación de un trade.

## Respuesta

Sí: el Lab está listo para comenzar la investigación y el diseño de estrategias con ambas IAs.

- 70 pruebas locales aprobadas y CI de instalación/pruebas aprobada en Linux y Windows.
- Kraken, CoinGecko, FRED y DefiLlama verificados con datos reales, sin warnings en la colección enriquecida.
- Código, contratos, pruebas e instrucciones ya publicados en Forebank.
- Claves locales fuera de GitHub; sin valores de credenciales en los resultados y cache comprobados.

Para arrancar, ambas IAs deben leer AGENTS.md y docs/START_RESEARCH.md. La primera tarea es confirmar los identificadores exactos y la elegibilidad del universo antes de analizar cada activo. Después investigan, diseñan sistemas congruentes y preparan sus propias revisiones y el resumen detallado de trading.

Antes de aprobar una ejecución manual faltan moneda, fees efectivos y snapshot vigente/reconciliado de cuenta, además de la revisión real de ambas IAs. Eso no bloquea el inicio de research. El control de MDL actual no es un monitor continuo.

Si Claude corre en otro entorno, necesita configurar allí las claves de datos de forma privada; no se copian con el repositorio.

## Evidencia

- [Preparación](../../docs/READINESS.md)
- [Guía de inicio](../../docs/START_RESEARCH.md)
- [CI completada con éxito](https://github.com/carolinehernandez1126-ui/Forebank/actions/runs/40269345762)
- Commit de código validado: `f3e89de984ca61368fabaf461ef689ac11b37271`.

## Límite de esta conclusión

La prueba de conectividad y las verificaciones de software no son investigación de inversión sobre ETH ni recomendación de trading. No se ha fabricado una revisión de Claude, no se ha reconciliado una cuenta por inferencia y no se ha ejecutado ninguna orden.
