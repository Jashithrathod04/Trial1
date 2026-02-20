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

# -----------------------
# -----------------------
st.markdown("""
<style>

/* Historic Background Image */
.stApp {
    background-image: url("https://images.pexels.com/photos/30254081/pexels-photo-30254081.jpeg");
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
}

/* Elegant parchment overlay for readability */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(245, 239, 224, 0.90);
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

/* Dashboard container */
.dashboard-container {
    padding: 2rem;
    border-radius: 18px;
    background-color: rgba(60, 40, 30, 0.95);
    backdrop-filter: blur(6px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
    margin-bottom: 2rem;
}

/* Metric cards */
.metric-box {
    padding: 1.2rem;
    border-radius: 14px;
    background: rgba(92, 64, 51, 0.95);
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    text-align: center;
    transition: 0.3s ease;
}

.metric-box:hover {
    transform: translateY(-4px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.12);
}

/* Tabs */
div[data-baseweb="tab-list"] {
    background-color: rgba(92, 72, 52, 0.20);
    border-radius: 12px;
    padding: 4px;
}

button[data-baseweb="tab"] {
    font-weight: 600;
    color: #5c4834;
}

button[data-baseweb="tab"][aria-selected="true"] {
    background-color: #5c4834 !important;
    color: white !important;
    border-radius: 10px;
}

/* Buttons */
.stButton > button {
    background-color: #6b4f3b;
    color: white;
    border-radius: 10px;
    padding: 0.6rem 1.5rem;
    font-weight: 600;
    border: none;
}

.stButton > button:hover {
    background-color: #4b3621;
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
        <h4>🤖 Model</h4>
        <p><b>Gemini 3 Flash Preview</b></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-box">
        <h4>🎯 Mode</h4>
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

st.divider()
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
