"""
app.py — Financial Statement Analyzer
A demo app built with Antigravity, showcasing agentic coding across tools.
"""
import streamlit as st
import pandas as pd
import charts as charts_module
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
from themes import THEMES

# ── Page config ───────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FinSight — Financial Statement Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Theme selector (must happen before any CSS is injected) ───────────────
if "theme" not in st.session_state:
    st.session_state["theme"] = "Default"

THEME_ICONS = {
    "Default":            "◈ Default",
    "Bloomberg Terminal": "⬛ Terminal",
    "Glassmorphism":      "🫧 Glass",
    "Synthwave":          "🌆 Synthwave",
}
THEME_NAMES = list(THEMES.keys())

# Theme toggle lives at the very top of the sidebar
with st.sidebar:
    st.markdown(
        "<p style='font-size:0.65rem;text-transform:uppercase;letter-spacing:0.1em;"
        "color:#555;margin-bottom:4px'>Theme</p>",
        unsafe_allow_html=True,
    )
    selected_theme = st.radio(
        "theme_radio",
        options=THEME_NAMES,
        format_func=lambda t: THEME_ICONS[t],
        index=THEME_NAMES.index(st.session_state["theme"]),
        horizontal=False,
        label_visibility="collapsed",
        key="theme_radio",
    )
    if selected_theme != st.session_state["theme"]:
        st.session_state["theme"] = selected_theme
        st.rerun()

theme = THEMES[st.session_state["theme"]]

# ── Apply theme: CSS + chart palette ─────────────────────────────────────
st.markdown(f"<style>{theme['css']}</style>", unsafe_allow_html=True)
charts_module.apply_theme(theme["chart_colors"], theme["font_family"])

# ── Sidebar (continued) ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown("---")
    st.markdown("## 📊 FinSight")
    st.markdown(
        "<p style='color:#8D99AE;font-size:0.85rem'>Financial Statement Analyzer</p>",
        unsafe_allow_html=True,
    )
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
price_color = charts_module.COLORS["positive"] if price_change_pct >= 0 else charts_module.COLORS["negative"]
price_arrow = "▲" if price_change_pct >= 0 else "▼"
st.markdown(f"""
<div class="hero">
  <h1>{company_name} <span class="badge">{ticker}</span></h1>
  <p>{sector} &nbsp;·&nbsp; {industry}</p>
  {"<p style='margin-top:12px;font-size:1.6rem;font-weight:700'>" + currency + " " + f"{price:,.2f}" + f" <span style='font-size:1rem;color:{price_color}'>{price_arrow} {abs(price_change_pct)*100:.2f}%</span></p>" if price else ""}
</div>
""", unsafe_allow_html=True)

if description:
    with st.expander("Company Overview", expanded=False):
        st.markdown(f"<p style='line-height:1.7'>{description}</p>", unsafe_allow_html=True)


# ── KPI cards ─────────────────────────────────────────────────────────────
val = metrics.get("valuation", {})
mkt_cap = val.get("Market Cap ($B)")
pe = val.get("P/E (TTM)")
ev_ebitda = val.get("EV/EBITDA")

latest_revenue = metrics["revenue"].iloc[-1] / 1e9 if "revenue" in metrics and not metrics["revenue"].empty else None
latest_net_margin = metrics["net_margin"].iloc[-1] if "net_margin" in metrics and not metrics["net_margin"].empty else None

kpi_cols = st.columns(5)
kpis = [
    ("Market Cap",    f"${mkt_cap:.1f}B"         if mkt_cap          else "—", None),
    ("Revenue (TTM)", f"${latest_revenue:.1f}B"   if latest_revenue   else "—", None),
    ("Net Margin",    f"{latest_net_margin:.1f}%" if latest_net_margin else "—", None),
    ("P/E Ratio",     f"{pe:.1f}x"                if pe               else "—", None),
    ("EV/EBITDA",     f"{ev_ebitda:.1f}x"         if ev_ebitda        else "—", None),
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
        col_color = [
            charts_module.COLORS["positive"] if v >= 0 else charts_module.COLORS["negative"]
            for v in fcf_m.values
        ]
        import plotly.graph_objects as go
        fig = go.Figure(go.Bar(x=fcf_m.index, y=fcf_m.values, marker_color=col_color))
        fig.update_layout(**charts_module.CHART_LAYOUT, title="Free Cash Flow Margin (%)", yaxis_ticksuffix="%")
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
