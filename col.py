# Mapa de colonias de la CDMX

import json
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

##URL del archivo csv de la página de datos abiertos del GOBCDMX
url = "https://datos.cdmx.gob.mx/dataset/04a1900a-0c2f-41ed-94dc-3d2d5bad4065/resource/03368e1e-f05e-4bea-ac17-58fc650f6fee/download/coloniascdmx.csv"

#Directorio de trabajo
dir = os.chdir("C:/Users/ALIENWARE/Documents/dataviz")

#Importar archivo
test = pd.read_csv(url)

##Corroborar que no haya NAs
validos = test[~test["geo_shape"].isna()]

#Nombres de las variables contenidas en CSV
validos.iloc[0]


features = []
#Se itera sobre todas las filas para construir tanto el diccionario properties como el diccionario geometry
for colonia in validos.iterrows():
    ids = colonia[1]["id"]
    nombre = colonia[1]["nombre"]
    entidad = colonia[1]["entidad"]
    geopoint = str(colonia[1]["geo_point_2d"]).split(',')
    cve_alc = colonia[1]["cve_alc"]
    alcaldia = colonia[1]["alcaldia"]
    cve_col = colonia[1]["cve_col"]
    secc_com = str(colonia[1]["secc_com"]).split(',')
    secc_par = str(colonia[1]["secc_par"]).split(',')
    geometry = json.loads(colonia[1]["geo_shape"])
    properties = {
        "id": ids,
        "nombre": nombre,
        "entidad": entidad,
        "geopoint": geopoint,
        "cve_alc": cve_alc,
        "alcaldia": alcaldia,
        "cve_col": cve_col,
        "secc_com": secc_com,
        "secc_par": secc_par,
    }
    feat = {
        "type": "Feature",
        "properties": properties,
        "geometry": geometry
    }
    features.append(feat)

diccio = {"type": "FeatureCollection", "name": "Colonias_CDMX", "features": features}

#Guardar archivo GeoJSON
with open("colonias.json", "w") as outfile:
    json.dump(diccio, outfile)



##Abrir el archivo GeoJSON generado
colonias = gpd.read_file("colonias.json")



##Importar shapefile del Marco Geostadístico Nacional 2020. Este archivo está almacenado en mi computadora.
cdmx = gpd.read_file("C:/Users/ALIENWARE/Documents/censo2020/conjunto_de_datos/09mun.shp")
#Reproyectar
cdmx=cdmx.to_crs(epsg=4326)


##Mapear colonias con delimitación por alcaldía
fig, ax = plt.subplots(figsize=(6, 6))
#Título
ax.set_title("Colonias de la Ciudad de México",
             fontsize=25, fontname="Century Gothic", fontweight="bold", color="black")
#Sin ejes
ax.axis('off')
#Capa colonias
colonias.plot(linewidth=0.3, ax=ax,color="#1C00ff00",
         edgecolor='.5')
#Capa alcaldías
cdmx.plot(linewidth=0.3, ax=ax,
         edgecolor='.5', color="#1C00ff00")
plt.axis("equal")
##Salvar y mostrar
plt.savefig("mapacol.png",format="png",dpi=600,transparent=False)
plt.show()



#############
###Guardar colonias en shapefile por si se quiere usar en GIS.
colonias.to_file("colonias.shp")

