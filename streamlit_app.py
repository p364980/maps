import streamlit as st
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')
print(len(data))

st.sidebar.write("Project name")
st.sidebar.button('Click')

st.write("hello world")
