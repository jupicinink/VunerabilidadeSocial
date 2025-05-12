import pandas as pd
import numpy as np


n = 100


np.random.seed(42) 

dados = pd.DataFrame({
    "ID_SETOR": [f"{i:04d}" for i in range(n)],
    "renda_media": np.random.normal(loc=1800, scale=800, size=n).astype(int),
    "sem_esgoto_percent": np.random.uniform(0, 80, size=n).round(1),
    "em_area_de_risco": np.random.choice([True, False], size=n, p=[0.3, 0.7])
})


dados["renda_media"] = dados["renda_media"].apply(lambda x: max(x, 300))

# Aplicar critérios de vulnerabilidade
dados["vulneravel"] = (
    (dados["renda_media"] < 1100) &
    (dados["sem_esgoto_percent"] > 30) &
    (dados["em_area_de_risco"])
).astype(int)


dados.to_csv("dados_vulnerabilidade_sinteticos.csv", index=False)

print("CSV gerado com sucesso: dados_vulnerabilidade_sinteticos.csv")
