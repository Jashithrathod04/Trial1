import streamlit as st
import google.generativeai as genai
from datetime import datetime


# -----------------------
# Configure Gemini API (Streamlit Secrets)
# -----------------------
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-3-flash-preview")

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="ArtRestorer AI",
    page_icon="🎨",
    layout="wide"
)


# ==============================
# CINEMATIC PAINT SPLASH SCREEN
# ==============================

splash_html = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
    margin: 0;
    overflow: hidden;
    background: radial-gradient(circle at center, #2b1d13, #120b07);
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    font-family: Georgia, serif;
}
.splash-container {
    text-align: center;
    position: relative;
}
.brush {
    position: absolute;
    top: 45%;
    left: -20%;
    font-size: 3rem;
    animation: brushMove 2.5s ease-out forwards;
}
.paint-stroke {
    position: absolute;
    top: 50%;
    left: -40%;
    width: 80%;
    height: 80px;
    background: linear-gradient(90deg, #C6A75E, #E0C27B, #C6A75E);
    border-radius: 50px;
    animation: paintSwipe 2.5s ease-out forwards;
}
.title {
    font-size: 3rem;
    color: #C6A75E;
    opacity: 0;
    animation: fadeIn 2s ease forwards;
    animation-delay: 2s;
}
@keyframes brushMove {
    0% { left: -20%; }
    100% { left: 100%; }
}
@keyframes paintSwipe {
    0% { left: -40%; }
    100% { left: 110%; }
}
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
</style>
</head>
<body>
<div class="splash-container">
    <div class="paint-stroke"></div>
    <div class="brush">🖌️</div>
    <div class="title">ArtRestorer AI</div>
</div>
</body>
</html>
"""

if "splash_shown" not in st.session_state:
    components.html(splash_html, height=800)
    time.sleep(3)
    st.session_state.splash_shown = True
    st.rerun()
# -----------------------
# -----------------------
st.markdown("""
<style>

/* Historic Background Image */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1598300053653-9b0c9e0b9d1e?auto=format&fit=crop&w=1920&q=80");
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
}

/* Elegant parchment overlay for readability */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(245, 239, 224, 0);
    z-index: 0;
}

/* Keep content above overlay */
.main > div {
    position: relative;
    z-index: 1;
}

/* Typography – Museum Style */
html, body, [class*="css"] {
    font-family: 'Georgia', serif;
    color: #2f2a24;
}

/* ===== PREMIUM DASHBOARD CONTAINER ===== */
.dashboard-container {
    padding: 3rem;
    border-radius: 22px;
    background: linear-gradient(145deg, rgba(40,25,20,0.95), rgba(70,45,35,0.95));
    backdrop-filter: blur(10px);
    box-shadow: 0 0 40px rgba(0,0,0,0.6);
    border: 1px solid rgba(198,167,94,0.4);
    margin-bottom: 2.5rem;
    text-align: center;
}

/* ===== TITLE ===== */
.dashboard-title {
    font-size: 2.4rem;
    font-weight: 700;
    color: #C6A75E;
    letter-spacing: 1px;
    text-shadow: 0 0 15px rgba(198,167,94,0.5);
}

/* ===== SUBTITLE ===== */
.dashboard-subtitle {
    margin-top: 0.8rem;
    font-size: 1.05rem;
    color: #f5e6d3;
    opacity: 0.9;
}

/* ===== METRIC CARDS ===== */
.metric-box {
    padding: 1.6rem;
    border-radius: 16px;
    background: rgba(50,30,20,0.95);
    box-shadow: 0 6px 25px rgba(0,0,0,0.5);
    text-align: center;
    transition: all 0.3s ease;
    border: 1px solid rgba(198,167,94,0.2);
}

.metric-box h4 {
    color: #C6A75E;
    margin-bottom: 0.6rem;
}

.metric-box p {
    color: #f5e6d3;
}

.metric-box:hover {
    transform: translateY(-6px);
    border: 1px solid #C6A75E;
    box-shadow: 0 0 25px rgba(198,167,94,0.5);
}

.metric-box:hover {
    transform: translateY(-4px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.12);
}


/* ===== Animated Gold Glow Title ===== */
@keyframes goldGlow {
    0% { text-shadow: 0 0 10px rgba(198,167,94,0.4); }
    50% { text-shadow: 0 0 25px rgba(198,167,94,0.9); }
    100% { text-shadow: 0 0 10px rgba(198,167,94,0.4); }
}

