import streamlit as st


def tag():
    tag = ["qiskit", "about"]
    date = "2021"
    return tag, date


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
    key = "advocate"
    url = str("[go to up](#" + key + ")")

    st.header("Became advocate !", anchor=key)
    preview = """
        Preview ...............................................
        ..........................................................;
        ...........................................................
    """
    with st.expander(preview):
        article()
        st.markdown(url)
