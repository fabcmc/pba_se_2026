# 🇬🇧 Data Analysis for the "Alfabetiza Sergipe" 2026 Program (Programa Brasil Alfabetizado in the State of Sergipe) — SEED & FGV DGPE

This repository centralizes the data analysis codes and workflows developed by me and validated by the **Fundação Getulio Vargas (FGV DGPE)** team responsible for implementing the PBA SE 2026. This project is being carried out in compliance with the contractual milestones established with the **State Secretariat of Education of Sergipe (SEED)** for the pedagogical and statistical monitoring of the literacy program's classes (PBA 2026).

The primary objective of this analysis suite is to process the educational data generated during the program's execution to produce the official technical reports designated in the contract between FGV DGPE and the State Secretariat of Education of Sergipe (SEED).

---

## 🔒 Data Governance and Compliance (LGPD)

In strict compliance with the Brazilian **General Data Protection Law (LGPD - Law No. 13,709/2018)** and institutional compliance guidelines, **no Personally Identifiable Information (PII)** is exposed in this public repository.

* All textual data (Names of students, literacy teachers, and coordinators) and numerical records (CPFs and Phone Numbers) have been replaced with fictitious equivalents generated deterministically using the `Faker` library.
* Referential integrity and data crossovers between different notebooks have been fully preserved through a local persistent mapping architecture.
* Macro-level spatial data (**Neighborhoods** and **Full Addresses**) have also been replaced with fictitious equivalents generated deterministically via `Faker`.
* The anonymization pipeline utilized in this project is documented in the `protect_sensitive_data.ipynb` file.

---

## 📐 Analysis File Structure (.ipynb)

The analysis notebooks are systematically organized using a specific prefix that identifies the group of classes evaluated, followed by the type of assessment activity in the pedagogical cycle.

### 🧩 Understanding the Prefix Nomenclature

1.  **`SE_2026.1` (Regular Classes):** Reports concerning the main group of classes in Sergipe that started their activities on the first semester of 2026, according to the regularly planned schedule.

### 📑 Mapping Notebooks by Pedagogical Evaluation Cycle

| Jupyter Notebook File | Group Scope | Pedagogical Evaluation Cycle |
| :--- | :--- | :--- |
| `mapa_ambientes_aula_pba_se.py` | Dashboard | Map of schools and other places which could handle the classes in each town - on placed Render |
| `mapas_pba_2026.ipynb` | Dashboard | Map of coordinators per town: used to help manage coordinators while implementing the PBA groups |
| `analise_f1_alfabetizandos_n1_e_n2.ipynb` | Regular Classes | First Socioemotional Report and Formativa 1 Assessment Analysis to understand causes of bad results |
| `analise_desistentes.ipynb` | Regular Classes | Diagnostic Evaluation (Baseline/Entry) to understand students' evasion data behaviour |
| `SE_2026.1_Atividade_Entrada.ipynb` | Regular Classes | Diagnostic Evaluation (Baseline/Entry) |
| `SE_2026.1_Formativa_1.ipynb` | Regular Classes | First Socioemotional Report and Formativa 1 Assessment Analysis |

### 🛠️ Auxiliary and Infrastructure Files
* `PBA SE.code-workspace`: VS Code workspace configuration file.
* `protect_sensitive_data.ipynb`: Script responsible for masking, PII sanitization, and the controlled generation of stable encryption/anonymization dictionaries.

---

## 💻 Tech Stack and Execution

The analyses were entirely developed using the **Python** programming language and its scientific data analysis ecosystem:

* **Data Manipulation and Cleaning:** `pandas`, `numpy`
* **Dashboard visualization:** `plotly`, `dash`, `Render`
* **Anonymization and Synthetic Sampling:** `faker`
* **Data Structure I/O:** `openpyxl`, `xlrd`

### 📂 Reproducibility and Data Download

Due to storage guidelines and **GitHub file size limit policies** for large datasets, the original and processed source files (`.xlsx`, `.csv`, among others) have been omitted from this repository's main file tree.

To reproduce all analyses, metrics, and charts present in the notebooks, the complete dataset package containing the public tables (fully anonymized with fictitious data) must be downloaded externally:

