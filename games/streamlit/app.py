import streamlit as st
import home
import qnim
import qpokemon

st.set_page_config(page_title="Games", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

css = """
    <style>
        #MainMenu {visibility: hidden;}
        footer::before {content:'Xtra Orbitals™️ | Since 2021 | ';}

        .header{
            background: #555;
            color: #f1f1f1; 
            position: fixed;
            top: 0;} 

        .header {
            overflow: hidden;
            background-color: #333;}

        .header a {
            float: left;
            color: #f2f2f2;
            text-align: center;
            padding: 10px 16px;
            text-decoration: none;
            font-size: 15px;}

        .header a:hover {
            background-color: #ddd;
            color: black;}

        .header a.separateur {
            background-color: #000;
            color: white;}

        .header a.active {
            background-color: #FFF;
            color: black;}
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

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
