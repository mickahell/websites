import streamlit as st
import sys
from os import path

sys.path.append(path.abspath('../'))

import function


def tag():
    tag = ["hackaton", "game"]
    date = "04/2021"
    lecture_time = "3"
    key = "qchack"
    title = "QChack | Honor mention"
    extra = ""
    preview = """
            Preview ...............................................
            ..........................................................;
            ...........................................................
            """

    return tag, date, lecture_time, key, title, extra, preview


def article():
    article = """
        BlablablablablablablaBlablablablablablablaBlablablablablablablaBlablablablablablabla
        BlablablablablablablaBlablablablablablablaBlablablablablablablaBlablablablablablabla
        BlablablablablablablaBlablablablablablablaBlablablablablablablaBlablablablablablabla
        BlablablablablablablaBlablablablablablablaBlablablablablablablaBlablablablablablabla
        BlablablablablablablaBlablablablablablablaBlablablablablablablaBlablablablablablabla
    """
    st.write(article, unsafe_allow_html=True)


def preview():
    tags, date, lecture_time, key, title, extra, preview = tag()

    function.metadata(tags, date, lecture_time, key, title, extra)

    with st.expander(preview):
        article()
        st.markdown(str("[go to up](#" + key + ")"))
