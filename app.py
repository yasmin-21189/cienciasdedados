import streamlit as st
import pandas as pd

st.title("Painel de Atendimento Médico")

# Upload do CSV
uploaded_file = st.file_uploader("atendimento.csv", type="csv")

if uploaded_file is not None:
    # Lê o CSV
    df = pd.read_csv(uploaded_file, sep=';', encoding='latin-1')
    df.columns = df.columns.str.strip()  # remove espaços extras nos nomes das colunas
    
    st.success("CSV carregado com sucesso!")
    
    # Mostrar os dados
    st.dataframe(df.head())  # mostra as primeiras linhas
else:
    st.warning("Faça upload do arquivo CSV para visualizar os dados.")
