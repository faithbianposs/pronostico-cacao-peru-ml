from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data/interim/dataset_integrado_midagri_2017_2023.csv"
OUTPUT = ROOT / "data/processed/cacao_mensual_regional_2017_2023.csv"
SERIES = ROOT / "data/processed/cacao_series_activas.csv"


def main():
    df = pd.read_csv(INPUT)
    cacao = df[(df["crop_key"] == "cacao") & (~df["is_national"])].copy()

    # La regla se fija con el periodo pretest 2017-2021 para evitar usar 2022-2023
    # al decidir qué regiones permanecen en el experimento.
    pretest = cacao[cacao["year"].between(2017, 2021)]
    annual = (
        pretest.groupby(["region", "year"], as_index=False)["production_t"].sum()
    )
    active = (
        annual.assign(positive=lambda x: x["production_t"] > 0)
        .groupby("region")["positive"]
        .sum()
    )
    active_regions = active[active >= 4].index

    cacao = cacao[cacao["region"].isin(active_regions)].sort_values(["region", "date"])
    cacao.to_csv(OUTPUT, index=False)

    summary = (
        cacao.groupby("region")
        .agg(
            first_date=("date", "min"),
            last_date=("date", "max"),
            months=("date", "count"),
            production_total_t=("production_t", "sum"),
        )
        .reset_index()
    )
    summary.to_csv(SERIES, index=False)

    print(f"Series activas: {summary.shape[0]}")
    print(f"Observaciones región-mes: {cacao.shape[0]}")


if __name__ == "__main__":
    main()
