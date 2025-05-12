import os
from pathlib import Path

pasta_csv = Path(r"C:\Users\c23418\OneDrive - Bruning Tecnometal Ltda\Documentos\PI2025\Arquivos\csv")

# Listar todos os arquivos da pasta para verificar nomes
print("Arquivos encontrados na pasta:")
for arquivo in os.listdir(pasta_csv):
    if arquivo.endswith(".csv"):
        print("-", arquivo)
