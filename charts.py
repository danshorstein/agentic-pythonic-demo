"""
charts.py — builds Plotly figures for the Streamlit dashboard
"""
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd

# ── Color palette ─────────────────────────────────────────────────────────
COLORS = {
    "primary": "#6C63FF",
    "secondary": "#48CAE4",
    "accent": "#F72585",
    "positive": "#2DC653",
    "negative": "#E63946",
    "muted": "#8D99AE",
    "bg": "#0D1117",
    "card": "#161B22",
    "border": "#30363D",
    "text": "#E6EDF3",
}

CHART_LAYOUT = dict(
    paper_bgcolor=COLORS["bg"],
    plot_bgcolor=COLORS["bg"],
    font=dict(family="Inter, sans-serif", color=COLORS["text"], size=13),
    xaxis=dict(gridcolor=COLORS["border"], zerolinecolor=COLORS["border"]),
    yaxis=dict(gridcolor=COLORS["border"], zerolinecolor=COLORS["border"]),
    margin=dict(l=50, r=30, t=50, b=50),
    legend=dict(bgcolor=COLORS["card"], bordercolor=COLORS["border"], borderwidth=1),
)


def apply_theme(chart_colors: dict, font_family: str = "Inter, sans-serif") -> None:
    """Swap the module-level color palette and chart layout in-place."""
    COLORS.update(chart_colors)
    new_layout = dict(
        paper_bgcolor=COLORS["bg"],
        plot_bgcolor=COLORS["bg"],
        font=dict(family=font_family, color=COLORS["text"], size=13),
        xaxis=dict(gridcolor=COLORS["border"], zerolinecolor=COLORS["border"]),
        yaxis=dict(gridcolor=COLORS["border"], zerolinecolor=COLORS["border"]),
        margin=dict(l=50, r=30, t=50, b=50),
        legend=dict(bgcolor=COLORS["card"], bordercolor=COLORS["border"], borderwidth=1),
    )
    CHART_LAYOUT.clear()
    CHART_LAYOUT.update(new_layout)


def _billions(series: pd.Series) -> pd.Series:
    return (series / 1e9).round(2)


def revenue_profit_chart(metrics: dict) -> go.Figure:
    """Grouped bar: Revenue, Gross Profit, Operating Income, Net Income."""
    years = None
    traces = []
    pairs = [
        ("revenue", "Revenue", COLORS["primary"]),
        ("gross_profit", "Gross Profit", COLORS["secondary"]),
        ("operating_income", "Operating Income", "#F9C74F"),
        ("net_income", "Net Income", COLORS["positive"]),
    ]
    for key, label, color in pairs:
        s = metrics.get(key)
        if s is not None and not s.empty:
            s = _billions(s).sort_index()
            if years is None:
                years = s.index.tolist()
            traces.append(go.Bar(name=label, x=s.index, y=s.values, marker_color=color))

    fig = go.Figure(data=traces)
    fig.update_layout(
        **CHART_LAYOUT,
        barmode="group",
        title="Revenue & Profit ($B)",
        bargap=0.15,
        bargroupgap=0.05,
    )
    return fig


def margins_chart(metrics: dict) -> go.Figure:
    """Line chart of gross, operating, net, EBITDA margins."""
    fig = go.Figure()
    pairs = [
        ("gross_margin", "Gross Margin", COLORS["primary"]),
        ("ebitda_margin", "EBITDA Margin", COLORS["secondary"]),
        ("operating_margin", "Operating Margin", "#F9C74F"),
        ("net_margin", "Net Margin", COLORS["positive"]),
    ]
    for key, label, color in pairs:
        s = metrics.get(key)
        if s is not None and not s.empty:
            s = s.sort_index()
            fig.add_trace(go.Scatter(
                name=label, x=s.index, y=s.values,
                mode="lines+markers",
                line=dict(color=color, width=2.5),
                marker=dict(size=8),
            ))
    fig.update_layout(
        **CHART_LAYOUT,
        title="Profitability Margins (%)",
        yaxis_ticksuffix="%",
    )
    return fig


