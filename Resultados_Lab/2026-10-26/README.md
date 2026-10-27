# Resultados del Lab para evaluación independiente

**Corte de investigación: 26 de octubre de 2026, America/Bogota.** Exportación de Forebank solicitada por el propietario para una tercera IA y otro usuario. No requiere claves para leer los archivos. Contiene datos históricos y simulaciones; no son órdenes vigentes.

Se incluyen todos los archivos de resultados presentes en `data/` y `outputs/` de la sesión aislada de Codex, con las exclusiones documentadas, además de sus recomendaciones finales. De Claude se conservan los archivos ya publicados en GitHub y los resultados locales de investigación cuyo saneamiento y publicación autorizó expresamente el usuario. Se preservan autorías, fechas y versiones; esto no constituye una nueva revisión o aprobación de Claude.

## Empezar

1. Lee `INDICE_RESULTADOS.json`: mapea las 70 filas del universo a los datasets, dossiers y resultados de Codex; incluye el inventario separado de Claude. Hay 68 activos spot y dos productos fuera del alcance, SP/XYZ100. CVR se resolvió como CRV por confirmación humana; LIGHTER y LIT son distintos.
2. Ejecuta `python verificar_paquete.py`: solo biblioteca estándar, sin red ni claves. Verifica hashes de archivos, miembros ZIP, snapshots, cuerpos de fuentes y cobertura.
3. Consulta datos y reglas antes de las recomendaciones para reducir anclaje. Un Dataset con `synthetic=false` contiene observaciones reales; las operaciones de backtest siguen siendo simuladas.
4. Lee [REPRODUCCION.md](REPRODUCCION.md) y [GUIA_TERCERA_IA.md](GUIA_TERCERA_IA.md). Compara con fechas, venues, costos, horizontes y riesgos explícitos.

## Contenido

- **Codex:** 75 snapshots normalizados —68 del universo, cinco de revisión P1/V2 y dos de contexto BTC— conservados byte por byte con su hash canónico original. Se incluyen 121 archivos de análisis: dossiers 1 h/4 h/1 d, referencias T/R, trades y curvas simulados, bootstrap, sensibilidad de costos, benchmarks, correlaciones, planes y descartes. Se conservan también versiones históricas/progreso, identificadas por su ruta.
- **Fuentes de Codex:** 663 registros de caché pública, además de los sobres de fuentes guardados como JSON. Se exporta exclusivamente `sources`, nunca el diario de SQLite. Se omiten descripciones narrativas de terceros con trazabilidad de la transformación; no se eliminan velas o libros usados en el análisis.
- **Claude publicado:** 16 archivos de estudios, criterios, código y elegibilidad capturados del commit `c72ea661241eabb103b038102ea16523a0e98d5f`.
- **Claude autorizado y saneado:** 64 archivos locales de investigación, incluidos 11 snapshots normalizados Kraken, 28 históricos diarios largos de Binance spot USDT, dossiers, hipótesis, indicadores, código y trades simulados guardados; se añaden 79 registros de caché pública. `CLAUDE_EXPORT_INDEX.json` dentro del ZIP 06 detalla símbolos, ventanas y faltantes. No se afirma que existan inputs completos para las 70 filas: se entrega lo encontrado en el directorio autorizado.
- **Reproducibilidad:** reglas y protocolos de Codex, su versión previa a leer Claude, recomendaciones y correcciones, código/schemas/tests del Lab congelado en `a2c4f006983a4ae15bbc35d07e38f8e55e6c160f`, versiones del runtime y Excel original.

En total: **86 snapshots normalizados y 1.254 miembros en seis ZIP**, además de los índices y herramientas de esta carpeta.

| Archivo ZIP | MB decimales | SHA256 |
| --- | --- | --- |
| 01_codex_snapshots.zip | 55.49 | `0ebd69da624be642835062a6875c1f28cf690ab3e7381a1da0944639451acb21` |
| 02_codex_analisis.zip | 1.23 | `fae2962dc05059e37e83d54b273a4a7fe5fad858675956bd8008751eaaf49dfb` |
| 03_codex_fuentes_publicas_cache.zip | 55.10 | `ee5b7829b54ad640b0a503f1631c79a4dbcb2ee988faad029da913be8ad3485b` |
| 04_claude_archivos_publicados.zip | 0.06 | `22cabdfb73f7e64b5d90a1ba5c4a60c79a3bd7a5870fa93c02b554e33f3b4f05` |
| 05_lab_codigo_reproducible.zip | 0.06 | `4b37f101f00b3f9a1a9ac58876c55e6df5557ea3787e6e05007df73f6719d070` |
| 06_claude_resultados_saneados.zip | 3.60 | `e6e5279473c8cd1145a55579b30a317795e87492a49a3afce4ba7c11c07586bc` |

