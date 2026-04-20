import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Load data
df = pd.read_csv("data/final_optimized_dataset.csv")

df["Disaster_Date"] = pd.to_datetime(df["Disaster_Date"])
df["Year"] = df["Disaster_Date"].dt.year

st.title("📊 Interactive Analysis")

# ------------------- SIDEBAR -------------------
st.sidebar.header("Filters")

companies = st.sidebar.multiselect(
    "Select Companies",
    df["Company"].unique(),
    default=df["Company"].unique()
)

year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["Year"].min()),
    int(df["Year"].max()),
    (2015, 2024)
)

disaster_type = st.sidebar.multiselect(
    "Select Disaster Type",
    df["Type"].unique(),
    default=df["Type"].unique()
)

# ------------------- FILTER -------------------
filtered = df[
    (df["Company"].isin(companies)) &
    (df["Year"] >= year_range[0]) &
    (df["Year"] <= year_range[1]) &
    (df["Type"].isin(disaster_type))
]

# ------------------- METRICS -------------------
col1, col2 = st.columns(2)

col1.metric("Total Events", len(filtered))
col2.metric("Avg Change (%)", round(filtered["Change (%)"].mean(), 2))

# ------------------- GRAPHS -------------------
col1, col2 = st.columns(2)

# Trend
with col1:
    fig1 = px.line(
        filtered,
        x="Disaster_Date",
        y="Change (%)",
        color="Company",
        title="Stock Impact Trend"
    )
    st.plotly_chart(fig1, use_container_width=True)

# Disaster Impact
with col2:
    fig2 = px.bar(
        filtered,
        x="Disaster",
        y="Change (%)",
        color="Impact",
        title="Disaster Impact"
    )
    st.plotly_chart(fig2, use_container_width=True)

# ------------------- EXTRA GRAPH -------------------
st.subheader("📦 Impact Distribution")

fig3 = px.box(
    filtered,
    x="Impact",
    y="Change (%)",
    color="Company"
)

st.plotly_chart(fig3, use_container_width=True)

# ------------------- INSIGHTS -------------------
st.subheader("📌 Insights")

if len(filtered) > 0:
    avg = filtered["Change (%)"].mean()

    if avg < -5:
        st.error("🔴 High Risk")
    elif avg < -2:
        st.warning("🟡 Moderate Risk")
    else:
        st.success("🟢 Low Risk")