import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
import streamlit.components.v1 as components

st.set_page_config(page_title="RocketViz AI",layout="wide")

# =========================================================
# GLOBAL CSS (GLASSMORPHISM + GLOW)
# =========================================================

st.markdown("""
<style>

.stApp{
background: radial-gradient(circle at top,#020617,#020024,#090979,#00d4ff);
color:white;
}

/* GLASS CARDS */

.glass{
backdrop-filter: blur(20px);
background: rgba(255,255,255,0.05);
padding:25px;
border-radius:20px;
border:1px solid rgba(255,255,255,0.1);
box-shadow:0 0 30px rgba(0,255,255,0.4);
transition:0.4s;
}

.glass:hover{
transform:scale(1.05);
box-shadow:0 0 60px rgba(0,255,255,0.9);
}

/* GLOW TEXT */

.glow{
font-size:3rem;
font-weight:700;
background: linear-gradient(90deg,#00e5ff,#00ff9c,#00e5ff);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
animation:shine 4s linear infinite;
}

@keyframes shine{
0%{background-position:0%}
100%{background-position:200%}
}

/* BUTTON */

.stButton>button{
background:linear-gradient(90deg,#00e5ff,#00ff9c);
border:none;
border-radius:30px;
padding:12px 30px;
font-size:16px;
box-shadow:0 0 20px #00e5ff;
transition:0.3s;
}

.stButton>button:hover{
transform:scale(1.1);
box-shadow:0 0 40px #00ff9c;
}

/* SIDEBAR */

[data-testid="stSidebar"]{
background:rgba(255,255,255,0.04);
backdrop-filter: blur(20px);
border-right:1px solid rgba(255,255,255,0.1);
box-shadow:0 0 20px rgba(0,255,255,0.4);
}



.stTabs [data-baseweb="tab"]{
font-size:18px;
color:white;
padding:12px;
border-radius:15px;
transition:0.3s;
}

.stTabs [aria-selected="true"]{
background:linear-gradient(90deg,#00e5ff,#00ff9c);
color:black;
box-shadow:0 0 20px #00e5ff;
}

</style>
""",unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page="splash"


# =========================================================
# =========================================================
# SPLASH SCREEN
# =========================================================

if st.session_state.page == "splash":

    splash_html = """
    <html>
    <style>

    body{
    margin:0;
    background:black;
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
    color:white;
    font-family:sans-serif;
    overflow:hidden;
    }

    .title{
    font-size:3.5rem;
    font-weight:700;
    background:linear-gradient(90deg,#00e5ff,#00ff9c);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    animation:glow 2s infinite alternate;
    }

    @keyframes glow{
    from{ text-shadow:0 0 10px #00e5ff}
    to{ text-shadow:0 0 40px #00ff9c}
    }

    .rocket{
    font-size:5rem;
    animation:fly 2s infinite;
    }

    @keyframes fly{
    0%{transform:translateY(0)}
    50%{transform:translateY(-30px)}
    100%{transform:translateY(0)}
    }

    </style>

    <body>

    <div style="text-align:center">

    <div class="rocket">🚀</div>

    <div class="title">RocketViz AI</div>

    <p>Rocket Launch Simulation & Mission Analytics</p>

    </div>

    </body>
    </html>
    """

    components.html(splash_html, height=800)

    if "splash_shown" not in st.session_state:
        time.sleep(3)
        st.session_state.splash_shown = True
        st.session_state.page = "landing"
        st.rerun()


# =========================================================
# LANDING PAGE
# =========================================================

elif st.session_state.page=="landing":

    st.markdown("<div class='glow'>RocketViz AI</div>",unsafe_allow_html=True)

    st.write("")

    st.markdown("""
<div class="glass">

### 🚀 Explore the Universe of Rocket Science

Simulate rocket launches using real physics principles and explore space missions through interactive analytics.

Features:

• Rocket launch simulation  
• Mission dataset analytics  
• Interactive charts  
• Payload vs fuel insights  
• Mission success exploration  

</div>
""",unsafe_allow_html=True)

    st.write("")

    if st.button("🚀 Launch App"):
        st.session_state.page="signup"



# =========================================================
# SIGNUP PAGE
# =========================================================

elif st.session_state.page=="signup":

    st.markdown("<div class='glow'>Create Mission Profile</div>",unsafe_allow_html=True)

    name=st.text_input("Astronaut Name")

    email=st.text_input("Email")

    st.image("https://api.dicebear.com/7.x/bottts/svg?seed=rocket",width=120)

    if st.button("Enter Dashboard"):
        st.session_state.user=name
        st.session_state.page="dashboard"



# =========================================================
# DASHBOARD
elif st.session_state.page=="dashboard":

    st.markdown("<div class='glow'>Mission Control Dashboard</div>",unsafe_allow_html=True)

    # ===============================
    # TOP DASHBOARD CARDS
    # ===============================

    col1,col2,col3=st.columns(3)

    with col1:
        st.markdown("""
        <div class="glass">
        <h3>🚀 Missions</h3>
        <h2>120</h2>
        </div>
        """,unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="glass">
        <h3>🛰 Payload Avg</h3>
        <h2>3200 kg</h2>
        </div>
        """,unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="glass">
        <h3>⛽ Fuel Avg</h3>
        <h2>4500 L</h2>
        </div>
        """,unsafe_allow_html=True)

    st.write("")
    st.write("")

    # ===============================
    # FEATURE TABS
    # ===============================

    tab1, tab2 = st.tabs([
        "🚀 Rocket Simulation",
        "📊 Mission Analytics"
    ])

    # ==========================================
    # TAB 1 : ROCKET SIMULATION
    # ==========================================

    with tab1:

        st.markdown("<div class='glow'>Rocket Launch Simulator</div>",unsafe_allow_html=True)

        thrust=st.slider("Thrust",10000,200000,50000)
        payload=st.slider("Payload Weight",100,10000,2000)
        fuel=st.slider("Fuel Amount",500,20000,5000)

        g=9.81
        mass=payload+fuel+5000

        velocity=0
        altitude=0

        data=[]

        for t in range(200):

            drag=0.02*velocity**2

            accel=(thrust-(mass*g)-drag)/mass

            velocity+=accel
            altitude+=velocity

            fuel-=5
            mass-=5

            data.append([t,velocity,altitude])

        df=pd.DataFrame(data,columns=["Time","Velocity","Altitude"])

        fig=px.line(df,x="Time",y="Altitude",title="Rocket Altitude")

        st.plotly_chart(fig,use_container_width=True)

    # ==========================================
    # TAB 2 : ANALYTICS
    # ==========================================

    with tab2:

        st.markdown("<div class='glow'>Mission Analytics</div>",unsafe_allow_html=True)

        n=200

        df=pd.DataFrame({

        "Payload Weight":np.random.randint(500,8000,n),

        "Fuel Consumption":np.random.randint(2000,10000,n),

        "Mission Cost":np.random.randint(50,500,n),

        "Mission Success":np.random.choice(["Success","Failure"],n)

        })

        fig=px.scatter(
        df,
        x="Payload Weight",
        y="Fuel Consumption",
        color="Mission Success",
        size="Mission Cost"
        )

        st.plotly_chart(fig,use_container_width=True)

        fig2=px.histogram(df,x="Mission Cost")

        st.plotly_chart(fig2,use_container_width=True)
