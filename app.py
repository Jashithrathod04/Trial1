import streamlit as st
import google.generativeai as genai
from datetime import datetime
import time
import streamlit.components.v1 as components
import pandas as pd
import matplotlib.pyplot as plt

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
# FULL SCREEN SPLASH SCREEN
# ==============================

splash_html = """
<!DOCTYPE html>
<html>
<head>
<style>

body {
    margin: 0;
    overflow: hidden;
    background: linear-gradient(145deg, #1a120b, #3b2a1a);
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    font-family: Georgia, serif;
}

/* Container */
.splash-container {
    text-align: center;
    color: #C6A75E;
    animation: fadeIn 2s ease forwards;
}

/* Animated Brush Stroke Line */
.brush-line {
    width: 0;
    height: 3px;
    background: linear-gradient(90deg, transparent, #C6A75E, #E0C27B, #C6A75E, transparent);
    margin: 20px auto;
    animation: drawLine 2.5s ease forwards;
}

/* Title */
.title {
    font-size: 3rem;
    letter-spacing: 2px;
    opacity: 0;
    animation: titleReveal 3s ease forwards;
    animation-delay: 1s;
}

/* Subtitle */
.subtitle {
    font-size: 1rem;
    margin-top: 1rem;
    color: #f5e6d3;
    opacity: 0;
    animation: fadeIn 3s ease forwards;
    animation-delay: 2s;
}

/* Animations */

@keyframes drawLine {
    0% { width: 0; }
    100% { width: 60%; }
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes titleReveal {
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
}

</style>
</head>
<body>

<div class="splash-container">
    <div class="title">🎨 ArtRestorer AI</div>
    <div class="brush-line"></div>
    <div class="subtitle">
        Preserving Cultural Heritage Through Artificial Intelligence
    </div>
</div>

</body>
</html>
"""



if "splash_shown" not in st.session_state:
    components.html(splash_html, height=800)
    time.sleep(3)
    st.session_state.splash_shown = True
    st.rerun()

st.empty()
# -----------------------


if "page" not in st.session_state:
    st.session_state.page = "landing"



if st.session_state.page == "landing":

    import streamlit.components.v1 as components

