import streamlit as st


def tag():
    tag = ["hackaton", "coop"]
    date = "02/2021"
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
    key = "quantronauts"
    url = str("[go to up](#" + key + ")")

    st.header("Xanadu Hackaton", anchor=key)
    preview = """
        Preview ...............................................
        ..........................................................;
        ...........................................................
    """
    with st.expander(preview):
        article()
        st.markdown(url)
