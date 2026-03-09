# 🏦 Pipeline ETL - Processamento de Dados Bancários

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## 📖 Sobre o Projeto
Este projeto foi desenvolvido como parte do **Bootcamp DIO + TOTVS**. Trata-se de um pipeline de dados (ETL) construído em Python, focado em processar dados bancários fictícios. 

O objetivo principal é demonstrar a capacidade de extrair informações de arquivos brutos, aplicar regras de negócio por meio de transformações de dados e carregá-los em um banco de dados relacional para análises futuras. A arquitetura foi pensada de forma modular, separando responsabilidades para facilitar a manutenção e escalabilidade.

## ⚙️ Arquitetura do Pipeline
O pipeline segue a estrutura clássica de ETL:
* **Extract (Extração):** Leitura dos dados brutos a partir de um arquivo `.csv` localizado no diretório `data/raw/`.
* **Transform (Transformação):** Limpeza, formatação e aplicação de regras de negócio utilizando a biblioteca `pandas` (ex: cálculos de saldo, padronização de strings e tratamento de nulos).
* **Load (Carregamento):** Inserção dos dados processados em um banco de dados relacional **SQLite** (`bank.db`), deixando-os prontos para consumo por ferramentas de BI ou outras aplicações.

## 📂 Estrutura do Repositório
```text
📦 pipeline-etl-dio
 ┣ 📂 data
 ┃ ┗ 📂 raw
 ┃   ┗ 📜 dados_bancarios.csv        # Dados brutos de entrada
 ┣ 📂 database
 ┃ ┗ 📜 create_tables.sql            # Scripts de definição de banco (DDL)
 ┣ 📂 notebooks
 ┃ ┗ 📜 exploracao_dados.ipynb       # Análise exploratória inicial (Jupyter)
 ┣ 📂 src
 ┃ ┗ 📂 etl
 ┃   ┣ 📜 __init__.py
 ┃   ┣ 📜 extract.py                 # Módulo de extração
 ┃   ┣ 📜 transform.py               # Módulo de transformação
 ┃   ┣ 📜 load.py                    # Módulo de carregamento
 ┃   ┗ 📜 pipeline.py                # Script principal de orquestração
 ┣ 📂 tests                          # Diretório reservado para testes unitários
 ┣ 📜 bank.db                        # Banco de dados SQLite gerado
 ┣ 📜 requirements.txt               # Dependências do projeto
 ┗ 📜 README.md

## 🚀 Como Executar o Projeto

**1. Clone o repositório:**

```bash
git clone [https://github.com/karlarenatadev/pipeline-etl-dio.git](https://github.com/karlarenatadev/pipeline-etl-dio.git)
cd pipeline-etl-dio
```
**2. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**3. Execute o Pipeline:**
```bash
python src/etl/pipeline.py
```

**Saída esperada no terminal:**
```Plaintext
Extraindo dados do arquivo...
100 registros carregados
Transformando dados...
Transformação concluída
Carregando dados no banco...
Dados carregados com sucesso
Pipeline executado com sucesso
```
