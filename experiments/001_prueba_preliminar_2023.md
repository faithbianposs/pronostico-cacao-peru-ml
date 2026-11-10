# Experimento 001: prueba temporal preliminar

## Propósito

Comprobar que el conjunto integrado admite un problema real de pronóstico mensual y comparar modelos de aprendizaje automático con una referencia estacional.

## Corte temporal

- Historia para rezagos: 2017.
- Train: 2018–2021.
- Validation: 2022.
- Test: 2023.
- Horizonte: un mes.
- Test: 192 observaciones región–mes, 16 regiones x 12 meses.

## Modelos registrados

Seasonal Naïve, Ridge, Random Forest, Extra Trees y XGBoost.

## Hallazgo principal

Ridge obtuvo MAE 117.71 t, RMSE 227.33 t y MASE 0.911 en 2023. Seasonal Naïve obtuvo MAE 131.41 t, RMSE 267.19 t y MASE 1.018. La mejora de Ridge no fue uniforme: su sMAPE fue mayor que el baseline, por lo que el resultado debe presentarse por métrica y no como una victoria general del aprendizaje automático.

## Limitaciones de esta ejecución

1. Es una prueba preliminar y todavía no corresponde al walk-forward final.
2. ETS y ARIMA/SARIMA aún no están incluidos.
3. No se aplicó una prueba de significancia de diferencias de error.
4. Las variables climáticas todavía no forman parte del conjunto analítico.
5. El CSV de resultados se conserva como evidencia de la ejecución preliminar. Las configuraciones exactas de la siguiente corrida deberán quedar fijadas en `config/` antes de reemplazar resultados del PPI.
