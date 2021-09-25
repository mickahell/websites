import streamlit as st
import sys
from os import path

sys.path.append(path.abspath('../'))

import function


def tag():
    tag = ["qiskit", "game"]
    date = "01/2021"
    lecture_time = "7"
    key = "pokemon"
    title = "A quantum robot who play Pokemon"
    extra = ""
    preview = """A quantum game and algorithm to fight in Pokemon."""

    return tag, date, lecture_time, key, title, extra, preview


def article():
    article_view = """
        <iframe
            title="Quantum Pokémon Fight article"
            width="100%"
            height="900"
            src="https://fullstackquantumcomputation.tech/blog/post-quantum-pokemon-fight/">
        </iframe>
        """
    st.write(article_view, unsafe_allow_html=True)


def preview():
    tags, date, lecture_time, key, title, extra, preview = tag()

    function.metadata(tags, date, lecture_time, key, title, extra)

    with st.expander(preview):
        article()
        st.markdown(str("[go to up](#" + key + ")"))
