import yfinance as yf
yf.pdr_override() 
from pandas_datareader import data as pdr


def extended_info(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info

    # Extended Information
    result = { 
        "Market Cap": info.get("marketCap", "N/A"),
        "Revenue (TTM)": info.get("totalRevenue", "N/A"),
        "Net Income (TTM)": info.get("netIncomeToCommon", "N/A"),
        "5Yr Avg Net Income": "N/A",  # Placeholder (requires calculation)
        "P/E (TTM)": info.get("trailingPE", "N/A"),
        "5Yr P/E": "N/A",  # Placeholder (requires calculation)
        "PS Ratio": info.get("priceToSalesTrailing12Months", "N/A"),
        "Profit Margin (TTM)": info.get("profitMargins", "N/A"),
        "5Yr Profit Margin": "N/A",  # Placeholder (requires calculation)
        "Gross Profit Margin (TTM)": info.get("grossMargins", "N/A"),
        "3Yr Compound Revenue Growth": "N/A",  # Placeholder (requires calculation)
        "5Yr Compound Revenue Growth": "N/A",  # Placeholder (requires calculation)
        "10Yr Compound Revenue Growth": "N/A",  # Placeholder (requires calculation)
        "Free Cash Flow (TTM)": info.get("freeCashflow", "N/A"),
        "5Yr Avg FCF (TTM)": "N/A",  # Placeholder (requires calculation)
        "Price/FCF (TTM)": "N/A",  # Placeholder (requires calculation)
        "5Yr Avg Price/FCF": "N/A",  # Placeholder (requires calculation)
        "Dividend Yield (TTM)": info.get("dividendYield", "N/A"),
        "Dividends Paid": "N/A",  # Placeholder (requires calculation)
        "Forward Dividend Yield": "N/A",  # Placeholder (requires calculation)
        "Enterprise Value (Traditional)": info.get("enterpriseValue", "N/A"),
        "Return on Assets": info.get("returnOnAssets", "N/A"),
        "Return on Equity": info.get("returnOnEquity", "N/A"),
        "Return on Invested Capital (TTM)": "N/A",  # Placeholder (requires calculation)
        "5Yr Return on Invested Capital": "N/A",  # Placeholder (requires calculation)
        "5Yr Compound Book Value Growth": "N/A",  # Placeholder (requires calculation)
        "10Yr Compound Book Value Growth": "N/A",  # Placeholder (requires calculation)
        "52 WK High": info.get("fiftyTwoWeekHigh", "N/A"),
        "52 WK Low": info.get("fiftyTwoWeekLow", "N/A"),
        "ATH": "N/A",  # Placeholder (requires calculation)
        "25 Day MA": "N/A",  # Placeholder (requires calculation)
        "50 Day MA": info.get("fiftyDayAverage", "N/A"),
        "100 Day MA": "N/A",  # Placeholder (requires calculation)
        "200 Day MA": info.get("twoHundredDayAverage", "N/A"),
        "Free Cash (TTM)":info.get("freeCashFlow(TTM)","N/A")
    }
    return result

def display_extended_info(ticker_symbol):
    data = extended_info(ticker_symbol)
    print("\n=== Extended Information ===")
    print("=" * 50)
    for key, value in data.items():
        if isinstance(value, (int, float)):
            print(f"{key}: {value:,.2f}")
        else:
            print(f"{key}: {value}")
    print("=" * 50)

# Example usage
if __name__ == "__main__":
    ticker_symbol = input("Enter a stock ticker (e.g., AAPL): ").upper()
    display_extended_info(ticker_symbol)
