# App control
import streamlit as st
import home
import perso_fractal

st.set_page_config(page_title="Fractals Museum", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

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

# Menu
menu = """
    <div class="header">
        <a class="active" href="http://xtraorbitals.xyz"><b>Home</b></a>
        <a href="http://quantum-lab.xtraorbitals.xyz"><b>Lab</b></a>
        <a href="http://games.xtraorbitals.xyz"><b>Games</b></a>
        <a class="separateur" <b>|</b></a>
        <a href="http://about.xtraorbitals.xyz"><b>About</b></a>
    </div>
"""
st.markdown(menu, unsafe_allow_html=True)

PAGES = {
    "Home": home,
    "Creation": perso_fractal,
}
st.sidebar.title('Navigation')
selection = st.sidebar.selectbox("Which page do you want to see", list(PAGES.keys()))
page = PAGES[selection]
page.app()
