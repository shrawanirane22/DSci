import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Load data
df = pd.read_csv("data/final_optimized_dataset.csv")
df["Disaster_Date"] = pd.to_datetime(df["Disaster_Date"])
df["Year"] = df["Disaster_Date"].dt.year

st.title("🌍 Disaster Impact Overview")

# ------------------- METRICS -------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Events", len(df))
col2.metric("Avg Change (%)", round(df["Change (%)"].mean(), 2))
col3.metric("Most Common Impact", df["Impact"].mode()[0])

# ------------------- GRAPHS -------------------
col1, col2 = st.columns(2)

# Impact by Type
with col1:
    fig1 = px.bar(
        df,
        x="Type",
        y="Change (%)",
        color="Impact",
        title="Impact by Disaster Type"
    )
    st.plotly_chart(fig1, use_container_width=True)

# Company Distribution
with col2:
    fig2 = px.box(
        df,
        x="Company",
        y="Change (%)",
        title="Company-wise Impact"
    )
    st.plotly_chart(fig2, use_container_width=True)

# Trend
st.subheader("📈 Trend Over Time")

fig3 = px.line(
    df,
    x="Disaster_Date",
    y="Change (%)",
    color="Company"
)

st.plotly_chart(fig3, use_container_width=True)