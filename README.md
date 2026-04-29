# FinSight — Financial Statement Analyzer

> **Part of the Agentic Coding Demo Series** — built across Antigravity, Claude Code, and Codex.

A Python app that pulls live financial statements from Yahoo Finance and delivers beautiful, interactive metric analysis via a Streamlit dashboard.

## Features

- 📥 **Live data** — income statement, balance sheet, and cash flows via `yfinance`
- 📊 **Rich visualizations** — interactive Plotly charts (dark mode)
- 💡 **Key metrics** — margins, growth rates, liquidity, leverage, returns, valuation multiples
- ⚡ **Fast** — 1-hour response caching so repeated lookups are instant

## Tabs

| Tab | What you get |
|-----|-------------|
| 💰 Income | Revenue & profit bars, raw statement table |
| 📈 Margins & Growth | Margin trends, YoY revenue growth |
| 💸 Cash Flow | Operating CF vs FCF, FCF margin |
| 🏦 Balance Sheet | Current/quick ratio, D/E, ROE, ROA |
| 🏷️ Valuation | P/E, EV/EBITDA, P/S, P/B multiples |

## Quickstart

```bash
pip3 install -r requirements.txt
streamlit run app.py
```

## Project Structure

```
.
├── app.py          # Streamlit UI
├── fetcher.py      # yfinance data retrieval
├── analyzer.py     # metric calculations
├── charts.py       # Plotly chart builders
└── requirements.txt
```

## Built With

- [Streamlit](https://streamlit.io)
- [yfinance](https://github.com/ranaroussi/yfinance)
- [Plotly](https://plotly.com/python/)
- [pandas](https://pandas.pydata.org)
