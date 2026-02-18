import streamlit as st
import time
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Farma Buddy 🌱",
    page_icon="🌿",
    layout="wide"
)

if "splash_done" not in st.session_state:
    st.session_state.splash_done = False

# ---------------- SPLASH SCREEN ----------------
if not st.session_state.splash_done:

    splash_html = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>

    body {
        margin: 0;
        overflow: hidden;
        height: 100vh;
        background: linear-gradient(180deg, #e8f5e9 0%, #c8e6c9 40%, #a5d6a7 100%);
        font-family: 'Segoe UI', sans-serif;
        position: relative;
    }

    /* Subtle animated gradient overlay */
    .gradient-overlay {
        position: absolute;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.4), transparent 60%);
        animation: moveGradient 12s ease-in-out infinite alternate;
    }

    /* Floating light particles */
    .particle {
        position: absolute;
        width: 8px;
        height: 8px;
        background: rgba(255,255,255,0.6);
        border-radius: 50%;
        animation: floatParticle 10s linear infinite;
    }

    .p1 { top: 20%; left: 10%; animation-delay: 0s; }
    .p2 { top: 40%; left: 80%; animation-delay: 2s; }
    .p3 { top: 70%; left: 30%; animation-delay: 4s; }
    .p4 { top: 60%; left: 60%; animation-delay: 6s; }

    /* Elegant Sun Glow */
    .sun {
        position: absolute;
        top: 12%;
        right: 12%;
        width: 120px;
        height: 120px;
        background: radial-gradient(circle, #fff176 40%, transparent 70%);
        border-radius: 50%;
        animation: pulseSun 6s ease-in-out infinite;
    }

    /* Center Content */
    .container {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        z-index: 5;
    }

    .logo {
        font-size: 85px;
        animation: zoomFade 2s ease-out;
    }

    .app-name {
        font-size: 48px;
        font-weight: 600;
        color: #1b5e20;
        margin-top: 10px;
        animation: fadeIn 3s ease-in-out;
    }

    .tagline {
        font-size: 18px;
        color: #2e7d32;
        margin-top: 10px;
        letter-spacing: 1px;
        animation: fadeIn 4s ease-in-out;
    }

    .progress-bar {
        width: 300px;
        height: 5px;
        background: rgba(0,0,0,0.1);
        margin: 30px auto;
        border-radius: 10px;
        overflow: hidden;
    }

    .progress-fill {
        height: 100%;
        width: 0%;
        background: linear-gradient(90deg, #1b5e20, #43a047);
        animation: loadProgress 5s linear forwards;
    }

    /* Animations */
    @keyframes zoomFade {
        0% {transform: scale(0.8); opacity: 0;}
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

    @keyframes floatParticle {
        0% {transform: translateY(0px);}
        50% {transform: translateY(-20px);}
        100% {transform: translateY(0px);}
    }

    @keyframes pulseSun {
        0% {transform: scale(1); opacity: 0.8;}
        50% {transform: scale(1.1); opacity: 1;}
        100% {transform: scale(1); opacity: 0.8;}
    }

    @keyframes moveGradient {
        0% {transform: translate(-10%, -10%);}
        100% {transform: translate(10%, 10%);}
    }

    </style>
    </head>

    <body>

        <div class="gradient-overlay"></div>

        <div class="sun"></div>

        <div class="particle p1"></div>
        <div class="particle p2"></div>
        <div class="particle p3"></div>
        <div class="particle p4"></div>

        <div class="container">
            <div class="logo">🌾</div>
            <div class="app-name">Farma Buddy</div>
            <div class="tagline">Smart Farming. Smarter Future.</div>

            <div class="progress-bar">
                <div class="progress-fill"></div>
            </div>
        </div>

    </body>
    </html>
    """

    components.html(splash_html, height=750)
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
