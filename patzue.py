##Mapa de unidades económicas de Pátzcuaro a nivel manzana

import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import zipfile
import requests
import os
import io

##Directorio de trabajo
dir = os.chdir("C:/Users/ALIENWARE/Documents/censo2020/mich")


##URLS de cartografía e de unidades económicas de Michoacán
urls = ["https://www.inegi.org.mx/contenidos/masiva/denue/denue_16_csv.zip",
        "https://www.inegi.org.mx/contenidos/productos/prod_serv/contenidos/espanol/bvinegi/productos/geografia/marcogeo/889463807469/16_michoacandeocampo.zip"]

# Descomprimir y extraer los archivos


for url in urls:
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()

##Abrir archivo de unidades económicas

df = pd.read_csv("conjunto_de_datos/denue_inegi_16_.csv")

##Crear claves
df["manzana"]= df["manzana"].apply(int)
#clave mun
df["municipio"] =df['cve_ent'].astype(str).str.zfill(2)+df['cve_mun'].astype(str).str.zfill(3)

#Filtrar Pátzcuaro
df=df[(df.municipio=="16066")]

#clave manzana
df["CVEGEO"] =df['cve_ent'].astype(str).str.zfill(2)+df['cve_mun'].astype(str).str.zfill(3)+df['cve_loc'].astype(str).str.zfill(4)+df['ageb'].astype(str).str.zfill(4)+df['manzana'].astype(str).str.zfill(3)

##Agrupar por manzana
df=df.groupby('CVEGEO',as_index=False)[['id']].count()
df["id"]=df["id"].apply(int)


##Importar shapes
mza=gpd.read_file("conjunto_de_datos/16m.shp")


#Pegar los datos al shape
mza = mza.merge(df, how="left",on="CVEGEO")

#crear claves para filtrar
mza["municipio"] =mza['CVE_ENT'].astype(str).str.zfill(2)+mza['CVE_MUN'].astype(str).str.zfill(3)
mza["localidad"] =mza['CVE_ENT'].astype(str).str.zfill(2)+mza['CVE_MUN'].astype(str).str.zfill(3)+mza['CVE_LOC'].astype(str).str.zfill(4)



#Filtrar Pátzcuaro y las localides con manzanas alejadas (la búsqueda de las manzanas alejadas la hice de manera manual)
mza=mza[(mza.municipio=="16066") & (mza.localidad!="160660013") &
        (mza.localidad!="160660009") &
        (mza.localidad!="160660015") &
        (mza.localidad!="160660043") &
        (mza.localidad!="160660028")]
mun=mun[mun.CVEGEO=="16066"]


##Mapa

fig, ax = plt.subplots(figsize=(8,6))

# Título
ax.set_title("Unidades económicas en Pátzcuaro\n a nivel manzana",
             fontsize=25, fontname="Century Gothic",
             fontweight="bold", color="black")
# Sin ejes
ax.axis('off')
# Manzanas
mza.plot(column='id', cmap='Reds', linewidth=0.1, ax=ax,
        edgecolor='.5', legend=True,
        legend_kwds={'label': "Número de unidades económicas"})

# Fuente
ax.annotate("Fuente: Elaboración propia con datos de INEGI\nINEGI. Directorio Estadístico Nacional de Unidades Económicas (DENUE)", xy=(0.1, .08),
            xycoords="figure fraction",
            horizontalalignment="left", verticalalignment="top", fontsize=13, color="black",
            fontname="Century Gothic")
plt.axis("equal")
##Salvar y mostrar
 plt.savefig("uemichpatz2.png",format="png",dpi=1000,transparent=False)
plt.show()
