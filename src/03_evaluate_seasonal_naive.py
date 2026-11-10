from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data/processed/cacao_modelado_lags_2018_2023.csv"
OUTPUT = ROOT / "results/tables/seasonal_naive_2023.csv"


def smape(y, yhat):
    den = np.abs(y) + np.abs(yhat)
    return 100 * np.mean(np.where(den == 0, 0, 2 * np.abs(y - yhat) / den))


def main():
    df = pd.read_csv(INPUT)
    history = df[df["year"].between(2018, 2022)]
    test = df[df["year"] == 2023]

    y = test["target_production_t"].to_numpy()
    pred = test["seasonal_naive"].to_numpy()
    scale = mean_absolute_error(history["target_production_t"], history["seasonal_naive"])

    row = {
        "model": "SeasonalNaive",
        "MAE_t": mean_absolute_error(y, pred),
        "RMSE_t": mean_squared_error(y, pred) ** 0.5,
        "sMAPE_pct": smape(y, pred),
        "R2": r2_score(y, pred),
        "MASE": mean_absolute_error(y, pred) / scale,
        "n_test": len(test),
    }
    pd.DataFrame([row]).to_csv(OUTPUT, index=False)
    print(pd.DataFrame([row]).to_string(index=False))


if __name__ == "__main__":
    main()
