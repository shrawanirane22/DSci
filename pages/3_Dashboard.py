import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

h1, h2, h3 {
    color: #00f5d4;
}

div.stButton > button {
    background-color: #00f5d4;
    color: black;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

df = pd.read_csv("data/final_optimized_dataset.csv")

st.title("📊 Overall Disaster Impact Overview")

# FIXED GRAPH
fig1 = px.bar(
    df,
    x="Type",   # ✅ correct column
    y="Change (%)",   # ✅ correct column
    color="Impact",   # ✅ correct column
    title="Overall Impact by Disaster Type"
)

st.plotly_chart(fig1, use_container_width=True)

# SECOND GRAPH
fig2 = px.box(
    df,
    x="Company",
    y="Change (%)",
    title="Company-wise Impact Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

st.markdown("""
<style>
.stApp {
    background-image: radial-gradient(circle at 20% 20%, rgba(0,255,255,0.2), transparent),
                      radial-gradient(circle at 80% 80%, rgba(255,0,255,0.2), transparent);
}
</style>
""", unsafe_allow_html=True)