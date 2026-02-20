import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from datetime import datetime

# -----------------------
# Load API Key
# -----------------------
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use Gemini 1.5 Pro
model = genai.GenerativeModel("gemini-1.5-pro")

# -----------------------
# App Configuration
# -----------------------
st.set_page_config(
    page_title="ArtRestorer AI",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 ArtRestorer AI")
st.subheader("AI-Powered Cultural Heritage Restoration Assistant")

st.markdown("""
This system uses Generative AI to simulate culturally sensitive and historically informed
art restoration recommendations.
""")

# -----------------------
# Sidebar Controls
# -----------------------
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

# -----------------------
# Input Section
# -----------------------
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

# -----------------------
# Prompt Template
# -----------------------
def create_prompt():
    base_prompt = f"""
You are an expert art historian and conservation specialist.

Artwork Type: {artwork_type}
Art Period: {art_period}
Artist: {artist_name if artist_name else "Unknown"}
Damage Description: {damage_description}

Provide a structured restoration analysis including:

1. Restoration Strategy
2. Historical & Cultural Context
3. Material and Technique Recommendations
4. Ethical Considerations
5. Visitor-Friendly Explanation

Ensure the response is culturally sensitive, historically accurate,
and avoids speculative fabrication beyond reasonable art historical inference.
"""
    return base_prompt

# -----------------------
# Generate Response
# -----------------------
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
                        "top_p": 0.9,
                        "max_output_tokens": 2048
                    }
                )

            result = response.text

            st.success("Restoration Plan Generated Successfully!")

            if show_prompt:
                st.subheader("🧠 Generated Prompt")
                st.code(prompt)

            st.subheader("📜 AI Restoration Report")
            st.write(result)

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

# -----------------------
# History Section
# -----------------------
if "history" in st.session_state and st.session_state.history:
    st.header("🕓 Restoration History")

    for item in reversed(st.session_state.history[-5:]):
        with st.expander(f"{item['timestamp']} — {item['artwork_type']} ({item['period']})"):
            st.write("**Damage:**", item["damage"])
            st.write("**AI Output:**")
            st.write(item["output"])
