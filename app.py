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
    .hero {
        text-align: center;
        padding-top: 120px;
    }

    .headline {
        font-size: 52px;
        font-weight: 700;
        color: #1b5e20;
    }

    .subtext {
        font-size: 20px;
        color: #2e7d32;
        margin-top: 20px;
    }

    .stButton > button {
        background-color: #2e7d32;
        color: white;
        padding: 12px 28px;
        font-size: 18px;
        border-radius: 10px;
        border: none;
        transition: 0.3s ease;
    }

    .stButton > button:hover {
        background-color: #1b5e20;
        transform: scale(1.05);
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="hero">', unsafe_allow_html=True)

    st.markdown('<div class="headline">AI-Powered Smart Farming</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtext">Optimize yield. Reduce waste. Make data-driven decisions.</div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("🌿 Get Started"):
            st.session_state.page = "dashboard"
            st.rerun()

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

