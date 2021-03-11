#Mapa de carpetas de investigación robo cajero automático
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import os


##Seleccionar directorio de trabajo y crear carpeta
dir = os.chdir ('C:/Users/ALIENWARE/Documents/dataviz')


url="https://archivo.datos.cdmx.gob.mx/victimas_completa_2019_2020.csv"

df = pd.read_csv(url)


##Limpieza de base de datos
# Columnas a minúsculas
df.columns = df.columns.str.lower()


##Dejar solo los datos de 2020
df = df[df["año_hecho"] == 2020]
df = df[df["categoria"] == "ROBO A CUENTAHABIENTE SALIENDO DEL CAJERO CON VIOLENCIA"]

#Capas

##Importar shapes
##Contorno de entidad
cdmx=gpd.read_file("C:/Users/ALIENWARE/Documents/censo2020/conjunto_de_datos/09ent.shp")
#Ageb
ageb=gpd.read_file("C:/Users/ALIENWARE/Documents/censo2020/conjunto_de_datos/09a.shp")

#Reproyectar
cdmx=cdmx.to_crs(epsg=4326)
ageb=ageb.to_crs(epsg=4326)

# Mapa
fig,ax = plt.subplots( 1,figsize = (10,10),facecolor = 'black' )
# Título
ax.set_title( 'Ciudad de México\nRobo a cuentahabiente saliendo del cajero con violencia, 2020',
              fontsize = 20,fontname = 'Century Gothic',
              fontweight = 'bold',color = 'white' )
# Capa entidad
cdmx.plot( ax = ax,color = "#000000",
           edgecolor = "grey",
           linewidth = 0.8 )
# Capa ageb
ageb.plot( ax = ax,color = "#000000",
           edgecolor = "grey",
           linewidth = 0.1 )
# Capa puntos

ax.scatter( df["longitud"],df["latitud"],
            alpha = 0.4,color = "#de2d26" )
ax.axis( 'off' )

# Fuente
ax.annotate( 'Fuente: @claudiodanielpc con datos del Gobierno de la Ciudad de México.\n'
             'Agencia Digital de Innovación Pública. Víctimas en carpetas de investigación FGJ.',
             xy = (0.1,.08),
             xycoords = 'figure fraction',
             horizontalalignment = 'left',verticalalignment = 'top',fontsize = 16,color = 'white',
             fontname = 'Century Gothic' )
# plt.show()
# Salvar
plt.savefig( "cdmxrobocajero.png",format = "png",dpi = 600,transparent = False )
