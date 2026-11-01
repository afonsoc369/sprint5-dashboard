import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Vehicle Insights", page_icon="🚗", layout="wide")

DATA_PATH = Path(__file__).parent / "vehicles_us.csv"

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_PATH)
    for column in ["price", "odometer", "model_year"]:
        if column in data.columns:
            data[column] = pd.to_numeric(data[column], errors="coerce")
    return data

st.title("🚗 Vehicle Insights")
st.markdown("Explore anúncios de veículos usados através de gráficos interativos.")
st.caption("Projeto Sprint 5 • Streamlit + Plotly")

try:
    vehicles = load_data()
except FileNotFoundError:
    st.error("Ficheiro vehicles_us.csv não encontrado. Coloque o CSV na pasta principal do projeto.")
    st.stop()

# Filtros
with st.sidebar:
    st.header("Filtros")
    if "type" in vehicles.columns:
        types = sorted(vehicles["type"].dropna().astype(str).unique())
        selected_types = st.multiselect("Tipo de veículo", types, default=types)
        if selected_types:
            vehicles = vehicles[vehicles["type"].astype(str).isin(selected_types)]
    if "condition" in vehicles.columns:
        conditions = sorted(vehicles["condition"].dropna().astype(str).unique())
        selected_conditions = st.multiselect("Condição", conditions, default=conditions)
        if selected_conditions:
            vehicles = vehicles[vehicles["condition"].astype(str).isin(selected_conditions)]

if vehicles.empty:
    st.warning("Não existem anúncios para os filtros selecionados.")
    st.stop()

# Indicadores
c1, c2, c3 = st.columns(3)
c1.metric("Anúncios", f"{len(vehicles):,}".replace(",", " "))
if "price" in vehicles.columns:
    c2.metric("Preço mediano", f"${vehicles['price'].median():,.0f}")
if "odometer" in vehicles.columns:
    c3.metric("Quilometragem mediana", f"{vehicles['odometer'].median():,.0f} km")

st.divider()
st.header("Exploração visual")

left, right = st.columns(2)
with left:
    st.subheader("Distribuição dos preços")
    price_col = "price" if "price" in vehicles.columns else None
    if price_col:
        bins = st.slider("Número de intervalos do histograma", 10, 80, 35)
        if st.button("Criar histograma", use_container_width=True):
            fig = px.histogram(vehicles, x="price", nbins=bins, title="Distribuição dos preços",
                               labels={"price": "Preço (USD)", "count": "Número de anúncios"})
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Clique no botão para gerar o histograma.")
    else:
        st.warning("A coluna 'price' não existe no CSV.")

with right:
    st.subheader("Preço vs. quilometragem")
    if {"price", "odometer"}.issubset(vehicles.columns):
        color_col = "type" if "type" in vehicles.columns else None
        if st.button("Criar gráfico de dispersão", use_container_width=True):
            fig = px.scatter(vehicles, x="odometer", y="price", color=color_col,
                             hover_data=[c for c in ["model", "model_year", "condition"] if c in vehicles.columns],
                             title="Preço em função da quilometragem",
                             labels={"odometer": "Quilometragem", "price": "Preço (USD)"})
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Clique no botão para gerar o gráfico de dispersão.")
    else:
        st.warning("O CSV precisa das colunas 'price' e 'odometer'.")

st.divider()
st.header("Pré-visualização dos dados")
st.dataframe(vehicles.head(100), use_container_width=True)
st.caption("A tabela apresenta no máximo 100 linhas para facilitar a navegação.")
