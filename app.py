import yfinance as yf

# פונקציה לשליפת נתונים
def get_stock_metrics(ticker):
    try:
        stock = yf.Ticker(ticker)
        financials = stock.financials
        balance_sheet = stock.balance_sheet
        cash_flow = stock.cashflow

        # בדיקת זמינות נתונים ושימוש ב-iloc
        metrics = {
            "Revenue (TTM)": financials.loc['Total Revenue'].iloc[0] if 'Total Revenue' in financials.index else "N/A",
            "Net Income (TTM)": financials.loc['Net Income'].iloc[0] if 'Net Income' in financials.index else "N/A",
            "Free Cash Flow (TTM)": cash_flow.loc['Total Cash From Operating Activities'].iloc[0] if 'Total Cash From Operating Activities' in cash_flow.index else "N/A",
            "Shares Outstanding": balance_sheet.loc['Common Stock'].iloc[0] if 'Common Stock' in balance_sheet.index else "N/A",
            "Long-Term Liabilities": balance_sheet.loc['Long Term Liabilities'].iloc[0] if 'Long Term Liabilities' in balance_sheet.index else "N/A",
        }
        return metrics
    except Exception as e:
        print(f"Error: {e}")
        return None

# הרצה רגילה בטרמינל

if __name__ == "__main__":
    # קבלת קלט מהמשתמש
    ticker_symbol = input("Enter a stock ticker (e.g., AAPL): ").upper()

    # יצירת אובייקט Ticker
    ticker = yf.Ticker(ticker_symbol)

    # בדיקת זמינות מידע
    info = ticker.info
    if not info:
        print("No data available for this ticker. Please try another one.")
    else:
        # סיכום מידע כללי
        print(f"Company: {info.get('longName', 'N/A')}")
        print(f"Sector: {info.get('sector', 'N/A')}")
        print(f"Industry: {info.get('industry', 'N/A')}")
        print(f"Market Cap: {info.get('marketCap', 'N/A')}")
        print(f"Current Price: {info.get('currentPrice', 'N/A')}")
        print(f"Dividend Yield: {info.get('dividendYield', 'N/A')}")

        # דוחות פיננסיים
        financials = ticker.financials
        if not financials.empty:
            print("\nFinancials (last reported year):")
            print(financials)
        else:
            print("\nNo financial data available.")

        # תמחור שוק
        print("\nMarket Metrics:")
        print(f"Trailing PE: {info.get('trailingPE', 'N/A')}")
        print(f"Forward PE: {info.get('forwardPE', 'N/A')}")
        print(f"Price to Sales: {info.get('priceToSalesTrailing12Months', 'N/A')}")




"""    result = get_stock_metrics(ticker)
    if result:
        print("\nFinancial Metrics:")
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
       print("Could not retrieve data. Please try another ticker.")
"""
