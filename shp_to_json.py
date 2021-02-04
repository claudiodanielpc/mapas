import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt



##Importar shapefile de alcaldías del Marco Geostadístico Nacional 2020. Este archivo está almacenado en mi computadora.
cdmx = gpd.read_file("C:/Users/ALIENWARE/Documents/censo2020/conjunto_de_datos/09mun.shp")


#Guardar como GeoJSON
cdmx.to_file("cdmx.geojson", driver="GeoJSON")

#Abrir el archivo generado con Pandas
df=pd.read_json("cdmx.geojson")


##Transformar a Geopandas dataframe
df=gpd.GeoDataFrame.from_features(df['features'])


##Mapear
fig, ax = plt.subplots(figsize=(5, 5))
#Sin ejes
ax.axis('off')
#Capa
df.plot(linewidth=0.3, ax=ax,color="#1C00ff00",
         edgecolor='.5')

plt.show()