import geopandas as gpd
from pathlib import Path

pasta = Path("C:/Users/c23418/OneDrive - Bruning Tecnometal Ltda/Documentos/PI 2025/Arquivos")
shapefile = gpd.read_file(pasta /"./Setorização_de_Risco.shp")
print(shapefile.head())

print(shapefile.columns)
print(shapefile.shape)
shapefile.drop(columns="geometry").to_csv("Setorização_de_Risco.csv", index=False)
