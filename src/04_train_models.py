"""Entrenamiento reproducible para la siguiente iteración del experimento.

Los resultados que ya aparecen en el PPI se conservan en
results/tables/resultados_preliminares_2023.csv. Este script deja fijado el
protocolo para que las siguientes corridas queden versionadas. La próxima
entrega debe reemplazar cualquier búsqueda informal por una configuración
cerrada documentada en `config/` y registrar el nuevo CSV mediante commit.
"""

from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

try:
    from xgboost import XGBRegressor
except ImportError:
    XGBRegressor = None

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/processed/cacao_modelado_lags_2018_2023.csv"

NUMERIC = [
    "lag1", "lag2", "lag3", "lag6", "lag12",
    "roll3", "roll6", "roll12", "month_sin", "month_cos", "trend",
]
CATEGORICAL = ["region"]


def build_preprocessor(scale=False):
    num = StandardScaler() if scale else "passthrough"
    return ColumnTransformer([
        ("num", num, NUMERIC),
        ("region", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL),
    ])


def main():
    df = pd.read_csv(DATA)
    train = df[df["year"].between(2018, 2021)]
    val = df[df["year"] == 2022]
    test = df[df["year"] == 2023]
    train_val = pd.concat([train, val], ignore_index=True)
    xcols = NUMERIC + CATEGORICAL

    models = {
        "Ridge": Pipeline([( "prep", build_preprocessor(scale=True)), ("model", Ridge(alpha=1.0))]),
        "RandomForest": Pipeline([( "prep", build_preprocessor()), ("model", RandomForestRegressor(n_estimators=400, random_state=42, n_jobs=-1))]),
        "ExtraTrees": Pipeline([( "prep", build_preprocessor()), ("model", ExtraTreesRegressor(n_estimators=400, random_state=42, n_jobs=-1))]),
    }
    if XGBRegressor is not None:
        models["XGBoost"] = Pipeline([( "prep", build_preprocessor()), ("model", XGBRegressor(n_estimators=400, max_depth=4, learning_rate=0.03, subsample=0.9, colsample_bytree=0.9, random_state=42, n_jobs=2))])

    rows = []
    for name, model in models.items():
        model.fit(train[xcols], train["target_production_t"])
        val_pred = model.predict(val[xcols])
        val_mae = mean_absolute_error(val["target_production_t"], val_pred)
        model.fit(train_val[xcols], train_val["target_production_t"])
        pred = model.predict(test[xcols])
        rows.append({
            "model": name,
            "validation_MAE_t": val_mae,
            "test_MAE_t": mean_absolute_error(test["target_production_t"], pred),
            "test_RMSE_t": mean_squared_error(test["target_production_t"], pred) ** 0.5,
            "note": "corrida reproducible de referencia; no reemplaza el CSV preliminar hasta validar configuración final"
        })

    out = pd.DataFrame(rows)
    path = ROOT / "results/tables/reproduction_reference_models.csv"
    out.to_csv(path, index=False)
    print(out.to_string(index=False))


if __name__ == "__main__":
    main()
