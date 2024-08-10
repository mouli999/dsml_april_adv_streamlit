import pandas as pd
import streamlit as st
import datetime
import yfinance as yf


st.write(
    """
    # Stock price analyser 

      Shown are the stock prices of apple company
      
    """
)

ticker_symbol ="AAPL"

ticker_data=yf.Ticker(ticker_symbol)       # ticker data is object of Ticker class
ticker_df=ticker_data.history(period="1d", start="2019-01-01",end="2023-02-14")

st.write(f"""
        ### {ticker_symbol}' stock price info:"""
         
         )

st.dataframe(ticker_df.head(10))      # only 10 rows

## showcasing line charts
# st.write("""
#          ## Daily closing Price on a line chart:""")

# st.line_chart(ticker_df.close)

col1,col2=st.columns(2)
with col1:
    st.header("Daily Closing prices on a Line Chart:")
    st.line_chart(ticker_df.close)
with col2:
    st.header("Daily Volume on a Line Chart:")
    st.line_chart(ticker_df.Volume)
