import streamlit as st
import home
import qnim
import qpokemon
import common
import to_github

st.set_page_config(page_title="Games", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

common.css()
common.menu_app()

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

st.sidebar.write("---")

with st.sidebar.expander("Feedback"):
    with st.form("feedback", clear_on_submit=True):
        subject_select = st.radio("Subject", list(PAGES.keys()))
        subject = PAGES[subject_select].info()
        content = st.text_area("Content")
        submitted = st.form_submit_button("Submit")
        if submitted:
            if len(content) > 0:
                to_github.feedbacks(subject=subject, content=content)
                st.write("Thanks for submitting your feedbacks ✌️")
            else:
                st.write("You forget your feedback...")
page = PAGES[selection]
page.app()
