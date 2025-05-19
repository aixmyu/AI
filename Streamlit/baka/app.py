#streamlit project app: baka AI
#@aixmyu

# Windows command prompt
#streamlit\.venv\Scripts\activate.bat
#streamlit run app.py
#deactivate

import streamlit as st
# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6b")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-6b")

cat = st.image
st.write('welcome baka')
st.write('what is ur name?')
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
