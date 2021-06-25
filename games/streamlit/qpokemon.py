import streamlit as st


def app():
    st.write("# Quantum Pokémon fight")

    rules = st.beta_expander("Rules", expanded=False)
    rules_view = """
    A Pokémon fight is a turn by turn game, each opponent as a team of 3 Pokémons and the last who still have Pokémon in shape win the game !  
    At each turn the fastest Pokémon attack first, if the speed stats are the same the choice will be random.  
    Each fire, electric, ice and poison attack can inflicted (almost) permanent damages and stats alteration :
    
    |   Type   |          Effect          |    Stats    |
    |:--------:|:------------------------:|:-----------:|
    | Fire     | Permanent damages        | drop attack |
    | Ice      | Can't attack             |             |
    | Electric | Can not attack sometimes | drop speed  |
    | Poison   | Permanent damages        |             |
        """
    rules.write(rules_view, unsafe_allow_html=True)

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
