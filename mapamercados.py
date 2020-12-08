#Código para visualizar la ubicación de los mercados públicos en la CDMX
##Se importa la paquetería
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlopen
from scipy.stats import gaussian_kde


###Url de los puntos de ubicación de los mercados públicos
urlmercado="https://datos.cdmx.gob.mx/explore/dataset/mercados-publicos/download/?format=csv&timezone=America/Mexico_City&lang=es&use_labels_for_header=true&csv_separator=%2C"

##url colonias
urlcolonia="https://datos.cdmx.gob.mx/explore/dataset/coloniascdmx/download/?format=geojson&timezone=America/Mexico_City&lang=es"

###Leer datos
#Puntos
mercados=pd.read_csv(urlopen(urlmercado))
##Colonias
colonia=gpd.read_file(urlcolonia)

#Fuente y color de títulos y fuente
font="Century Gothic"
col="black"

##Se calcula la densidad de los puntos
xy = np.vstack([mercados.longitud,mercados.latitud])
z = gaussian_kde(xy)(xy)

##Mapa con ambas capas
fig, ax = plt.subplots(figsize=(10,10))
colonia.plot(ax=ax,color="#bdbdbd",edgecolor="white",linewidth=0.4)
ax.scatter(mercados.longitud,mercados.latitud,
alpha=0.7,
c=z,
s=55)
#Título
plt.title("Mercados públicos en la Ciudad de México",fontsize=25, 
fontname=font, color=col)
##Quitar los ejes
ax.axis("off")
#Fuente
ax.annotate("Fuente: @claudiodanielpc con información de la Agencia Digital de Innovación Pública de la Ciudad de México",xy=(0.1, .08), xycoords="figure fraction", 
horizontalalignment="left", verticalalignment="top", fontsize=10, color=col,
fontname=font)
plt.axis("equal")


#Salvar y mostrar
plt.savefig("mercados.png",format="png",dpi=600,transparent=False)
plt.show()