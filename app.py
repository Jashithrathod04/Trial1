import streamlit as st

st.set_page_config(page_title="Farma Buddy", layout="centered")

# Splash screen HTML + CSS + JS
splash_html = """
<style>

html, body, [data-testid="stAppViewContainer"] {
    background-color: #e8f5e9;
    margin: 0;
    padding: 0;
    overflow: hidden;
    font-family: 'Segoe UI', sans-serif;
}

/* Splash Container */
.splash-container {
    position: fixed;
    width: 100%;
    height: 100vh;
    background: linear-gradient(to bottom, #e8f5e9, #c8e6c9);
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

/* Sun Rays */
.sun {
    position: absolute;
    top: 15%;
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background: radial-gradient(circle, #a5d6a7 40%, transparent 70%);
    animation: rotateSun 10s linear infinite;
    opacity: 0.4;
}

@keyframes rotateSun {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

/* Logo Animation */
.logo {
    font-size: 90px;
    display: inline-block;
    animation: logoPulseBounce 4s ease-in-out infinite;
}

/* Grow → Shrink → Bounce */
@keyframes logoPulseBounce {

    0%   { transform: scale(0.8); }
    20%  { transform: scale(1.2); }
    40%  { transform: scale(0.9); }
    60%  { transform: scale(1.15); }
    75%  { transform: scale(0.95); }
    90%  { transform: scale(1.05); }
    100% { transform: scale(1); }

}

/* App Name */
.app-name {
    font-size: 48px;
    font-weight: 600;
    color: #1b5e20;
    margin-top: 20px;
    letter-spacing: 1px;
}

/* Tagline */
.tagline {
    font-size: 18px;
    color: #2e7d32;
    margin-top: 10px;
    opacity: 0.9;
}

/* Floating particles */
.particle {
    position: absolute;
    width: 6px;
    height: 6px;
    background: #81c784;
    border-radius: 50%;
    opacity: 0.6;
    animation: floatUp 6s linear infinite;
}

@keyframes floatUp {
    0% {
        transform: translateY(50px);
        opacity: 0;
    }
    50% {
        opacity: 0.7;
    }
    100% {
        transform: translateY(-200px);
        opacity: 0;
    }
}

/* Fade out animation */
.fade-out {
    animation: fadeOut 1s forwards;
}

@keyframes fadeOut {
    to {
        opacity: 0;
        visibility: hidden;
    }
}

</style>

<div id="splash" class="splash-container">

    <div class="sun"></div>

    <div class="logo">🌱</div>

    <div class="app-name">Farma Buddy</div>

    <div class="tagline">Empowering Farmers with Smart Insights</div>

</div>

<script>

// Create floating particles dynamically
for (let i = 0; i < 20; i++) {
    let particle = document.createElement("div");
    particle.className = "particle";
    particle.style.left = Math.random() * 100 + "vw";
    particle.style.animationDelay = Math.random() * 5 + "s";
    particle.style.animationDuration = 4 + Math.random() * 4 + "s";
    document.body.appendChild(particle);
}

// Hide splash after 5 seconds
setTimeout(function() {
    document.getElementById("splash").classList.add("fade-out");
}, 5000);

</script>
"""

st.markdown(splash_html, unsafe_allow_html=True)

# Main App Content
st.title("🌾 Welcome to Farma Buddy")
st.write("Your intelligent farming assistant is ready!")

st.success("App Loaded Successfully 🚀")
