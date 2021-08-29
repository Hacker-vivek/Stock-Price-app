import yfinance as yf
import pandas as pd
import streamlit as st
import yfinance as yf
  

st.write (
    '''
 # Simple Stock Price App

 Shown are the stock ** closing price ** and *** volume *** of APPLE  
    
    '''
)

tickerSymbol ="AAPL"
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d',start='2011-05-31',end='2021-05-31')

st.write(
    '''
   ##Closing Price

    '''
)
st.line_chart(tickerDf.Close)
st.write(
    '''
   ##Volume Price

    '''
)
st.line_chart(tickerDf.Volume)


