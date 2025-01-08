import streamlit as st
import yfinance as yf

# כותרת ראשית
st.title("Stock Financial Metrics")

# שדה להזנת המניה
ticker = st.text_input("Enter a stock ticker (e.g., AAPL, MSFT)")

# פונקציה לשליפת נתונים
def get_stock_metrics(ticker):
    stock = yf.Ticker(ticker)
    financials = stock.financials
    balance_sheet = stock.balance_sheet
    cash_flow = stock.cashflow

    metrics = {
        "Revenue (TTM)": financials.loc['Total Revenue'][0],
        "Net Income (TTM)": financials.loc['Net Income'][0],
        "Free Cash Flow (TTM)": cash_flow.loc['Total Cash From Operating Activities'][0],
        "Shares Outstanding": balance_sheet.loc['Common Stock'][0],
        "Long-Term Liabilities": balance_sheet.loc['Long Term Liabilities'][0],
    }
    return metrics

# הצגת תוצאות
if ticker:
    try:
        metrics = get_stock_metrics(ticker.upper())
        st.write(f"### Financial Metrics for {ticker}")
        for key, value in metrics.items():
            st.write(f"{key}: {value:,}")
    except Exception as e:
        st.error("Could not retrieve data. Please check the ticker and try again.")