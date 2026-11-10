# Próximos hitos

## Hito 1: cerrar reproducibilidad de la prueba preliminar
- fijar los hiperparámetros exactos de cada modelo;
- guardar semilla y versiones de dependencias;
- generar predicciones fila a fila para 2023.

## Hito 2: validación temporal final
- implementar expanding-window walk-forward;
- conservar horizonte de un mes;
- reportar métricas agregadas y por región.

## Hito 3: modelos estadísticos
- ETS;
- ARIMA/SARIMA cuando la serie lo admita;
- misma ventana y mismo horizonte que ML.

## Hito 4: contraste estadístico
- revisar supuestos para Diebold–Mariano;
- aplicar solo cuando la estructura de errores lo permita.

## Hito 5: variables exógenas
- evaluar precio rezagado;
- investigar lluvia, temperatura y ONI;
- documentar disponibilidad temporal para evitar leakage.

## Hito 6: deep learning condicional
- evaluar LSTM únicamente si el número efectivo de secuencias es suficiente;
- usar la misma separación temporal y métricas.
