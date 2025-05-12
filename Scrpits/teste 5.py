from pathlib import Path
import pandas as pd
pasta_csv = Path(r"C:\Users\c23418\OneDrive - Bruning Tecnometal Ltda\Documentos\PI2025\Arquivos\csv")

# === 1. Ler dados censitários ===
domicilios = pd.read_csv(pasta_csv /"Censo 2022 - Características dos domicílios - Porto Alegre (RS).csv", sep=';', encoding='utf-8')
favela = pd.read_csv(pasta_csv /"Censo 2022 - População residente em favelas - Porto Alegre (RS).csv", sep=';', encoding='utf-8')
instru = pd.read_csv(pasta_csv /"Censo 2022 - Nível de instrução - Porto Alegre (RS).csv", sep=';', encoding='utf-8')
territorio = pd.read_csv(pasta_csv /"Censo 2022 - Território - Porto Alegre (RS).csv", sep=';', encoding='utf-8')

# === 2. Converter strings com vírgula para float ===
def conv_percent(valor):
    return float(valor.replace(',', '.'))

domicilios["Não possui(%)"] = domicilios["Não possui(%)"].apply(conv_percent)
favela["Percentual"] = favela["Percentual"].apply(conv_percent)

# === 3. Extrair indicadores relevantes ===
sem_esgoto = domicilios.loc[domicilios["Característica"] == "Conectados à rede de esgoto", "Não possui(%)"].values[0]
sem_agua = domicilios.loc[domicilios["Característica"] == "Abastecidos pela rede geral de água", "Não possui(%)"].values[0]
pop_favela = favela.loc[favela["Situação"] == "Em favelas", "Percentual"].values[0]
pop_sem_instrucao = instru.loc[instru["Nível de instrução"] == "Sem instrução e fundamental incompleto", "População (pessoas)"].values[0]

# === 4. Total da população (calculado a partir do nível de instrução) ===
total_pop = instru["População (pessoas)"].sum()
percentual_sem_instrucao = round((pop_sem_instrucao / total_pop) * 100, 2)

# === 5. Juntar dados em um dataframe resumo ===
dados = {
    "Município": ["Porto Alegre"],
    "Código do Município": [4314902],
    "% Sem esgoto": [sem_esgoto],
    "% Sem água encanada": [sem_agua],
    "% Em favelas": [pop_favela],
    "% Sem instrução/fund. incompleto": [percentual_sem_instrucao],
    "Densidade hab/km²": [territorio["Densidade demográfica(hab/km²)"].values[0]]
}

df_vulnerabilidade = pd.DataFrame(dados)

# === 6. Carregar os dados de risco (convertidos para CSV) ===
inundacao = pd.read_csv(pasta_csv /"inundacao_atributos.csv", encoding="latin1")
corrida = pd.read_csv(pasta_csv /"Corrida_de_Massa_Área.csv", encoding="latin1")
enxurrada = pd.read_csv(pasta_csv / "Enxurrada_Área.shp.csv", encoding="latin1")
risco_geo = pd.read_csv(pasta_csv /"risco_geologico_porto_alegre.csv", encoding="latin1")

# Contagem total de registros de risco (linhas)
total_riscos = len(inundacao) + len(corrida) + len(enxurrada) + len(risco_geo)

# Adicionar ao dataframe final
df_vulnerabilidade["Nº total de áreas de risco mapeadas"] = total_riscos

# === 7. Exportar o resultado ===
df_vulnerabilidade.to_csv(pasta_csv /"resumo_vulnerabilidade_risco_porto_alegre.csv", index=False, encoding="latin1")

print("✅ Análise gerada com sucesso. Veja: resumo_vulnerabilidade_risco_porto_alegre.csv")
