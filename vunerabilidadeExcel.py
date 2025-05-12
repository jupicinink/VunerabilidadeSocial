import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Caminhos
pasta_csv = r"C:\Users\c23418\OneDrive - Bruning Tecnometal Ltda\Documentos\PI2025\Arquivos\csv"
pasta = r"C:\Users\c23418\OneDrive - Bruning Tecnometal Ltda\Documentos\PI2025\Arquivos"
arquivo_excel = f"{pasta_csv}/atlasivs_dadosbrutos_Porto_Alegre.xlsx"
arquivo_shp = f"{pasta}/RS_Municipios_2024.shp"



# Leitura dos dados
df = pd.read_excel(arquivo_excel, sheet_name="Município")
gdf_shp = gpd.read_file(arquivo_shp)

# Padronização do código de município
gdf_shp['CD_MUN_6'] = gdf_shp['CD_MUN'].astype(str).str[:6]
df['Municipio_6digt'] = df['Municipio_6digt'].astype(str).str.zfill(6)

# Filtra Porto Alegre
gdf_poa = gdf_shp[gdf_shp['CD_MUN_6'] == '431490']
df_poa = df[df['Municipio_6digt'] == '431490']

# Merge
gdf_ivs = gdf_poa.merge(df_poa, left_on='CD_MUN_6', right_on='Municipio_6digt')

# Plotagem com legenda
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_aspect("auto")

plot = gdf_ivs.plot(
    column='ivs',
    cmap='OrRd',
    legend=True,
    ax=ax,
    edgecolor='black',
    legend_kwds={
        'label': "Índice de Vulnerabilidade Social (IVS)",
        'orientation': "vertical",
        'shrink': 0.7,
        'pad': 0.02
    }
)

plt.title("Mapa de IVS - Porto Alegre", fontsize=14)
plt.axis('off')
plt.tight_layout()
plt.show()
