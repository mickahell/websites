import streamlit as st

st.set_page_config(page_title="Games", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

header = """
<div align="center">
    <h1>Games</h1>
</div>
<br /><br />
"""
st.markdown(header, unsafe_allow_html=True)
