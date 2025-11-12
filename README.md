# 🛰️ Análise Espacial da Vulnerabilidade Social ao Clima em Porto Alegre

Este repositório contém um projeto de modelagem matemática e geoespacial focado na identificação de áreas com alta **Vulnerabilidade Social** em relação aos **Riscos Climáticos** no município de **Porto Alegre (RS)**. O objetivo é apoiar a formulação de políticas públicas de mitigação e adaptação.

---

## 🛠️ Tecnologias e Dependências

O projeto é construído sobre a linguagem **Python** e utiliza as seguintes bibliotecas principais para Geoprocessamento e Análise de Dados:

| Categoria | Tecnologia | Uso Principal |
| :--- | :--- | :--- |
| **Geoprocessamento** | **GeoPandas** | Manipulação, leitura e análise de dados geoespaciais (Shapefiles). |
| **Dados** | **Pandas** | Leitura, limpeza e tratamento de dados tabulares do Censo 2022. |
| **Computação Numérica** | **NumPy** | Suporte para operações matemáticas e vetoriais de alto desempenho. |
| **Visualização** | **Matplotlib / Seaborn** | Geração de mapas temáticos e gráficos estatísticos dos resultados. |

---

## 🔍 Fatores de Vulnerabilidade Analisados

A metodologia integra dados de risco físico com indicadores socioeconômicos para classificar a vulnerabilidade por setor censitário.

### 1. 🏚️ Risco de Exposição Física
* **Indicador:** Presença ou proximidade a áreas de **risco geológico/hidrológico** (inundações, enxurradas, deslizamentos).
* **Fonte:** Shapefiles georreferenciados de áreas de risco (e.g., CPRM - Serviço Geológico do Brasil).

### 2. 💸 Vulnerabilidade Socioeconômica
* **Indicador:** **Baixa renda domiciliar média** e outros fatores demográficos/sociais do Censo.
* **Fonte:** Dados desagregados do Censo 2022 (IBGE).

### 3. 🚫 Vulnerabilidade Estrutural
* **Indicador:** Deficiência no acesso e na qualidade do **saneamento básico** (esgoto adequado e abastecimento de água).
* **Fonte:** Dados desagregados do Censo 2022 (IBGE).

---

## ⚙️ Metodologia e Workflow

O pipeline de análise é executado via scripts Python e segue as seguintes etapas:

1.  **Leitura e Preparação de Dados:**
    * Carregamento de dados vetoriais (Shapefiles) de risco e setores censitários usando `GeoPandas`.
    * Carregamento e tratamento dos dados socioeconômicos do Censo usando `Pandas`.
2.  **Interseção Espacial:**
    * Cálculo da sobreposição (`gpd.overlay` ou métodos similares) entre as áreas de risco e os setores censitários para determinar a **população exposta**.
3.  **Cálculo de Indicadores:**
    * Normalização e ponderação dos indicadores de Renda e Saneamento.
    * Combinação dos indicadores (Risco Físico, Renda, Saneamento) em um **Índice Composto de Vulnerabilidade Social ao Clima**.
4.  **Classificação Final:**
    * Classificação de cada setor censitário em categorias de vulnerabilidade (ex: Baixa, Média, Alta, Muito Alta).
5.  **Exportação:**
    * Geração de novos Shapefiles ou arquivos GeoJSON e CSV para visualização em Sistemas de Informação Geográfica (GIS) e relatórios.

---

## 📂 Estrutura do Repositório

| Diretório/Arquivo | Conteúdo | Finalidade |
| :--- | :--- | :--- |
| `Arquivos/` | Dados `.shp` e `.csv` | Armazenamento dos **dados de entrada** (risco, censo) e resultados intermediários. |
| `Scrpits/` | Scripts Python | Contém o **código-fonte** de todo o pipeline de processamento e análise geoespacial. |
| `vunerabilidadeExcel.py` | Script Principal | Exemplo de script que executa a interseção e a classificação de vulnerabilidade. |
| `README.md` | Este arquivo | Documentação e guia de referência do projeto. |

---

## 🎯 Contribuição e Propósito

Este projeto visa gerar conhecimento aprofundado para que gestores e formuladores de políticas públicas possam:
* **Priorizar** investimentos em infraestrutura e saneamento básico.
* **Planejar** ações de Defesa Civil e resposta a desastres em áreas de maior risco.
* **Alocar** recursos sociais de maneira eficiente e baseada em dados geográficos.
