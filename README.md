# Pronóstico mensual de la producción de cacao en el Perú mediante aprendizaje automático

Repositorio de evidencias del PPI y short paper de Ingeniería de Sistemas. El estudio evalúa modelos de aprendizaje automático para pronosticar la producción mensual regional de cacao en el Perú usando datos agrícolas abiertos de MIDAGRI/SIEA y validación temporal.

## Objetivo general

Evaluar el desempeño de modelos de aprendizaje automático para el pronóstico mensual de la producción regional de cacao en el Perú, mediante un esquema de validación temporal y comparación con una referencia estacional.

## Pregunta de investigación

¿Los modelos de aprendizaje automático evaluados superan a un modelo Seasonal Naïve en el pronóstico mensual de la producción regional de cacao en el Perú cuando se mantiene una separación temporal entre entrenamiento, validación y prueba?

## Datos

- Periodo: 2017–2023.
- Unidad de análisis: región–mes.
- Series regionales activas de cacao: 16.
- Observaciones de cacao: 1,344.
- Historia inicial: 2017.
- Entrenamiento preliminar: 2018–2021.
- Validación: 2022.
- Test final fuera de muestra: 2023.

Los archivos oficiales originales no se redistribuyen como parte central del repositorio. En `data/SOURCES.md` se documenta su procedencia. Los datos derivados conservan campos de trazabilidad hacia los anuarios utilizados.

## Modelos evaluados en la prueba preliminar

- Seasonal Naïve, referencia estacional t-12.
- Ridge Regression.
- Random Forest.
- Extra Trees.
- XGBoost.

ETS, ARIMA/SARIMA, walk-forward completo y aprendizaje profundo forman parte del trabajo pendiente y se incorporarán mediante commits posteriores cuando la comparación sea metodológicamente equivalente.

## Resultados preliminares sobre 2023

| Modelo | MAE (t) | RMSE (t) | sMAPE (%) | MASE |
|---|---:|---:|---:|---:|
| Seasonal Naïve | 131.41 | 267.19 | 34.31 | 1.018 |
| Ridge | 117.71 | 227.33 | 58.30 | 0.911 |
| XGBoost | 127.67 | 229.76 | 57.78 | 0.989 |
| Extra Trees | 135.38 | 262.06 | 49.53 | 1.048 |
| Random Forest | 142.44 | 297.46 | 53.05 | 1.103 |

Estos resultados son preliminares. Ridge obtuvo el menor MAE y RMSE y un MASE menor que 1. El resultado no se interpreta como superioridad uniforme porque sMAPE favorece a la referencia estacional.

## Estructura

```text
.
├── config/              # configuración del experimento
├── data/
│   ├── interim/         # integración trazable de los anuarios
│   ├── processed/       # datos de cacao listos para análisis/modelado
│   └── SOURCES.md       # procedencia y reglas de uso
├── docs/                # PPI, short paper y figuras
├── experiments/         # bitácora de ejecuciones y decisiones
├── results/
│   ├── figures/         # gráficos derivados
│   └── tables/          # métricas y tablas exportables
└── src/                 # scripts de preparación y evaluación
```

## Reproducibilidad

Cada avance importante se registra como un commit separado. El repositorio conserva datos derivados, decisiones metodológicas, configuraciones y resultados. El test 2023 no se utiliza para seleccionar regiones ni hiperparámetros.

## Estado del proyecto

- [x] Integración 2017–2023.
- [x] Selección de 16 series regionales activas de cacao.
- [x] Generación de variables temporales.
- [x] Seasonal Naïve.
- [x] Comparación preliminar con Ridge, Random Forest, Extra Trees y XGBoost.
- [ ] Validación walk-forward con ventana expansiva.
- [ ] ETS y ARIMA/SARIMA.
- [ ] Prueba de significancia de errores cuando corresponda.
- [ ] Integración de variables climáticas, si la fuente resulta compatible.
- [ ] LSTM únicamente si el número efectivo de secuencias permite una comparación justa.

## Autor y contexto académico

Proyecto de Ingeniería de Sistemas, Universidad Peruana Unión, Filial Juliaca. Docente: Dr. Esteban Tocto Cano.
