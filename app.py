import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson
import numpy as np

st.set_page_config(page_title="Painel de Atendimento Médico", layout="wide")

# Upload do CSV pelo usuário
uploaded_file = st.file_uploader("atendimentos.csv", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep=';', encoding='latin-1')
    df.columns = df.columns.str.strip()

    st.title("Painel de Atendimento Médico")

    # Resumo
    media_idade = df["Idade"].mean()
    total_atestados = df[df["Atestado"] == 1].shape[0]
    total_respiratorio = df[df["SindRespiratoria"] == 1].shape[0]

    st.markdown("### Resumo dos Atendimentos")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Média de Idade", f"{media_idade:.1f} anos")
    with col2:
        st.metric("Atestados Emitidos", total_atestados)
    with col3:
        st.metric("Casos Respiratórios", total_respiratorio)

    st.divider()
    
    # Aqui você coloca o restante do seu código (gráficos, análises etc.)
    st.markdown("### Exportar Dados")
    csv = df.to_csv(index=False, sep=';', encoding='utf-8-sig').encode('utf-8-sig')
    st.download_button(
        label="Baixar CSV",
        data=csv,
        file_name='atendimentos.csv',
        mime='text/csv',
    )
else:
    st.warning("Faça upload do arquivo CSV para visualizar os dados e gráficos.")
