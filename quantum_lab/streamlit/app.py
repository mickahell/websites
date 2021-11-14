import streamlit as st
import quantum_lab
import quantum_app
import article
from common import common

st.set_page_config(page_title="Online Quantum Lab", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

common.css()
common.menu_app()

PAGES = {
    "Online Quantum Lab": quantum_lab,
    "Quantum App": quantum_app,
    "Article": article,
}

col_select, col_null = st.columns([1, 4])

selection = col_select.selectbox("Navigation", list(PAGES.keys()))
page = PAGES[selection]
page.app()

