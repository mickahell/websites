import streamlit as st
import quantum_lab
import quantum_app

st.set_page_config(page_title="Quantum Lab", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
#st.markdown(hide_menu_style, unsafe_allow_html=True)

PAGES = {
    #"Lab": quantum_lab,
    "Dockeurise": quantum_app,
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Which page do you want to see", list(PAGES.keys()))
page = PAGES[selection]
page.app()
