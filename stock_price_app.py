from tracemalloc import start
from turtle import title
import yfinance as yf
import streamlit as st
import pandas as pd


#title
st.write("""
# Stock Price App

Shown are the **stock closing** price, **volume**, **cash flow** and **earnings**.

""")


#define the ticker symbol
tickers_list = ['AAPL', 'GOOGL', 'AMZN', 'TSLA', 'BAC', 'BA'] 

# Set ticker 
chosen_ticker = st.selectbox("Please choose ticker symbol", options = tickers_list)

#get data on this ticker
tickerData = yf.Ticker(chosen_ticker)

#the time and period options
period_list = ['1d', '5d', '1mo', '6mo', '1y', '2y', '5y', '10y', 'max']

# Set period 
chosen_period = 'max'
chosen_period = st.selectbox("Please choose period", options = period_list)

#get the historical prices for this ticker
tickerDf = tickerData.history(period= chosen_period)

#show plot for Closing Price and Volume Price
st.write("""
## Closing Price 
""" + chosen_ticker) 
st.line_chart(tickerDf.Close)

st.write("""
## Volume Price
""" + chosen_ticker)
st.line_chart(tickerDf.Volume)

st.write("""
## Cash Flow
""" + chosen_ticker)
tickerData.cashflow

st.write("""
## Earnings
""" + chosen_ticker)
tickerData.earnings