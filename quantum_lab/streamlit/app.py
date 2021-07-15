import streamlit as st
import quantum_lab
import quantum_app
import article

st.set_page_config(page_title="Online Quantum Lab", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

hide_menu_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer::before {content:'Xtra Orbitals™️ | Since 2021 | ';}
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

PAGES = {
    "Online Quantum Lab": quantum_lab,
    "Quantum App": quantum_app,
    "Article": article,
}

col_select, col_null = st.beta_columns([1, 4])

selection = col_select.selectbox("Navigation", list(PAGES.keys()))
page = PAGES[selection]
page.app()

