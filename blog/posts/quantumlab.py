import streamlit as st


def tag():
    tag = ["experiment"]
    date = "03/2021"
    return tag, date


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
    key = "lab"
    url = str("[go to up](#" + key + ")")

    st.header("Docker images for Quantum Lab", anchor=key)
    preview = """
        A simple docker image to simulate a full Quantum laboratory.
    """
    with st.expander(preview):
        article()
        st.markdown(url)
