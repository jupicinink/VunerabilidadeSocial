import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from pathlib import Path

# Caminho para os arquivos
pasta_csv = Path(r"C:\Users\c23418\OneDrive - Bruning Tecnometal Ltda\Documentos\PI2025\Arquivos")

# Carregar os shapefiles
inundacao = gpd.read_file(pasta_csv / "Inundação_Área.shp")
setorizacao = gpd.read_file(pasta_csv / "Setorização_de_Risco.shp")
municipios = gpd.read_file(pasta_csv / "RS_Municipios_2024.shp")

# Criar figura
fig, ax = plt.subplots(figsize=(12, 10))

# Plotar camadas
municipios.plot(ax=ax, color='white', edgecolor='black')
inundacao.plot(ax=ax, color='blue', alpha=0.5)
setorizacao.plot(ax=ax, color='green', alpha=0.3)

# Criar legenda personalizada
legenda = [
    Patch(facecolor='blue', edgecolor='black', label='Inundação'),
    Patch(facecolor='green', edgecolor='black', label='Setorização de Risco'),
]

# Adicionar legenda
ax.legend(handles=legenda)
plt.title("Mapa de Riscos e Municípios")
plt.show()
