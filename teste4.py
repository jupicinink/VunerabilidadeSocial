
import pandas as pd


domicilios = pd.read_csv("Censo 2022 - Características dos domicílios - Porto Alegre (RS).csv")
favela = pd.read_csv("Censo 2022 - População residente em favelas - Porto Alegre (RS).csv")
renda = pd.read_csv("Censo 2022 - Características dos domicílios - Porto Alegre (RS).csv")  
territorio = pd.read_csv("Censo 2022 - Território - Porto Alegre (RS).csv")


inundacao = pd.read_csv("inundacao_atributos.csv")
enxurrada = pd.read_csv("Enxurrada_Área.csv")
risco_geologico = pd.read_csv("risco_geologico_porto_alegre.csv")


riscos = pd.concat([inundacao, enxurrada, risco_geologico], ignore_index=True)

#
vulnerabilidade = domicilios[
    (domicilios["sem_esgoto"] > 30) &         
    (domicilios["sem_agua_encanada"] > 20) &  
    (domicilios["renda_media"] < 1200)        
]


comparacao = vulnerabilidade.merge(riscos, how="inner", on="codigo_setor")  


comparacao.to_csv("setores_vulneraveis_em_risco.csv", index=False)

print(f"Setores vulneráveis em áreas de risco encontrados: {comparacao.shape[0]}")
