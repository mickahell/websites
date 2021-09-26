# App control
import streamlit as st
import home
import menu
import perso_fractal


st.set_page_config(page_title="Beta : Fractals Museum", page_icon=":art:", layout='wide', initial_sidebar_state='auto')

menu.css()
menu.menu_app()

PAGES = {
    "Home": home,
    "Creation": perso_fractal,
}
st.sidebar.header(':art: Science Museum')
st.sidebar.subheader('Navigation')
selection = st.sidebar.selectbox("Which page do you want to see", list(PAGES.keys()))
page = PAGES[selection]
page.app()
