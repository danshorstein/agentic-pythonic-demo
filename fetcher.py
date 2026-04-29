"""
fetcher.py — pulls financial statement data from yfinance
"""
import yfinance as yf
import pandas as pd


def get_company_data(ticker: str) -> dict:
    """Fetch all financial data for a given ticker symbol."""
    t = yf.Ticker(ticker)
    info = t.info

    # Financial statements (annual, last 4 years)
    income_stmt = t.financials          # income statement
    balance_sheet = t.balance_sheet
    cash_flow = t.cashflow

    # Transpose so years are rows, metrics are columns
    def clean(df: pd.DataFrame) -> pd.DataFrame:
        if df is None or df.empty:
            return pd.DataFrame()
        df = df.T.copy()
        df.index = pd.to_datetime(df.index).year
        df.index.name = "Year"
        return df

    return {
        "info": info,
        "income_stmt": clean(income_stmt),
        "balance_sheet": clean(balance_sheet),
        "cash_flow": clean(cash_flow),
    }
