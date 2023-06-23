import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

# Função para obter os dados da API do Covid-19
def obter_dados_covid():
    url = "https://disease.sh/v3/covid-19/countries"
    response = requests.get(url)
    data = response.json()
    return data

# Função para exibir os dados
def exibir_dados(data):
    # Converter os dados em um DataFrame do Pandas
    df = pd.DataFrame(data)

    # Ordenar por casos em ordem decrescente
    df = df.sort_values(by="cases", ascending=False)

    # Selecionar os 10 maiores países
    top_10 = df.head(10)

    # Exibir tabela com os dados dos 10 maiores países
    st.subheader("Top 10 países com mais casos:")
    st.dataframe(top_10)

    # Exibir gráfico de casos
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    ax1.bar(top_10["country"], top_10["cases"])
    ax1.set_title("Top 10 Países com Mais Casos")
    ax1.set_xlabel("País")
    ax1.set_ylabel("Total de Casos")
    plt.xticks(rotation=90)
    st.pyplot(fig1)

    # Exibir gráfico de óbitos
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    ax2.plot(top_10["country"], top_10["deaths"], marker="o")
    ax2.set_title("Top 10 Países com Mais Óbitos")
    ax2.set_xlabel("País")
    ax2.set_ylabel("Total de Óbitos")
    plt.xticks(rotation=90)
    st.pyplot(fig2)

# Obter os dados da API
data = obter_dados_covid()

# Exibir os dados
exibir_dados(data)
