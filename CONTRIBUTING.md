# Convención de commits

Se recomienda un commit por avance verificable.

Ejemplos:

- `data: integra anuario 2020 y valida totales mensuales`
- `feat: genera lag12 y medias móviles sin fuga temporal`
- `exp: entrena Ridge con validación 2022`
- `exp: compara XGBoost contra Seasonal Naive en test 2023`
- `eval: incorpora walk-forward y MASE por origen`
- `docs: actualiza PPI con resultados reproducibles`

No reemplazar silenciosamente un resultado. Si cambia una métrica, el commit debe explicar qué cambió en datos, variables, modelo o protocolo.
