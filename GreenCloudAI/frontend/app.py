import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.greencloud_ai import analyze_cloud_data

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="GreenCloud AI",
    page_icon="🌿",
    layout="wide"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>

.stApp{
background: linear-gradient(
135deg,
#0B1020,
#0F172A,
#111827
);
}

/* Sidebar */

[data-testid="stSidebar"]{
background: rgba(10,15,30,0.95);
border-right:1px solid rgba(255,255,255,0.1);
}

/* Hero Section */

.hero-container{
background: rgba(255,255,255,0.06);
backdrop-filter: blur(20px);
border:1px solid rgba(255,255,255,0.1);
padding:40px;
border-radius:25px;
box-shadow:0 0 40px rgba(0,229,255,0.15);
margin-bottom:30px;
}

.hero-title{
font-size:60px;
font-weight:800;
color:white;
}

.hero-subtitle{
font-size:22px;
color:#00E676;
margin-top:10px;
}

.metric-card{
background: rgba(255,255,255,0.05);
backdrop-filter: blur(15px);
padding:25px;
border-radius:20px;
text-align:center;
border:1px solid rgba(255,255,255,0.1);
transition:0.3s;
}

.metric-card:hover{
transform: translateY(-5px);
box-shadow:0 0 30px rgba(0,229,255,0.3);
}

.metric-number{
font-size:40px;
font-weight:700;
color:#00E676;
}

.metric-label{
font-size:18px;
color:white;
}

.section-title{
font-size:30px;
font-weight:700;
color:white;
margin-top:20px;
margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# SIDEBAR
# -----------------------------------

with st.sidebar:

    st.markdown("## 🌿 GreenCloud AI")

    selected = option_menu(
        menu_title=None,
        options=[
            "Home",
            "Dashboard",
            "Analytics",
            "Sustainability",
            "IBM Assistant"
        ],
        icons=[
            "house",
            "speedometer2",
            "bar-chart",
            "leaf",
            "robot"
        ],
        default_index=0
    )

# -----------------------------------
# HOME
# -----------------------------------

if selected == "Home":

    st.markdown("""
    <div class="hero-container">

    <div class="hero-title">
    🌿 GreenCloud AI
    </div>

    <div class="hero-subtitle">
    Intelligent Cloud Resource Optimization
    for Sustainable Data Centers
    </div>

    <br>

    <h4 style="color:white;">
    Optimize • Predict • Sustain
    </h4>

    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
        <div class="metric-number">150</div>
        <div class="metric-label">Servers</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
        <div class="metric-number">2.4</div>
        <div class="metric-label">MWh Saved</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
        <div class="metric-number">1.9</div>
        <div class="metric-label">CO₂ Tons Reduced</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
        <div class="metric-number">94</div>
        <div class="metric-label">Green Score</div>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------
# DASHBOARD
# -----------------------------------

elif selected == "Dashboard":

    st.markdown(
        "<div class='section-title'>🚀 Cloud Optimization Dashboard</div>",
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "Upload Cloud Dataset",
        type=["csv"]
    )

    if uploaded_file:

        df = pd.read_csv(uploaded_file)

        result = analyze_cloud_data(df)

        st.success("Dataset analyzed successfully!")

        st.subheader("Analysis Results")

        st.dataframe(result)

# -----------------------------------
# ANALYTICS
# -----------------------------------

elif selected == "Analytics":

    st.markdown(
        "<div class='section-title'>📊 Analytics Center</div>",
        unsafe_allow_html=True
    )

    st.info(
        "Interactive charts will be connected to your dataset next."
    )

# -----------------------------------
# SUSTAINABILITY
# -----------------------------------

elif selected == "Sustainability":

    st.markdown(
        "<div class='section-title'>🌱 Sustainability Center</div>",
        unsafe_allow_html=True
    )

    st.metric(
        "Green Score",
        "94/100"
    )

    st.metric(
        "Estimated CO₂ Reduction",
        "1.9 Tons"
    )

    st.metric(
        "Energy Saved",
        "2.4 MWh"
    )

# -----------------------------------
# IBM ASSISTANT
# -----------------------------------
elif selected == "IBM Assistant":

    st.markdown(
        "<div class='section-title'>🤖 IBM Watson Assistant</div>",
        unsafe_allow_html=True
    )

    user_question = st.chat_input("Ask GreenCloud AI...")

    if user_question:

        st.chat_message("user").write(user_question)

        question = user_question.lower()

        if "cpu" in question:
            answer = "High CPU usage means the server may need more resources. Low CPU usage means resources can be reduced."

        elif "memory" in question:
            answer = "Memory usage helps identify overloaded and underutilized servers."

        elif "storage" in question:
            answer = "Storage optimization can reduce cloud costs and energy consumption."

        elif "green score" in question:
            answer = "Green Score measures sustainability and energy efficiency."

        elif "sustainability" in question:
            answer = "GreenCloud AI improves sustainability by reducing unused cloud resources."

        elif "cloud" in question:
            answer = "Cloud optimization helps improve performance while reducing energy consumption."

        else:
            answer = "GreenCloud AI recommends optimizing cloud resources to save energy and reduce carbon emissions."

        st.chat_message("assistant").write(answer)
