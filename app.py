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
    df.reset_index(inplace=True)  # Convert index to column
    return df

df = load_data()

# Clean data
df = df.dropna()
df = df.tail(500)


# ==================================================
# SIDEBAR CONTROLS (Stage 6)
# ==================================================

st.sidebar.header("⚙ Simulation Controls")

pattern = st.sidebar.selectbox(
    "Pattern Type",
    ["Sine Wave", "Random Noise"]
)

amplitude = st.sidebar.slider("Amplitude", 1, 50, 10)
frequency = st.sidebar.slider("Frequency", 1, 10, 3)
drift = st.sidebar.slider("Drift (Trend)", -2.0, 2.0, 0.1)

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
    fig2.add_trace(go.Scatter(x=df["Timestamp"], y=df["High"], name="High"))
    fig2.add_trace(go.Scatter(x=df["Timestamp"], y=df["Low"], name="Low"))
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

    if pattern == "Sine Wave":
        wave = amplitude * np.sin(frequency * t)
    else:
        wave = np.random.normal(0, amplitude, len(t))

    trend = drift * t
    simulated_price = 100 + wave + trend

    fig_sim = go.Figure()
    fig_sim.add_trace(go.Scatter(x=t, y=simulated_price,
                                 name="Simulated Price"))
    fig_sim.update_layout(title="Simulated Price Movement")
    st.plotly_chart(fig_sim, use_container_width=True)

    # Metrics
    volatility_index = np.std(simulated_price)
    avg_drift = np.mean(np.diff(simulated_price))

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📊 Volatility Index", f"{volatility_index:.2f}")

    with col2:
        st.metric("📈 Average Drift", f"{avg_drift:.4f}")
