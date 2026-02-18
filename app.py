import streamlit as st
import time
import streamlit.components.v1 as components

st.set_page_config(page_title="Farma Buddy", layout="wide")

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "splash"

# ---------------- SPLASH SCREEN ----------------
if st.session_state.page == "splash":

    splash_html = """
    <style>
    body {
        margin: 0;
        overflow: hidden;
        background: linear-gradient(to bottom, #e8f5e9, #c8e6c9);
        font-family: 'Segoe UI', sans-serif;
    }

    .container {
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }

    .logo {
        font-size: 90px;
        animation: logoPulseBounce 4s ease-in-out infinite;
    }

    @keyframes logoPulseBounce {
        0% { transform: scale(0.8); }
        20% { transform: scale(1.2); }
        40% { transform: scale(0.9); }
        60% { transform: scale(1.15); }
        75% { transform: scale(0.95); }
        90% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    .app-name {
        font-size: 48px;
        font-weight: 600;
        color: #1b5e20;
        margin-top: 20px;
    }
    </style>

    <div class="container">
        <div class="logo">🌱</div>
        <div class="app-name">Farma Buddy</div>
    </div>
    """

    components.html(splash_html, height=700)

    time.sleep(4)
    st.session_state.page = "landing"
    st.rerun()


# ---------------- LANDING SCREEN ----------------
elif st.session_state.page == "landing":

    st.markdown("""
    <style>

    /* Full page gradient background */
    .main {
        background: linear-gradient(135deg, #e8f5e9, #a5d6a7);
    }

    .glass-wrapper {
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 60px;
        width: 700px;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }

    .headline {
        font-size: 48px;
        font-weight: 700;
        color: #1b5e20;
    }

    .subtext {
        font-size: 20px;
        color: #2e7d32;
        margin-top: 20px;
        line-height: 1.6;
    }

    .stButton > button {
        background: linear-gradient(90deg, #2e7d32, #43a047);
        color: white;
        padding: 14px 32px;
        font-size: 18px;
        border-radius: 12px;
        border: none;
        transition: 0.3s ease;
        margin-top: 30px;
    }

    .stButton > button:hover {
        transform: scale(1.07);
        box-shadow: 0 6px 20px rgba(0,0,0,0.2);
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="glass-wrapper">', unsafe_allow_html=True)
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.markdown('<div class="headline">AI-Powered Smart Farming</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtext">Empowering farmers with intelligent insights, predictive analytics, and sustainable solutions for a smarter agricultural future.</div>', unsafe_allow_html=True)

    if st.button("🌿 Get Started"):
        st.session_state.page = "dashboard"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ---------------- DASHBOARD ----------------
elif st.session_state.page == "dashboard":

    st.title("🌾 Farma Buddy Dashboard")
    st.success("Welcome to your AI Farming Assistant")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🌦 Weather Intelligence")
        st.write("Real-time crop-aligned forecasting.")

    with col2:
        st.success("🌿 AI Crop Advisory")
        st.write("Personalized yield optimization insights.")

    with col3:
        st.warning("💧 Smart Irrigation")
        st.write("Optimize water usage with AI.")
