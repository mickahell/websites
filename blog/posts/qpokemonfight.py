import streamlit as st


def tag():
    tag = ["qiskit", "game"]
    date = "01/2021"
    return tag, date


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
    key = "pokemon"
    url = str("[go to up](#" + key + ")")

    st.header("A quantum robot who play Pokémon", anchor=key)
    preview = """
        A quantum game and algorithm to fight in Pokemon.
    """
    with st.expander(preview):
        article()
        st.markdown(url)
