import streamlit as st


def app():
    st.write("# Quantum Pokémon fight")
    article = st.beta_expander("How does it works ?", expanded=False)
    article_view = """
        <iframe
            title="Quantum Pokémon Fight article"
            width="100%"
            height="720"
            src="https://fullstackquantumcomputation.tech/blog/post-quantum-pokemon-fight/">
        </iframe>
        """
    article.write(article_view, unsafe_allow_html=True)

    qpokemon = st.beta_expander("Game", expanded=True)
    qpokemon_view = """
    <iframe
        title="Quantum Pokémon Fight"
        width="100%"
        height="510"
        src="https://qpokemon-fight.xtraorbitals.xyz">
    </iframe>
    """
    qpokemon.write(qpokemon_view, unsafe_allow_html=True)
    st.write("<h3>See on <a href='https://qpokemon-fight.xtraorbitals.xyz'><b>QPokémon game page</b></a></h3>", unsafe_allow_html=True)
    badge = """
        [![GitHub release (latest by date)](https://img.shields.io/github/v/release/mickahell/quantum_pokemon-fight)](https://github.com/mickahell/quantum_pokemon-fight/releases)
        """
    st.markdown(badge)
