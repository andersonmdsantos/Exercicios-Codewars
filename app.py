import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

try:
    df = pd.read_csv("pizzas.csv")
except Exception as e:
    st.error(f"Erro ao carregar o arquivo CSV: {e}")
    st.stop()

modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)

st.title("Prevendo o valor de uma pizza")
st.divider()

diametro = st.number_input("Digite o tamanho do diametro da pizza: ")

if diametro > 0:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"O valor da pizza com diâmentro de {diametro:.2f} centímetros é de R$ {preco_previsto:.2f}.")
    st.balloons()
else:
    st.warning("Por favor, insira um diâmetro maior que zero.")