import streamlit as st
import home
import candidature
import common

st.set_page_config(page_title="Candidatures", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

common.css()

title = """
<div align="center">
    <h1>Candidatures</h1>
</div>
<br /><br />
"""
st.markdown(title, unsafe_allow_html=True)

PAGES = {
    "Home": home,
    "Candidature": candidature
}

selection = st.sidebar.radio("Candidatures", list(PAGES.keys()))

st.sidebar.write("---")

page = PAGES[selection]
page.app()
