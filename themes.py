"""
themes.py — Visual theme definitions for FinSight
"""

THEMES = {
    "Default": {
        "font_family": "Inter, sans-serif",
        "chart_colors": {
            "primary":  "#6C63FF",
            "secondary": "#48CAE4",
            "accent":   "#F72585",
            "positive": "#2DC653",
            "negative": "#E63946",
            "muted":    "#8D99AE",
            "bg":       "#0D1117",
            "card":     "#161B22",
            "border":   "#30363D",
            "text":     "#E6EDF3",
        },
        "css": """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
html, body, [class*="css"] {
  font-family: 'Inter', sans-serif;
  background-color: #0D1117;
  color: #E6EDF3;
}
section[data-testid="stSidebar"] {
  background-color: #161B22;
  border-right: 1px solid #30363D;
}
[data-testid="stMetric"] {
  background: #161B22;
  border: 1px solid #30363D;
  border-radius: 12px;
  padding: 16px 20px;
}
[data-testid="stMetricLabel"] { color: #8D99AE !important; font-size: 12px !important; }
[data-testid="stMetricValue"] { color: #E6EDF3 !important; font-size: 22px !important; font-weight: 600 !important; }
[data-testid="stMetricDelta"] { font-size: 13px !important; }
.stTabs [role="tab"] { color: #8D99AE; font-weight: 500; padding: 8px 20px; border-radius: 8px 8px 0 0; }
.stTabs [role="tab"][aria-selected="true"] { color: #6C63FF; border-bottom: 2px solid #6C63FF; background: rgba(108,99,255,0.08); }
.hero { background: linear-gradient(135deg,#1a1040 0%,#0D1117 50%,#0a2a3d 100%); border: 1px solid #30363D; border-radius: 16px; padding: 32px 40px; margin-bottom: 24px; }
.hero h1 { font-size: 2.2rem; font-weight: 700; margin: 0; color: #E6EDF3; }
.hero p { color: #8D99AE; margin: 6px 0 0; font-size: 1rem; }
.section-header { font-size: 0.75rem; font-weight: 600; color: #8D99AE; letter-spacing: 0.08em; text-transform: uppercase; margin: 24px 0 8px; }
.badge { display: inline-block; background: rgba(108,99,255,0.15); color: #6C63FF; font-size: 0.75rem; font-weight: 600; padding: 3px 10px; border-radius: 99px; margin-left: 10px; vertical-align: middle; }
hr { border-color: #30363D; }
.stTextInput input { background: #0D1117; border: 1px solid #30363D; color: #E6EDF3; border-radius: 8px; }
.stTextInput input:focus { border-color: #6C63FF !important; box-shadow: 0 0 0 3px rgba(108,99,255,0.2); }
.stButton button { background: linear-gradient(135deg,#6C63FF,#48CAE4); color: white; border: none; border-radius: 8px; font-weight: 600; padding: 10px 24px; width: 100%; transition: opacity 0.2s; }
.stButton button:hover { opacity: 0.88; }
""",
    },

    # ── Bloomberg Terminal ─────────────────────────────────────────────────
    "Bloomberg Terminal": {
        "font_family": "'JetBrains Mono', monospace",
        "chart_colors": {
            "primary":  "#00FF41",
            "secondary": "#FFB000",
            "accent":   "#FF6B6B",
            "positive": "#00FF41",
            "negative": "#FF4136",
            "muted":    "#3a5a3a",
            "bg":       "#000000",
            "card":     "#050505",
            "border":   "#1a3a1a",
            "text":     "#00FF41",
        },
        "css": """
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&display=swap');

html, body, [class*="css"] {
  font-family: 'JetBrains Mono', monospace !important;
  background-color: #000000 !important;
  color: #00FF41 !important;
}

/* CRT scanline overlay */
body::after {
  content: '';
  position: fixed;
  top: 0; left: 0;
  width: 100vw; height: 100vh;
  background: repeating-linear-gradient(
    0deg,
    rgba(0,0,0,0.10) 0px, rgba(0,0,0,0.10) 1px,
    transparent 1px, transparent 3px
  );
  pointer-events: none;
  z-index: 9998;
}

/* Phosphor glow on text */
body { text-shadow: 0 0 4px rgba(0,255,65,0.3); }

.stApp, .stApp > *, .main, .block-container {
  background-color: #000000 !important;
}

section[data-testid="stSidebar"] {
  background-color: #000000 !important;
  border-right: 1px solid #00FF41 !important;
  box-shadow: 4px 0 20px rgba(0,255,65,0.05) !important;
}

[data-testid="stMetric"] {
  background: #000000 !important;
  border: 1px solid #00FF41 !important;
  border-radius: 0 !important;
  padding: 16px 20px;
  box-shadow: 0 0 10px rgba(0,255,65,0.08) !important;
}
[data-testid="stMetricLabel"] {
  color: #3a6a3a !important;
  font-size: 10px !important;
  text-transform: uppercase !important;
  letter-spacing: 0.12em !important;
  font-family: 'JetBrains Mono', monospace !important;
}
[data-testid="stMetricValue"] {
  color: #00FF41 !important;
  font-size: 20px !important;
  font-weight: 700 !important;
  font-family: 'JetBrains Mono', monospace !important;
}
[data-testid="stMetricDelta"] { font-size: 12px !important; }

.stTabs [role="tab"] {
  color: #3a6a3a !important;
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 0.8rem !important;
  padding: 8px 16px !important;
  border-radius: 0 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.06em !important;
}
.stTabs [role="tab"][aria-selected="true"] {
  color: #00FF41 !important;
  border-bottom: 2px solid #00FF41 !important;
  background: rgba(0,255,65,0.04) !important;
  box-shadow: 0 4px 12px rgba(0,255,65,0.1) !important;
}
.stTabs [data-baseweb="tab-list"] {
  background: #000000 !important;
  border-bottom: 1px solid #1a3a1a !important;
}

.hero {
  background: #000000 !important;
  border: 1px solid #00FF41 !important;
  border-radius: 0 !important;
  padding: 32px 40px !important;
  margin-bottom: 24px !important;
  box-shadow: 0 0 30px rgba(0,255,65,0.06), inset 0 0 30px rgba(0,255,65,0.02) !important;
}
.hero h1 {
  color: #00FF41 !important;
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 1.8rem !important;
  letter-spacing: 0.04em !important;
  text-shadow: 0 0 16px rgba(0,255,65,0.6) !important;
}
.hero p { color: #3a6a3a !important; font-family: 'JetBrains Mono', monospace !important; }

.section-header {
  color: #3a6a3a !important;
  font-family: 'JetBrains Mono', monospace !important;
  letter-spacing: 0.12em !important;
  font-size: 0.7rem !important;
}

.badge {
  display: inline-block !important;
  background: rgba(0,255,65,0.08) !important;
  color: #00FF41 !important;
  font-size: 0.7rem !important;
  font-weight: 700 !important;
  padding: 2px 8px !important;
  border-radius: 0 !important;
  border: 1px solid #00FF41 !important;
  margin-left: 10px !important;
  text-shadow: 0 0 8px rgba(0,255,65,0.8) !important;
}

hr { border-color: #1a3a1a !important; }

.stTextInput input {
  background: #000000 !important;
  border: 1px solid #00FF41 !important;
  color: #00FF41 !important;
  border-radius: 0 !important;
  font-family: 'JetBrains Mono', monospace !important;
}
.stTextInput input:focus {
  border-color: #00FF41 !important;
  box-shadow: 0 0 0 3px rgba(0,255,65,0.15), 0 0 12px rgba(0,255,65,0.2) !important;
}
.stTextInput input::placeholder { color: #3a6a3a !important; }

.stButton button {
  background: transparent !important;
  color: #00FF41 !important;
  border: 1px solid #00FF41 !important;
  border-radius: 0 !important;
  font-family: 'JetBrains Mono', monospace !important;
  font-weight: 700 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.08em !important;
  transition: all 0.15s !important;
  box-shadow: 0 0 8px rgba(0,255,65,0.1) !important;
}
.stButton button:hover {
  background: rgba(0,255,65,0.08) !important;
  box-shadow: 0 0 16px rgba(0,255,65,0.3) !important;
}

/* Dataframe */
[data-testid="stDataFrame"] { border: 1px solid #1a3a1a !important; }

/* Expander */
[data-testid="stExpander"] {
  border: 1px solid #1a3a1a !important;
  border-radius: 0 !important;
  background: #000000 !important;
}

/* Radio (theme toggle) */
.stRadio label { color: #3a6a3a !important; font-family: 'JetBrains Mono', monospace !important; font-size: 0.75rem !important; }

/* Selectbox / other inputs */
[data-testid="stSelectbox"] div { border-color: #1a3a1a !important; background: #000000 !important; color: #00FF41 !important; }
""",
    },

    # ── Glassmorphism ──────────────────────────────────────────────────────
    "Glassmorphism": {
        "font_family": "'Plus Jakarta Sans', sans-serif",
        "chart_colors": {
            "primary":  "#a78bfa",
            "secondary": "#67e8f9",
            "accent":   "#f9a8d4",
            "positive": "#6ee7b7",
            "negative": "#fca5a5",
            "muted":    "#64748b",
            "bg":       "#0c0920",
            "card":     "#16103a",
            "border":   "#2d2060",
            "text":     "#e2d9f3",
        },
        "css": """
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

@keyframes gradientDrift {
  0%   { background-position: 0%   50%; }
  50%  { background-position: 100% 50%; }
  100% { background-position: 0%   50%; }
}

html, body, [class*="css"] {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  color: #e2d9f3 !important;
}

.stApp {
  background: linear-gradient(135deg, #0c0920, #1a0535, #0a1535, #0c0920) !important;
  background-size: 400% 400% !important;
  animation: gradientDrift 18s ease infinite !important;
}

.main, .block-container {
  background: transparent !important;
}

section[data-testid="stSidebar"] {
  background: rgba(15, 10, 40, 0.6) !important;
  backdrop-filter: blur(24px) !important;
  -webkit-backdrop-filter: blur(24px) !important;
  border-right: 1px solid rgba(255,255,255,0.07) !important;
}

[data-testid="stMetric"] {
  background: rgba(255,255,255,0.04) !important;
  border: 1px solid rgba(255,255,255,0.08) !important;
  border-top: 1px solid rgba(167,139,250,0.35) !important;
  border-radius: 20px !important;
  padding: 18px 22px !important;
  backdrop-filter: blur(16px) !important;
  -webkit-backdrop-filter: blur(16px) !important;
  box-shadow: 0 8px 32px rgba(0,0,0,0.25), 0 1px 0 rgba(255,255,255,0.05) inset !important;
  transition: transform 0.2s, box-shadow 0.2s !important;
}
[data-testid="stMetric"]:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 16px 48px rgba(0,0,0,0.35), 0 0 0 1px rgba(167,139,250,0.2) !important;
}
[data-testid="stMetricLabel"] {
  color: #94a3b8 !important;
  font-size: 11px !important;
  font-weight: 300 !important;
  letter-spacing: 0.06em !important;
  text-transform: uppercase !important;
}
[data-testid="stMetricValue"] {
  color: #e2d9f3 !important;
  font-size: 22px !important;
  font-weight: 600 !important;
  letter-spacing: -0.02em !important;
}
[data-testid="stMetricDelta"] { font-size: 13px !important; }

.stTabs [role="tab"] {
  color: #64748b !important;
  font-weight: 500 !important;
  padding: 8px 20px !important;
  border-radius: 99px !important;
  transition: all 0.25s !important;
  font-family: 'Plus Jakarta Sans', sans-serif !important;
}
.stTabs [role="tab"][aria-selected="true"] {
  color: #a78bfa !important;
  background: rgba(167,139,250,0.1) !important;
  border-bottom: 2px solid #a78bfa !important;
  box-shadow: 0 2px 16px rgba(167,139,250,0.15) !important;
}
.stTabs [data-baseweb="tab-list"] {
  background: rgba(255,255,255,0.02) !important;
  border-radius: 12px !important;
  padding: 4px !important;
  gap: 4px !important;
}

.hero {
  background: rgba(255,255,255,0.03) !important;
  border: 1px solid rgba(255,255,255,0.07) !important;
  border-radius: 28px !important;
  padding: 36px 44px !important;
  margin-bottom: 28px !important;
  backdrop-filter: blur(24px) !important;
  -webkit-backdrop-filter: blur(24px) !important;
  box-shadow:
    0 32px 80px rgba(0,0,0,0.4),
    0 1px 0 rgba(255,255,255,0.06) inset,
    0 -1px 0 rgba(0,0,0,0.2) inset !important;
}
.hero h1 {
  color: #e2d9f3 !important;
  font-weight: 700 !important;
  font-size: 2.2rem !important;
  letter-spacing: -0.03em !important;
  font-family: 'Plus Jakarta Sans', sans-serif !important;
}
.hero p { color: #64748b !important; font-weight: 300 !important; }

.section-header {
  color: #64748b !important;
  letter-spacing: 0.08em !important;
  font-weight: 500 !important;
  font-size: 0.72rem !important;
}

.badge {
  display: inline-block !important;
  background: rgba(167,139,250,0.12) !important;
  color: #a78bfa !important;
  font-size: 0.72rem !important;
  font-weight: 600 !important;
  padding: 3px 12px !important;
  border-radius: 99px !important;
  border: 1px solid rgba(167,139,250,0.25) !important;
  margin-left: 10px !important;
  vertical-align: middle !important;
  backdrop-filter: blur(8px) !important;
}

hr { border-color: rgba(255,255,255,0.06) !important; }

.stTextInput input {
  background: rgba(255,255,255,0.04) !important;
  border: 1px solid rgba(255,255,255,0.08) !important;
  color: #e2d9f3 !important;
  border-radius: 14px !important;
  backdrop-filter: blur(8px) !important;
  font-family: 'Plus Jakarta Sans', sans-serif !important;
}
.stTextInput input:focus {
  border-color: rgba(167,139,250,0.6) !important;
  box-shadow: 0 0 0 3px rgba(167,139,250,0.15), 0 0 20px rgba(167,139,250,0.1) !important;
}
.stTextInput input::placeholder { color: #4a4a6a !important; }

.stButton button {
  background: rgba(167,139,250,0.12) !important;
  color: #c4b5fd !important;
  border: 1px solid rgba(167,139,250,0.3) !important;
  border-radius: 14px !important;
  font-weight: 600 !important;
  backdrop-filter: blur(8px) !important;
  transition: all 0.25s !important;
  letter-spacing: 0.01em !important;
}
.stButton button:hover {
  background: rgba(167,139,250,0.22) !important;
  border-color: rgba(167,139,250,0.5) !important;
  box-shadow: 0 8px 32px rgba(167,139,250,0.2) !important;
  transform: translateY(-1px) !important;
}

[data-testid="stExpander"] {
  background: rgba(255,255,255,0.02) !important;
  border: 1px solid rgba(255,255,255,0.06) !important;
  border-radius: 16px !important;
  backdrop-filter: blur(12px) !important;
}

.stRadio label { color: #64748b !important; font-family: 'Plus Jakarta Sans', sans-serif !important; font-size: 0.8rem !important; }
""",
    },

    # ── Synthwave ──────────────────────────────────────────────────────────
    "Synthwave": {
        "font_family": "'Inter', sans-serif",
        "chart_colors": {
            "primary":  "#FF2D78",
            "secondary": "#00F5FF",
            "accent":   "#FFEE00",
            "positive": "#39FF14",
            "negative": "#FF2D78",
            "muted":    "#9d4edd",
            "bg":       "#0a0010",
            "card":     "#120020",
            "border":   "#3d0060",
            "text":     "#f0e6ff",
        },
        "css": """
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;500;600;700&display=swap');

@keyframes neonPulse {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0.75; }
}

@keyframes tabGlow {
  0%, 100% { box-shadow: 0 2px 12px rgba(255,45,120,0.4); }
  50%       { box-shadow: 0 2px 24px rgba(255,45,120,0.8); }
}

html, body, [class*="css"] {
  font-family: 'Inter', sans-serif !important;
  background-color: #0a0010 !important;
  color: #f0e6ff !important;
}

/* Grid background */
.stApp {
  background-color: #0a0010 !important;
  background-image:
    linear-gradient(rgba(255,45,120,0.07)  1px, transparent 1px),
    linear-gradient(90deg, rgba(0,245,255,0.04) 1px, transparent 1px) !important;
  background-size: 56px 56px !important;
}

.main, .block-container {
  background: transparent !important;
}

section[data-testid="stSidebar"] {
  background-color: #08000e !important;
  border-right: 1px solid rgba(255,45,120,0.35) !important;
  box-shadow: 4px 0 32px rgba(255,45,120,0.08) !important;
}

[data-testid="stMetric"] {
  background: #0e001e !important;
  border: 1px solid rgba(255,45,120,0.3) !important;
  border-top: 1px solid rgba(0,245,255,0.4) !important;
  border-radius: 6px !important;
  padding: 16px 20px !important;
  box-shadow:
    0 0 16px rgba(255,45,120,0.08),
    inset 0 0 24px rgba(255,45,120,0.03) !important;
}
[data-testid="stMetricLabel"] {
  color: #9d4edd !important;
  font-size: 10px !important;
  text-transform: uppercase !important;
  letter-spacing: 0.14em !important;
  font-family: 'Orbitron', sans-serif !important;
  font-weight: 400 !important;
}
[data-testid="stMetricValue"] {
  color: #f0e6ff !important;
  font-size: 22px !important;
  font-weight: 700 !important;
  text-shadow: 0 0 12px rgba(0,245,255,0.4) !important;
}
[data-testid="stMetricDelta"] { font-size: 13px !important; }

.stTabs [role="tab"] {
  color: #5a2a7a !important;
  font-weight: 500 !important;
  padding: 8px 20px !important;
}
.stTabs [role="tab"][aria-selected="true"] {
  color: #FF2D78 !important;
  border-bottom: 2px solid #FF2D78 !important;
  background: rgba(255,45,120,0.06) !important;
  animation: tabGlow 2.5s ease-in-out infinite !important;
}
.stTabs [data-baseweb="tab-list"] {
  background: transparent !important;
  border-bottom: 1px solid rgba(255,45,120,0.15) !important;
}

.hero {
  background: linear-gradient(135deg, #150025 0%, #0a0010 50%, #001525 100%) !important;
  border: 1px solid rgba(255,45,120,0.45) !important;
  border-radius: 6px !important;
  padding: 32px 40px !important;
  margin-bottom: 24px !important;
  box-shadow:
    0 0 60px rgba(255,45,120,0.08),
    0 0 120px rgba(0,245,255,0.04),
    inset 0 0 60px rgba(255,45,120,0.02) !important;
}
.hero h1 {
  color: #f0e6ff !important;
  font-family: 'Orbitron', sans-serif !important;
  font-size: 1.9rem !important;
  font-weight: 900 !important;
  letter-spacing: 0.06em !important;
  text-shadow:
    0 0 20px rgba(0,245,255,0.5),
    0 0 60px rgba(0,245,255,0.2),
    0 0 80px rgba(255,45,120,0.15) !important;
}
.hero p { color: #9d4edd !important; }

.section-header {
  color: #9d4edd !important;
  font-family: 'Orbitron', sans-serif !important;
  font-size: 0.62rem !important;
  letter-spacing: 0.18em !important;
  font-weight: 400 !important;
}

.badge {
  display: inline-block !important;
  background: rgba(255,45,120,0.12) !important;
  color: #FF2D78 !important;
  font-size: 0.65rem !important;
  font-weight: 700 !important;
  padding: 2px 10px !important;
  border-radius: 3px !important;
  border: 1px solid rgba(255,45,120,0.5) !important;
  margin-left: 10px !important;
  vertical-align: middle !important;
  text-shadow: 0 0 8px rgba(255,45,120,0.9) !important;
  letter-spacing: 0.06em !important;
}

hr { border-color: rgba(255,45,120,0.15) !important; }

.stTextInput input {
  background: #0e001e !important;
  border: 1px solid rgba(255,45,120,0.35) !important;
  color: #f0e6ff !important;
  border-radius: 4px !important;
  font-family: 'Inter', sans-serif !important;
}
.stTextInput input:focus {
  border-color: #00F5FF !important;
  box-shadow: 0 0 0 3px rgba(0,245,255,0.12), 0 0 16px rgba(0,245,255,0.25) !important;
}
.stTextInput input::placeholder { color: #4a1a6a !important; }

.stButton button {
  background: transparent !important;
  color: #00F5FF !important;
  border: 1px solid rgba(0,245,255,0.6) !important;
  border-radius: 4px !important;
  font-weight: 600 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.1em !important;
  font-size: 0.8rem !important;
  transition: all 0.18s !important;
  text-shadow: 0 0 8px rgba(0,245,255,0.7) !important;
  box-shadow: 0 0 10px rgba(0,245,255,0.08), inset 0 0 10px rgba(0,245,255,0.04) !important;
}
.stButton button:hover {
  background: rgba(0,245,255,0.08) !important;
  box-shadow: 0 0 24px rgba(0,245,255,0.35), inset 0 0 16px rgba(0,245,255,0.08) !important;
  border-color: #00F5FF !important;
}

[data-testid="stExpander"] {
  border: 1px solid rgba(255,45,120,0.2) !important;
  border-radius: 4px !important;
  background: #0a0018 !important;
}

.stRadio label { color: #5a2a7a !important; font-size: 0.78rem !important; }

h1, h2, h3, h4 {
  font-family: 'Orbitron', sans-serif !important;
  letter-spacing: 0.04em !important;
}
""",
    },
}
