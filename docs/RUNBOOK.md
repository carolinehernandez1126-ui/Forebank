# Operación y publicación

## Instalación

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
.\.venv\Scripts\python.exe -m pip install -e . --no-build-isolation --no-deps
.\.venv\Scripts\lab.exe --help
.\.venv\Scripts\lab.exe demo
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m ruff check src tests
```

El lock registra las versiones probadas en Python 3.12. Los cambios de dependencias requieren verificar tests y regenerar el lock de forma deliberada. El paquete editable permite colaborar sobre el código sin reinstalarlo tras cada edición.

En el entorno Windows inicial hubo restricciones del directorio temporal del sandbox y una variable SSLKEYLOGFILE del antivirus que apuntaba a un dispositivo no accesible. Se completó la instalación con pip desde el intérprete principal. Si ocurre algo similar, no desactivar la validación TLS: usar un temporal dentro del workspace para pruebas y revisar esa variable del proceso. Ejemplo de pruebas en el workspace:

```powershell
New-Item -ItemType Directory -Force outputs | Out-Null
.\.venv\Scripts\python.exe -m pytest -q --basetemp=outputs/pytest-tmp
```

## Configurar

1. Capital confirmado: 50.000. Confirmar moneda de cuenta y activos. Actualizar config/assets.toml (symbol, kraken_pair, CoinGecko ID, cadena opcional).
2. Máximos confirmados: MDL 3% y MDD 6%; operativos definidos por debajo: 2%/4%, además de reserva. Revisar moneda, fees y bases de cuenta en config/lab.toml antes de actualizar policy_verified; no volver a pedir los parámetros ya suministrados.
3. Copiar el ejemplo a private/account.json, actualizar fechas UTC, saldos, flujos, posiciones y órdenes pendientes; reconciliar con Kraken. No publicar este archivo.
4. Obtener opcionalmente claves gratuitas CoinGecko/FRED y completar `.env` local.

## Investigación habitual

```powershell
.\.venv\Scripts\lab.exe collect --asset BTC/USD --enrich --output data/btc.json
.\.venv\Scripts\lab.exe analyze --dataset data/btc.json --output outputs/btc/dossier.json
.\.venv\Scripts\lab.exe collect --asset ETH/USD --enrich --output data/eth.json
.\.venv\Scripts\lab.exe correlations --datasets data/btc.json data/eth.json --output outputs/correlations.json
.\.venv\Scripts\lab.exe backtest --dataset data/btc.json --interval 60 --output outputs/btc/backtest.json
```

El backtest de referencia rechaza gaps y exige ventanas suficientes. Para importar histórico Kraken ya descargado y verificado:

```powershell
.\.venv\Scripts\lab.exe import-csv --dataset data/btc.json --csv private/XBTUSD_60.csv --interval 60 --source-url https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data --output data/btc-history.json
.\.venv\Scripts\lab.exe backtest --dataset data/btc-history.json --train-bars 2000 --test-bars 500 --output outputs/btc/long-backtest.json
```

CSV esperado: timestamp Unix segundos, open, high, low, close, volume, trades; siete columnas, con o sin encabezado. No convierte otra bolsa ni adivina el par. El operador comprueba par e intervalo; el hash del archivo queda en procedencia. La importación no refresca la cotización. Un dataset histórico debe conservar una cotización real reciente si se usa después para validar un plan.

## Preparar decisión

Usar los comandos del README para draft, review-template, risk-check y decide. `draft` no produce precios ni una tesis. Deben completarlos los agentes con evidencia. `review-template` deja abstención y un blocker. Modificar una propuesta requiere regenerar revisiones para el nuevo hash.

La propuesta v2 requiere `research` con corte, suficiencia, horizonte, alternativas, congruencia, escenarios, ejecución, seguimiento y gaps. Cada revisor acepta expresamente incertidumbre y coherencia con los flags correspondientes. No se necesita información perfecta ni todas las APIs, pero un gap crítico impide operar. `decide --output private/decision.json` escribe `private/decision.md` como resumen detallado. Mantener ambos privados hasta sanearlos. Los planes v1 se migran completando estos campos y renovando las dos revisiones.

Los informes JSON son contratos legibles por ambas IAs. Para regenerar JSON Schema:

```powershell
.\.venv\Scripts\lab.exe schemas
.\.venv\Scripts\lab.exe journal --output private/audit-export.json
```

Códigos de salida: `0` comando exitoso o gate aprobado, `1` error/entrada inválida, `2` riesgo bloqueado o decisión WAIT. Un error jamás debe interpretarse como aprobación. El gate escribe su resultado y deja audit trail. Mantener data/lab.sqlite entre sesiones, incluso tras una pérdida.

## Ejecución humana

Verificar cuenta, precio, spread, cantidad, stop, target, costos y fecha de validez. Si algo cambia materialmente, refrescar y revisar. Tras abrir una orden, registrarla en el estado de cuenta antes de otra propuesta. No asumir que READY reserva efectivo. Al completar/cancelar, reconciliar y llenar research/EXECUTION_TEMPLATE.md de forma saneada. Mantener detalles privados fuera del repositorio.

Sin monitor continuo, el operador debe vigilar el MDL y registrar daily_lockout si lo alcanza entre consultas. No operar apoyándose en un informe de ayer. No borrar lockouts para reintentar.

## GitHub

Repositorio real confirmado: **carolinehernandez1126-ui/Forebank**, ya creado y compartido con el usuario **jsforeroc80-debug**. Origin apunta a https://github.com/carolinehernandez1126-ui/Forebank.git. Identidad autorizada: jsforeroc80-debug; no utilizar sebasforero ni credenciales de la propietaria. La URL anterior confundía identidad y propietario del repo. No crear otro repositorio.

GitHub documenta una limitación de los fine-grained PAT para contribuir como colaborador de repositorios ajenos. Para este caso, crear desde jsforeroc80-debug un **PAT classic**, con vencimiento corto (ejemplo: 7 días), scope `repo` para repos privados y `workflow` para subir la CI. Si Forebank es público, `public_repo` permite un alcance menor que `repo`. No añadir scopes administrativos. El token no amplía el rol del colaborador; debe haber aceptado la invitación y tener escritura. Una organización puede imponer políticas adicionales.

El classic PAT no puede limitarse a un único repositorio: sus scopes pueden alcanzar otros repos a los que la cuenta tenga acceso. Nuestras operaciones se limitarán a Forebank y a verificar identidad. Revocar el acceso puntual al terminar si ya no es necesario. Si se necesita restricción técnica a un solo repo, evaluar una GitHub App instalada por la propietaria en lugar de fingir que un classic PAT tiene esa restricción.

Guardar GH_TOKEN en `.env` local. No pegarlo en el chat, imprimirlo ni incluirlo en la URL. `gh` y `git` no cargan `.env` automáticamente: cargar la variable solo en el proceso necesario, sin volcar el entorno a logs. No cambiar la sesión global de otra cuenta. Fuente: [documentación oficial de tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Con credenciales disponibles, primero comprobar identidad, permisos e historial remoto:

```powershell
gh api user --jq .login
gh repo view carolinehernandez1126-ui/Forebank --json nameWithOwner,defaultBranchRef,viewerPermission
git fetch origin
git log --oneline --all --decorate -n 15
git status --short
```

Si el remoto contiene README, licencia u otro historial, integrarlo sin sobrescribirlos y sin force-push. Elegir la rama de trabajo a partir del estado observado; no asumir que el remoto está vacío o que su rama principal se llama main. Revisar contenido staged antes del commit: no incluir datos privados ni payloads sujetos a restricciones. Publicar mediante rama/PR cuando corresponda, conservando la visibilidad existente. Compartir acceso con colaboradores desde GitHub y activar protección de rama y revisiones independientes.

`.github/workflows/ci.yml` ejecuta lint, tests y demo offline en Linux/Windows sin secretos. No colecta datos ni programa operaciones. No se crean cron jobs ni recordatorios por esta instalación.
