#streamlit project app: baka AI
#@aixmyu

# Windows command prompt
#streamlit\.venv\Scripts\activate.bat
#streamlit run app.py
#deactivate

import streamlit as st

# Define the pages
main_page = st.Page("welcome.py", title="Welcome", icon="🎈")
page_2 = st.Page("page_2.py", title="Page 2", icon="❄️")
page_3 = st.Page("page_3.py", title="Page 3", icon="❄️")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3])

# Run the selected page
pg.run()

# Load model directly
# from transformers import AutoTokenizer, AutoModelForCausalLM
#tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6b")
#model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-6b")


