import streamlit as st
import yfinance as yf

# כותרת ראשית
st.title("Stock Financial Metrics")

# שדה להזנת המניה
ticker = st.text_input("Enter a stock ticker (e.g., AAPL, MSFT)")

# פונקציה לשליפת נתונים
def get_stock_metrics(ticker):
    try:
        stock = yf.Ticker(ticker)
        st.write("Fetching data for:", ticker)  # דיבוג
        financials = stock.financials
        balance_sheet = stock.balance_sheet
        cash_flow = stock.cashflow

        # בדיקה אם הנתונים ריקים
        if financials.empty or balance_sheet.empty or cash_flow.empty:
            st.error("No data available for this ticker. It might not exist or lack financial data.")
            return None

        metrics = {
            "Revenue (TTM)": financials.loc['Total Revenue'][0],
            "Net Income (TTM)": financials.loc['Net Income'][0],
            "Free Cash Flow (TTM)": cash_flow.loc['Total Cash From Operating Activities'][0],
            "Shares Outstanding": balance_sheet.loc['Common Stock'][0],
            "Long-Term Liabilities": balance_sheet.loc['Long Term Liabilities'][0],
        }
        return metrics
    except Exception as e:
        st.error(f"Error retrieving data for {ticker}: {e}")
        return None