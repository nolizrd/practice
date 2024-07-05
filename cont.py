import geopandas as gpd

# Загрузка данных из файла (например, GeoJSON, Shapefile)
gdf = gpd.read_file('hh.geojson')

# Получение контура (границы) полигона
gdf_boundary = gdf.boundary

# Сохранение контура в файл GeoJSON
gdf_boundary.to_file("contour.geojson", driver='GeoJSON')
