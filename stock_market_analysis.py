import pandas as pd
import streamlit as st
import yfinance as yf

ticker_symbols = ["MSFT", "AAPL", "GOOGL", "AMZN", "TSLA"]
options1=st.selectbox("Select the column to visualize", ticker_symbols)
st.title(f"{options1} Stock Price Analysis")
ticker_symbol = options1

data=yf.Ticker(ticker_symbol)
ticker_df = data.history(period="3mo")
headers = ticker_df.columns.tolist()


st.dataframe(ticker_df)

options=st.selectbox("Select the column to visualize", headers)

st.write(f"Showing Chart For: {options}")
st.line_chart(ticker_df[options])