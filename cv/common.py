import streamlit as st


def css():
    """CSS basic page
    Arg: Nothing
    Return: Nothing
    """
    title = """
    <div align="center">
        <h1>Resume</h1>
    </div>
    <br /><br />
    """
    st.markdown(title, unsafe_allow_html=True)
    footer = """
        <style>
            #MainMenu {visibility: hidden;}
            footer::before {content:'Xtra Orbitals™️ | Since 2021 | ';}
        </style>
    """
    st.markdown(footer, unsafe_allow_html=True)
