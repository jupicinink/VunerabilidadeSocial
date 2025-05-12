import geopandas as gpd
import matplotlib.pyplot as plt

# Caminho completo
base_path = "C:/Users/c23418/OneDrive - Bruning Tecnometal Ltda/Documentos/PI2025"
arquivo = f"{base_path}/Enxurrada_Área.shp"

# Carregar shapefile
enxurrada = gpd.read_file(arquivo)

# Verifica se o GeoDataFrame está vazio
if enxurrada.empty:
    print("❌ O arquivo está vazio!")
else:
    # Verifica e corrige o sistema de coordenadas se necessário
    if enxurrada.crs is None:
        enxurrada.set_crs(epsg=4326, inplace=True)

    # Reprojetar para garantir compatibilidade
    enxurrada = enxurrada.to_crs(epsg=4326)

    # Corrigir geometrias inválidas
    enxurrada = enxurrada[enxurrada.is_valid]
    enxurrada = enxurrada[~enxurrada.geometry.is_empty]

    # Plotagem segura
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_aspect("auto")  # Evita erro de aspecto

    enxurrada.plot(ax=ax, color='cyan', alpha=0.5, edgecolor='black')
    plt.title("Mapa - Enxurrada Área")
    plt.show()
