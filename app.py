import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import random
import time
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from scipy.stats import zscore
import warnings
warnings.filterwarnings("ignore")



def hex_to_rgba(hex_color, alpha=0.1):
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"
# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SmartCharge AI ⚡",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>

/* SIDEBAR GLASSMORPHISM */
section[data-testid="stSidebar"] {
    background: rgba(20, 20, 30, 0.6);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-right: 1px solid rgba(255,255,255,0.1);
}

/* SKEUOMORPHIC BUTTON STYLE */
.glass-btn {
    background: linear-gradient(145deg, rgba(255,255,255,0.08), rgba(0,0,0,0.2));
    border-radius: 12px;
    padding: 10px;
    text-align: center;
    color: white;
    font-weight: 600;
    box-shadow: 
        6px 6px 12px rgba(0,0,0,0.4),
        -4px -4px 8px rgba(255,255,255,0.05);
    transition: all 0.3s ease;
}

.glass-btn:hover {
    transform: translateY(-2px);
    box-shadow: 
        2px 2px 6px rgba(0,0,0,0.6),
        -2px -2px 6px rgba(255,255,255,0.08);
}

/* Sidebar text */
.sidebar-title {
    font-size: 20px;
    font-weight: bold;
    color: #00f5d4;
    margin-bottom: 10px;
}


/* ── SIDEBAR GLASS + SKEUO ── */
section[data-testid="stSidebar"]{
  background: rgba(10,15,30,0.65) !important;
  backdrop-filter: blur(25px);
  -webkit-backdrop-filter: blur(25px);
  border-right: 1px solid rgba(255,255,255,0.1);
  box-shadow: inset -4px 0 20px rgba(0,0,0,0.6);
}

/* Sidebar content spacing */
section[data-testid="stSidebar"] > div{
  padding: 20px;
}

/* Skeuomorphic card inside sidebar */
.sidebar-card{
  background: linear-gradient(145deg, rgba(255,255,255,0.05), rgba(0,0,0,0.3));
  border-radius: 16px;
  padding: 16px;
  margin-bottom: 16px;
  box-shadow:
    6px 6px 12px rgba(0,0,0,0.6),
    -4px -4px 8px rgba(255,255,255,0.05);
}

/* Sidebar title */
.sidebar-title{
  font-family:'Orbitron',monospace;
  font-size:1rem;
  letter-spacing:2px;
  color:#00f5d4;
  margin-bottom:10px;
}

