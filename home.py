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

st.markdown("""
<style>
.stApp {
    background-image: radial-gradient(circle at 20% 20%, rgba(0,255,255,0.2), transparent),
                      radial-gradient(circle at 80% 80%, rgba(255,0,255,0.2), transparent);
}
</style>
""", unsafe_allow_html=True)