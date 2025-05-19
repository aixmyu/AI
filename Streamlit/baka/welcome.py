import streamlit as st

# Main page content
st.markdown("# Welcome 🎈")
st.sidebar.markdown("# Welcome 🎈")

cat = st.image
st.write('welcome baka')
st.write('what is ur name?')
if st.text_input("Your name", key="name"):
    st.balloons()
# You can access the value at any point with:)st.session_state.name