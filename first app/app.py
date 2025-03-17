
import streamlit as st
import pandas as pd
st.title("MY FIRST APP")
st.write("welcome to my first app. Here, you will be able to access filtered information on the penguins.csv dataset, through their species and island!")
data = pd.read_csv("/Users/lissachaves/Documents/GitHub/TELLES_Python_portfolio/data/penguins.csv")
species = st.sidebar.selectbox('Select species', data['species'].unique())
island = st.sidebar.selectbox('Select island', data['island'].unique())
filtered_data = data[(data['species'] == species) & (data['island'] == island)]
st.write(filtered_data)
