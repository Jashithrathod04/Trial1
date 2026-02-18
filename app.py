import streamlit as st
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Farma Buddy 🌱",
    page_icon="🌿",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.block-container {
    padding-top: 0rem;
}

/* SPLASH SCREEN */
#splash {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #d4f8d4, #a8e6a3, #e8fbe8);
    overflow: hidden;
    z-index: 9999;
    animation: fadeOut 2s ease-in-out 5s forwards;
}

/* Center Content */
.splash-content {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
}

/* Logo Animation */
.logo {
    font-size: 80px;
    animation: bounceZoom 3s ease-in-out;
}

/* App Name */
.app-name {
    font-size: 48px;
    font-weight: bold;
    color: #1b5e20;
    margin-top: 10px;
    animation: fadeSlide 3s ease-in-out;
}

/* Tagline */
.tagline {
    font-size: 22px;
    color: #2e7d32;
    margin-top: 15px;
    animation: fadeSlide 4s ease-in-out;
}

/* Progress Bar */
.progress-bar {
    width: 300px;
    height: 6px;
    background: #c8e6c9;
    margin: 25px auto;
    border-radius: 5px;
    overflow: hidden;
}

.progress-fill {
    height: 100%;
    width: 0%;
    background: #2e7d32;
    animation: loadProgress 5s linear forwards;
}

/* Floating Leaves */
.leaf {
    position: absolute;
    font-size: 30px;
    animation: floatLeaf 8s linear infinite;
}

.leaf:nth-child(1) { left: 10%; animation-delay: 0s; }
.leaf:nth-child(2) { left: 30%; animation-delay: 2s; }
.leaf:nth-child(3) { left: 60%; animation-delay: 4s; }
.leaf:nth-child(4) { left: 80%; animation-delay: 1s; }

/* Sun Glow */
.sun {
    position: absolute;
    top: 10%;
    right: 10%;
    font-size: 80px;
    animation: pulseSun 4s infinite;
}

/* Clouds */
.cloud {
    position: absolute;
    top: 20%;
    font-size: 50px;
    animation: moveCloud 20s linear infinite;
}

/* ANIMATIONS */
@keyframes bounceZoom {
    0% {transform: scale(0.5); opacity: 0;}
    50% {transform: scale(1.2);}
    100% {transform: scale(1); opacity: 1;}
}

@keyframes fadeSlide {
    0% {opacity: 0; transform: translateY(20px);}
    100% {opacity: 1; transform: translateY(0);}
}

@keyframes loadProgress {
    0% {width: 0%;}
    100% {width: 100%;}
}

@keyframes floatLeaf {
    0% {top: -10%;}
    100% {top: 110%;}
}

@keyframes pulseSun {
    0% {transform: scale(1);}
    50% {transform: scale(1.1);}
    100% {transform: scale(1);}
}

@keyframes moveCloud {
    0% {left: -20%;}
    100% {left: 120%;}
}

@keyframes fadeOut {
    0% {opacity: 1;}
    100% {opacity: 0; visibility: hidden;}
}

</style>
""", unsafe_allow_html=True)

# ---------------- SPLASH HTML ----------------
st.markdown("""
<div id="splash">

    <div class="sun">☀️</div>

    <div class="cloud" style="left:-20%;">☁️</div>

    <div class="leaf">🍃</div>
    <div class="leaf">🌿</div>
    <div class="leaf">🍀</div>
    <div class="leaf">🌱</div>

    <div class="splash-content">
        <div class="logo">🌾</div>
        <div class="app-name">Farma Buddy</div>
        <div class="tagline">Smart Farming. Smarter Future.</div>

        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>
    </div>

</div>
""", unsafe_allow_html=True)

# Wait 5 seconds
time.sleep(5)

# ---------------- MAIN APP ----------------

st.markdown("<h1 style='color:#1b5e20;'>Welcome to Farma Buddy 🌱</h1>", unsafe_allow_html=True)
st.write("Your AI-powered smart farming ecosystem.")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.success("🌦 Weather Intelligence")
    st.write("Smart crop-aligned forecasting system.")

with col2:
    st.info("🌿 AI Crop Advisory")
    st.write("Personalized yield optimization insights.")

with col3:
    st.warning("💧 Smart Irrigation Planner")
    st.write("Water efficiency powered by AI.")

st.divider()

st.markdown("### 📊 Advanced Farm Analytics Dashboard")
st.write("Integrate your AI models here.")



