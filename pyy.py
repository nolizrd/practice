import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon

# Загрузка данных из CSV
df = pd.read_csv('data.csv')

# Создание списка координат для полигона
coords = df.sort_values(by='PointOrder')[['Longitude', 'Latitude']].values

# Создание полигона
polygon = Polygon(coords)

# Добавление свойств полигона
properties = {
    "name": "БУХТА БАБУШКА",
    "type": "место у воды",
    "description": "- А почему бухта так называется? – спрашивают туристы. - Потому что в ней уютно и тепло, как у бабушки в гостях! – улыбаясь, отвечают местные гиды.",
    "price": "250 рублей"
}

# Создание GeoDataFrame
gdf = gpd.GeoDataFrame([properties], geometry=[polygon], crs='epsg:4326')

# Сохранение в формате GeoJSON
gdf.to_file('output.geojson', driver='GeoJSON')
