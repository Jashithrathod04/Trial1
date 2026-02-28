import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time
import streamlit.components.v1 as components


import streamlit as st
import yfinance as yf
import pandas as pd



# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="Crypto Volatility Visualizer",
    page_icon="📈",
    layout="wide"
)

# ==================================================
# CINEMATIC SPLASH SCREEN (Neon Financial Theme)
# ==================================================

splash_html = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
    margin:0;
    overflow:hidden;
    background: radial-gradient(circle at center, #0f2027, #203a43, #2c5364);
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
    font-family: 'Segoe UI', sans-serif;
    color:white;
}
.container {
    text-align:center;
}
.title {
    font-size:3.5rem;
    font-weight:700;
    background: linear-gradient(90deg, #00f5ff, #00ff88);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    animation: glow 2s infinite alternate;
}
@keyframes glow {
    from { text-shadow:0 0 10px #00f5ff; }
    to { text-shadow:0 0 30px #00ff88; }
}
.wave {
    width:300px;
    height:3px;
    background: linear-gradient(90deg, transparent, #00ff88, transparent);
    margin:20px auto;
    animation: expand 2.5s forwards;
}
@keyframes expand {
    from { width:0; }
    to { width:300px; }
}
.subtitle {
    opacity:0;
    animation: fadeIn 3s forwards;
    animation-delay:1.5s;
}
@keyframes fadeIn {
    to { opacity:1; }
}
</style>
</head>
<body>
<div class="container">
    <div class="title">📊 Crypto Volatility Visualizer</div>
    <div class="wave"></div>
    <div class="subtitle">
        Mathematics for AI-II • Market Swing Simulation
    </div>
</div>
</body>
</html>
"""

if "splash_shown" not in st.session_state:
    components.html(splash_html, height=800)
    time.sleep(3)
    st.session_state.splash_shown = True
    st.rerun()

# ==================================================
# GLASSMORPHISM THEME
# ==================================================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #141e30, #243b55);
}
.glass {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 2rem;
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}
h1, h2, h3 {
    color:white;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================

st.markdown("""
<div class="glass">
<h1>🚀 Crypto Volatility Dashboard</h1>
Mathematical Simulation + Real Bitcoin Data Analysis
</div>
""", unsafe_allow_html=True)

st.divider()

# ==================================================
# LOAD DATASET
# ==================================================
# ==================================================
# LOAD DATASET (CORRECT VERSION)
# ==================================================

@st.cache_data
def load_data():
    df = yf.download("BTC-USD", period="5y", interval="1d")

    # Flatten MultiIndex columns if they exist
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df.reset_index()

    return df








# ==================================================
# SIDEBAR CONTROLS (Stage 6)
# ==================================================

# ==================================================
# ELEGANT SIDEBAR — GLASS STYLE LIKE YOUR IMAGE
# ==================================================

st.markdown("""
<style>
.sidebar-glass {
    background: rgba(255,255,255,0.10);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    border: 1px solid rgba(255,255,255,0.2);
}
.sidebar-title {
    font-size: 22px;
    font-weight: 700;
    color: #00f5ff;
    margin-bottom: 10px;
}
.sidebar-label {
    font-size: 14px;
    color: #d8e6f3;
    margin-top: 15px;
    font-weight: 600;
}
.sidebar-desc {
    font-size: 12px;
    opacity: 0.7;
    color: #c9d2df;
    margin-bottom: 5px;
}



/* Toggle container */
[data-testid="stToggle"] {
    margin-top: 10px;
}

/* Toggle track (background) */
[data-testid="stToggle"] div[role="switch"] {
    background-color: #bfc4cc !important;
    border-radius: 20px !important;
    width: 42px !important;
    height: 22px !important;
    transition: 0.3s ease-in-out !important;
}

/* Toggle ON state */
[data-testid="stToggle"] div[aria-checked="true"] {
    background-color: #00ff88 !important;
}

/* Toggle circle */
[data-testid="stToggle"] div[role="switch"]::before {
    background-color: white !important;
    width: 18px !important;
    height: 18px !important;
    border-radius: 50% !important;
    top: 2px !important;
    left: 2px !important;
    transition: 0.3s ease-in-out !important;
}

/* Move circle when ON */
[data-testid="stToggle"] div[aria-checked="true"]::before {
    transform: translateX(20px) !important;
}



</style>
""", unsafe_allow_html=True)







with st.sidebar:
    st.markdown('<div class="sidebar-glass">', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-title">⚙ Simulation Controls</div>', unsafe_allow_html=True)


    st.markdown('<div class="sidebar-label">Upload Bitcoin CSV</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-desc">Upload Kaggle Bitcoin dataset.</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=["csv"])

    # Pattern
    st.markdown('<div class="sidebar-label">Select Price Pattern</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-desc">Choose how price movement is simulated.</div>', unsafe_allow_html=True)
    pattern = st.selectbox("", ["Sine Wave (Cyclical)", "Cosine Wave (Shifted Cycle)", "Random Noise (Chaotic)", "Hybrid Model (Sine + Drift + Noise)"])

    # Amplitude
    st.markdown('<div class="sidebar-label">Amplitude (Volatility Size)</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-desc">Higher value = higher swings in price.</div>', unsafe_allow_html=True)
    amplitude = st.slider("", 1, 50, 15)

    # Frequency
    st.markdown('<div class="sidebar-label">Frequency (Swing Speed)</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-desc">Low = slow waves • High = rapid movement.</div>', unsafe_allow_html=True)
    frequency = st.slider("", 1, 10, 3)

    # Drift
    st.markdown('<div class="sidebar-label">Drift (Long-term Trend)</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-desc">Positive = bullish • Negative = bearish.</div>', unsafe_allow_html=True)
    drift = st.slider("", -2.0, 2.0, 0.1)

    # Noise
    st.markdown('<div class="sidebar-label">Noise Intensity</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-desc">Adds unpredictability like real crypto markets.</div>', unsafe_allow_html=True)
    noise = st.slider("", 0, 30, 5)

    # Comparison Mode Toggle
    st.markdown('<div class="sidebar-label">Enable Comparison Mode</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-desc">Compare stable vs volatile simulation.</div>', unsafe_allow_html=True)
    compare_mode = st.toggle("")

    # Main Button
    simulate_btn = st.button("Simulate", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)



if uploaded_file is not None:
    st.write("Using Uploaded CSV")

    df = pd.read_csv(uploaded_file)

    # Convert Timestamp → Date
    if "Timestamp" in df.columns:
        df["Date"] = pd.to_datetime(df["Timestamp"], unit="s")

    df = df.dropna()
    df = df.sort_values("Date")
    df = df.tail(500)

else:
    st.write("Using Yahoo Finance Data")
    df = load_data()
    df = df.dropna()
    df = df.tail(500)





# ==================================================
# TAB STRUCTURE
# ==================================================

tab1, tab2 = st.tabs(["📊 Real Market Analysis", "📈 Mathematical Simulation"])

# ==================================================
# TAB 1 — REAL DATA VISUALIZATION
# ==================================================

with tab1:

    st.subheader("Bitcoin Close Price Over Time")

    fig = px.line(df, x="Date", y="Close",
                  title="Bitcoin Close Price")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("High vs Low Price Comparison")

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=df["Date"], y=df["High"], name="High"))
    fig2.add_trace(go.Scatter(x=df["Date"], y=df["Low"], name="Low"))
    fig2.update_layout(title="High vs Low Price")
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Volume Analysis")

    fig3 = px.bar(df, x="Date", y="Volume",
                  title="Trading Volume")
    st.plotly_chart(fig3, use_container_width=True)

    # Volatility Index
    df["Volatility"] = df["Close"].pct_change().rolling(10).std()

    st.subheader("Rolling Volatility (10 Period)")

    fig4 = px.line(df, x="Date", y="Volatility",
                   title="Volatility Index")
    st.plotly_chart(fig4, use_container_width=True)

# ==================================================
# TAB 2 — MATHEMATICAL SIMULATION
# ==================================================

with tab2:

    st.subheader("Simulated Market Swing")

    t = np.linspace(0, 50, 500)

    # Pattern Logic
    if pattern == "Sine Wave (Cyclical)":
        wave = amplitude * np.sin(frequency * t)

    elif pattern == "Cosine Wave (Shifted Cycle)":
        wave = amplitude * np.cos(frequency * t)

    elif pattern == "Random Noise (Chaotic)":
        wave = np.random.normal(0, amplitude, len(t))

    elif pattern == "Hybrid Model (Sine + Drift + Noise)":
        sine_component = amplitude * np.sin(frequency * t)
        noise_component = np.random.normal(0, noise, len(t))
        wave = sine_component + noise_component

    else:
        wave = np.zeros(len(t))

    trend = drift * t
    simulated_price = 100 + wave + trend

    fig_sim = go.Figure()
    fig_sim.add_trace(go.Scatter(x=t, y=simulated_price,
                                 name="Simulated Price"))
    fig_sim.update_layout(title="Simulated Price Movement")
    st.plotly_chart(fig_sim, use_container_width=True)

    volatility_index = np.std(simulated_price)
    avg_drift = np.mean(np.diff(simulated_price))

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📊 Volatility Index", f"{volatility_index:.2f}")

    with col2:
        st.metric("📈 Average Drift", f"{avg_drift:.4f}")

    with col1:
        st.metric("📊 Volatility Index", f"{volatility_index:.2f}")

    with col2:
        st.metric("📈 Average Drift", f"{avg_drift:.4f}")
