import streamlit as st


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

st.title("📘 About the Project")

st.markdown("""
### 🔍 What is this project?

This project combines:
- Stock market data
- Natural disaster data

We analyze how disasters affect stock prices using time-window analysis.

---

### ⚙️ Methodology

1. Identify disaster event
2. Take stock prices before and after
3. Calculate percentage change
4. Classify impact:
   - 🔴 High
   - 🟡 Medium
   - 🟢 Low

---

### 💡 Why is this useful?

- Investors can assess risk
- Companies can evaluate resilience
- Analysts can study patterns
""")

st.markdown("""
<style>
.stApp {
    background-image: radial-gradient(circle at 20% 20%, rgba(0,255,255,0.2), transparent),
                      radial-gradient(circle at 80% 80%, rgba(255,0,255,0.2), transparent);
}
</style>
""", unsafe_allow_html=True)