import streamlit as st
import pandas as pd

st.title("Painel de Atendimento Médico")

# Upload do CSV
uploaded_file = st.file_uploader("atendimentos.csv", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep=';', encoding='latin-1')
    df.columns = df.columns.str.strip()

    st.write("Dados carregados com sucesso!")
    st.dataframe(df.head())
else:
    st.warning("Faça upload do arquivo CSV para visualizar os dados.")
