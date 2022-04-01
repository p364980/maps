import streamlit as st
import pandas as pd


st.sidebar.write("Project name")
df = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')


st.write("hello world")

st.write(df.head())

st.map(df)

mass = st.sidebar.slider('Mass', 0, 90000000, 500000)
