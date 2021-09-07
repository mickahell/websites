import streamlit as st
import menu
import sys
from os import path

sys.path.append(path.abspath('posts/'))

import advocate
import qchack
import qpokemonfight
import quantronauts

st.set_page_config(page_title="Blog", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

menu.css()
menu.menu_app()

title = """
<div align="center">
    <h1>Blog</h1>
</div>
<br /><br />
"""
st.markdown(title, unsafe_allow_html=True)

POSTS = [
    advocate,
    qchack,
    quantronauts,
    qpokemonfight,
]

for i in POSTS:
    i.preview()
