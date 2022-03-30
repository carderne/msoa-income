# msoa income

1. [Download the MSOA GIS data from here](https://geoportal.statistics.gov.uk/datasets/ons::middle-layer-super-output-areas-december-2001-boundaries-ew-bfc/about), reproject to WGS84 and save.
2. [Download the income data as CSV from here](https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/datasets/smallareaincomeestimatesformiddlelayersuperoutputareasenglandandwales).
4. Clone this repo:
```bash
git clone https://github.com/carderne/msoa-income.git
cd msoa-income
```
3. Run the script:
```bash
pip install pandas geopandas
python join.py income.csv msoas.gpkg msoas_joined.geojson
```
4. Convert to MBTiles:
```bash
tippecanoe -o msoas.mbtiles -Z4 -z12 -l msoas -f msoas_joined.geojson
```
