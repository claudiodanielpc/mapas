##Mapa de unidades económicas de Pátzcuaro a nivel manzana
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import zipfile
import requests
import os
import io

##URLS de cartografía e de unidades económicas de Michoacán
urls = ["https://www.inegi.org.mx/contenidos/masiva/denue/denue_16_csv.zip",
        "https://www.inegi.org.mx/contenidos/productos/prod_serv/contenidos/espanol/bvinegi/productos/geografia/marcogeo/889463807469/16_michoacandeocampo.zip"]

# Descomprimir y extraer los archivos
for url in urls:
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()

# Abrir archivo de unidades económicas
df = pd.read_csv(
    "conjunto_de_datos/denue_inegi_16_.csv",
    encoding="latin1",
    dtype={
        "manzana": int,
        "id": int,
        "cve_ent": str,
        "cve_mun": str,
        "cve_loc": str,
        "ageb": str,
    },
)

# Crear claves
df["municipio"] =df['cve_ent'].astype(str).str.zfill(2)+df['cve_mun'].astype(str).str.zfill(3)

# Filtrar Pátzcuaro
df = df[df["municipio"] == "16066"]

# Clave manzana
df["CVEGEO"] = (
    df["cve_ent"].str.zfill(2)
    + df["cve_mun"].str.zfill(3)
    + df["cve_loc"].str.zfill(4)
    + df["ageb"].str.zfill(4)
    + df["manzana"].astype(str).str.zfill(3)
)

##Agrupar por manzana
df = df.groupby("CVEGEO", as_index=False)[["id"]].count()


##Importar shapes
mza = gpd.read_file(
    "conjunto_de_datos/16m.shp",
    dtype={
        "CVE_ENT": str,
        "CVE_MUN": str,
        "CVE_LOC": str,
    },
)

# Pegar los datos al shape
mza = mza.merge(df, how="left", on="CVEGEO")

# Crear claves para filtrar
mza["municipio"] = mza["CVE_ENT"].str.zfill(2) + mza["CVE_MUN"].str.zfill(3)
mza["localidad"] = (
    mza["CVE_ENT"].str.zfill(2)
    + mza["CVE_MUN"].str.zfill(3)
    + mza["CVE_LOC"].str.zfill(4)
)

# Filtrar Pátzcuaro y las localides con manzanas alejadas (la búsqueda de las manzanas alejadas la hice de manera manual)
localidades_no_seleccionadas = {
    "160660013",
    "160660009",
    "160660015",
    "160660043",
    "160660028",
}
mza = mza[
    (mza["municipio"] == "16066")
    & (~mza["localidad"].isin(localidades_no_seleccionadas))
]


# Mapa
fig, ax = plt.subplots(figsize=(8, 6))

# Título
ax.set_title(
    "Unidades económicas en Pátzcuaro\n a nivel manzana",
    fontsize=25,
    fontname="Century Gothic",
    fontweight="bold",
    color="black",
)

# Manzanas
mza.plot(
    column="id",
    cmap="Reds",
    linewidth=0.1,
    ax=ax,
    edgecolor=".5",
    legend=True,
    legend_kwds={"label": "Número de unidades económicas"},
)

# Fuente
ax.annotate(
    "Fuente: Elaboración propia con datos de INEGI\nINEGI. Directorio Estadístico Nacional de Unidades Económicas (DENUE)",
    xy=(0.1, 0.08),
    xycoords="figure fraction",
    horizontalalignment="left",
    verticalalignment="top",
    fontsize=13,
    color="black",
    fontname="Century Gothic",
)

# Coordenadas elegidas manualmente
ax.set_ylim(832_000, 839_500)
ax.set_xlim(2.5375e6, 2.545e6)

ax.axis("off")
ax.axis("equal")

# Salvar y mostrar
plt.savefig("uemichpatz2.png", format="png", dpi=1000, transparent=False)
plt.show()
