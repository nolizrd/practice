import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon


df = pd.read_csv('count.csv')

# Создание списка координат для полигона
coords = df.sort_values(by='PointOrder')[['Longitude', 'Latitude']].values

# Создание полигона
polygon = Polygon(coords)

# Создание GeoDataFrame
gdf = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon])

# Сохранение в формате GeoJSON
gdf.to_file('gg.geojson', driver='GeoJSON')
