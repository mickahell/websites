import streamlit as st
import streamlit.components.v1 as components
import urllib.request


def isrunning(url):
    status = urllib.request.urlopen(url).getcode()
    if status == 200:
        return [url, "ok"]
    else:
        return [url, "ko"]


st.set_page_config(page_title="Xtra Orbitals", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

css = """
    <style>
        #MainMenu {visibility: hidden;}
        footer::before {content:'Xtra Orbitals™️ | Since 2021 | ';}
        
        .header {
            background: #555;
            color: #f1f1f1; 
            position: fixed;
            overflow: hidden;
            background-color: #333;
            top: 34px;
            left: 190px;}

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
        
        .logo a {
            color: black;
            position: fixed;
            top: 10px;}
            
        .logo img {
            width: 100px;
            opacity: 0.7;}
        
        .logo img:hover {
        opacity: 1;}
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

# Menu
menu = """
    <div class="logo">
        <a href="https://xtraorbitals.xyz">
            <img src="https://raw.githubusercontent.com/mickahell/xtraorbitals.xyz/main/logo.png"/>
        </a>
    </div>
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

col0, col1, col2, col3 = st.columns(4)
lab = col0.expander("Laboratories", True)
lab.write("""
    The laboratory is a place for Jupyter apps and tuto on how to Dockerize quantum apps.
    <form action="https://quantum-lab.xtraorbitals.xyz">
        <input type="submit" value="Quantum Lab" />
    </form>
    <br />
""", unsafe_allow_html=True)

games = col1.expander("Games", True)
games.write("""
    Place for testing and playing games against robots. Will you succeed to win ?!
    <form action="https://games.xtraorbitals.xyz">
        <input type="submit" value="Games" />
    </form>
    <br />
""", unsafe_allow_html=True)

museum = col2.expander("Museum", False)
museum.write("""
    Where science and art are ONE !
    <br />
""", unsafe_allow_html=True)

about = col3.expander("About", True)
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

## Check apps status

status = """
    ## Status
"""
st.markdown(status)

status_qiskit = isrunning("https://qiskit.xtraorbitals.xyz")
status_penny = isrunning("https://pennylane.xtraorbitals.xyz")
status_cirq = isrunning("https://cirq.xtraorbitals.xyz")
status_qpokemon = isrunning("https://qpokemon-fight.xtraorbitals.xyz/")
status_qnim = isrunning("https://qnim-game.xtraorbitals.xyz/")

# streamlit page
status_games = isrunning("https://games.xtraorbitals.xyz/")
status_about = isrunning("https://about.xtraorbitals.xyz/")
status_lab = isrunning("https://quantum-lab.xtraorbitals.xyz/")

for i in (status_qiskit, status_penny, status_cirq, status_qpokemon, status_qnim, status_games, status_about, status_lab):
    if i[1] != "ok":
        msg = i[0], " : is down !"
        st.write(msg)

components.html("""
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true});</script>
<br /><br />
<div class="mermaid">
%%{init: {'theme': 'base', 'themeVariables': {'primaryTextColor': '#FFF', 'primaryColor': '#000ccc', "fontSize": "20px"}}}%%
journey
            title Apps version
            section Laboratories
              Qiskit: 7: v1
              Pennylane: 7: v1
              Cirq: 7: v1
            section Games
              qPokemon: 7: v1
              qNim: 7: v1
            section Fractals
              Museum: 0: Building
              auto-fractal: 0: Building
            section qMaths
</div>
""", height=600, scrolling=False)
