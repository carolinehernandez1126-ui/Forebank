# 04 — Guía inicial de token fine-grained

Autor: Codex. Fecha de registro: 2026-10-25 (America/Bogota). **Estado: sustituido por el registro 05 para este caso.** Esta guía se emitió antes de saber que el usuario era colaborador de un repositorio de otra persona.

## Contenido de la respuesta histórica

La guía indicaba generar un token de `jsforeroc80-debug`, limitado a Forebank:

1. Iniciar sesión como jsforeroc80-debug.
2. Abrir Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token.
3. Usar nombre `Forebank-Research-Lab`, vencimiento de 7 días y Resource owner jsforeroc80-debug.
4. Seleccionar Only select repositories y Forebank.
5. Solicitar Contents read/write, Pull requests read/write, Workflows write, Actions read-only y Metadata read-only.
6. Generar y copiar el token.
7. Guardarlo en la línea GH_TOKEN del `.env` local, sin espacios y conservando las demás líneas.
8. Avisar «token guardado» sin mostrar el valor.

La respuesta explicó que `.env` estaba excluido de Git y que se comprobaría la identidad antes de publicar.

## Por qué se corrigió

La guía asumía propiedad del repositorio bajo la cuenta del usuario. La documentación de GitHub señala limitaciones para fine-grained PAT cuando se contribuye como colaborador a repositorios ajenos. El usuario aclaró esa relación y facilitó la URL real. La alternativa aplicada quedó registrada en [05 — Repositorio compartido](2026-10-25-05-repositorio-compartido.md).

Fuentes consultadas: [gestión de tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens), [permisos fine-grained](https://docs.github.com/en/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens).
