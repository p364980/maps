import streamlit as st
import pandas as pd

data = pd.read_csv('./data.csv')
print(data)

st.sidebar.write("Project name")
st.sidebar.button('Click')

st.write("hello world")
