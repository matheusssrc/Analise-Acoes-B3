import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Dashboard - Ações da B3", layout="wide")

st.title("Dashboard - Pipeline de Ciência de Dados com Ações da B3")

st.markdown(
    """
    Este dashboard complementa o projeto final de Ciência de Dados,
    utilizando a base tratada gerada no notebook do pipeline completo.
    """
)

@st.cache_data
def carregar_dados(caminho: str):
    df = pd.read_csv(caminho)
    if "data" in df.columns:
        df["data"] = pd.to_datetime(df["data"])
    return df

# Carregamento da base tratada
df = carregar_dados("dados_tratados_para_dashboard.csv")

# -------------------------------
# Sidebar - Filtros
# -------------------------------
st.sidebar.header("Filtros")

# Ativos = colunas que terminam com ".SA"
ativos_disponiveis = [c for c in df.columns if c.endswith(".SA")]
ativo_selecionado = st.sidebar.selectbox("Selecione o ativo", ativos_disponiveis)

# Período: filtro de datas
if "data" in df.columns:
    data_min = df["data"].min()
    data_max = df["data"].max()
    intervalo_datas = st.sidebar.date_input(
        "Período de análise",
        [data_min, data_max]
    )
    if len(intervalo_datas) == 2:
        inicio, fim = intervalo_datas
        df = df[(df["data"] >= pd.to_datetime(inicio)) & (df["data"] <= pd.to_datetime(fim))]

st.sidebar.markdown("---")
st.sidebar.markdown("**Métricas de retorno (BOVA11)**")

st.sidebar.markdown("---")
st.sidebar.markdown("**Métricas de retorno (BOVA11)**")

if "BOVA11.SA_ret" in df.columns:
    # garante que a serie é numerica
    serie_ret = pd.to_numeric(df["BOVA11.SA_ret"], errors="coerce")

    ret_medio = float(serie_ret.mean())
    ret_std = float(serie_ret.std())

    # usa numpy para calcular o produto acumulado e faz cast explicito para float
    arr = serie_ret.to_numpy(dtype="float64")
    ret_acum = float(np.prod(arr + 1.0) - 1.0)

    st.sidebar.metric("Retorno médio diário", f"{ret_medio:.4%}")
    st.sidebar.metric("Volatilidade diária", f"{ret_std:.4%}")
    st.sidebar.metric("Retorno acumulado", f"{ret_acum:.2%}")
else:
    st.sidebar.info("Coluna de retorno de BOVA11 não encontrada.")

# -------------------------------
# Layout principal - Gráficos
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"Preço ajustado - {ativo_selecionado}")
    fig_preco = px.line(df, x="data", y=ativo_selecionado)
    fig_preco.update_layout(xaxis_title="Data", yaxis_title="Preço ajustado")
    st.plotly_chart(fig_preco, use_container_width=True)

with col2:
    st.subheader(f"Distribuição de retornos - {ativo_selecionado}")
    ret_col = ativo_selecionado + "_ret"
    if ret_col in df.columns:
        fig_ret = px.histogram(df, x=ret_col, nbins=50)
        fig_ret.update_layout(xaxis_title="Retorno diário", yaxis_title="Frequência")
        st.plotly_chart(fig_ret, use_container_width=True)
    else:
        st.info("Não há coluna de retorno para este ativo.")

# -------------------------------
# Visão tabular (com nomes e ordem customizados)
# -------------------------------
st.markdown("---")
st.subheader("Visão tabular (amostra)")

# Mapeamento de nomes técnicos -> nomes amigáveis
mapa_colunas = {
    "data": "Data",
    "BOVA11.SA": "Preço BOVA11",
    "PETR4.SA": "Preço PETR4",
    "VALE3.SA": "Preço VALE3",
    "BOVA11.SA_ret": "Retorno BOVA11",
    "PETR4.SA_ret": "Retorno PETR4",
    "VALE3.SA_ret": "Retorno VALE3",
    "ret_bova_futuro": "Retorno futuro BOVA11",
    "target_up": "Retorno futuro positivo (1 = Sim)",
    "PETR4.SA_ret_vol_21d": "Vol 21d PETR4",
    "VALE3.SA_ret_vol_21d": "Vol 21d VALE3",
    "BOVA11.SA_ret_vol_21d": "Vol 21d BOVA11",
}

# Ordem das colunas na visão tabular
colunas_tabela = [
    "data",
    "BOVA11.SA",
    "PETR4.SA",
    "VALE3.SA",
    "BOVA11.SA_ret",
    "PETR4.SA_ret",
    "VALE3.SA_ret",
    "ret_bova_futuro",
    "target_up",
    "PETR4.SA_ret_vol_21d",
    "VALE3.SA_ret_vol_21d",
    "BOVA11.SA_ret_vol_21d",
]

# Garante que só usamos colunas que realmente existem no df
colunas_presentes = [c for c in colunas_tabela if c in df.columns]

df_tab = df[colunas_presentes].rename(columns=mapa_colunas)

st.dataframe(df_tab.head(100))