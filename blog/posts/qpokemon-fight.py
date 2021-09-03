import streamlit as st


def app():
    article = st.expander("How does it works ?", expanded=True)
    article_view = """
        <iframe
            title="Quantum Pokémon Fight article"
            width="100%"
            height="720"
            src="https://fullstackquantumcomputation.tech/blog/post-quantum-pokemon-fight/">
        </iframe>
        """
    article.write(article_view, unsafe_allow_html=True)
