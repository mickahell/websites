import streamlit as st
import quantum_lab
import quantum_app
import article

st.set_page_config(page_title="Online Quantum Lab", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

css = """
    <style>
        #MainMenu {visibility: hidden;}
        footer::before {content:'Xtra Orbitals™️ | Since 2021 | ';}

        .header {
            background: #555;
            color: #f1f1f1; 
            position: fixed;
            overflow: hidden;
            background-color: #333;
            top: 34px;
            left: 190px;}

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

        .logo a {
            color: black;
            position: fixed;
            top: 10px;}

        .logo img {
            width: 100px;
            opacity: 0.7;}

        .logo img:hover {
        opacity: 1;}
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

# Menu
menu = """
    <div class="logo">
        <a href="https://xtraorbitals.xyz">
            <img src="https://raw.githubusercontent.com/mickahell/xtraorbitals.xyz/main/logo.png"/>
        </a>
    </div>
    <div class="header">
        <a href="https://xtraorbitals.xyz"><b>Home</b></a>
    </div>
"""
st.markdown(menu, unsafe_allow_html=True)

PAGES = {
    "Online Quantum Lab": quantum_lab,
    "Quantum App": quantum_app,
    "Article": article,
}

col_select, col_null = st.columns([1, 4])

selection = col_select.selectbox("Navigation", list(PAGES.keys()))
page = PAGES[selection]
page.app()

