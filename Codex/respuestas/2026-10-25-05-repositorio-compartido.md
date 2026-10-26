# 05 — Repositorio compartido y autenticación

Autor: Codex. Fecha de registro: 2026-10-25 (America/Bogota). Estado: vigente al registrarse. Se omite únicamente la ruta absoluta del editor local, sustituyéndola por el nombre `.env`.

## Respuesta

**Sí, cambia el tipo de token.** Trabajaremos como **jsforeroc80-debug**, colaborador de [carolinehernandez1126-ui/Forebank](https://github.com/carolinehernandez1126-ui/Forebank). Ya corregí el remoto.

GitHub documenta una limitación de los tokens **fine-grained** para colaboradores de repositorios ajenos. La guía anterior debe sustituirse por un **token classic de tu cuenta**. [Documentación oficial](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Pasos indicados:

1. Iniciar sesión en GitHub como jsforeroc80-debug.
2. Abrir [Crear token classic](https://github.com/settings/tokens/new) y elegir Generate new token (classic).
3. En Note, escribir Forebank-Research-Lab y seleccionar vencimiento de 7 días.
4. Seleccionar `repo` si es privado o `public_repo` si es público; añadir `workflow` para subir la CI.
5. Generar y copiar el token.
6. Abrir el `.env` local.
7. Completar únicamente `GH_TOKEN` y guardar.

Estos scopes permiten las operaciones previstas, dentro de los permisos ya otorgados al colaborador. [Referencia oficial](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps).

**El token classic no puede limitarse exclusivamente a Forebank:** puede alcanzar otros repositorios accesibles por tu cuenta según sus scopes. Lo usaré únicamente para este proyecto; puedes revocarlo al terminar.

Avisar «token guardado», sin compartir su valor.
