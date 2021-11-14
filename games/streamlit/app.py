import streamlit as st
import home
import qnim
import qpokemon
from common import common

st.set_page_config(page_title="Games", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

common.css()
common.menu_app()

title = """
<div align="center">
    <h1>Games</h1>
</div>
<br /><br />
"""
st.markdown(title, unsafe_allow_html=True)

PAGES = {
    "Home": home,
    "QPokémon fight": qpokemon,
    "QNim game": qnim,
}

selection = st.sidebar.radio("Games", list(PAGES.keys()))
page = PAGES[selection]
page.app()
