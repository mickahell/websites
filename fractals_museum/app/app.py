# App control
import streamlit as st
import home
import common
import perso_fractal
import study_result


st.set_page_config(page_title="Beta : Fractals Museum", page_icon=":art:", layout='wide', initial_sidebar_state='auto')

common.css()
common.menu_app()

PAGES = {
    "Home": home,
    "Creation": perso_fractal,
    "Study": study_result,
}
st.sidebar.header(':art: Science Museum')
st.sidebar.subheader('Navigation')
selection = st.sidebar.selectbox("Which page do you want to see", list(PAGES.keys()))
page = PAGES[selection]
page.app()
