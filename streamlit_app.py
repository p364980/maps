import streamlit as st
import pandas as pd


st.sidebar.write("Project name")

mass = st.sidebar.slider('Mass', 0, 100)

df = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')


st.write("hello world")

st.write(df.head())
df = df[df.mass < (mass * 10000)]
st.map(df)

