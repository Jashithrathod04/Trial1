import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
import streamlit.components.v1 as components

st.set_page_config(page_title="RocketViz AI",layout="wide")





# =========================================================
# DATA SOURCE (DEFAULT CSV + USER UPLOAD)
# =========================================================

st.sidebar.title("📂 Data Source")

uploaded_file = st.sidebar.file_uploader(
    "Upload Mission Dataset (CSV)",
    type=["csv"]
)

# Default dataset path
default_data = pd.read_csv("space_missions_dataset.csv")

if uploaded_file is not None:
    df_data = pd.read_csv(uploaded_file)
    st.sidebar.success("Using Uploaded Dataset")
else:
    df_data = default_data
    st.sidebar.info("Using Default Space Missions Dataset")

df_data.columns = df_data.columns.str.strip()




df = df_data.rename(columns={
"Fuel Consumption (tons)": "Fuel",
"Payload Weight (tons)": "Payload",
"Mission Cost (billion USD)": "Cost",
"Distance from Earth (light-years)": "Distance",
"Mission Duration (years)": "Duration",
"Scientific Yield (points)": "Science",
"Mission Success (%)": "Success"
})





# =========================================================
# DATA CLEANING
# =========================================================

df_data["Launch Date"] = pd.to_datetime(df_data["Launch Date"])

df_data = df_data.drop_duplicates()

df_data = df_data.fillna(method="ffill")
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

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
        "🏠 Home",
        "🚀 Rocket Simulation",
        "📊 Mission Analytics",
        "📊 Mission Data Explorer",
        "🚀 Rocket Physics Simulation",
        "📈 Mission Analytics",
        "🔍 Comparative Insights",
        "ℹ️ About Project"
    ])

    # ==========================================
    # TAB 1 : ROCKET SIMULATION
    # ==========================================

    with tab2:

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

    with tab3:

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





    with tab1: 

        st.markdown("<div class='glow'>RocketLab AI Dashboard</div>",unsafe_allow_html=True)

        st.write("""
        Interactive rocket launch simulator and mission analytics platform.
        
        This application explores rocket physics and real mission data
        to understand how thrust, fuel, payload, and cost influence
        space missions.
        """)
        
        st.image("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa",use_column_width=True)
        
        st.info("Use the tabs above to explore mission data, simulate rocket launches, and discover insights.")


    with tab4:

        st.markdown("<div class='glow'>Mission Data Explorer</div>",unsafe_allow_html=True)
    
        vehicle = st.selectbox(
            "Launch Vehicle",
            df["Launch Vehicle"].unique()
        )
    
        cost_range = st.slider(
            "Mission Cost Range",
            float(df["Cost"].min()),
            float(df["Cost"].max()),
            (float(df["Cost"].min()), float(df["Cost"].max()))
        )
    
        filtered = df[
            (df["Launch Vehicle"] == vehicle) &
            (df["Cost"] >= cost_range[0]) &
            (df["Cost"] <= cost_range[1])
        ]
    
        st.dataframe(filtered)




    with tab5:


        st.markdown("<div class='glow'>Rocket Physics Simulation</div>",unsafe_allow_html=True)

        payload=st.slider("Payload Weight",100,10000,2000,key="payload_slider")

        fuel=st.slider("Fuel Amount",500,20000,5000,key="fuel_slider")
        
        thrust=st.slider("Thrust",10000,200000,60000,key="thrust_slider")
        
        drag_coeff=st.slider("Drag Coefficient",0.01,0.2,0.05,key="drag_slider")
        
        g=9.81
        mass=payload+fuel+5000
        
        velocity=0
        altitude=0
        fuel_left=fuel
        
        data=[]
        
        for t in range(200):
        
            drag=drag_coeff*(velocity**2)
        
            accel=(thrust-(mass*g)-drag)/mass
        
            velocity+=accel
            altitude+=velocity
        
            fuel_left-=5
            mass-=5
        
            data.append([t,velocity,altitude,fuel_left])
        
        df_sim=pd.DataFrame(data,columns=["Time","Velocity","Altitude","Fuel"])
        
        fig1=px.line(df_sim,x="Time",y="Altitude",title="Altitude vs Time")
        st.plotly_chart(fig1,use_container_width=True)
        
        fig2=px.line(df_sim,x="Time",y="Velocity",title="Velocity vs Time")
        st.plotly_chart(fig2,use_container_width=True)
        
        fig3=px.line(df_sim,x="Time",y="Fuel",title="Fuel Remaining")
        st.plotly_chart(fig3,use_container_width=True)






    with tab6:

        st.markdown("<div class='glow'>Mission Analytics</div>",unsafe_allow_html=True)
    
        # Scatter plot
        fig1 = px.scatter(
            df,
            x="Payload",
            y="Fuel",
            color="Launch Vehicle",
            title="Payload vs Fuel Consumption"
        )
    
        st.plotly_chart(fig1, use_container_width=True)
    
        # Bar chart
        fig2 = px.bar(
            df,
            x="Launch Vehicle",
            y="Cost",
            title="Mission Cost by Launch Vehicle"
        )
    
        st.plotly_chart(fig2, use_container_width=True)
    
        # Line plot
        fig3 = px.line(
            df.sort_values("Distance"),
            x="Distance",
            y="Duration",
            title="Distance vs Mission Duration"
        )
    
        st.plotly_chart(fig3, use_container_width=True)
    
        # Box plot
        fig4 = px.box(
            df,
            y="Crew Size",
            title="Crew Size Distribution"
        )
    
        st.plotly_chart(fig4, use_container_width=True)
    
        # Heatmap
        corr = df[["Payload","Fuel","Cost","Distance","Duration","Science","Crew Size"]].corr()
    
        fig5 = px.imshow(corr, text_auto=True, title="Correlation Heatmap")
    
        st.plotly_chart(fig5, use_container_width=True)

          
    with tab7:

        st.markdown("<div class='glow'>Comparative Insights</div>",unsafe_allow_html=True)
    
        avg_payload = df["Payload"].mean()
    
        comparison = pd.DataFrame({
            "Type":["Real Missions","Simulation"],
            "Payload":[avg_payload,payload]
        })
    
        fig = px.bar(
            comparison,
            x="Type",
            y="Payload",
            title="Simulation vs Real Mission Payload"
        )
    
        st.plotly_chart(fig,use_container_width=True)


    with tab8:



        st.markdown("<div class='glow'>About This Project</div>",unsafe_allow_html=True)

        st.write("""
        
        RocketViz AI is an interactive platform that explores
        rocket launch physics and mission analytics.
        
        Technologies Used:
        
        • Python  
        • Streamlit  
        • Pandas  
        • Plotly  
        
        This project demonstrates how mathematical modelling
        and data science can be used to analyse space missions
        and simulate rocket launches.
        
        Developed for CRS Artificial Intelligence course.
        
        """)




    









        

















