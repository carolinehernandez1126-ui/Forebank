# 01 — Entrega inicial del Research Lab

Autor: Codex. Fecha de registro: 2026-10-25 (America/Bogota). Estado: histórico; los resultados iniciales de 49 pruebas se ampliaron después a 70. Los enlaces a documentos locales se adaptaron al contexto de este archivo.

## Respuesta

Dejé un **Research Lab funcional** en esta carpeta.

Incluye:

- Datos de Kraken, CoinGecko, DefiLlama y FRED.
- Indicadores técnicos, estadísticas, correlaciones y backtesting walk-forward con costos.
- Controles de pérdida diaria, drawdown, exposición y tamaño de posición.
- Propuestas auditables con revisión independiente de Codex y Claude; cualquier discrepancia produce `WAIT`.
- Instrucciones para [Claude](../contexto/CLAUDE.md), plantillas de investigación y CI para GitHub.

**Verificación inicial:** 49 pruebas aprobadas. Probé descargas reales de BTC/ETH en Kraken y TVL de Ethereum en DefiLlama.

Las APIs necesarias están detalladas en [APIS.md](../contexto/APIS.md):

| Fuente | Qué necesitas |
|---|---|
| Kraken público | Sin clave |
| DefiLlama libre | Sin clave |
| CoinGecko Demo | Clave gratuita recomendada |
| FRED | Clave gratuita recomendada |
| Codex y Claude | Sus sesiones actuales; sin APIs de modelos para este MVP |

Como usarás capital propio, el **MDL es interno y configurable**. La regla oficial consultada corresponde a [Kraken Prop](https://support.kraken.com/articles/maximum-daily-loss-mdl-explained). La ejecución será manual; todavía no hay monitor continuo ni estrategia validada para operar.

En esa primera entrega faltaban capital, moneda, activos y límites definitivos. Git quedó inicializado localmente; la publicación estaba pendiente por el diagnóstico inicial de autenticación.

## Aclaraciones posteriores

El usuario confirmó después capital 50.000 y máximos de MDL 3% / MDD 6%. La comprobación posterior con red mostró que la sesión antigua era válida, pero correspondía a otra cuenta. El destino correcto y el acceso como colaborador se documentan en los registros 05 y 06. El código del Lab seguía local al crear este archivo.
