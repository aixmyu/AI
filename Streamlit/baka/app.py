#streamlit project app: baka AI
#@aixmyu

# Windows command prompt
#streamlit\.venv\Scripts\activate.bat
#streamlit run app.py
#deactivate

import streamlit as st
import os

# Set the path as environment variable
os.environ['PATH'] = 'C:\Users\reths\tools\AI\streamlit\.venv'
# Load model directly
# from transformers import AutoTokenizer, AutoModelForCausalLM
#tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6b")
#model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-6b")

cat = st.image
st.write('welcome baka')
st.write('what is ur name?')
if st.text_input("Your name", key="name"):
    st.balloons()
# You can access the value at any point with:)st.session_state.name
