import streamlit as st


def css():
    css = """
        <style>
            #MainMenu {visibility: hidden;}
            footer::before {content:'Xtra Orbitals™️ | Since 2021 | ';}
        </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def menu_app():
    pass


def menu_main():
    pass


def author():
    pass
