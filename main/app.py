import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Xtra Orbitals", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

css = """
    <style>
        #MainMenu {visibility: hidden;}
        footer::before {content:'Xtra Orbitals™️ | Since 2021 | ';}
        
        .header{
            background: #555;
            color: #f1f1f1; 
            position: fixed;
            top: 0;}
            
        .header {
            overflow: hidden;
            background-color: #333;}

        .header a {
            float: left;
            color: #f2f2f2;
            text-align: center;
            padding: 10px 16px;
            text-decoration: none;
            font-size: 15px;}

        .header a:hover {
            background-color: #ddd;
            color: black;}
        
        .header a.separateur {
            background-color: #000;
            color: white;}

        .header a.active {
            background-color: #FFF;
            color: black;}
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

# Menu
menu = """
    <div class="header">
        <a class="active" href="http://xtraorbitals.xyz"><b>Home</b></a>
        <a href="http://quantum-lab.xtraorbitals.xyz"><b>Lab</b></a>
        <a href="http://games.xtraorbitals.xyz"><b>Games</b></a>
        <a class="separateur" <b>|</b></a>
        <a href="http://about.xtraorbitals.xyz"><b>About</b></a>
    </div>
"""
st.markdown(menu, unsafe_allow_html=True)

title = """
    <div align="center">
        <h1>Xtra Orbitals</h1>
    </div>
    <br /><br />
"""
st.markdown(title, unsafe_allow_html=True)

here = """
    ## One platform to unify them all
    This platform has as purpose to unify and make available all of my projects, so **Welcome** in my **webservices platform** !
"""
st.markdown(here)

col0, col1, col2, col3 = st.beta_columns(4)
lab = col0.beta_expander("Laboratories", True)
lab.write("""
    The laboratory is a place for Jupyter apps and tuto on how to Dockerize quantum apps.
    <form action="https://quantum-lab.xtraorbitals.xyz">
        <input type="submit" value="Quantum Lab" />
    </form>
    <br />
""", unsafe_allow_html=True)

games = col1.beta_expander("Games", True)
games.write("""
    Place for testing and playing games against robots. Will you succeed to win ?!
    <form action="https://games.xtraorbitals.xyz">
        <input type="submit" value="Games" />
    </form>
    <br />
""", unsafe_allow_html=True)

museum = col2.beta_expander("Museum", False)
museum.write("""
    Where science and art are ONE !
    <br />
""", unsafe_allow_html=True)

about = col3.beta_expander("About", True)
about.write("""
    Everything you always wanted to know without daring to ask, about here.
    <form action="https://about.xtraorbitals.xyz">
        <input type="submit" value="About" />
    </form>
    <br />
""", unsafe_allow_html=True)

## Tag cloud
# Create some sample text
# text = 'Quantum, games, AI, robots, pokemon, lab, python, qiskit, pennylane, fractals, fun'

components.html("""
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true});</script>
<br /><br />
<div class="mermaid">
%%{init: {'theme': 'base', 'themeVariables': {'primaryTextColor': '#FFF', 'primaryColor': '#000ccc', "fontSize": "20px"}}}%%
journey
            title Apps status
            section Laboratories
              Qiskit: 7: On
              Pennylane: 7: On
              Cirq: 7: On
            section Games
              qPokemon: 7: On
              qNim: 7: On
            section Fractals
              Museum: 0: Building
              auto-fractal: 0: Building
            section qMaths
</div>
""", height=600, scrolling=False)
