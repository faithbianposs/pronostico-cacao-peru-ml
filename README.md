# Pronóstico mensual de la producción de cacao en el Perú mediante aprendizaje automático

Repositorio de evidencias del PPI y short paper de Ingeniería de Sistemas. El estudio evalúa modelos de aprendizaje automático para pronosticar la producción mensual regional de cacao en el Perú con datos agrícolas abiertos de MIDAGRI/SIEA y validación temporal.

## Objetivo general

Evaluar el desempeño de modelos de aprendizaje automático para el pronóstico mensual de la producción regional de cacao en el Perú, mediante un esquema de validación temporal y comparación con una referencia estacional.

## Pregunta de investigación

¿Los modelos de aprendizaje automático evaluados superan a un modelo Seasonal Naïve en el pronóstico mensual de la producción regional de cacao en el Perú cuando se mantiene una separación temporal entre entrenamiento, validación y prueba?

## Datos utilizados

- Periodo: 2017–2023.
- Unidad de análisis: región–mes.
- Series regionales activas de cacao: 16.
- Observaciones de cacao: 1,344.
- Historia inicial: 2017.
- Entrenamiento preliminar: 2018–2021.
- Validación: 2022.
- Test final fuera de muestra: 2023.

Los archivos oficiales originales no se redistribuyen como parte central del repositorio. En [`data/SOURCES.md`](data/SOURCES.md) se documenta su procedencia. Los datos derivados conservan trazabilidad hacia los anuarios utilizados.

## Modelos evaluados

- Seasonal Naïve, referencia estacional $t-12$.
- Ridge Regression.
- Random Forest.
- Extra Trees.
- XGBoost.

ETS, ARIMA/SARIMA, validación walk-forward completa y aprendizaje profundo forman parte del trabajo pendiente y se incorporarán mediante commits posteriores cuando la comparación sea metodológicamente equivalente.

## Resultados preliminares sobre 2023

| Modelo | MAE (t) | RMSE (t) | sMAPE (%) | MASE |
|---|---:|---:|---:|---:|
| Seasonal Naïve | 131.41 | 267.19 | 34.31 | 1.018 |
| **Ridge** | **117.71** | **227.33** | 58.30 | **0.911** |
| XGBoost | 127.67 | 229.76 | 57.78 | 0.989 |
| Extra Trees | 135.38 | 262.06 | 49.53 | 1.048 |
| Random Forest | 142.44 | 297.46 | 53.05 | 1.103 |

En esta primera configuración, Ridge obtuvo el menor MAE y RMSE y un MASE menor que 1. La lectura se mantiene como preliminar porque sMAPE favorece a la referencia estacional y todavía falta ejecutar la validación walk-forward completa.

### Lectura rápida del avance

- El Seasonal Naïve funciona como baseline explícito para evitar comparar ML contra una referencia débil.
- Ridge mejora al baseline en MAE, RMSE y MASE sobre el test 2023.
- XGBoost queda cerca del baseline y no muestra una mejora uniforme.
- Extra Trees y Random Forest no superan al Seasonal Naïve en esta configuración.
- Los resultados no se interpretan como evidencia de que un algoritmo complejo sea necesariamente mejor.

## Evidencias principales

| Evidencia | Ruta |
|---|---|
| Dataset mensual de cacao | [`data/processed/cacao_mensual_regional_2017_2023.csv`](data/processed/cacao_mensual_regional_2017_2023.csv) |
| Dataset con rezagos | [`data/processed/cacao_modelado_lags_2018_2023.csv`](data/processed/cacao_modelado_lags_2018_2023.csv) |
| Configuración experimental | [`config/experiment_preliminary.json`](config/experiment_preliminary.json) |
| Script del baseline | [`src/03_evaluate_seasonal_naive.py`](src/03_evaluate_seasonal_naive.py) |
| Script de modelos ML | [`src/04_train_models.py`](src/04_train_models.py) |
| Resultados comparativos | [`results/tables/resultados_preliminares_2023.csv`](results/tables/resultados_preliminares_2023.csv) |
| Predicciones Seasonal Naïve | [`results/tables/seasonal_naive_2023.csv`](results/tables/seasonal_naive_2023.csv) |
| Bitácora del experimento | [`experiments/001_prueba_preliminar_2023.md`](experiments/001_prueba_preliminar_2023.md) |
| Mapa de evidencias | [`EVIDENCE.md`](EVIDENCE.md) |
| PPI vigente | [`docs/ppi/PPI_Cacao_2026.pdf`](docs/ppi/PPI_Cacao_2026.pdf) |
| Short paper | [`docs/short_paper/short_paper_cacao_2026.pdf`](docs/short_paper/short_paper_cacao_2026.pdf) |

## Estructura del repositorio

```text
.
├── config/              # configuración de experimentos
├── data/
│   ├── interim/         # integración trazable de los anuarios
│   ├── processed/       # datos de cacao listos para análisis/modelado
│   └── SOURCES.md       # procedencia y reglas de uso
├── docs/                # PPI, short paper y figuras
├── experiments/         # bitácora de ejecuciones y decisiones
├── results/
│   ├── figures/         # gráficos derivados
│   └── tables/          # métricas, predicciones y tablas exportables
└── src/                 # scripts de preparación y evaluación
```

## Reproducibilidad

Cada avance relevante se registra como un commit independiente. El repositorio conserva datos derivados, decisiones metodológicas, configuraciones, scripts, métricas y resultados. El test 2023 no se utiliza para seleccionar regiones ni hiperparámetros.

Para reproducir el baseline estacional:

```bash
python -m pip install -r requirements.txt
python src/03_evaluate_seasonal_naive.py
```

El resultado esperado para el test 2023 es aproximadamente:

```text
MAE   = 131.4145
RMSE  = 267.1935
MASE  = 1.0175
n     = 192 observaciones región-mes
```

## Estado del proyecto

- [x] Integración 2017–2023.
- [x] Selección de 16 series regionales activas de cacao.
- [x] Generación de variables temporales.
- [x] Seasonal Naïve reproducible.
- [x] Comparación preliminar con Ridge, Random Forest, Extra Trees y XGBoost.
- [ ] Validación walk-forward con ventana expansiva.
- [ ] ETS y ARIMA/SARIMA.
- [ ] Predicciones exportadas por cada modelo ML bajo el mismo protocolo.
- [ ] Prueba de significancia de errores cuando corresponda.
- [ ] Integración de variables climáticas, si la fuente resulta compatible.
- [ ] LSTM únicamente si el número efectivo de secuencias permite una comparación justa.

## Próximo hito

El siguiente avance experimental será implementar una validación walk-forward común para todos los modelos y guardar, para cada ejecución, configuración, predicciones, métricas y notas metodológicas.

## Contexto académico

Proyecto de Ingeniería de Sistemas, Universidad Peruana Unión, Filial Juliaca. Docente: Dr. Esteban Tocto Cano.
