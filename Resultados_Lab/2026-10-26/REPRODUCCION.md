# Reproducción y verificación

## Integridad sin dependencias

Descarga la carpeta completa y ejecuta:

```text
python verificar_paquete.py
```

Solo usa la biblioteca estándar, sin red ni claves. Comprueba los seis ZIP y sus miembros, 75 hashes canónicos de snapshots Codex, 11 de Claude, cuerpos de fuentes y el mapa de 70 filas. No ejecutes con `python -O`: desactivaría las aserciones y el verificador lo rechaza.

## Replay numérico de Codex

Python >=3.12. Verifica primero los ZIP y revisa el código. Desde esta carpeta:

```text
python -m zipfile -e 05_lab_codigo_reproducible.zip replay_work
python -m venv .venv_revision
```

Activa ese entorno según tu sistema y ejecuta:

```text
python -m pip install -r replay_work/environment/requirements-runtime.txt
python -m pip install -e replay_work/lab_source --no-build-isolation --no-deps
python reproducir_resultados.py --asset BTC
python reproducir_resultados.py
```

Instalar librerías puede requerir Internet; la verificación y el replay posterior funcionan sin red ni credenciales. El runtime está documentado en `environment/runtime_versions.json`; se conserva también el lock original. Si `SSLKEYLOGFILE` apunta a una ruta ambiental inaccesible en Windows, retírala solo del proceso necesario, sin desactivar TLS.

El runner lee los ZIP y no modifica resultados. Usa AST para importar exclusivamente imports y funciones seleccionadas de los scripts analíticos propios verificados, omitiendo bloques de colección/escritura y `__main__`. No ejecuta instrucciones procedentes de datos o páginas.

Reproduce:

- Referencias T/R: tramo elegible, desarrollo, holdout y costos duplicados, contrastando trades y métricas con tolerancia numérica declarada.
- Diagnósticos Q de AVAX/ASTER/BCH y los siguientes 58 activos, a costos base y dobles.
- Relación reward/risk de las cinco evaluaciones prospectivas P1/V2; no inventa backtests de ellas.

Resultados ya contrastados: **530 tramos T/R, 122 casos Q y cinco evaluaciones P1**. LIGHTER carece del warmup diario T/R; HYPE tiene tramo completo pero no la partición desarrollo/holdout del protocolo. SP/XYZ100 están fuera del alcance spot.

El replay acredita igualdad con resultados almacenados; no demuestra ventaja futura, cumplimiento continuo MDL/MDD, liquidez histórica ni probabilidades calibradas. No produce una Proposal operativa.

## Auditoría de Claude

`04_claude_archivos_publicados.zip` conserva sus documentos/código públicos con commit de origen. `06_claude_resultados_saneados.zip` añade exclusivamente investigación local autorizada: 64 archivos, 11 datasets normalizados, 28 históricos largos y 79 registros de caché pública. Consulta `CLAUDE_EXPORT_INDEX.json` y el catálogo principal.

Se verifican sus bytes, hashes e inventario; **el runner de Codex no reproduce C1T ni otras estrategias de Claude**. Sus scripts se conservan como evidencia y algunos usan rutas relativas o consultan APIs. Una evaluación posterior debe aislarlos, conectar cada resultado con los inputs realmente disponibles y declarar lo que falte. No asumir cobertura numérica completa de los 70 activos por la sola presencia de sus recomendaciones.

Los históricos largos son Binance spot USDT. No reemplazan velas Kraken USD sin sesgo de venue/moneda. Faltantes de timestamp de descarga y valores no finitos originales deben conservarse como incertidumbre. La caché SQLite de Claude se exportó desde el archivo consolidado inmutable, sin WAL ni diario.

Para revisar bootstrap, curvas o trades, usa `zipfile` y las rutas de `MANIFIESTO.json`/`INDICE_RESULTADOS.json`. Un toque intrabar no demuestra un fill real.