def growth_chart(metrics: dict) -> go.Figure:
    """Bar chart of YoY revenue growth."""
    s = metrics.get("revenue_growth")
    if s is None or s.empty:
        return go.Figure()
    s = s.dropna().sort_index()
    colors = [COLORS["positive"] if v >= 0 else COLORS["negative"] for v in s.values]
    fig = go.Figure(go.Bar(x=s.index, y=s.values, marker_color=colors))
    fig.update_layout(
        **CHART_LAYOUT,
        title="YoY Revenue Growth (%)",
        yaxis_ticksuffix="%",
    )
    return fig


def cash_flow_chart(metrics: dict) -> go.Figure:
    """Grouped bar: Operating CF vs FCF."""
    fig = go.Figure()
    for key, label, color in [
        ("operating_cf", "Operating Cash Flow", COLORS["secondary"]),
        ("fcf", "Free Cash Flow", COLORS["primary"]),
    ]:
        s = metrics.get(key)
        if s is not None and not s.empty:
            s = _billions(s).sort_index()
            fig.add_trace(go.Bar(name=label, x=s.index, y=s.values, marker_color=color))
    fig.update_layout(
        **CHART_LAYOUT,
        barmode="group",
        title="Cash Flow ($B)",
    )
    return fig


def liquidity_leverage_chart(metrics: dict) -> go.Figure:
    """Dual-axis: current ratio + debt/equity."""
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    for key, label, color, secondary in [
        ("current_ratio", "Current Ratio", COLORS["secondary"], False),
        ("quick_ratio", "Quick Ratio", "#F9C74F", False),
        ("debt_to_equity", "Debt / Equity", COLORS["accent"], True),
    ]:
        s = metrics.get(key)
        if s is not None and not s.empty:
            s = s.sort_index()
            fig.add_trace(
                go.Scatter(name=label, x=s.index, y=s.values,
                           mode="lines+markers",
                           line=dict(color=color, width=2.5),
                           marker=dict(size=8)),
                secondary_y=secondary,
            )

    fig.update_layout(**CHART_LAYOUT, title="Liquidity & Leverage")
    fig.update_yaxes(title_text="Ratio", secondary_y=False, gridcolor=COLORS["border"])
    fig.update_yaxes(title_text="Debt / Equity", secondary_y=True, gridcolor=COLORS["border"])
    return fig


def returns_chart(metrics: dict) -> go.Figure:
    """Line chart of ROE and ROA."""
    fig = go.Figure()
    for key, label, color in [
        ("roe", "Return on Equity (ROE)", COLORS["primary"]),
        ("roa", "Return on Assets (ROA)", COLORS["secondary"]),
    ]:
        s = metrics.get(key)
        if s is not None and not s.empty:
            s = s.sort_index()
            fig.add_trace(go.Scatter(
                name=label, x=s.index, y=s.values,
                mode="lines+markers",
                line=dict(color=color, width=2.5),
                marker=dict(size=8),
            ))
    fig.update_layout(
        **CHART_LAYOUT,
        title="Returns (%)",
        yaxis_ticksuffix="%",
    )
    return fig


def valuation_gauge(metrics: dict) -> go.Figure:
    """Horizontal bar chart of valuation multiples."""
    val = metrics.get("valuation", {})
    keys_to_show = ["P/E (TTM)", "P/E (Fwd)", "EV/EBITDA", "P/S (TTM)", "P/B"]
    labels, values = [], []
    for k in keys_to_show:
        v = val.get(k)
        if v is not None:
            labels.append(k)
            values.append(round(v, 1))

    fig = go.Figure(go.Bar(
        x=values, y=labels, orientation="h",
        marker_color=COLORS["primary"],
        text=values, textposition="outside",
        textfont=dict(color=COLORS["text"]),
    ))
    fig.update_layout(
        **CHART_LAYOUT,
        title="Valuation Multiples (latest)",
        xaxis=dict(gridcolor=COLORS["border"]),
        yaxis=dict(gridcolor="rgba(0,0,0,0)"),
    )
    return fig