.dashboard-title {
    font-size: 2.6rem;
    font-weight: 700;
    color: #C6A75E;
    letter-spacing: 1.5px;
    animation: goldGlow 3s ease-in-out infinite;
}
/* Tabs */
/* ===== Glass + Gold Tabs ===== */
div[data-baseweb="tab-list"] {
    background: rgba(40,25,20,0.6);
    backdrop-filter: blur(12px);
    border-radius: 18px;
    padding: 6px;
    border: 1px solid rgba(198,167,94,0.3);
    box-shadow: 0 0 20px rgba(0,0,0,0.5);
}

/* Default tab */
button[data-baseweb="tab"] {
    font-weight: 600;
    color: #f5e6d3;
    border-radius: 12px;
    transition: all 0.3s ease;
}

/* Hover effect */
button[data-baseweb="tab"]:hover {
    background: rgba(198,167,94,0.15);
    color: #C6A75E;
}

/* Active tab */
button[data-baseweb="tab"][aria-selected="true"] {
    background: linear-gradient(145deg, #C6A75E, #8C6B2F) !important;
    color: black !important;
    border-radius: 12px;
    box-shadow: 0 0 15px rgba(198,167,94,0.6);
}

/* Buttons */
/* ===== Glowing Gold Buttons ===== */

@keyframes buttonGlow {
    0% { box-shadow: 0 0 10px rgba(198,167,94,0.3); }
    50% { box-shadow: 0 0 25px rgba(198,167,94,0.8); }
    100% { box-shadow: 0 0 10px rgba(198,167,94,0.3); }
}

.stButton > button {
    background-color: #6b4f3b;
    color: white;
    border-radius: 10px;
    padding: 0.6rem 1.5rem;
    font-weight: 600;
    background: linear-gradient(145deg, #C6A75E, #8C6B2F);
    color: black;
    border-radius: 12px;
    padding: 0.7rem 1.6rem;
    font-weight: 700;
    border: none;
    transition: all 0.3s ease;
    animation: buttonGlow 3s ease-in-out infinite;
}

.stButton > button:hover {
    background-color: #4b3621;
    transform: scale(1.06);
    box-shadow: 0 0 35px rgba(198,167,94,1);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: rgba(101, 67, 33, 0.95);
}
/* ===== Sidebar Wood Texture ===== */
section[data-testid="stSidebar"] {
    background-image: url("https://images.pexels.com/photos/326333/pexels-photo-326333.jpeg?auto=compress&cs=tinysrgb&w=1200");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Dark overlay for readability */
section[data-testid="stSidebar"]::before {
    content: "";
    position: absolute;
    inset: 0;
    background: rgba(50, 30, 20, 0.75);
    z-index: 0;
}

/* Keep sidebar content above overlay */
section[data-testid="stSidebar"] > div {
    position: relative;
    z-index: 1;
}

/* Sidebar text styling */
section[data-testid="stSidebar"] * {
    color: #f5e6d3 !important;
    font-family: 'Georgia', serif;
}

/* Sidebar sliders and inputs styling */
section[data-testid="stSidebar"] .stSlider label,
section[data-testid="stSidebar"] .stRadio label {
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


# -----------------------
# Elegant Dashboard Header
# -----------------------

st.markdown("""
<div class="dashboard-container">
    <div class="dashboard-title">🎨 ArtRestorer AI</div>
    <div class="dashboard-subtitle">
        AI-Powered Cultural Heritage Restoration Assistant<br>
        This system uses Generative AI to simulate culturally sensitive and historically informed art restoration recommendations.
    </div>
</div>
""", unsafe_allow_html=True)

# Dashboard Metrics Row
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-box">
        <h4>🤖 AI Engine</h4>
        <p><b>Gemini 3 Flash Preview</b></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-box">
        <h4>🎯 System Mode</h4>
        <p><b>Cultural Restoration Analysis</b></p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-box">
        <h4>⚡ Status</h4>
        <p><b>Operational</b></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<hr style="border: none; height: 1px; 
background: linear-gradient(to right, transparent, #C6A75E, transparent); 
margin: 3rem 0;">
""", unsafe_allow_html=True)
# -----------------------
# Tabs
# -----------------------
tab1, tab2 = st.tabs(["🎨 Restoration Generator", "🕓 Recent Restoration History"])

# =======================
# TAB 1 — GENERATOR
# =======================
with tab1:

    st.subheader("AI-Powered Cultural Heritage Restoration Assistant")

    st.markdown("""
    This system uses Generative AI to simulate culturally sensitive and historically informed
    art restoration recommendations.
    """)

    # Sidebar Settings
    st.sidebar.header("⚙️ Restoration Settings")

    temperature = st.sidebar.slider(
        "Creativity Level (Temperature)",
        0.0, 1.0, 0.3, 0.1
    )

    output_type = st.sidebar.radio(
        "Output Type",
        [
            "Full Restoration Report",
            "Restoration Strategy Only",
            "Cultural Interpretation",
            "Visitor-Friendly Summary"
        ]
    )

    show_prompt = st.sidebar.checkbox("Show Generated Prompt")

    st.header("🖌 Artwork Details")

    col1, col2 = st.columns(2)

    with col1:
        artwork_type = st.selectbox(
            "Artwork Type",
            [
                "Oil Painting",
                "Mural",
                "Miniature Painting",
                "Stone Sculpture",
                "Manuscript",
                "Tapestry",
                "Woodblock Print",
                "Temple Carving"
            ]
        )

        art_period = st.selectbox(
            "Art Period",
            [
                "Renaissance",
                "Mughal",
                "Gothic",
                "Medieval",
                "Edo Period",
                "Ancient Mayan",
                "South Asian Classical",
                "Abstract Expressionist"
            ]
        )

    with col2:
        artist_name = st.text_input("Artist (Optional)")
        damage_description = st.text_area(
            "Describe the Damage",
            height=150
        )

    generate_button = st.button("🔍 Generate Restoration Plan")

    def create_prompt():
        section_instruction = ""

        if output_type == "Restoration Strategy Only":
            section_instruction = "Provide only the restoration strategy section."
        elif output_type == "Cultural Interpretation":
            section_instruction = "Focus only on historical and cultural interpretation."
        elif output_type == "Visitor-Friendly Summary":
            section_instruction = "Provide only a simplified explanation suitable for museum visitors."
        else:
            section_instruction = """
Provide a structured report including:
1. Restoration Strategy
2. Historical & Cultural Context
3. Material and Technique Recommendations
4. Ethical Considerations
5. Visitor-Friendly Explanation
"""

        prompt = f"""
You are an expert art historian and conservation specialist.

Artwork Type: {artwork_type}
Art Period: {art_period}
Artist: {artist_name if artist_name else "Unknown"}
Damage Description: {damage_description}

{section_instruction}

Ensure the response is culturally sensitive, historically grounded,
and avoids speculative fabrication beyond reasonable art historical inference.
"""
        return prompt

    if generate_button:

        if not damage_description.strip():
            st.warning("Please describe the damage before generating.")
        else:
            prompt = create_prompt()

            try:
                with st.spinner("Analyzing artwork and generating restoration strategy..."):
                    response = model.generate_content(
                        prompt,
                        generation_config={
                            "temperature": temperature,
                            "top_p": 0.95,
                            "top_k": 40,
                            "max_output_tokens": 2048,
                        }
                    )

                result = response.text

                st.success("Restoration Plan Generated Successfully!")
                st.subheader("📜 AI Restoration Output")
                st.write(result)

                if show_prompt:
                    st.subheader("🧠 Generated Prompt")
                    st.code(prompt)

                # Save History
                if "history" not in st.session_state:
                    st.session_state.history = []

                st.session_state.history.append({
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "artwork_type": artwork_type,
                    "period": art_period,
                    "damage": damage_description,
                    "output": result
                })

            except Exception as e:
                st.error(f"Error generating content: {e}")


# =======================
# TAB 2 — HISTORY
# =======================
with tab2:

    st.subheader("🕓 Recent Restoration History")

    if "history" not in st.session_state or not st.session_state.history:
        st.info("No restoration history yet. Generate a report first.")
    else:
        for item in reversed(st.session_state.history[-10:]):
            with st.expander(f"{item['timestamp']} — {item['artwork_type']} ({item['period']})"):
                st.write("**Damage Description:**")
                st.write(item["damage"])
                st.write("**AI Output:**")
                st.write(item["output"])