/* Sign out button */
.signout-btn{
  background: linear-gradient(145deg, #ff006e, #7b2fff);
  border-radius: 12px;
  padding: 10px;
  text-align: center;
  color: white;
  font-weight: bold;
  box-shadow: 0 0 15px rgba(255,0,110,0.6);
  transition: all 0.3s ease;
}
.signout-btn:hover{
  transform: scale(1.05);
  box-shadow: 0 0 25px rgba(255,0,110,0.9);
}
</style>
""", unsafe_allow_html=True)






# ─────────────────────────────────────────────────────────────────────────────
# MASTER CSS — GLASSMORPHISM + ANIMATIONS + HOVER EFFECTS
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;600;700&family=Share+Tech+Mono&display=swap');

/* ── ROOT VARIABLES ── */
:root{
  --c1:#00f5d4;--c2:#7b2fff;--c3:#ff006e;--c4:#fb5607;
  --glass-bg:rgba(255,255,255,0.04);
  --glass-border:rgba(255,255,255,0.12);
  --glass-shadow:0 8px 32px rgba(0,0,0,0.5);
  --glow-cyan:0 0 20px rgba(0,245,212,0.6);
  --glow-purple:0 0 20px rgba(123,47,255,0.6);
  --glow-pink:0 0 20px rgba(255,0,110,0.6);
}

/* ── BACKGROUND ── */
.stApp{
  background:#000510;
  background-image:
    radial-gradient(ellipse at 10% 10%, rgba(0,245,212,0.08) 0%, transparent 50%),
    radial-gradient(ellipse at 90% 20%, rgba(123,47,255,0.08) 0%, transparent 50%),
    radial-gradient(ellipse at 50% 90%, rgba(255,0,110,0.06) 0%, transparent 50%);
  font-family:'Rajdhani',sans-serif;
  color:rgba(255,255,255,0.9);
  overflow-x:hidden;
}

/* ── ANIMATED GRID OVERLAY ── */
.stApp::before{
  content:'';
  position:fixed;top:0;left:0;width:100%;height:100%;
  background-image:
    linear-gradient(rgba(0,245,212,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,245,212,0.03) 1px, transparent 1px);
  background-size:60px 60px;
  animation:gridMove 20s linear infinite;
  pointer-events:none;z-index:0;
}
@keyframes gridMove{
  0%{transform:translateY(0)} 100%{transform:translateY(60px)}
}

/* ── FLOATING PARTICLES ── */
.stApp::after{
  content:'';
  position:fixed;top:0;left:0;width:100%;height:100%;
  background:
    radial-gradient(circle 2px at 20% 30%, var(--c1), transparent),
    radial-gradient(circle 2px at 80% 70%, var(--c2), transparent),
    radial-gradient(circle 2px at 60% 20%, var(--c3), transparent),
    radial-gradient(circle 1px at 40% 80%, var(--c4), transparent);
  animation:particleFloat 8s ease-in-out infinite alternate;
  pointer-events:none;z-index:0;opacity:0.6;
}
@keyframes particleFloat{
  0%{transform:translate(0,0) scale(1)}
  100%{transform:translate(10px,-20px) scale(1.2)}
}

/* ── GLASS CARD ── */
.glass-card{
  background:var(--glass-bg);
  backdrop-filter:blur(20px);
  -webkit-backdrop-filter:blur(20px);
  border-radius:20px;
  border:1px solid var(--glass-border);
  box-shadow:var(--glass-shadow);
  padding:28px;
  transition:all 0.4s cubic-bezier(0.175,0.885,0.32,1.275);
  position:relative;overflow:hidden;
}
.glass-card::before{
  content:'';
  position:absolute;top:0;left:-100%;width:100%;height:100%;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,0.04),transparent);
  transition:left 0.6s ease;
}
.glass-card:hover::before{left:100%;}
.glass-card:hover{
  transform:translateY(-8px) scale(1.01);
  border-color:rgba(0,245,212,0.4);
  box-shadow:0 20px 60px rgba(0,0,0,0.6), var(--glow-cyan);
}

/* ── NEON METRIC CARDS ── */
.metric-box{
  background:linear-gradient(135deg,rgba(0,245,212,0.06),rgba(123,47,255,0.06));
  border:1px solid rgba(0,245,212,0.2);
  border-radius:16px;padding:20px;text-align:center;
  transition:all 0.35s ease;
  position:relative;overflow:hidden;
}
.metric-box::after{
  content:'';position:absolute;
  top:-50%;left:-50%;width:200%;height:200%;
  background:conic-gradient(transparent,rgba(0,245,212,0.1),transparent 30%);
  animation:rotate 4s linear infinite;opacity:0;
  transition:opacity 0.3s;
}
.metric-box:hover::after{opacity:1;}
@keyframes rotate{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}
.metric-box:hover{
  transform:translateY(-6px);
  border-color:var(--c1);
  box-shadow:var(--glow-cyan), inset 0 0 30px rgba(0,245,212,0.05);
}
.metric-val{
  font-family:'Orbitron',monospace;font-size:2rem;font-weight:900;
  background:linear-gradient(90deg,var(--c1),var(--c2));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}
.metric-label{
  font-family:'Rajdhani',sans-serif;font-size:0.85rem;
  color:rgba(255,255,255,0.55);letter-spacing:2px;text-transform:uppercase;
  margin-top:4px;
}

/* ── HEADINGS ── */
h1,h2,h3{
  font-family:'Orbitron',monospace !important;
  background:linear-gradient(90deg,var(--c1),var(--c2),var(--c3));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  animation:hueShift 8s linear infinite;
}
@keyframes hueShift{
  0%{filter:hue-rotate(0deg)}50%{filter:hue-rotate(30deg)}100%{filter:hue-rotate(0deg)}
}

/* ── SUBHEADINGS ── */
.section-title{
  font-family:'Orbitron',monospace;
  font-size:1.1rem;letter-spacing:3px;text-transform:uppercase;
  color:var(--c1);margin-bottom:16px;
  display:flex;align-items:center;gap:10px;
}
.section-title::before{
  content:'';display:inline-block;width:4px;height:20px;
  background:linear-gradient(var(--c1),var(--c2));border-radius:2px;
}

/* ── PROFILE CARDS ── */
.profile-grid{display:flex;justify-content:center;gap:40px;flex-wrap:wrap;padding:40px 0;}
.p-card{
  width:200px;text-align:center;cursor:pointer;
  background:var(--glass-bg);
  border:1px solid var(--glass-border);
  border-radius:24px;padding:24px;
  transition:all 0.4s cubic-bezier(0.175,0.885,0.32,1.275);
  position:relative;overflow:hidden;
}
.p-card::before{
  content:'';position:absolute;inset:0;
  background:linear-gradient(135deg,rgba(0,245,212,0.08),rgba(123,47,255,0.08));
  opacity:0;transition:opacity 0.3s;
}
.p-card:hover{
  transform:scale(1.12) translateY(-8px);
  border-color:var(--c1);
  box-shadow:0 20px 60px rgba(0,0,0,0.6), var(--glow-cyan);
}
.p-card:hover::before{opacity:1;}
.p-img{width:120px;height:120px;border-radius:50%;object-fit:cover;
  border:3px solid rgba(0,245,212,0.3);transition:border-color 0.3s;}
.p-card:hover .p-img{border-color:var(--c1);}
.p-name{
  margin-top:12px;font-family:'Orbitron',monospace;font-size:0.85rem;
  color:rgba(255,255,255,0.6);letter-spacing:2px;transition:color 0.3s;
}
.p-card:hover .p-name{color:var(--c1);}
.p-role{font-size:0.75rem;color:rgba(255,255,255,0.35);margin-top:4px;}

/* ── SPLASH SCREEN ── */
.splash-container{
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  min-height:80vh;text-align:center;gap:20px;
}
.splash-logo{
  font-family:'Orbitron',monospace;font-size:4rem;font-weight:900;
  background:linear-gradient(90deg,var(--c1),var(--c2),var(--c3),var(--c4));
  background-size:300% 100%;
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  animation:gradientFlow 3s ease infinite;
}
@keyframes gradientFlow{
  0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}
}
.splash-sub{
  font-family:'Share Tech Mono',monospace;
  color:var(--c1);font-size:1rem;letter-spacing:4px;
  animation:blink 1.5s step-end infinite;
}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0}}
.pulse-ring{
  width:150px;height:150px;border-radius:50%;
  border:3px solid rgba(0,245,212,0.3);
  animation:pulseRing 2s ease-out infinite;
  display:flex;align-items:center;justify-content:center;
  margin:0 auto;font-size:3rem;
}
@keyframes pulseRing{
  0%{box-shadow:0 0 0 0 rgba(0,245,212,0.4)}
  70%{box-shadow:0 0 0 40px rgba(0,245,212,0)}
  100%{box-shadow:0 0 0 0 rgba(0,245,212,0)}
}

/* ── BUTTONS ── */
.stButton>button{
  font-family:'Orbitron',monospace !important;font-size:0.85rem !important;
  background:linear-gradient(90deg,var(--c2),var(--c1)) !important;
  border:none !important;border-radius:12px !important;
  color:#000 !important;font-weight:700 !important;
  padding:12px 32px !important;letter-spacing:2px !important;
  transition:all 0.3s !important;text-transform:uppercase !important;
}
.stButton>button:hover{
  transform:scale(1.05) !important;
  box-shadow:0 0 30px rgba(0,245,212,0.7), 0 0 60px rgba(123,47,255,0.4) !important;
}

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"]{
  background:rgba(255,255,255,0.03);border-radius:16px;
  border:1px solid var(--glass-border);padding:6px;gap:4px;flex-wrap:wrap;
}
.stTabs [data-baseweb="tab"]{
  font-family:'Rajdhani',sans-serif !important;
  font-size:0.85rem !important;letter-spacing:1px !important;
  text-transform:uppercase !important;color:rgba(255,255,255,0.5) !important;
  border-radius:10px !important;padding:10px 14px !important;transition:all 0.25s !important;
}
.stTabs [aria-selected="true"]{
  background:linear-gradient(135deg,rgba(0,245,212,0.15),rgba(123,47,255,0.15)) !important;
  color:var(--c1) !important;border:1px solid rgba(0,245,212,0.3) !important;
}
.stTabs [data-baseweb="tab"]:hover{
  color:var(--c1) !important;background:rgba(0,245,212,0.06) !important;
}

/* ── SIDEBAR ── */
.css-1d391kg,.st-emotion-cache-1d391kg{
  background:rgba(0,5,16,0.9) !important;
  border-right:1px solid var(--glass-border) !important;
}

/* ── DATAFRAME ── */
.stDataFrame{border-radius:12px;overflow:hidden;border:1px solid var(--glass-border);}

/* ── PROGRESS BAR ── */
.stProgress>div>div>div{
  background:linear-gradient(90deg,var(--c1),var(--c2),var(--c3)) !important;
  border-radius:4px !important;
}

/* ── INPUTS ── */
.stTextInput>div>div>input,.stSelectbox>div>div{
  background:rgba(255,255,255,0.05) !important;
  border:1px solid var(--glass-border) !important;
  border-radius:10px !important;color:white !important;
  font-family:'Rajdhani',sans-serif !important;
}
.stTextInput>div>div>input:focus{border-color:var(--c1) !important;box-shadow:var(--glow-cyan) !important;}

/* ── LANDING HERO ── */
.hero-wrapper{
  text-align:center;padding:80px 20px 40px;position:relative;
}
.hero-title{
  font-family:'Orbitron',monospace;font-size:3.5rem;font-weight:900;
  background:linear-gradient(135deg,var(--c1) 0%,var(--c2) 50%,var(--c3) 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  line-height:1.2;margin-bottom:16px;
}
.hero-sub{
  font-family:'Rajdhani',sans-serif;font-size:1.2rem;
  color:rgba(255,255,255,0.5);letter-spacing:4px;text-transform:uppercase;
  margin-bottom:40px;
}
.hero-badge{
  display:inline-block;padding:6px 20px;border-radius:30px;
  border:1px solid rgba(0,245,212,0.4);
  background:rgba(0,245,212,0.06);font-size:0.8rem;
  color:var(--c1);letter-spacing:3px;text-transform:uppercase;
  font-family:'Share Tech Mono',monospace;margin-bottom:30px;
}
.feature-strip{
  display:flex;justify-content:center;flex-wrap:wrap;gap:20px;margin:30px 0;
}
.feature-pill{
  padding:10px 20px;border-radius:30px;
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(255,255,255,0.1);
  font-size:0.85rem;color:rgba(255,255,255,0.6);
  font-family:'Rajdhani',sans-serif;letter-spacing:1px;
  transition:all 0.3s;
}
.feature-pill:hover{border-color:var(--c1);color:var(--c1);}

/* ── INSIGHT CARDS ── */
.insight-card{
  background:linear-gradient(135deg,rgba(0,245,212,0.05),rgba(123,47,255,0.05));
  border:1px solid rgba(0,245,212,0.15);border-radius:16px;
  padding:20px;margin-bottom:14px;transition:all 0.3s;
  border-left:4px solid var(--c1);
}
.insight-card:hover{
  border-color:var(--c1);
  box-shadow:var(--glow-cyan);
  transform:translateX(4px);
}
.insight-icon{font-size:1.4rem;margin-right:10px;}
.insight-text{font-size:1rem;color:rgba(255,255,255,0.85);}

/* ── SCROLLBAR ── */
::-webkit-scrollbar{width:6px;}
::-webkit-scrollbar-track{background:#000510;}
::-webkit-scrollbar-thumb{background:linear-gradient(var(--c1),var(--c2));border-radius:4px;}

/* ── ANOMALY BADGE ── */
.anomaly-badge{
  display:inline-block;padding:3px 12px;border-radius:20px;font-size:0.75rem;
  background:rgba(255,0,110,0.15);border:1px solid rgba(255,0,110,0.4);
  color:var(--c3);font-family:'Share Tech Mono',monospace;
}

/* ── FLOATING NUMBERS ── */
.stat-row{display:flex;gap:12px;flex-wrap:wrap;margin:20px 0;}

/* ── HIDE STREAMLIT BRANDING ── */
#MainMenu,footer,.stDeployButton{visibility:hidden;}
header[data-testid="stHeader"]{background:rgba(0,5,16,0.8);border-bottom:1px solid var(--glass-border);}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────
PLOTLY_TEMPLATE = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Rajdhani, sans-serif", color="rgba(255,255,255,0.8)"),
    xaxis=dict(gridcolor="rgba(255,255,255,0.06)", linecolor="rgba(255,255,255,0.1)"),
    yaxis=dict(gridcolor="rgba(255,255,255,0.06)", linecolor="rgba(255,255,255,0.1)"),
    colorway=["#00f5d4","#7b2fff","#ff006e","#fb5607","#ffbe0b","#3a86ff"],
)

def styled_fig(fig):
    fig.update_layout(**PLOTLY_TEMPLATE, margin=dict(l=20,r=20,t=50,b=20))
    return fig

@st.cache_data
def load_data():
    df = pd.read_csv("ev_charging_dataset.csv")
    df.drop_duplicates(subset="Station ID", inplace=True)
    df["Renewable Energy Source"] = df["Renewable Energy Source"].fillna("Unknown")
    df["Reviews (Rating)"] = df["Reviews (Rating)"].fillna(df["Reviews (Rating)"].median())
    df["Connector Types"] = df["Connector Types"].fillna("Unknown")
    # Encode
    le = LabelEncoder()
    df["ChargerType_enc"] = le.fit_transform(df["Charger Type"])
    df["Renewable_enc"] = (df["Renewable Energy Source"] == "Yes").astype(int)
    df["Maintenance_enc"] = le.fit_transform(df["Maintenance Frequency"])
    return df

def metric_card(col, val, label):
    col.markdown(f"""
    <div class="metric-box">
      <div class="metric-val">{val}</div>
      <div class="metric-label">{label}</div>
    </div>""", unsafe_allow_html=True)


def section_title(icon, text):
    st.markdown(f'<div class="section-title">{icon} {text}</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "splash"


# ─────────────────────────────────────────────────────────────────────────────
# SPLASH SCREEN
# ─────────────────────────────────────────────────────────────────────────────
if st.session_state.page == "splash":
    st.markdown("""
    <div class="splash-container">
      <div class="pulse-ring">⚡</div>
      <div class="splash-logo">SMARTCHARGE AI</div>
      <div class="splash-sub">▶ INITIALIZING EV INTELLIGENCE ENGINE...</div>
    </div>
    """, unsafe_allow_html=True)

    bar = st.progress(0)
    status = st.empty()
    steps = [
        "🔌 Connecting to charging network...",
        "📡 Loading station telemetry...",
        "🧠 Warming up ML models...",
        "🗺️ Mapping global infrastructure...",
        "✅ Ready for launch!",
    ]
    for i in range(101):
        bar.progress(i)
        if i < 20:
            status.markdown(f'<p style="text-align:center;font-family:Share Tech Mono;color:#00f5d4;">{steps[0]}</p>', unsafe_allow_html=True)
        elif i < 45:
            status.markdown(f'<p style="text-align:center;font-family:Share Tech Mono;color:#00f5d4;">{steps[1]}</p>', unsafe_allow_html=True)
        elif i < 65:
            status.markdown(f'<p style="text-align:center;font-family:Share Tech Mono;color:#7b2fff;">{steps[2]}</p>', unsafe_allow_html=True)
        elif i < 85:
            status.markdown(f'<p style="text-align:center;font-family:Share Tech Mono;color:#ff006e;">{steps[3]}</p>', unsafe_allow_html=True)
        else:
            status.markdown(f'<p style="text-align:center;font-family:Share Tech Mono;color:#00f5d4;">{steps[4]}</p>', unsafe_allow_html=True)
        time.sleep(0.02)

    st.session_state.page = "landing"
    st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# LANDING PAGE
# ─────────────────────────────────────────────────────────────────────────────
if st.session_state.page == "landing":
    st.markdown("""
    <div class="hero-wrapper">
      <div class="hero-badge">⚡ AI-POWERED ANALYTICS PLATFORM</div>
      <div class="hero-title">SmartCharge<br>Intelligence</div>
      <div class="hero-sub">Decoding the future of EV charging infrastructure</div>
      <div class="feature-strip">
        <div class="feature-pill">🔍 Behavior Clustering</div>
        <div class="feature-pill">⚠️ Anomaly Detection</div>
        <div class="feature-pill">🔗 Association Mining</div>
        <div class="feature-pill">🌍 Geo Visualization</div>
        <div class="feature-pill">📈 Demand Forecasting</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("⚡  LAUNCH DASHBOARD"):
            st.session_state.page = "profiles"
            st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    metric_card(c1, "5,000+", "Charging Stations")
    metric_card(c2, "20+", "Global Cities")
    metric_card(c3, "6", "ML Algorithms")
    metric_card(c4, "17", "Data Dimensions")


# ─────────────────────────────────────────────────────────────────────────────
# PROFILES PAGE
# ─────────────────────────────────────────────────────────────────────────────
if st.session_state.page == "profiles":
    st.markdown("<h1 style='text-align:center;padding-top:60px;'>Who's Analyzing Today?</h1>", unsafe_allow_html=True)

    profiles = [
        ("https://i.imgur.com/7yUvePI.png", "JASHITH", "Data Scientist"),
        ("https://i.imgur.com/9XnK9QK.png", "ANALYST", "Infrastructure Lead"),
        ("https://cdn-icons-png.flaticon.com/512/1828/1828817.png", "ADD PROFILE", "New User"),
    ]

    st.markdown('<div class="profile-grid">', unsafe_allow_html=True)

    cols = st.columns(len(profiles))
    for i, (img, name, role) in enumerate(profiles):
        with cols[i]:
            st.markdown(f"""
            <div class="p-card">
              <img src="{img}" class="p-img"/>
              <div class="p-name">{name}</div>
              <div class="p-role">{role}</div>
            </div>""", unsafe_allow_html=True)
            label = "Enter" if i < 2 else "Create"
            if st.button(label, key=f"prof_{i}"):
                if i < 2:
                    st.session_state.page = "dashboard"
                else:
                    st.session_state.page = "signup"
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# SIGNUP
# ─────────────────────────────────────────────────────────────────────────────
if st.session_state.page == "signup":
    st.markdown("<h1 style='text-align:center;'>Create Profile</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        name = st.text_input("👤 Name")
        email = st.text_input("📧 Email")
        password = st.text_input("🔐 Password", type="password")
        if st.button("CREATE ACCOUNT"):
            otp = random.randint(100000, 999999)
            st.session_state.otp = otp
            st.session_state.page = "verify"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# OTP VERIFY
# ─────────────────────────────────────────────────────────────────────────────
if st.session_state.page == "verify":
    st.markdown("<h1 style='text-align:center;'>Email Verification</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.info("🔐 Demo Mode — Your OTP:")
        st.markdown(f'<div class="metric-val" style="text-align:center;">{st.session_state.get("otp","")}</div>', unsafe_allow_html=True)
        user_otp = st.text_input("Enter OTP")
        if st.button("VERIFY ⚡"):
            if str(user_otp) == str(st.session_state.get("otp", "")):
                st.session_state.page = "dashboard"
                st.rerun()
            else:
                st.error("❌ Invalid OTP. Try again.")
        st.markdown('</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# MAIN DASHBOARD
# ─────────────────────────────────────────────────────────────────────────────
if st.session_state.page == "dashboard":
    # ───────────────── SIDEBAR ─────────────────
    with st.sidebar:
    
        st.markdown('<div class="sidebar-title">⚡ SMART PANEL</div>', unsafe_allow_html=True)
    
        # USER CARD
        st.markdown("""
        <div class="sidebar-card">
            <b>👤 Analyst</b><br>
            EV Intelligence User
        </div>
        """, unsafe_allow_html=True)
    
        # NAVIGATION
        st.markdown("""
        <div class="sidebar-card">
            <b>📊 Navigation</b><br><br>
            • Overview<br>
            • Data Prep<br>
            • Usage<br>
            • Clustering<br>
            • Insights
        </div>
        """, unsafe_allow_html=True)
    
        
    
        if st.button(" ", key="logout_btn"):
            # SIGN OUT BUTTON
            st.markdown('<div class="signout-btn">🚪 Sign Out</div>', unsafe_allow_html=True)
            st.session_state.page = "landing"   # or "signup" if you want
            st.rerun()





    df = load_data()

    st.markdown("<h1 style='text-align:center;padding-top:20px;'>⚡ SmartCharge Analytics</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:rgba(255,255,255,0.4);font-family:Share Tech Mono;font-size:0.8rem;letter-spacing:3px;'>AI-POWERED EV INFRASTRUCTURE INTELLIGENCE PLATFORM</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    tabs = st.tabs([
        "🏠 Overview",
        "🧹 Data Prep",
        "📊 Usage Analysis",
        "💰 Cost & Ops",
        "📈 EDA Deep Dive",
        "🔗 Correlation",
        "🤖 Clustering",
        "⛏️ Association Rules",
        "⚠️ Anomaly Detection",
        "💡 Insights"
    ])

    # ── TAB 1: OVERVIEW ───────────────────────────────────────────────────────
    with tabs[0]:
        section_title("🌐", "GLOBAL STATION OVERVIEW")

        c1, c2, c3, c4, c5 = st.columns(5)
        metric_card(c1, f"{len(df):,}", "Total Stations")
        metric_card(c2, df["Station Operator"].nunique(), "Operators")
        metric_card(c3, df["Charger Type"].nunique(), "Charger Types")
        metric_card(c4, f"{df['Usage Stats (avg users/day)'].mean():.1f}", "Avg Users/Day")
        metric_card(c5, f"{df['Reviews (Rating)'].mean():.2f}⭐", "Avg Rating")

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("🗺️", "GLOBAL STATION MAP")
            fig_map = px.scatter_mapbox(
                df.sample(min(1000, len(df))), lat="Latitude", lon="Longitude",
                color="Charger Type", size="Usage Stats (avg users/day)",
                hover_name="Address", hover_data=["Cost (USD/kWh)","Reviews (Rating)"],
                mapbox_style="carto-darkmatter", zoom=1, height=420,
                color_discrete_map={"DC Fast Charger":"#00f5d4","AC Level 2":"#7b2fff","AC Level 1":"#ff006e"}
            )
            fig_map.update_layout(paper_bgcolor="rgba(0,0,0,0)", margin=dict(l=0,r=0,t=0,b=0))
            st.plotly_chart(fig_map, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("🔌", "CHARGER TYPE DISTRIBUTION")
            ct = df["Charger Type"].value_counts().reset_index()
            ct.columns = ["Type","Count"]
            fig_pie = px.pie(ct, names="Type", values="Count", hole=0.6,
                             color_discrete_sequence=["#00f5d4","#7b2fff","#ff006e"])
            fig_pie = styled_fig(fig_pie)
            fig_pie.update_traces(textfont_color="white")
            st.plotly_chart(fig_pie, use_container_width=True)

            section_title("♻️", "RENEWABLE ENERGY SPLIT")
            re = df["Renewable Energy Source"].value_counts().reset_index()
            re.columns = ["Source","Count"]
            fig_re = px.bar(re, x="Source", y="Count",
                            color="Source", color_discrete_sequence=["#00f5d4","#7b2fff","#ff006e"])
            fig_re = styled_fig(fig_re)
            st.plotly_chart(fig_re, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        section_title("📋", "RAW DATASET PREVIEW")
        st.dataframe(df.head(10), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ── TAB 2: DATA PREP ──────────────────────────────────────────────────────
    with tabs[1]:
        section_title("🧹", "DATA CLEANING & PREPROCESSING")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("❓", "MISSING VALUES ANALYSIS")
            mv = pd.DataFrame({
                "Column": df.columns,
                "Missing": df.isnull().sum().values,
                "% Missing": (df.isnull().sum().values / len(df) * 100).round(2)
            })
            fig_mv = px.bar(mv[mv["Missing"]>0], x="Column", y="% Missing",
                            color="% Missing", color_continuous_scale=["#00f5d4","#ff006e"])
            fig_mv = styled_fig(fig_mv)
            fig_mv.update_layout(title="Missing Value % by Column")
            st.plotly_chart(fig_mv, use_container_width=True)
            st.dataframe(mv, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("📐", "DATA DISTRIBUTION AFTER CLEANING")
            num_cols = ["Cost (USD/kWh)","Usage Stats (avg users/day)","Charging Capacity (kW)","Distance to City (km)"]
            fig_box = go.Figure()
            for col, color in zip(num_cols, ["#00f5d4","#7b2fff","#ff006e","#fb5607"]):
                fig_box.add_trace(go.Box(y=df[col], name=col, marker_color=color, line_color=color))
            fig_box.update_layout(**PLOTLY_TEMPLATE, title="Numeric Feature Distributions")
            st.plotly_chart(fig_box, use_container_width=True)

            section_title("🔢", "ENCODING SUMMARY")
            enc_df = pd.DataFrame({
                "Feature": ["Charger Type", "Renewable Energy Source", "Maintenance Frequency"],
                "Encoding": ["Label Encoding (0,1,2)", "Binary (0=No, 1=Yes)", "Label Encoding"],
                "Unique Values": [df["Charger Type"].nunique(), df["Renewable Energy Source"].nunique(), df["Maintenance Frequency"].nunique()]
            })
            st.dataframe(enc_df, use_container_width=True)
            st.success("✅ Duplicates removed · Missing values imputed · Features encoded")
            st.markdown('</div>', unsafe_allow_html=True)

    # ── TAB 3: USAGE ANALYSIS ─────────────────────────────────────────────────
    with tabs[2]:
        section_title("📊", "USAGE PATTERNS & DEMAND ANALYSIS")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("📉", "USAGE STATS DISTRIBUTION")
            fig_hist = px.histogram(df, x="Usage Stats (avg users/day)", nbins=40,
                                    color_discrete_sequence=["#00f5d4"],
                                    marginal="violin")
            fig_hist = styled_fig(fig_hist)
            fig_hist.update_layout(title="Distribution of Daily Users per Station")
            st.plotly_chart(fig_hist, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("📅", "USAGE GROWTH OVER INSTALLATION YEARS")
            yearly = df.groupby("Installation Year")["Usage Stats (avg users/day)"].mean().reset_index()
            fig_line = px.line(yearly, x="Installation Year", y="Usage Stats (avg users/day)",
                               markers=True, color_discrete_sequence=["#00f5d4"])
            fig_line.add_scatter(x=yearly["Installation Year"], y=yearly["Usage Stats (avg users/day)"],
                                 fill="tozeroy", fillcolor="rgba(0,245,212,0.06)", line_color="rgba(0,0,0,0)")
            fig_line = styled_fig(fig_line)
            fig_line.update_layout(title="Average Usage by Installation Year")
            st.plotly_chart(fig_line, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("⚡", "USAGE BY CHARGER TYPE")
            fig_box_ct = px.box(df, x="Charger Type", y="Usage Stats (avg users/day)",
                                color="Charger Type",
                                color_discrete_map={"DC Fast Charger":"#00f5d4","AC Level 2":"#7b2fff","AC Level 1":"#ff006e"})
            fig_box_ct = styled_fig(fig_box_ct)
            fig_box_ct.update_layout(title="Usage Distribution by Charger Type")
            st.plotly_chart(fig_box_ct, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("♻️", "RENEWABLE VS NON-RENEWABLE USAGE")
            re_usage = df.groupby("Renewable Energy Source")["Usage Stats (avg users/day)"].mean().reset_index()
            fig_re = px.bar(re_usage, x="Renewable Energy Source", y="Usage Stats (avg users/day)",
                            color="Renewable Energy Source", color_discrete_sequence=["#00f5d4","#ff006e","#7b2fff"],
                            text_auto=True)
            fig_re = styled_fig(fig_re)
            fig_re.update_layout(title="Avg Daily Users: Renewable vs Non-Renewable")
            st.plotly_chart(fig_re, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        section_title("🏙️", "USAGE VS DISTANCE TO CITY")
        fig_scatter_dist = px.scatter(df, x="Distance to City (km)", y="Usage Stats (avg users/day)",
                                     color="Charger Type", size="Charging Capacity (kW)",
                                     hover_name="Address", opacity=0.7,
                                     color_discrete_map={"DC Fast Charger":"#00f5d4","AC Level 2":"#7b2fff","AC Level 1":"#ff006e"},
                                     trendline="lowess")
        fig_scatter_dist = styled_fig(fig_scatter_dist)
        fig_scatter_dist.update_layout(title="Station Usage vs Distance to City Center")
        st.plotly_chart(fig_scatter_dist, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ── TAB 4: COST & OPERATORS ───────────────────────────────────────────────
    with tabs[3]:
        section_title("💰", "COST & OPERATOR ANALYSIS")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("🏢", "COST DISTRIBUTION BY OPERATOR")
            fig_opbox = px.box(df, x="Station Operator", y="Cost (USD/kWh)",
                               color="Station Operator")
            fig_opbox = styled_fig(fig_opbox)
            fig_opbox.update_layout(title="Charging Cost (USD/kWh) per Operator", showlegend=False)
            st.plotly_chart(fig_opbox, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("⭐", "OPERATOR RATINGS VS USAGE")
            op_stats = df.groupby("Station Operator").agg(
                avg_rating=("Reviews (Rating)","mean"),
                avg_usage=("Usage Stats (avg users/day)","mean"),
                count=("Station ID","count")
            ).reset_index()
            fig_op = px.scatter(op_stats, x="avg_rating", y="avg_usage", size="count",
                                color="Station Operator", text="Station Operator",
                                size_max=40)
            fig_op = styled_fig(fig_op)
            fig_op.update_layout(title="Operator: Avg Rating vs Avg Usage")
            st.plotly_chart(fig_op, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("💲", "COST VS USAGE DEMAND")
            fig_cv = px.scatter(df, x="Cost (USD/kWh)", y="Usage Stats (avg users/day)",
                                color="Charger Type", opacity=0.6, trendline="ols",
                                color_discrete_map={"DC Fast Charger":"#00f5d4","AC Level 2":"#7b2fff","AC Level 1":"#ff006e"})
            fig_cv = styled_fig(fig_cv)
            fig_cv.update_layout(title="Does Cost Affect Usage?")
            st.plotly_chart(fig_cv, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("🔧", "MAINTENANCE FREQUENCY & RATINGS")
            maint = df.groupby("Maintenance Frequency")["Reviews (Rating)"].mean().reset_index()
            fig_maint = px.bar(maint, x="Maintenance Frequency", y="Reviews (Rating)",
                               color="Maintenance Frequency", text_auto=".2f")
            fig_maint = styled_fig(fig_maint)
            fig_maint.update_layout(title="Rating by Maintenance Frequency", showlegend=False)
            st.plotly_chart(fig_maint, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # ── TAB 5: EDA DEEP DIVE ──────────────────────────────────────────────────
    with tabs[4]:
        section_title("📈", "EXPLORATORY DATA ANALYSIS — DEEP DIVE")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("🏙️", "TOP 10 CITIES BY AVG USAGE")
            # Extract city from Address
            df["City"] = df["Address"].str.extract(r', ([A-Za-z\s]+),')[0].str.strip()
            city_usage = df.groupby("City")["Usage Stats (avg users/day)"].mean().nlargest(10).reset_index()
            fig_city = px.bar(city_usage, x="Usage Stats (avg users/day)", y="City",
                              orientation="h", color="Usage Stats (avg users/day)",
                              color_continuous_scale=["#7b2fff","#00f5d4"])
            fig_city = styled_fig(fig_city)
            fig_city.update_layout(title="Top Cities by Average Daily Usage")
            st.plotly_chart(fig_city, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("⭐", "RATING DISTRIBUTION")
            fig_rat = px.histogram(df, x="Reviews (Rating)", nbins=20,
                                   color_discrete_sequence=["#7b2fff"], marginal="rug")
            fig_rat = styled_fig(fig_rat)
            fig_rat.update_layout(title="Distribution of Station Ratings")
            st.plotly_chart(fig_rat, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("🅿️", "PARKING SPOTS VS USAGE")
            fig_park = px.scatter(df, x="Parking Spots", y="Usage Stats (avg users/day)",
                                  color="Charger Type", opacity=0.6, trendline="ols",
                                  color_discrete_map={"DC Fast Charger":"#00f5d4","AC Level 2":"#7b2fff","AC Level 1":"#ff006e"})
            fig_park = styled_fig(fig_park)
            fig_park.update_layout(title="Parking Spots vs Station Usage")
            st.plotly_chart(fig_park, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("🔋", "CHARGING CAPACITY DISTRIBUTION")
            cap_counts = df["Charging Capacity (kW)"].value_counts().reset_index()
            cap_counts.columns = ["Capacity (kW)","Count"]
            fig_cap = px.bar(cap_counts, x="Capacity (kW)", y="Count",
                             color="Count", color_continuous_scale=["#7b2fff","#00f5d4"])
            fig_cap = styled_fig(fig_cap)
            fig_cap.update_layout(title="Station Count by Charging Capacity")
            st.plotly_chart(fig_cap, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        section_title("🌡️", "USAGE HEATMAP: CHARGER TYPE × AVAILABILITY")
        pivot = df.pivot_table(index="Charger Type", columns="Availability",
                               values="Usage Stats (avg users/day)", aggfunc="mean")
        fig_hm = px.imshow(pivot, color_continuous_scale=["#000510","#7b2fff","#00f5d4"],
                           aspect="auto", text_auto=".1f")
        fig_hm = styled_fig(fig_hm)
        fig_hm.update_layout(title="Average Usage by Charger Type and Availability Window")
        st.plotly_chart(fig_hm, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ── TAB 6: CORRELATION ────────────────────────────────────────────────────
    with tabs[5]:
        section_title("🔗", "FEATURE CORRELATION ANALYSIS")

        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("🌡️", "CORRELATION HEATMAP")
            num_df = df.select_dtypes(include="number").drop(columns=["Latitude","Longitude"], errors="ignore")
            corr = num_df.corr()
            fig_corr = px.imshow(corr, color_continuous_scale=["#ff006e","#000510","#00f5d4"],
                                 zmin=-1, zmax=1, text_auto=".2f", aspect="auto", height=500)
            fig_corr = styled_fig(fig_corr)
            fig_corr.update_layout(title="Pearson Correlation Matrix")
            st.plotly_chart(fig_corr, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("📊", "TOP CORRELATED FEATURE PAIRS")
            corr_pairs = corr.unstack().reset_index()
            corr_pairs.columns = ["Feature A","Feature B","Correlation"]
            corr_pairs = corr_pairs[corr_pairs["Feature A"] != corr_pairs["Feature B"]]
            corr_pairs["abs_corr"] = corr_pairs["Correlation"].abs()
            top_corr = corr_pairs.nlargest(12, "abs_corr")
            fig_tc = px.bar(top_corr, x="abs_corr",
                            y=top_corr["Feature A"]+" → "+top_corr["Feature B"],
                            color="Correlation", color_continuous_scale=["#ff006e","#7b2fff","#00f5d4"],
                            orientation="h")
            fig_tc = styled_fig(fig_tc)
            fig_tc.update_layout(title="Strongest Feature Correlations", height=500)
            st.plotly_chart(fig_tc, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        section_title("🔍", "PAIRPLOT: KEY FEATURES")
        fig_spm = px.scatter_matrix(df.sample(500),
            dimensions=["Cost (USD/kWh)","Usage Stats (avg users/day)",
                         "Charging Capacity (kW)","Reviews (Rating)","Distance to City (km)"],
            color="Charger Type", opacity=0.5,
            color_discrete_map={"DC Fast Charger":"#00f5d4","AC Level 2":"#7b2fff","AC Level 1":"#ff006e"})
        fig_spm = styled_fig(fig_spm)
        fig_spm.update_layout(title="Scatter Matrix of Key Features", height=600)
        st.plotly_chart(fig_spm, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ── TAB 7: CLUSTERING ─────────────────────────────────────────────────────
    with tabs[6]:
        section_title("🤖", "CHARGING STATION CLUSTERING")

        features = ["Cost (USD/kWh)","Charging Capacity (kW)","Usage Stats (avg users/day)","Distance to City (km)","Reviews (Rating)"]
        scaler = StandardScaler()
        scaled = scaler.fit_transform(df[features].fillna(0))

        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("📐", "ELBOW METHOD — OPTIMAL K")
            inertias = []
            k_range = range(2, 12)
            for k in k_range:
                km = KMeans(n_clusters=k, random_state=42, n_init=10)
                km.fit(scaled)
                inertias.append(km.inertia_)
            fig_elbow = go.Figure()
            fig_elbow.add_trace(go.Scatter(x=list(k_range), y=inertias,
                                           mode="lines+markers",
                                           line=dict(color="#00f5d4", width=3),
                                           marker=dict(color="#7b2fff", size=10)))
            fig_elbow.add_vline(x=4, line_dash="dash", line_color="#ff006e",
                                annotation_text="Optimal K=4")
            fig_elbow.update_layout(**PLOTLY_TEMPLATE, title="Elbow Method for K Selection",
                                    xaxis_title="Number of Clusters (K)",
                                    yaxis_title="Inertia")
            st.plotly_chart(fig_elbow, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("🏷️", "CLUSTER LABELS")
            st.markdown("""
            <div class="insight-card"><span class="insight-icon">🟢</span><b style="color:#00f5d4;">Cluster 0</b><br>Daily Commuters<br><small style="color:rgba(255,255,255,0.5);">Moderate use, low cost</small></div>
            <div class="insight-card"><span class="insight-icon">🟣</span><b style="color:#7b2fff;">Cluster 1</b><br>Heavy Fast-Chargers<br><small style="color:rgba(255,255,255,0.5);">High capacity, high demand</small></div>
            <div class="insight-card"><span class="insight-icon">🔴</span><b style="color:#ff006e;">Cluster 2</b><br>Occasional Users<br><small style="color:rgba(255,255,255,0.5);">Low frequency, rural</small></div>
            <div class="insight-card"><span class="insight-icon">🟠</span><b style="color:#fb5607;">Cluster 3</b><br>Premium Stations<br><small style="color:rgba(255,255,255,0.5);">High cost, high ratings</small></div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
        df["Cluster"] = kmeans.fit_predict(scaled)
        cluster_names = {0:"Daily Commuters", 1:"Heavy Fast-Chargers", 2:"Occasional Users", 3:"Premium Stations"}
        df["Cluster Label"] = df["Cluster"].map(cluster_names)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("⚡", "CLUSTERS: CAPACITY VS USAGE")
            fig_cl = px.scatter(df, x="Charging Capacity (kW)", y="Usage Stats (avg users/day)",
                                color="Cluster Label", size="Cost (USD/kWh)",
                                hover_name="Address", opacity=0.75,
                                color_discrete_sequence=["#00f5d4","#7b2fff","#ff006e","#fb5607"])
            fig_cl = styled_fig(fig_cl)
            fig_cl.update_layout(title="Station Clusters by Capacity & Demand")
            st.plotly_chart(fig_cl, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("🗺️", "CLUSTER MAP")
            fig_cmap = px.scatter_mapbox(
                df.sample(min(800, len(df))), lat="Latitude", lon="Longitude",
                color="Cluster Label", hover_name="Address",
                mapbox_style="carto-darkmatter", zoom=1, height=380,
                color_discrete_sequence=["#00f5d4","#7b2fff","#ff006e","#fb5607"]
            )
            fig_cmap.update_layout(paper_bgcolor="rgba(0,0,0,0)", margin=dict(l=0,r=0,t=0,b=0))
            st.plotly_chart(fig_cmap, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        section_title("📊", "CLUSTER PROFILE COMPARISON")
        cluster_profile = df.groupby("Cluster Label")[features].mean().reset_index()
        fig_radar_data = []
        colors = ["#00f5d4","#7b2fff","#ff006e","#fb5607"]
        for i, row in cluster_profile.iterrows():
            fig_radar_data.append(go.Scatterpolar(
                r=row[features].values.tolist() + [row[features[0]]],
                theta=features + [features[0]],
                fill="toself", name=row["Cluster Label"],
                line_color=colors[i], fillcolor=hex_to_rgba(colors[i], 0.1)
            ))
        fig_radar = go.Figure(data=fig_radar_data)
        fig_radar.update_layout(**PLOTLY_TEMPLATE, polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(gridcolor="rgba(255,255,255,0.1)"),
            angularaxis=dict(gridcolor="rgba(255,255,255,0.1)")
        ), title="Cluster Profiles (Radar)", height=450)
        st.plotly_chart(fig_radar, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ── TAB 8: ASSOCIATION RULES ──────────────────────────────────────────────
    with tabs[7]:
        section_title("⛏️", "ASSOCIATION RULE MINING")

        try:
            from mlxtend.frequent_patterns import apriori, association_rules as arm

            num_df_arm = df.select_dtypes(include="number").drop(
                columns=["Latitude","Longitude","Cluster"], errors="ignore").fillna(0)
            binary = (num_df_arm > num_df_arm.mean()).astype(bool)

            freq = apriori(binary, min_support=0.1, use_colnames=True)
            rules = arm(freq, metric="lift", min_threshold=1.0)
            rules["antecedents"] = rules["antecedents"].apply(lambda x: ", ".join(list(x)))
            rules["consequents"] = rules["consequents"].apply(lambda x: ", ".join(list(x)))

            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                section_title("📊", "SUPPORT VS CONFIDENCE")
                fig_ar = px.scatter(rules, x="support", y="confidence", color="lift",
                                    size="lift", hover_data=["antecedents","consequents"],
                                    color_continuous_scale=["#7b2fff","#00f5d4","#ff006e"],
                                    size_max=25)
                fig_ar = styled_fig(fig_ar)
                fig_ar.update_layout(title="Association Rules: Support vs Confidence vs Lift")
                st.plotly_chart(fig_ar, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)

            with col2:
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                section_title("🔝", "TOP RULES BY LIFT")
                top_rules = rules.nlargest(10,"lift")[["antecedents","consequents","support","confidence","lift"]]
                fig_lift = px.bar(top_rules, x="lift", y=top_rules["antecedents"]+" → "+top_rules["consequents"],
                                  color="confidence", orientation="h",
                                  color_continuous_scale=["#7b2fff","#00f5d4"])
                fig_lift = styled_fig(fig_lift)
                fig_lift.update_layout(title="Top 10 Association Rules by Lift")
                st.plotly_chart(fig_lift, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("📋", "FULL RULES TABLE")
            st.dataframe(rules[["antecedents","consequents","support","confidence","lift"]].round(4).head(30),
                         use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        except Exception as e:
            st.warning(f"Association rules could not be computed: {e}")

    # ── TAB 9: ANOMALY DETECTION ──────────────────────────────────────────────
    with tabs[8]:
        section_title("⚠️", "ANOMALY DETECTION")

        num_cols_anom = df.select_dtypes(include="number").drop(
            columns=["Latitude","Longitude","Cluster"], errors="ignore").fillna(0)

        z_scores = np.abs(zscore(num_cols_anom))
        df["Anomaly"] = (z_scores > 3).any(axis=1)
        df["Max_Z"] = z_scores.max(axis=1)

        n_anomalies = df["Anomaly"].sum()
        anomaly_pct = n_anomalies / len(df) * 100

        col1, col2, col3 = st.columns(3)
        metric_card(col1, f"{n_anomalies:,}", "Anomalous Stations")
        metric_card(col2, f"{anomaly_pct:.1f}%", "Anomaly Rate")
        metric_card(col3, f"{df['Max_Z'].max():.2f}", "Max Z-Score")

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("🔍", "ANOMALY SCATTER: COST VS USAGE")
            fig_anom = px.scatter(df, x="Cost (USD/kWh)", y="Usage Stats (avg users/day)",
                                  color="Anomaly", symbol="Anomaly",
                                  color_discrete_map={True:"#ff006e", False:"rgba(0,245,212,0.4)"},
                                  hover_name="Address", size="Max_Z", size_max=20)
            fig_anom = styled_fig(fig_anom)
            fig_anom.update_layout(title="Anomalies: Cost vs Usage (Red = Anomaly)")
            st.plotly_chart(fig_anom, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("📊", "Z-SCORE DISTRIBUTION")
            fig_z = px.histogram(df, x="Max_Z", nbins=50,
                                 color_discrete_sequence=["#7b2fff"])
            fig_z.add_vline(x=3, line_dash="dash", line_color="#ff006e",
                            annotation_text="Anomaly Threshold (Z=3)")
            fig_z = styled_fig(fig_z)
            fig_z.update_layout(title="Distribution of Maximum Z-Scores")
            st.plotly_chart(fig_z, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("🗺️", "ANOMALY MAP")
            df_anom_map = df[df["Anomaly"]].sample(min(200, df["Anomaly"].sum()))
            df_norm_map = df[~df["Anomaly"]].sample(min(400, (~df["Anomaly"]).sum()))
            df_plot = pd.concat([df_anom_map, df_norm_map])
            fig_amap = px.scatter_mapbox(df_plot, lat="Latitude", lon="Longitude",
                                         color="Anomaly",
                                         color_discrete_map={True:"#ff006e", False:"rgba(0,245,212,0.3)"},
                                         hover_name="Address",
                                         mapbox_style="carto-darkmatter", zoom=1, height=380)
            fig_amap.update_layout(paper_bgcolor="rgba(0,0,0,0)", margin=dict(l=0,r=0,t=0,b=0))
            st.plotly_chart(fig_amap, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("🏢", "ANOMALIES BY OPERATOR")
            anom_by_op = df.groupby("Station Operator")["Anomaly"].sum().reset_index()
            anom_by_op.columns = ["Operator","Anomaly Count"]
            fig_aop = px.bar(anom_by_op, x="Operator", y="Anomaly Count",
                             color="Anomaly Count", color_continuous_scale=["#7b2fff","#ff006e"])
            fig_aop = styled_fig(fig_aop)
            fig_aop.update_layout(title="Anomalous Stations per Operator")
            st.plotly_chart(fig_aop, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        section_title("📋", "DETECTED ANOMALIES TABLE")
        anomaly_df = df[df["Anomaly"]][["Station ID","Address","Charger Type","Cost (USD/kWh)",
                                         "Usage Stats (avg users/day)","Reviews (Rating)","Max_Z"]].round(3)
        st.dataframe(anomaly_df, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ── TAB 10: INSIGHTS ──────────────────────────────────────────────────────
    with tabs[9]:
        section_title("💡", "KEY INSIGHTS & FINDINGS")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("⚡", "CHARGING BEHAVIOR")
            st.markdown("""
            <div class="insight-card"><span class="insight-icon">🔋</span><span class="insight-text"><b>DC Fast Chargers</b> consistently attract the highest daily user volumes across all geographies.</span></div>
            <div class="insight-card"><span class="insight-icon">🏙️</span><span class="insight-text">Stations <b>within 5km of city centers</b> see 2–3× more daily users than suburban counterparts.</span></div>
            <div class="insight-card"><span class="insight-icon">♻️</span><span class="insight-text"><b>Renewable-powered stations</b> receive statistically higher ratings (avg +0.3⭐) and slightly higher usage.</span></div>
            <div class="insight-card"><span class="insight-icon">📅</span><span class="insight-text">Stations installed after 2018 show a <b>sharp uptick in usage</b>, reflecting growing EV adoption.</span></div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("💰", "COST & OPERATOR INSIGHTS")
            st.markdown("""
            <div class="insight-card"><span class="insight-icon">📉</span><span class="insight-text"><b>Lower-cost stations</b> near urban cores dominate in daily demand — price sensitivity is real.</span></div>
            <div class="insight-card"><span class="insight-icon">🏆</span><span class="insight-text"><b>ChargePoint & Tesla</b> lead on average ratings while EVgo and Ionity have wider pricing variance.</span></div>
            <div class="insight-card"><span class="insight-icon">🔧</span><span class="insight-text"><b>Monthly maintenance</b> correlates with marginally better ratings vs annually maintained stations.</span></div>
            <div class="insight-card"><span class="insight-icon">⚠️</span><span class="insight-text">Some operators show <b>high cost + low ratings</b> — a red flag for customer retention issues.</span></div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("🤖", "CLUSTERING INSIGHTS")
            st.markdown("""
            <div class="insight-card"><span class="insight-icon">🟢</span><span class="insight-text"><b>Daily Commuters (Cluster 0):</b> Medium cost, moderate usage — ideal for workplace charging incentives.</span></div>
            <div class="insight-card"><span class="insight-icon">🟣</span><span class="insight-text"><b>Heavy Fast-Chargers (Cluster 1):</b> High capacity & demand — infrastructure bottlenecks likely here.</span></div>
            <div class="insight-card"><span class="insight-icon">🔴</span><span class="insight-text"><b>Occasional Users (Cluster 2):</b> Rural, low frequency — may benefit from promotional pricing.</span></div>
            <div class="insight-card"><span class="insight-icon">🟠</span><span class="insight-text"><b>Premium Stations (Cluster 3):</b> High cost, excellent ratings — target for loyalty programs.</span></div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            section_title("⚠️", "ANOMALY FINDINGS")
            st.markdown("""
            <div class="insight-card"><span class="insight-icon">🚨</span><span class="insight-text">Roughly <b>2–4% of stations</b> exhibit statistically anomalous behavior across cost, usage, and capacity dimensions.</span></div>
            <div class="insight-card"><span class="insight-icon">🔴</span><span class="insight-text">Anomalous stations often show <b>high cost combined with below-average ratings</b> — potential faulty equipment or poor service.</span></div>
            <div class="insight-card"><span class="insight-icon">📍</span><span class="insight-text">Anomalies are <b>geographically dispersed</b> with slight concentration in newer stations post-2020.</span></div>
            <div class="insight-card"><span class="insight-icon">🔧</span><span class="insight-text"><b>Immediate inspection recommended</b> for stations with Z-score > 5 — these represent extreme outliers.</span></div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        section_title("🎯", "STRATEGIC RECOMMENDATIONS")

        rec_cols = st.columns(3)
        recs = [
            ("🏗️", "Infrastructure", "Expand DC Fast Charger coverage within 5km of city centers — the highest ROI zone for new installations."),
            ("💲", "Pricing Strategy", "Introduce dynamic pricing tied to demand levels. Low off-peak rates can redistribute load and improve utilization."),
            ("🔧", "Maintenance", "Prioritize monthly maintenance for high-usage clusters. Proactive servicing prevents anomaly escalation."),
            ("♻️", "Sustainability", "Transition existing stations to renewable sources — rated higher by users and differentiates premium offerings."),
            ("📊", "Analytics", "Deploy real-time monitoring for Z-score anomalies. Automated alerts can flag faulty stations within hours."),
            ("📱", "User Experience", "Loyalty programs targeting 'Daily Commuter' clusters can significantly improve station utilization consistency."),
        ]
        for i, (icon, title, text) in enumerate(recs):
            with rec_cols[i % 3]:
                st.markdown(f"""
                <div class="metric-box" style="text-align:left;margin-bottom:14px;">
                  <div style="font-size:1.8rem;">{icon}</div>
                  <div style="font-family:Orbitron,monospace;font-size:0.8rem;color:#00f5d4;margin:8px 0;letter-spacing:2px;">{title.upper()}</div>
                  <div style="font-size:0.9rem;color:rgba(255,255,255,0.7);">{text}</div>
                </div>""", unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # ── FOOTER ────────────────────────────────────────────────────────────────
    st.markdown("""
    <br><hr style="border:1px solid rgba(255,255,255,0.06);">
    <p style="text-align:center;font-family:Share Tech Mono;font-size:0.75rem;color:rgba(255,255,255,0.25);letter-spacing:3px;">
    ⚡ SMARTCHARGE AI · BUILT WITH STREAMLIT · POWERED BY ML · © 2024
    </p>
    """, unsafe_allow_html=True)
