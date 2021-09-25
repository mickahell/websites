import streamlit as st
import sys
from os import path

sys.path.append(path.abspath('../'))

import function


def tag():
    tag = ["experiment"]
    date = "03/2021"
    lecture_time = "3"
    key = "lab"
    title = "Docker images for Quantum Lab"
    extra = ""
    preview = """A simple docker image to simulate a full Quantum laboratory."""

    return tag, date, lecture_time, key, title, extra, preview


def article():
    article_view = """
        <iframe
            title="Quantum Laboratory"
            width="100%"
            height="900"
            src="https://fullstackquantumcomputation.tech/blog/post-quantum-lab/">
        </iframe>
        """
    st.write(article_view, unsafe_allow_html=True)


def preview():
    tags, date, lecture_time, key, title, extra, preview = tag()

    function.metadata(tags, date, lecture_time, key, title, extra)

    with st.expander(preview):
        article()
        st.markdown(str("[go to up](#" + key + ")"))