# -----------------------------
# CINEMATIC TOP SECTION
# -----------------------------


    landing_block = """
    <html>
    <head>
    <style>
    body {
        margin: 0;
        overflow: hidden;
        background: #000000;
        font-family: Georgia, serif;
    }
    
    /* PARTICLES */
    .particles {
        position: absolute;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle, rgba(255,215,0,0.12) 1px, transparent 1px);
        background-size: 70px 70px;
        animation: moveParticles 60s linear infinite;
        z-index: 1;
    }
    
    @keyframes moveParticles {
        from { background-position: 0 0; }
        to { background-position: 800px 800px; }
    }
    
    /* CURTAINS */
    .curtain-left, .curtain-right {
        position: absolute;
        top: 0;
        width: 50%;
        height: 100%;
        background: linear-gradient(to bottom, #3a0000, #120000);
        z-index: 3;
    }
    
    .curtain-left {
        left: 0;
        border-right: 4px solid #D4AF37;
        animation: openLeft 3s forwards ease-in-out;
    }
    
    .curtain-right {
        right: 0;
        border-left: 4px solid #D4AF37;
        animation: openRight 3s forwards ease-in-out;
    }
    
    @keyframes openLeft {
        to { transform: translateX(-100%); }
    }
    
    @keyframes openRight {
        to { transform: translateX(100%); }
    }
    
    /* MAIN CONTENT CONTAINER */
    .content {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        z-index: 2;
        width: 85%;
        max-width: 1200px;
        opacity: 0;
        animation: fadeIn 3s forwards;
        animation-delay: 2s;
    }
    
    @keyframes fadeIn {
        to { opacity: 1; }
    }
    
    .title {
        font-size: 4rem;
        color: #D4AF37;
        text-shadow: 0 0 20px #FFD700;
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { text-shadow: 0 0 10px #8B6914; }
        to { text-shadow: 0 0 35px #FFD700; }
    }
    
    .subtitle {
        font-size: 1.4rem;
        color: #E6C97F;
        margin-bottom: 40px;
    }
    
    /* FEATURE CARDS */
    .cards {
        display: flex;
        justify-content: center;
        gap: 25px;
        margin-bottom: 40px;
    }
    
    .card {
        background: rgba(20,20,20,0.85);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #C6A75E;
        width: 30%;
        color: #F5DEB3;
        transition: 0.3s ease;
    }
    
    .card:hover {
        box-shadow: 0 0 20px #D4AF37;
        transform: translateY(-8px);
    }
    
    .card h3 {
        color: #D4AF37;
    }
    
    /* TAGLINE */
    .tagline {
        font-size: 1.5rem;
        color: #D4AF37;
        margin-bottom: 30px;
    }
    
    /* BUTTON */
    .enter-btn {
        padding: 12px 30px;
        font-size: 1rem;
        background: transparent;
        color: #D4AF37;
        border: 2px solid #D4AF37;
        border-radius: 30px;
        cursor: pointer;
        transition: 0.3s ease;
    }
    
    .enter-btn:hover {
        background: #D4AF37;
        color: black;
        box-shadow: 0 0 15px #FFD700;
    }
    </style>
    </head>
    
    <body>
    
    <div class="particles"></div>
    <div class="curtain-left"></div>
    <div class="curtain-right"></div>
    
    <div class="content">
    
        <div class="title">Restora A.I</div>
        <div class="subtitle">AI-Powered Cultural Heritage Restoration Assistant</div>
    
        <div class="cards">
            <div class="card">
                <h3>AI Restoration Analysis</h3>
                <p>Generate culturally sensitive, historically accurate restoration strategies using advanced generative AI models.</p>
            </div>
    
            <div class="card">
                <h3>Cultural Integrity Protection</h3>
                <p>Preserve authenticity while restoring damaged artwork, monuments, and historical artifacts.</p>
            </div>
    
            <div class="card">
                <h3>Restoration Archive</h3>
                <p>Maintain and analyze past restoration records with intelligent tracking and documentation.</p>
            </div>
        </div>
    
        <div class="tagline">Preserve the Past. Restore the Future.</div>
    
    </div>
    
    </body>
    </html>
    """
    
    components.html(landing_block, height=750)
    
    if st.button("🎨 Enter the Gallery", use_container_width=True):

        transition = st.empty()
    
        transition.markdown("""
        <div style="
            position:fixed;
            top:0;
            left:0;
            width:100%;
            height:100%;
            backdrop-filter: blur(10px);
            background: rgba(0,0,0,0.6);
            animation: smoothFade 0.8s ease-in-out forwards;
            z-index:9999;
        ">
        </div>
    
        <style>
        @keyframes smoothFade {
            from {opacity:0;}
            to {opacity:1;}
        }
        </style>
        """, unsafe_allow_html=True)
    
        import time
        time.sleep(1)
    
        st.session_state.page = "signup"
        st.rerun()
    
    st.stop()





# ==============================
# SIGN UP PAGE
# ==============================

