"""
app.py — Financial Statement Analyzer
A demo app built with Antigravity, showcasing agentic coding across tools.
"""
import streamlit as st
import pandas as pd
from fetcher import get_company_data
from analyzer import compute_metrics
from charts import (
    revenue_profit_chart,
    margins_chart,
    growth_chart,
    cash_flow_chart,
    liquidity_leverage_chart,
    returns_chart,
    valuation_gauge,
)

# ── Page config ───────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FinSight — Financial Statement Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

  html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0D1117;
    color: #E6EDF3;
  }

  /* Sidebar */
  section[data-testid="stSidebar"] {
    background-color: #161B22;
    border-right: 1px solid #30363D;
  }

  /* Metric cards */
  [data-testid="stMetric"] {
    background: #161B22;
    border: 1px solid #30363D;
    border-radius: 12px;
    padding: 16px 20px;
  }
  [data-testid="stMetricLabel"] { color: #8D99AE !important; font-size: 12px !important; }
  [data-testid="stMetricValue"] { color: #E6EDF3 !important; font-size: 22px !important; font-weight: 600 !important; }
  [data-testid="stMetricDelta"] { font-size: 13px !important; }

  /* Tab styling */
  .stTabs [role="tab"] {
    color: #8D99AE;
    font-weight: 500;
    padding: 8px 20px;
    border-radius: 8px 8px 0 0;
  }
  .stTabs [role="tab"][aria-selected="true"] {
    color: #6C63FF;
    border-bottom: 2px solid #6C63FF;
    background: rgba(108,99,255,0.08);
  }

  /* Hero banner */
  .hero {
    background: linear-gradient(135deg, #1a1040 0%, #0D1117 50%, #0a2a3d 100%);
    border: 1px solid #30363D;
    border-radius: 16px;
    padding: 32px 40px;
    margin-bottom: 24px;
  }
  .hero h1 { font-size: 2.2rem; font-weight: 700; margin: 0; color: #E6EDF3; }
  .hero p  { color: #8D99AE; margin: 6px 0 0; font-size: 1rem; }

  /* Section headers */
  .section-header {
    font-size: 0.75rem;
    font-weight: 600;
    color: #8D99AE;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin: 24px 0 8px;
  }

  /* Tag badge */
  .badge {
    display: inline-block;
    background: rgba(108,99,255,0.15);
    color: #6C63FF;
    font-size: 0.75rem;
    font-weight: 600;
    padding: 3px 10px;
    border-radius: 99px;
    margin-left: 10px;
    vertical-align: middle;
  }

  /* Divider */
  hr { border-color: #30363D; }

  /* Input */
  .stTextInput input {
    background: #0D1117;
    border: 1px solid #30363D;
    color: #E6EDF3;
    border-radius: 8px;
  }
  .stTextInput input:focus { border-color: #6C63FF !important; box-shadow: 0 0 0 3px rgba(108,99,255,0.2); }

  /* Button */
  .stButton button {
    background: linear-gradient(135deg, #6C63FF, #48CAE4);
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    padding: 10px 24px;
    width: 100%;
    transition: opacity 0.2s;
  }
  .stButton button:hover { opacity: 0.88; }
</style>
""", unsafe_allow_html=True)


# ── Sidebar ───────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 📊 FinSight")
    st.markdown("<p style='color:#8D99AE;font-size:0.85rem'>Financial Statement Analyzer</p>", unsafe_allow_html=True)
    st.markdown("---")

    ticker_input = st.text_input(
        "Ticker Symbol",
        value="AAPL",
        placeholder="e.g. MSFT, NVDA, TSLA",
        help="Enter any US-listed stock ticker",
    )
    analyze_btn = st.button("Analyze →", use_container_width=True)

    st.markdown("---")
    st.markdown("<p class='section-header'>Quick picks</p>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    quick_tickers = ["AAPL", "MSFT", "NVDA", "GOOGL", "META", "AMZN"]
    for i, qt in enumerate(quick_tickers):
        col = col1 if i % 2 == 0 else col2
        with col:
            if st.button(qt, key=f"quick_{qt}"):
                st.session_state["ticker"] = qt
                st.rerun()

    st.markdown("---")
    st.markdown("""
    <p style='color:#8D99AE;font-size:0.75rem;line-height:1.6'>
    Data sourced from Yahoo Finance via <code>yfinance</code>.<br>
    Built with <strong>Antigravity</strong> 🚀<br>
    Part of the agentic coding demo series.
    </p>
    """, unsafe_allow_html=True)


# ── Resolve ticker ────────────────────────────────────────────────────────
if "ticker" not in st.session_state:
    st.session_state["ticker"] = "AAPL"

if analyze_btn and ticker_input:
    st.session_state["ticker"] = ticker_input.upper().strip()

ticker = st.session_state["ticker"]


# ── Main content ──────────────────────────────────────────────────────────
@st.cache_data(ttl=3600, show_spinner=False)
def load_data(ticker: str):
    data = get_company_data(ticker)
    metrics = compute_metrics(data)
    return data, metrics


with st.spinner(f"Fetching financial data for **{ticker}**…"):
    try:
        data, metrics = load_data(ticker)
        info = data["info"]
        load_error = None
    except Exception as e:
        load_error = str(e)

if load_error:
    st.error(f"❌ Could not load data for **{ticker}**: {load_error}")
    st.stop()

company_name = info.get("longName", ticker)
sector = info.get("sector", "—")
industry = info.get("industry", "—")
currency = info.get("financialCurrency", "USD")
price = info.get("currentPrice") or info.get("regularMarketPrice")
price_change_pct = info.get("regularMarketChangePercent", 0)
description = info.get("longBusinessSummary", "")

# ── Hero ──────────────────────────────────────────────────────────────────
price_color = "#2DC653" if price_change_pct >= 0 else "#E63946"
price_arrow = "▲" if price_change_pct >= 0 else "▼"
st.markdown(f"""
<div class="hero">
  <h1>{company_name} <span class="badge">{ticker}</span></h1>
  <p>{sector} &nbsp;·&nbsp; {industry}</p>
  {"<p style='margin-top:12px;font-size:1.6rem;font-weight:700;color:#E6EDF3'>" + currency + " " + f"{price:,.2f}" + f" <span style='font-size:1rem;color:{price_color}'>{price_arrow} {abs(price_change_pct)*100:.2f}%</span></p>" if price else ""}
</div>
""", unsafe_allow_html=True)

if description:
    with st.expander("Company Overview", expanded=False):
        st.markdown(f"<p style='color:#8D99AE;line-height:1.7'>{description}</p>", unsafe_allow_html=True)


# ── KPI cards ─────────────────────────────────────────────────────────────
val = metrics.get("valuation", {})
mkt_cap = val.get("Market Cap ($B)")
pe = val.get("P/E (TTM)")
ev_ebitda = val.get("EV/EBITDA")
ps = val.get("P/S (TTM)")

latest_revenue = metrics["revenue"].iloc[-1] / 1e9 if "revenue" in metrics and not metrics["revenue"].empty else None
latest_net_margin = metrics["net_margin"].iloc[-1] if "net_margin" in metrics and not metrics["net_margin"].empty else None

kpi_cols = st.columns(5)
kpis = [
    ("Market Cap", f"${mkt_cap:.1f}B" if mkt_cap else "—", None),
    ("Revenue (TTM)", f"${latest_revenue:.1f}B" if latest_revenue else "—", None),
    ("Net Margin", f"{latest_net_margin:.1f}%" if latest_net_margin else "—", None),
    ("P/E Ratio", f"{pe:.1f}x" if pe else "—", None),
    ("EV/EBITDA", f"{ev_ebitda:.1f}x" if ev_ebitda else "—", None),
]
for col, (label, val_str, delta) in zip(kpi_cols, kpis):
    with col:
        st.metric(label=label, value=val_str, delta=delta)

st.markdown("---")


# ── Tabs ──────────────────────────────────────────────────────────────────
tab_income, tab_margins, tab_cashflow, tab_balance, tab_valuation = st.tabs([
    "💰 Income",
    "📈 Margins & Growth",
    "💸 Cash Flow",
    "🏦 Balance Sheet",
    "🏷️ Valuation",
])


with tab_income:
    st.markdown("<p class='section-header'>Revenue & Profitability</p>", unsafe_allow_html=True)
    st.plotly_chart(revenue_profit_chart(metrics), use_container_width=True)

    # Raw table
    inc = data["income_stmt"]
    if not inc.empty:
        show_cols = [c for c in [
            "Total Revenue", "Gross Profit", "Operating Income", "EBITDA", "Net Income"
        ] if c in inc.columns]
        if show_cols:
            display = (inc[show_cols] / 1e9).round(2).sort_index()
            display.index.name = "Year"
            display.columns = [c + " ($B)" for c in display.columns]
            st.dataframe(display.style.format("${:.2f}"), use_container_width=True)


with tab_margins:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<p class='section-header'>Profitability Margins</p>", unsafe_allow_html=True)
        st.plotly_chart(margins_chart(metrics), use_container_width=True)
    with c2:
        st.markdown("<p class='section-header'>Revenue Growth YoY</p>", unsafe_allow_html=True)
        st.plotly_chart(growth_chart(metrics), use_container_width=True)


with tab_cashflow:
    st.markdown("<p class='section-header'>Operating Cash Flow vs Free Cash Flow</p>", unsafe_allow_html=True)
    st.plotly_chart(cash_flow_chart(metrics), use_container_width=True)

    if "fcf_margin" in metrics and not metrics["fcf_margin"].empty:
        st.markdown("<p class='section-header'>FCF Margin (%)</p>", unsafe_allow_html=True)
        fcf_m = metrics["fcf_margin"].sort_index()
        col_color = ["#2DC653" if v >= 0 else "#E63946" for v in fcf_m.values]
        import plotly.graph_objects as go
        from charts import CHART_LAYOUT
        fig = go.Figure(go.Bar(x=fcf_m.index, y=fcf_m.values, marker_color=col_color))
        fig.update_layout(**CHART_LAYOUT, title="Free Cash Flow Margin (%)", yaxis_ticksuffix="%")
        st.plotly_chart(fig, use_container_width=True)


with tab_balance:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<p class='section-header'>Liquidity & Leverage</p>", unsafe_allow_html=True)
        st.plotly_chart(liquidity_leverage_chart(metrics), use_container_width=True)
    with c2:
        st.markdown("<p class='section-header'>Returns on Capital</p>", unsafe_allow_html=True)
        st.plotly_chart(returns_chart(metrics), use_container_width=True)


with tab_valuation:
    st.markdown("<p class='section-header'>Current Valuation Multiples</p>", unsafe_allow_html=True)
    st.plotly_chart(valuation_gauge(metrics), use_container_width=True)

    val_dict = metrics.get("valuation", {})
    if val_dict:
        val_df = pd.DataFrame(val_dict.items(), columns=["Metric", "Value"]).set_index("Metric")
        st.dataframe(val_df, use_container_width=True)
