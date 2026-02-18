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

/* Remove default padding */
.block-container {
    padding-top: 0rem;
}

/* Splash Screen Full Page */
#splash {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #d4f8d4, #a8e6a3);
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    z-index: 9999;
    animation: fadeOut 2s ease-in-out 3s forwards;
}

/* Logo Animation */
.logo {
    font-size: 60px;
    animation: zoomIn 2s ease-in-out;
}

/* App Name */
.app-name {
    font-size: 42px;
    font-weight: bold;
    color: #1b5e20;
    margin-top: 10px;
    animation: fadeIn 2s ease-in-out;
}

/* Tagline */
.tagline {
    font-size: 20px;
    color: #2e7d32;
    margin-top: 10px;
    animation: fadeIn 3s ease-in-out;
}

/* Animations */
@keyframes zoomIn {
    0% {transform: scale(0.5); opacity: 0;}
    100% {transform: scale(1); opacity: 1;}
}

@keyframes fadeIn {
    0% {opacity: 0;}
    100% {opacity: 1;}
}

@keyframes fadeOut {
    0% {opacity: 1;}
    100% {opacity: 0; visibility: hidden;}
}

</style>
""", unsafe_allow_html=True)

# ---------------- SPLASH SCREEN ----------------
st.markdown("""
<div id="splash">
    <div class="logo">🌾</div>
    <div class="app-name">Farma Buddy</div>
    <div class="tagline">Smart Farming. Smarter Future.</div>
</div>
""", unsafe_allow_html=True)

# Small delay to allow animation
time.sleep(3)

# ---------------- MAIN APP ----------------

st.markdown("<h1 style='color:#1b5e20;'>Welcome to Farma Buddy 🌱</h1>", unsafe_allow_html=True)
st.write("Your AI-powered smart farming assistant.")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🌦 Weather Insights")
    st.write("Get real-time crop-friendly forecasts.")

with col2:
    st.success("🌿 Crop Advisory")
    st.write("AI-powered recommendations for better yield.")

with col3:
    st.warning("💧 Irrigation Planner")
    st.write("Optimize water usage intelligently.")

st.divider()

st.markdown("### 📊 Farm Analytics Dashboard")
st.write("Add your AI modules here.")

