"""
analyzer.py — calculates financial metrics from raw statement data
"""
import pandas as pd
import numpy as np


def safe_get(df: pd.DataFrame, *keys) -> pd.Series:
    """Try multiple possible column names (yfinance isn't always consistent)."""
    for key in keys:
        if key in df.columns:
            return df[key]
    return pd.Series(dtype=float)


def compute_metrics(data: dict) -> dict:
    inc = data["income_stmt"]
    bal = data["balance_sheet"]
    cf = data["cash_flow"]
    info = data["info"]

    metrics = {}

    # ── Income Statement ──────────────────────────────────────────────────
    revenue = safe_get(inc, "Total Revenue")
    gross_profit = safe_get(inc, "Gross Profit")
    operating_income = safe_get(inc, "Operating Income", "EBIT")
    ebitda = safe_get(inc, "EBITDA", "Normalized EBITDA")
    net_income = safe_get(inc, "Net Income")
    interest_expense = safe_get(inc, "Interest Expense")

    metrics["revenue"] = revenue
    metrics["gross_profit"] = gross_profit
    metrics["operating_income"] = operating_income
    metrics["net_income"] = net_income

    # Margins
    if not revenue.empty and revenue.notna().any():
        metrics["gross_margin"] = (gross_profit / revenue * 100).round(2)
        metrics["operating_margin"] = (operating_income / revenue * 100).round(2)
        metrics["net_margin"] = (net_income / revenue * 100).round(2)
        if not ebitda.empty:
            metrics["ebitda_margin"] = (ebitda / revenue * 100).round(2)

    # Revenue YoY growth
    if not revenue.empty and len(revenue) > 1:
        metrics["revenue_growth"] = revenue.pct_change(-1) * 100  # oldest→newest

    # ── Balance Sheet ─────────────────────────────────────────────────────
    current_assets = safe_get(bal, "Current Assets")
    current_liabilities = safe_get(bal, "Current Liabilities")
    cash = safe_get(bal, "Cash And Cash Equivalents", "Cash")
    inventory = safe_get(bal, "Inventory")
    total_assets = safe_get(bal, "Total Assets")
    total_equity = safe_get(bal, "Stockholders Equity", "Total Stockholders Equity")
    total_debt = safe_get(bal, "Total Debt", "Long Term Debt")

    if not current_assets.empty and not current_liabilities.empty:
        metrics["current_ratio"] = (current_assets / current_liabilities).round(2)

    if not cash.empty and not inventory.empty and not current_liabilities.empty:
        metrics["quick_ratio"] = (
            (current_assets - inventory) / current_liabilities
        ).round(2)

    if not total_debt.empty and not total_equity.empty:
        metrics["debt_to_equity"] = (total_debt / total_equity).round(2)

    if not net_income.empty and not total_assets.empty:
        metrics["roa"] = (net_income / total_assets * 100).round(2)

    if not net_income.empty and not total_equity.empty:
        metrics["roe"] = (net_income / total_equity * 100).round(2)

    # ── Cash Flow ─────────────────────────────────────────────────────────
    operating_cf = safe_get(cf, "Operating Cash Flow", "Cash Flow From Continuing Operating Activities")
    capex = safe_get(cf, "Capital Expenditure")

    metrics["operating_cf"] = operating_cf

    if not operating_cf.empty and not capex.empty:
        fcf = operating_cf + capex  # capex is usually negative in yfinance
        metrics["fcf"] = fcf
        if not revenue.empty:
            metrics["fcf_margin"] = (fcf / revenue * 100).round(2)

    # ── Valuation (latest from info) ──────────────────────────────────────
    valuation = {}
    for label, key in [
        ("P/E (TTM)", "trailingPE"),
        ("P/E (Fwd)", "forwardPE"),
        ("EV/EBITDA", "enterpriseToEbitda"),
        ("P/S (TTM)", "priceToSalesTrailing12Months"),
        ("P/B", "priceToBook"),
        ("Market Cap ($B)", "marketCap"),
        ("52w High", "fiftyTwoWeekHigh"),
        ("52w Low", "fiftyTwoWeekLow"),
    ]:
        val = info.get(key)
        if val:
            if key == "marketCap":
                val = round(val / 1e9, 2)
            valuation[label] = val
    metrics["valuation"] = valuation

    return metrics
