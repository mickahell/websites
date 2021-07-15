import streamlit as st

st.set_page_config(page_title="Xtra Orbitals", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

hide_menu_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer::before {content:'Xtra Orbitals™️ | Since 2021 | ';}
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

header = """
<div align="center">
    <h1>Xtra Orbitals</h1>
</div>
<br /><br />
"""
st.markdown(header, unsafe_allow_html=True)
