import streamlit as st
import pandas as pd
st.write("Hello, Streamlit!")
data = pd.read_csv("cars24-car-price.csv")
st.dataframe(data)