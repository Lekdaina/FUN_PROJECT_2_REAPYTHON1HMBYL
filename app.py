import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="Chatbot Offline Gratis", layout="centered")
st.title("💬 AI Chatbot Bubble Style (Gratis Tanpa API)")
st.caption("Powered by DialoGPT – 100% Offline")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("Tulis pesan di sini...")

if st.button("Kirim") and user_input:
    st.session_state.history.append(("user", user_input))
    response = get_response(user_input)
    st.session_state.history.append(("bot", response))

# Tampilkan bubble
for role, msg in st.session_state.history:
    bubble_class = "user-bubble" if role == "user" else "bot-bubble"
    st.markdown(f'<div class="{bubble_class}">{msg}</div>', unsafe_allow_html=True)