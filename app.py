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
        background: linear-gradient(to top, #a8e6a3 40%, #d4f8d4 100%);
        height: 100vh;
        font-family: Arial, sans-serif;
        position: relative;
    }

    /* Center Content */
    .container {
        position: absolute;
        top: 45%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        z-index: 5;
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
        margin: 30px auto;
        border-radius: 10px;
        overflow: hidden;
    }

    .progress-fill {
        height: 100%;
        width: 0%;
        background: #1b5e20;
        animation: loadProgress 5s linear forwards;
    }

    /* Sun */
    .sun {
        position: absolute;
        top: 10%;
        right: 10%;
        width: 100px;
        height: 100px;
        background: #ffeb3b;
        border-radius: 50%;
        box-shadow: 0 0 40px #ffeb3b;
        animation: rotateSun 10s linear infinite;
    }

    .sun::before {
        content: "";
        position: absolute;
        top: -20px;
        left: -20px;
        width: 140px;
        height: 140px;
        border-radius: 50%;
        border: 4px dashed rgba(255, 235, 59, 0.6);
    }

    /* Clouds */
    .cloud {
        position: absolute;
        font-size: 50px;
        animation: moveCloud 20s linear infinite;
    }

    .cloud1 { top: 15%; left: -10%; }
    .cloud2 { top: 25%; left: -30%; animation-delay: 10s; }

    /* Ground */
    .ground {
        position: absolute;
        bottom: 0;
        width: 100%;
        height: 120px;
        background: #4caf50;
    }

    /* Crops */
    .crop {
        position: absolute;
        bottom: 120px;
        font-size: 40px;
        animation: growCrop 4s ease-in-out forwards;
        opacity: 0;
    }

    .crop1 { left: 30%; animation-delay: 1s; }
    .crop2 { left: 45%; animation-delay: 2s; }
    .crop3 { left: 60%; animation-delay: 3s; }

    /* Floating Leaves */
    .leaf {
        position: absolute;
        font-size: 30px;
        animation: floatLeaf 6s ease-in-out infinite;
    }

    .leaf1 { left: 20%; top: 30%; }
    .leaf2 { left: 70%; top: 40%; animation-delay: 2s; }

    /* Animations */
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

    @keyframes moveCloud {
        0% {transform: translateX(0);}
        100% {transform: translateX(150vw);}
    }

    @keyframes growCrop {
        0% {transform: scaleY(0); opacity: 0;}
        100% {transform: scaleY(1); opacity: 1;}
    }

    @keyframes floatLeaf {
        0% {transform: translateY(0);}
        50% {transform: translateY(20px);}
        100% {transform: translateY(0);}
    }

    @keyframes rotateSun {
        0% {transform: rotate(0deg);}
        100% {transform: rotate(360deg);}
    }

    </style>
    </head>

    <body>

        <div class="sun"></div>

        <div class="cloud cloud1">☁️</div>
        <div class="cloud cloud2">☁️</div>

        <div class="leaf leaf1">🍃</div>
        <div class="leaf leaf2">🌿</div>

        <div class="container">
            <div class="logo">🌾</div>
            <div class="app-name">Farma Buddy</div>
            <div class="tagline">Smart Farming. Smarter Future.</div>

            <div class="progress-bar">
                <div class="progress-fill"></div>
            </div>
        </div>

        <div class="crop crop1">🌱</div>
        <div class="crop crop2">🌿</div>
        <div class="crop crop3">🌾</div>

        <div class="ground"></div>

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
