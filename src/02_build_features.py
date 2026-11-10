from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data/processed/cacao_mensual_regional_2017_2023.csv"
OUTPUT = ROOT / "data/processed/cacao_features_reproducibles.csv"


def main():
    df = pd.read_csv(INPUT, parse_dates=["date"]).sort_values(["region", "date"])
    g = df.groupby("region", group_keys=False)

    for lag in (1, 2, 3, 6, 12):
        df[f"lag{lag}"] = g["production_t"].shift(lag)

    # La ventana termina en t-1. No incluye el mes que se pronostica.
    shifted = g["production_t"].shift(1)
    df["roll3"] = shifted.groupby(df["region"]).rolling(3).mean().reset_index(level=0, drop=True)
    df["roll6"] = shifted.groupby(df["region"]).rolling(6).mean().reset_index(level=0, drop=True)
    df["roll12"] = shifted.groupby(df["region"]).rolling(12).mean().reset_index(level=0, drop=True)

    df["month_sin"] = np.sin(2 * np.pi * df["month"] / 12)
    df["month_cos"] = np.cos(2 * np.pi * df["month"] / 12)
    df["trend"] = g.cumcount() + 1
    df["seasonal_naive"] = df["lag12"]

    df["split"] = np.select(
        [df["year"].between(2018, 2021), df["year"].eq(2022), df["year"].eq(2023)],
        ["train", "validation", "test"],
        default="history",
    )

    required = ["lag1", "lag2", "lag3", "lag6", "lag12", "roll3", "roll6", "roll12"]
    out = df[df["year"] >= 2018].dropna(subset=required).copy()
    out.to_csv(OUTPUT, index=False)
    print(out["split"].value_counts())


if __name__ == "__main__":
    main()
