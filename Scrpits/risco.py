import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from pathlib import Path
import pandas as pd

# Caminho
pasta_csv = Path(r"C:\Users\c23418\OneDrive - Bruning Tecnometal Ltda\Documentos\PI2025\Arquivos")
setorizacao = gpd.read_file(pasta_csv / "Setorização_de_Risco.shp")
municipios = gpd.read_file(pasta_csv / "RS_Municipios_2024.shp")

# Colunas de tipo de risco
colunas_risco = ['tipolo_g1', 'tipolo_g2', 'tipolo_g3', 'tipolo_g4', 'tipolo_g5']

# Unificar os tipos de risco em uma nova coluna 'RISCOS_COMBINADOS'
def extrair_risco(row):
    riscos = set()
    for col in colunas_risco:
        val = row[col]
        if isinstance(val, str) and val.strip():
            riscos.add(val.strip())
    return ', '.join(riscos)

setorizacao["RISCOS_COMBINADOS"] = setorizacao.apply(extrair_risco, axis=1)

# Dicionário de cores
cores = {
    "Inundação": "blue",
    "Enxurrada": "cyan",
    "Deslizamento": "red",
    "Queda": "orange",
    "Erosão": "brown",
    "Corrida de massa": "purple"
}

# Plotagem
fig, ax = plt.subplots(figsize=(12, 10))

# Plotar municípios como camada de base
municipios.plot(ax=ax, color='white', edgecolor='black')

# Plotar os setores de risco por tipo
for risco, cor in cores.items():
    camada = setorizacao[setorizacao["RISCOS_COMBINADOS"].str.contains(risco, case=False, na=False)]
    if not camada.empty:
        camada.plot(ax=ax, color=cor, label=risco, alpha=0.6, edgecolor='black')

# Legenda
legenda = [Patch(facecolor=cor, edgecolor='black', label=risco) for risco, cor in cores.items()]
ax.legend(handles=legenda)
plt.title("Setorização de Risco por Tipo")
plt.show()
