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

# FIX DATE COLUMN
df['Disaster_Date'] = pd.to_datetime(df['Disaster_Date'])
df['Year'] = df['Disaster_Date'].dt.year

st.title("📊 Interactive Dashboard")

# USER INPUT
company = st.selectbox("Select Company", df["Company"].unique())

year_range = st.slider(
    "Select Year Range",
    int(df["Year"].min()),
    int(df["Year"].max()),
    (2015, 2024)
)

disaster_type = st.selectbox(
    "Select Disaster Type",
    ["All"] + list(df["Type"].unique())
)

# FILTER
filtered = df[
    (df["Company"] == company) &
    (df["Year"] >= year_range[0]) &
    (df["Year"] <= year_range[1])
]

if disaster_type != "All":
    filtered = filtered[filtered["Type"] == disaster_type]

# GRAPH LAYOUT
col1, col2 = st.columns(2)

# STOCK IMPACT TREND (approx representation)
with col1:
    fig1 = px.line(
        filtered,
        x="Disaster_Date",
        y="Change (%)",
        title="Stock Impact Trend"
    )
    st.plotly_chart(fig1, use_container_width=True)

# IMPACT ANALYSIS
with col2:
    fig2 = px.bar(
        filtered,
        x="Disaster",
        y="Change (%)",
        color="Impact",
        title="Disaster Impact"
    )
    st.plotly_chart(fig2, use_container_width=True)

# INSIGHTS
st.subheader("📌 Insights")

if len(filtered) > 0:
    avg = filtered["Change (%)"].mean()

    if avg < -5:
        st.error("🔴 High Risk")
    elif avg < -2:
        st.warning("🟡 Moderate Risk")
    else:
        st.success("🟢 Low Risk")

st.markdown("""
<style>
.stApp {
    background-image: radial-gradient(circle at 20% 20%, rgba(0,255,255,0.2), transparent),
                      radial-gradient(circle at 80% 80%, rgba(255,0,255,0.2), transparent);
}
</style>
""", unsafe_allow_html=True)