import streamlit as st
import pandas as pd


st.sidebar.write("Project name")
df = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')
st.write(df.head())

st.map(df)

st.sidebar.button('Click')

st.write("hello world")
