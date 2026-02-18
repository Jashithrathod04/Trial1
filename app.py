import streamlit as st
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Farma Buddy 🌱",
    page_icon="🌿",
    layout="wide"
)

# ---------------- SESSION CONTROL ----------------
if "splash_done" not in st.session_state:
    st.session_state.splash_done = False

# ---------------- SPLASH SCREEN ----------------
if not st.session_state.splash_done:

    st.markdown("""
    <style>

    /* Center container */
    .splash-container {
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background: linear-gradient(135deg, #d4f8d4, #a8e6a3);
        border-radius: 10px;
    }

    .logo {
        font-size: 90px;
        animation: zoomBounce 2s ease-in-out;
    }

    .app-name {
        font-size: 48px;
        font-weight: bold;
        color: #1b5e20;
        margin-top: 10px;
        animation: fadeIn 3s ease-in-out;
    }

    .tagline {
        font-size: 20px;
        color: #2e7d32;
        margin-top: 10px;
        animation: fadeIn 4s ease-in-out;
    }

    .progress-bar {
        width: 300px;
        height: 6px;
        background: #c8e6c9;
        margin-top: 30px;
        border-radius: 10px;
        overflow: hidden;
    }

    .progress-fill {
        height: 100%;
        width: 0%;
        background: #1b5e20;
        animation: loadProgress 5s linear forwards;
    }

    .leaf {
        position: absolute;
        font-size: 30px;
        animation: floatLeaf 6s linear infinite;
    }

    .leaf1 { left: 20%; top: 10%; animation-delay: 0s; }
    .leaf2 { left: 70%; top: 20%; animation-delay: 2s; }
    .leaf3 { left: 40%; top: 5%; animation-delay: 4s; }

    @keyframes zoomBounce {
        0% {transform: scale(0.5); opacity: 0;}
        50% {transform: scale(1.2);}
        100% {transform: scale(1); opacity: 1;}
    }

    @keyframes fadeIn {
        0% {opacity: 0;}
        100% {opacity: 1;}
    }

    @keyframes loadProgress {
        0% {width: 0%;}
        100% {width: 100%;}
    }

    @keyframes floatLeaf {
        0% {transform: translateY(0px);}
        50% {transform: translateY(20px);}
        100% {transform: translateY(0px);}
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="splash-container">

        <div class="leaf leaf1">🌿</div>
        <div class="leaf leaf2">🍃</div>
        <div class="leaf leaf3">🌱</div>

        <div class="logo">🌾</div>
        <div class="app-name">Farma Buddy</div>
        <div class="tagline">Smart Farming. Smarter Future.</div>

        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>

    </div>
    """, unsafe_allow_html=True)

    time.sleep(5)
    st.session_state.splash_done = True
    st.rerun()

# ---------------- MAIN APP ----------------

st.markdown("<h1 style='color:#1b5e20;'>Welcome to Farma Buddy 🌱</h1>", unsafe_allow_html=True)
st.write("Your AI-powered smart farming ecosystem.")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.success("🌦 Weather Intelligence")
    st.write("Crop-friendly forecasting system.")

with col2:
    st.info("🌿 AI Crop Advisory")
    st.write("Personalized yield optimization.")

with col3:
    st.warning("💧 Smart Irrigation Planner")
    st.write("Efficient water usage powered by AI.")

st.divider()

st.markdown("### 📊 Farm Analytics Dashboard")
st.write("Integrate your AI modules here.")