if st.session_state.page == "signup":

    st.markdown("""
    <div style="
        background: linear-gradient(145deg, rgba(30,20,15,0.95), rgba(50,35,25,0.95));
        padding: 3rem;
        border-radius: 20px;
        box-shadow: 0 0 40px rgba(0,0,0,0.7);
        text-align: center;
    ">
        <h1 style="color:#C6A75E;">Create Your Restora A.I Account</h1>
        <p style="color:#f5e6d3;">
            Join the cultural restoration intelligence network.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")

    with col2:
        institution = st.text_input("Institution / Organization")
        role = st.selectbox(
            "Role",
            ["Museum Curator", "Art Historian", "Conservation Specialist", "Student", "Researcher"]
        )
        country = st.text_input("Country")

    agree = st.checkbox("I agree to ethical AI restoration guidelines")

    st.divider()

    if st.button("Create Account"):

        if not full_name or not email or not password:
            st.warning("Please complete all required fields.")
        elif not agree:
            st.warning("You must agree to the ethical guidelines.")
        else:
            # Store basic user info
            st.session_state.user = {
                "name": full_name,
                "email": email,
                "role": role,
                "institution": institution,
                "country": country
            }

            st.success("Account Created Successfully!")

             # Create cinematic transition overlay
            transition = st.empty()
        
            transition.markdown("""
            <div style="
                position:fixed;
                top:0;
                left:0;
                width:100%;
                height:100%;
                backdrop-filter: blur(12px);
                background: radial-gradient(circle at center, rgba(0,0,0,0.7), rgba(0,0,0,0.95));
                animation: fadeIn 0.8s ease-in-out forwards;
                z-index:9999;
                display:flex;
                align-items:center;
                justify-content:center;
                color:white;
                font-size:24px;
                font-weight:500;
                letter-spacing:1px;
            ">
                Preparing Your Creative Dashboard...
            </div>
        
            <style>
            @keyframes fadeIn {
                from {opacity:0;}
                to {opacity:1;}
            }
            </style>
            """, unsafe_allow_html=True)
        
            import time
            time.sleep(1.3)
        
            st.session_state.page = "dashboard"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("← Back to Landing"):
        st.session_state.page = "landing"
        st.rerun()

    st.stop()






if st.session_state.page == "dashboard":
    # YOUR EXISTING DASHBOARD CODE HERE

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
    username = st.session_state.get("user", {}).get("name", "Guest")
    st.markdown("""
    <div class="dashboard-container">
        <div class="dashboard-title">
            🎨 Restora AI
        </div>
        <div style="color:#f5e6d3; margin-top:10px;">
            Welcome
        </div>
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
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🎨 Restoration Generator",
    "🕓 Recent Restoration History",
    "🤖 Restora Chat",
    "📊 Restoration Insights",
    "🧾 Restoration Report",
    "💬 User Feedback"
     ])
    
    # =======================
    # TAB 1 — GENERATOR
    # =======================
    with tab1:
    
        

        # ==============================
        


        
    
        
    
    
        st.header("🖌 Artwork Details")

        # Sidebar Settings
        st.sidebar.header("⚙️  Settings")
        st.sidebar.divider()

        if st.sidebar.button("🚪 Sign Out", use_container_width=True):
            # Clear user session
            if "user" in st.session_state:
                del st.session_state["user"]
            
            # Redirect to landing
            st.session_state.page = "landing"
            
            st.rerun()


        # Restoration Settings (Now inside tab)
        # ==============================
        
        st.markdown("### ⚙️ Restoration Settings")
        
        colA, colB = st.columns(2)
        
        with colA:
            temperature = st.slider(
                "Creativity Level (AI Temperature)",
                0.0, 1.0, 0.3, 0.1
            )
        
        with colB:
            show_prompt = st.checkbox("Show Generated Prompt")
        
        output_type = st.radio(
            "Select Output Type",
            [
                "Full Restoration Report",
                "Restoration Strategy Only",
                "Cultural Interpretation",
                "Visitor-Friendly Summary"
            ],
            horizontal=True
        )
        
        st.divider()


        # -----------------------------
        # Image Upload Section
        # -----------------------------
        st.subheader("🖼 Upload Damaged Artwork Image (Optional)")
        
        uploaded_image = st.file_uploader(
            "Upload an image of the damaged artwork",
            type=["jpg", "jpeg", "png"]
        )
        
        if uploaded_image:
            st.image(uploaded_image, caption="Uploaded Artwork Preview", use_container_width=True)
            
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
                        from PIL import Image

                        if uploaded_image:
                            image = Image.open(uploaded_image)
                        
                            response = model.generate_content(
                                [prompt, image],
                                generation_config={
                                    "temperature": temperature,
                                    "top_p": 0.95,
                                    "top_k": 40,
                                    "max_output_tokens": 2048,
                                }
                            )
                        else:
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



    with tab3:

        st.markdown("## 🤖 Restora A.I Assistant")
    
        # -------------------------
        # Chat Memory
        # -------------------------
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
    
        # -------------------------
        # Ready Made Prompts
        # -------------------------
        st.markdown("### 🎨 Quick Prompts")
    
        col1, col2 = st.columns(2)
    
        with col1:
            if st.button("Analyze Renaissance Painting"):
                prompt = "Provide a culturally sensitive restoration strategy for a damaged Renaissance oil painting."
                st.session_state.chat_history.append(("user", prompt))
    
            if st.button("Monument Crack Repair Advice"):
                prompt = "Suggest restoration techniques for structural cracks in historical monuments while preserving authenticity."
                st.session_state.chat_history.append(("user", prompt))
    
        with col2:
            if st.button("Artifact Preservation Plan"):
                prompt = "Create a conservation plan for a fragile 18th century manuscript."
                st.session_state.chat_history.append(("user", prompt))
    
            if st.button("Ethical Restoration Guidelines"):
                prompt = "Explain ethical principles in AI-assisted cultural heritage restoration."
                st.session_state.chat_history.append(("user", prompt))
    
        st.divider()
    
        # -------------------------
        # Chat Input
        # -------------------------
        user_input = st.chat_input("Ask Restora A.I...")
    
        if user_input:
            st.session_state.chat_history.append(("user", user_input))
    
            # 🔥 Replace this with your real AI model call
            ai_response = f"""
            Based on your request:
    
            "{user_input}"
    
            I recommend a conservation strategy emphasizing:
            • Minimal intervention
            • Historical authenticity
            • Reversible restoration techniques
            • Detailed documentation
    
            Would you like a structured technical restoration report?
            """
    
            st.session_state.chat_history.append(("assistant", ai_response))
    
        # -------------------------
        # Display Messages
        # -------------------------
        for role, message in st.session_state.chat_history:
            with st.chat_message(role):
                st.markdown(message)

                




    with tab4:
        st.title("📊 Real-Time Restoration Insights")

        # Check if history exists
        if "history" not in st.session_state or not st.session_state.history:
            st.info("No restoration data available yet. Generate a restoration first.")
        else:
    
            history = st.session_state.history
    
            # -----------------------------
            # REAL-TIME METRICS
            # -----------------------------
            total_restorations = len(history)
    
            # Count artworks by type
            artwork_counts = {}
            for item in history:
                art_type = item["artwork_type"]
                artwork_counts[art_type] = artwork_counts.get(art_type, 0) + 1
    
            most_common_type = max(artwork_counts, key=artwork_counts.get)
    
            # Count by period
            period_counts = {}
            for item in history:
                period = item["period"]
                period_counts[period] = period_counts.get(period, 0) + 1
    
            most_common_period = max(period_counts, key=period_counts.get)
    
            col1, col2, col3 = st.columns(3)
    
            with col1:
                st.metric("Total Restorations", total_restorations)
    
            with col2:
                st.metric("Most Restored Type", most_common_type)
    
            with col3:
                st.metric("Most Common Period", most_common_period)
    
            st.divider()
    
            # -----------------------------
            # RESTORATION TREND (REAL-TIME)
            # -----------------------------
            st.subheader("📈 Restoration Trend")
    
            # Convert timestamps to dates
            dates = []
            for item in history:
                date = item["timestamp"].split(" ")[0]
                dates.append(date)
    
            # Count restorations per day
            date_counts = {}
            for d in dates:
                date_counts[d] = date_counts.get(d, 0) + 1
    
            trend_df = pd.DataFrame({
                "Date": list(date_counts.keys()),
                "Restorations": list(date_counts.values())
            })
    
            trend_df = trend_df.sort_values("Date")
    
            st.line_chart(trend_df.set_index("Date"))
    
            st.divider()
    
            # -----------------------------
            # ARTWORK TYPE DISTRIBUTION
            # -----------------------------
            st.subheader("🎨 Artwork Type Distribution")
    
            type_df = pd.DataFrame({
                "Artwork Type": list(artwork_counts.keys()),
                "Count": list(artwork_counts.values())
            })
    
            st.bar_chart(type_df.set_index("Artwork Type"))
              
              
    with tab5:
        st.title("🧾 AI Restoration Report Generator")
    
        artwork_name = st.text_input("Artwork Name")
        damage_type = st.selectbox(
            "Primary Damage Detected",
            ["Cracks", "Color Fading", "Moisture Damage", "Dust & Surface Dirt"]
        )
    
        confidence = st.slider("AI Confidence Score (%)", 50, 100, 85)
    
        if st.button("Generate Report"):
            st.success("Report Generated Successfully!")
    
            report = (
                f"🖼 Artwork: {artwork_name}\n\n"
                f"🔍 Detected Damage: {damage_type}\n\n"
                f"🤖 AI Restoration Confidence: {confidence}%\n\n"
                "🛠 Restoration Method:\n"
                "- Digital crack reconstruction\n"
                "- Color tone rebalancing\n"
                "- Texture preservation algorithm\n\n"
                f"📅 Date: {pd.Timestamp.today().date()}\n\n"
                "🏛 Powered by Restora A.I"
            )
    
            st.text_area("Restoration Report", report, height=300)
    
            st.download_button(
                "📥 Download Report",
                report,
                file_name="restoration_report.txt"
            )





            
    with tab6:

        st.title("💬 User Feedback & System Evaluation")
    
        if "feedback_list" not in st.session_state:
            st.session_state.feedback_list = []
    
        st.subheader("⭐ Rate Your Experience")
    
        rating = st.slider("Overall Experience Rating", 1, 5, 4)
    
        usability = st.slider("Ease of Use", 1, 5, 4)
        accuracy = st.slider("AI Accuracy", 1, 5, 4)
    
        comments = st.text_area("Additional Feedback (Optional)")
    
        if st.button("Submit Feedback"):
            feedback_entry = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "rating": rating,
                "usability": usability,
                "accuracy": accuracy,
                "comments": comments
            }
    
            st.session_state.feedback_list.append(feedback_entry)
            st.success("Thank you! Your feedback has been recorded.")
    
        st.divider()
    
        # -----------------------------
        # REAL-TIME FEEDBACK ANALYTICS
        # -----------------------------
        if st.session_state.feedback_list:
    
            st.subheader("📊 Feedback Insights")
    
            feedback_data = st.session_state.feedback_list
    
            avg_rating = sum(f["rating"] for f in feedback_data) / len(feedback_data)
            avg_usability = sum(f["usability"] for f in feedback_data) / len(feedback_data)
            avg_accuracy = sum(f["accuracy"] for f in feedback_data) / len(feedback_data)
    
            col1, col2, col3 = st.columns(3)
    
            with col1:
                st.metric("⭐ Avg Rating", f"{avg_rating:.2f}")
    
            with col2:
                st.metric("🖱 Avg Usability", f"{avg_usability:.2f}")
    
            with col3:
                st.metric("🎯 Avg Accuracy", f"{avg_accuracy:.2f}")
    
            st.divider()
    
            # Rating Distribution
            rating_counts = {}
            for f in feedback_data:
                rating_counts[f["rating"]] = rating_counts.get(f["rating"], 0) + 1
    
            rating_df = pd.DataFrame({
                "Rating": list(rating_counts.keys()),
                "Count": list(rating_counts.values())
            })
    
            st.subheader("⭐ Rating Distribution")
            st.bar_chart(rating_df.set_index("Rating"))
    
            # Show recent feedback
            st.subheader("📝 Recent Comments")
            for f in reversed(feedback_data[-5:]):
                if f["comments"]:
                    with st.expander(f"{f['timestamp']} — {f['rating']}⭐"):
                        st.write(f["comments"])            
        
            
               
               






                