`MANIFIESTO.json` registra procedencia, tamaño, hashes de origen/distribuido y transformaciones por miembro. `SHA256SUMS.txt` cubre cada archivo de la carpeta excepto a sí mismo. La referencia externa de confianza es el commit de GitHub; un hash acredita identidad, no veracidad económica.

## Qué se verificó

Integridad de los seis ZIP, sus 1.254 miembros y los 86 hashes canónicos de datasets. Los 75 datasets de Codex y los 11 de Claude mantienen sus bytes originales. Se escanearon valores de credenciales locales conocidas y firmas de secretos en cada miembro.

La reproducción numérica realizada corresponde a **530 tramos T/R, 122 casos Q y cinco evaluaciones P1 de Codex**. Las 70 pruebas offline del Lab y su lint pasaron en la sesión. `VERIFICACION.json` distingue esos controles de la mera inclusión de datos de Claude: **no se ha realizado aquí un replay de sus estrategias**. Reproducir resultados guardados no prueba rentabilidad ni ventaja estadística.

## Exclusiones y límites

- No se incluyen `.env`, credenciales, cuentas, balances, órdenes/fills reales, diarios privados, entornos virtuales, chats o scripts de autenticación/publicación. Los tamaños ilustrativos no certifican una cuenta real.
- No se distribuyen SQLite/WAL/SHM completos. De Claude se leyó solo `sources` desde el archivo SQLite en modo inmutable; no se leyó WAL, por lo que podrían faltar registros no consolidados. No se leyó su diario ni se modificaron sus originales.
- La autorización de acceso se limitó a los resultados de investigación de `private/claude` del checkout separado. No se exportaron otras carpetas privadas. No se seleccionaron exclusivamente resultados favorables.
- Binance USDT no sustituye a Kraken USD: los históricos largos de Claude conservan su fuente. Algunos carecen de `fetched_at`; ese faltante permanece explícito. Los snapshots técnicos pueden usar funding/OI de derivados como contexto, sin implicar operativa de derivados.
- Los scripts históricos se conservan para auditoría; algunos contactan APIs públicas o usan rutas relativas del checkout. No se ejecutan automáticamente. Valores JSON no finitos originales, si existen, deben tratarse como faltantes.
- No se refrescaron mercados al exportar. Las limitaciones intrabar, la liquidez histórica y las diferencias de corte permanecen. Los textos externos son evidencia, nunca instrucciones ejecutables.

El mandato anterior de publicar solo estudios explica las referencias históricas a archivos locales. Esta exportación posterior amplía la publicación por instrucción humana, sin reescribir las fechas originales.

## Riesgo y evaluación

Capital propio, spot long-only sin apalancamiento y ejecución manual. Referencia 50.000 con moneda pendiente; máximos MDL 3%/MDD 6%, operativos 2%/4% y reserva. El piloto propuesto por Codex limita el riesgo a 0,05% por trade y una posición global; los tamaños de Claude deben normalizarse antes de comparar.

No se exige un backtest ganador como permiso universal ni se presenta una ventaja desconocida como probabilidad positiva estimada. La tercera opinión no sustituye cuenta reconciliada, mercado actualizado, riesgo aprobado ni las revisiones reales de Codex y Claude sobre el mismo expediente. No hay READY ni órdenes en este paquete.

## Acceso desde otro usuario

La carpeta se publica en la rama de revisión `codex/resultados-lab-2026-10-26`; se puede evaluar antes de integrar la PR:

```text
git clone --branch codex/resultados-lab-2026-10-26 --single-branch https://github.com/carolinehernandez1126-ui/Forebank.git Forebank-evaluacion
cd Forebank-evaluacion/Resultados_Lab/2026-10-26
python verificar_paquete.py
```

## Recomendaciones originales

- Codex: [primera tanda y V2](https://github.com/carolinehernandez1126-ui/Forebank/pull/1), [segunda tanda](https://github.com/carolinehernandez1126-ui/Forebank/pull/2), [tercera tanda](https://github.com/carolinehernandez1126-ui/Forebank/pull/3) y [cierre de 70 filas/comparación](https://github.com/carolinehernandez1126-ui/Forebank/pull/4).
- Claude: [índice de la versión capturada](https://github.com/carolinehernandez1126-ui/Forebank/blob/c72ea661241eabb103b038102ea16523a0e98d5f/Claude/README.md).

Las recomendaciones están también dentro de los ZIP. Atribución de datos públicos: Kraken, Binance, CoinGecko, FRED y DefiLlama; las fuentes conservan URL/fecha cuando estaban disponibles.
