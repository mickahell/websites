import streamlit as st


def tag():
    tag = ["hackaton", "game"]
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
    key = "qchack"
    url = str("[go to up](#" + key + ")")

    st.header("QChack | Honor mention", anchor=key)
    preview = """
        Preview ...............................................
        ..........................................................;
        ...........................................................
    """
    with st.expander(preview):
        article()
        st.markdown(url)
