import sys

import pandas as pd
import geopandas as gpd


def main(csv, gpkg, out):
    df = pd.read_csv(csv).assign(
        Income=lambda x: pd.to_numeric(x.Income.str.replace(",", ""))
    )

    gpd.read_file(gpkg).get(["MSOA01CD", "geometry"]).merge(
        df, how="inner", left_on="MSOA01CD", right_on="MSOA"
    ).to_file(out)


if __name__ == "__main__":
    csv = sys.argv[1]
    gpkg = sys.argv[2]
    out = sys.argv[3]
    main(csv, gpkg, out)
