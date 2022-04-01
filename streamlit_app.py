import streamlit as st
import pandas as pd

data = pd.read_csv('data.csv')
data.head()

st.sidebar.write("Project name")
st.write("hello world")