👉 **[Click here to download the anonymized data files](https://1drv.ms/f/c/835153c0338453fe/IgATek26k9XxQKkWwnW19oaZAR5A0vMburMirPT5rMdVszg?e=fq907K)**

> 📥 **Storage Instructions:** After downloading, extract and place the files directly inside the local folder structure at `Data_files/public_data/` before launching Jupyter Notebook.

### 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/fabcmc/pba_SE_2026.git
    ```
2. Install the required dependencies:
   ```bash
   pip install pandas numpy faker openpyxl jupyter
   ```
3. Ensure that you have placed the data downloaded in the previous step inside `Data_files/public_data/`.
4. Start the Jupyter server to browse the reports:
   ```bash
   jupyter notebook
   ```

> *Note: This repository reflects the technical commitment to methodological excellence, analytical rigor, and respect for data privacy guidelines in public administration, combining my own execution of the analyses with the specialized validation of the FGV DGPE team.*

---

# 🇧🇷 Análise de Dados para o Programa "Alfabetiza Sergipe" 2026 (Programa Brasil Alfabetizado no Estado de Sergipe) — SEED & FGV DGPE

Este repositório centraliza os códigos e fluxos de trabalho de análise de dados desenvolvidos por mim e validados pela equipe da **Fundação Getulio Vargas (FGV DGPE)** responsável pela implementação do PBA SE 2026. Este projeto está sendo realizado em cumprimento às metas contratuais estabelecidas com a **Secretaria de Estado da Educação de Sergipe (SEED)** para o monitoramento pedagógico e estatístico das turmas do programa de alfabetização (PBA 2026).

O objetivo principal desta suíte de análises é processar os dados educacionais gerados durante a execução do programa para produzir os relatórios técnicos oficiais designados no contrato entre a FGV DGPE e a Secretaria de Estado da Educação de Sergipe (SEED).

---

## 🔒 Governança de Dados e Conformidade (LGPD)

Em estrita conformidade com a **Lei Geral de Proteção de Dados (LGPD - Lei nº 13.709/2018)** e com as diretrizes de compliance institucional, **nenhuma Informação Pessoal Identificável (PII)** está exposta neste repositório público.

* Todos os dados textuais (nomes de alunos, alfabetizadores e coordenadores) e registros numéricos (CPFs e números de telefone) foram substituídos por equivalentes fictícios gerados deterministicamente utilizando a biblioteca `Faker`.
* A integridade referencial e os cruzamentos de dados entre diferentes notebooks foram totalmente preservados por meio de uma arquitetura de mapeamento persistente local.
* Dados espaciais em nível macro (**bairros** e **endereços completos**) também foram substituídos por equivalentes fictícios gerados deterministicamente via `Faker`.
* O pipeline de anonimização utilizado neste projeto está documentado no arquivo `protect_sensitive_data.ipynb`.

---

## 📐 Estrutura dos Arquivos de Análise (.ipynb)

Os notebooks de análise estão organizados sistematicamente utilizando um prefixo específico que identifica o grupo de turmas avaliadas, seguido pelo tipo de atividade de avaliação no ciclo pedagógico.

### 🧩 Entendendo a Nomenclatura dos Prefixos

1. **`SE_2026.1` (Turmas Regulares):** Relatórios relativos ao grupo principal de turmas em Sergipe que iniciaram suas atividades no primeiro semestre de 2026, de acordo com o cronograma planejado regularmente.

### 📑 Mapeamento de Notebooks por Ciclo de Avaliação Pedagógica

| Arquivo Jupyter Notebook | Escopo do Grupo | Ciclo de Avaliação Pedagógica |
| :--- | :--- | :--- |
| `mapa_ambientes_aula_pba_se.py` | Dashboard | Mapa de escolas e outros locais que poderiam abrigar as turmas em cada município - hospedado no Render |
| `mapas_pba_2026.ipynb` | Dashboard | Mapa de coordenadores por município: usado para ajudar a gerenciar os coordenadores durante a implementação dos grupos do PBA |
| `analise_f1_alfabetizandos_n1_e_n2.ipynb` | Turmas Regulares | Análise de Relatório Socioemocional de Entrada e Formativa 1 para entender os motivos de resultados ruins |
| `analise_desistentes.ipynb` | Turmas Regulares | Avaliação Diagnóstica (Linha de Base/Entrada) para entender o comportamento dos dados de evasão dos alunos |
| `SE_2026.1_Atividade_Entrada.ipynb` | Turmas Regulares | Avaliação Diagnóstica (Linha de Base/Entrada) |
| `SE_2026.1_Formativa_1.ipynb` | Turmas Regulares | Análise de Relatório Socioemocional de Entrada e Formativa 1 |

### 🛠️ Arquivos Auxiliares e de Infraestrutura
* `PBA SE.code-workspace`: Arquivo de configuração do espaço de trabalho (workspace) do VS Code.
* `protect_sensitive_data.ipynb`: Script responsável pelo mascaramento, sanitização de PII e geração controlada de dicionários estáveis de criptografia/anonimização.

---

## 💻 Tecnologias e Execução

As análises foram totalmente desenvolvidas utilizando a linguagem de programação **Python** e seu ecossistema de análise de dados científicos:

* **Manipulação e Limpeza de Dados:** `pandas`, `numpy`
* **Visualização em Dashboard:** `plotly`, `dash`, `Render`
* **Anonimização e Amostragem Sintética:** `faker`
* **E/S de Estrutura de Dados (I/O):** `openpyxl`, `xlrd`

### 📂 Reprodutibilidade e Download de Dados

Devido às diretrizes de armazenamento e às **políticas de limite de tamanho de arquivo do GitHub** para grandes conjuntos de dados, os arquivos de origem originais e processados (`.xlsx`, `.csv`, entre outros) foram omitidos da árvore de arquivos principal deste repositório.

Para reproduzir todas as análises, métricas e gráficos presentes nos notebooks, o pacote completo de dados contendo as tabelas públicas (totalmente anonimizadas com dados fictícios) deve ser baixado externamente:

👉 **[Clique aqui para baixar os arquivos de dados anonimizados](https://1drv.ms/f/c/835153c0338453fe/IgATek26k9XxQKkWwnW19oaZAR5A0vMburMirPT5rMdVszg?e=fq907K)**

> 📥 **Instruções de Armazenamento:** Após o download, extraia e coloque os arquivos diretamente dentro da estrutura de pastas locais em `Data_files/public_data/` antes de iniciar o Jupyter Notebook.

### 🚀 Como Executar Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/fabcmc/pba_SE_2026.git
   ```
2. Instale as dependências requeridas:
   ```bash
   pip install pandas numpy faker openpyxl jupyter
   ```
3. Certifique-se de que inseriu os dados baixados no passo anterior em `Data_files/public_data/`.
4. Inicie o servidor do Jupyter para navegar pelos relatórios:
   ```bash
   jupyter notebook
   ```

> *Nota: Este repositório reflete o compromisso técnico com a excelência metodológica, rigor analítico e respeito às diretrizes de privacidade de dados na administração pública, combinando a execução própria das análises com a validação especializada da equipe da FGV DGPE.*