# B3 Insights – Pipeline de Ciência de Dados com Ações da B3

O objetivo deste projeto é aplicar um **pipeline completo de Ciência de Dados** sobre dados reais de ações da B3, gerando análise exploratória, um modelo preditivo simples e um **dashboard interativo** para apoiar a leitura de risco, retorno e correlação entre ativos.

Trabalho desenvolvido na disciplina **Fundamentos de Ciência de Dados**.

Autores: **Matheus Rossi Carvalho** e **Jonathan Gonçalves Possa**

---

## Como funciona

1. O notebook em Google Colab coleta dados históricos de três ativos da B3 via `yfinance`.  
2. Os dados são limpos, preparados e enriquecidos com:
   - retornos diários  
   - volatilidade móvel de 21 dias  
   - retorno futuro de BOVA11  
   - variável alvo binária `target_up`  
3. É realizada uma **Análise Exploratória de Dados (EDA)** com estatísticas, distribuições, volatilidade e correlação entre os ativos.  
4. Um modelo de **classificação (Regressão Logística)** é treinado com `scikit-learn` para prever se o retorno futuro de BOVA11 será positivo.  
5. A base tratada é exportada para CSV e utilizada por um **dashboard Streamlit** (`app.py`).  
6. No dashboard, o usuário consegue filtrar ativos e períodos, visualizar métricas e explorar gráficos e tabela de dados de forma interativa.

---

## Funcionalidades

- Coleta automática de dados de ações da B3 via `yfinance`.  
- Pipeline organizado nas etapas 4.1 a 4.7 de Ciência de Dados (escolha do dataset, coleta, limpeza, EDA, modelagem, visualização e storytelling).  
- Criação de variáveis derivadas:
  - retornos diários por ativo  
  - volatilidade móvel (21 dias)  
  - retorno futuro de BOVA11  
  - alvo binário `target_up`  
- Análises de:
  - distribuição de retornos  
  - volatilidade ao longo do tempo  
  - correlação entre ativos  
- Modelo de **Regressão Logística** como baseline preditivo para o sinal do retorno futuro de BOVA11.  
- **Dashboard em Streamlit** com:
  - filtro de ativo (PETR4, VALE3, BOVA11)  
  - filtro de período por intervalo de datas  
  - métricas de retorno médio, volatilidade e retorno acumulado de BOVA11  
  - gráfico de preço ajustado ao longo do tempo  
  - histograma de retornos do ativo selecionado  
  - visão tabular com nomes de colunas amigáveis  

---

## Organização do Projeto

O projeto foi estruturado separando claramente:

- O **notebook** responsável pelo pipeline completo de Ciência de Dados.  
- O **dataset tratado** exportado para CSV.  
- O **dashboard Streamlit**, que consome o CSV e apresenta os resultados.  
- O **roteiro de slides** utilizado para apresentação e storytelling do trabalho.

---

## Estrutura de Pastas

```bash
.
├── CDIA_PF_Acoes_B3.ipynb                  # Notebook principal – pipeline completo (Colab)
├── dados_tratados_para_dashboard.csv       # Base final tratada para uso no dashboard
├── app.py                                  # Dashboard interativo em Streamlit
├── requeriments.txt                        # Dependências do projeto
└── README.md                               # Documentação do projeto
```

---

## Requisitos

### Para executar o notebook (pipeline completo)

- Python 3.10 ou superior (no ambiente local, se não usar apenas o Colab)  
- Google Colab ou Jupyter Notebook  
- Bibliotecas principais:
  - `pandas`  
  - `numpy`  
  - `yfinance`  
  - `matplotlib` / `seaborn` (para gráficos no notebook)  
  - `scikit-learn` (para a Regressão Logística)  

### Para executar o dashboard (app.py)

- Python 3.10 ou superior  
- Bibliotecas:
  - `pandas`  
  - `plotly`  
  - `streamlit`  

Exemplo de instalação mínima para o dashboard:

```bash
pip install streamlit pandas plotly
```

---

## Como executar

### 1. Executar o pipeline no Colab

1. Abrir o arquivo `CDIA_PF_Acoes_B3.ipynb` no Google Colab.  
2. Executar todas as células em ordem, garantindo:
   - coleta dos dados via `yfinance`  
   - limpeza e preparação da base  
   - EDA e modelagem  
   - geração do arquivo `dados_tratados_para_dashboard.csv`  
3. Fazer download do arquivo `dados_tratados_para_dashboard.csv` para a mesma pasta onde ficará o `app.py`.

### 2. Subir o dashboard localmente com Streamlit

Na pasta onde estão `app.py` e `dados_tratados_para_dashboard.csv`:

```bash
# (opcional) criar ambiente virtual
python -m venv .venv

# ativar venv no Windows (PowerShell)
.venv\Scriptsctivate

# instalar dependências
pip install streamlit pandas plotly

# executar o dashboard
streamlit run app.py
```

O Streamlit abrirá o dashboard em `http://localhost:8501`.

---

## Considerações

- O modelo de Regressão Logística foi utilizado como **baseline didático**, com foco em demonstrar o fluxo de modelagem, não em otimizar performance para uso real em investimentos.  
- O projeto pode ser expandido com:
  - mais ativos e classes de ativos  
  - indicadores técnicos adicionais  
  - variáveis macroeconômicas  
  - modelos mais complexos (árvores, ensembles, etc.)  
  - agendamento de atualização automática dos dados e do dashboard  

---

## Licença

MIT License

---

## Autores

- **Matheus Rossi Carvalho**  
  - LinkedIn: https://www.linkedin.com/in/matheus-rossi-carvalho  
  - GitHub: https://github.com/matheusssrc  

- **Jonathan Gonçalves Possa**
  - LinkedIn: https://www.linkedin.com/in/jonathan-possa/  
