import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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

apps = """
    <br /><br />
    <h2>Apps available</h2>
"""
st.markdown(apps, unsafe_allow_html=True)
col0, col1, col2, col3 = st.beta_columns(4)
lab = col0.beta_expander("Quantum Lab", True)
lab.write("```python3.8, networkx, numpy, matplotlib, notebook, pandas, scipy, tk```")
games = col1.beta_expander("Games", True)
games.write("```qiskit, qiskit[visualization], qiskit-nature```")
fractals = col2.beta_expander("Fractals", True)
fractals.write("```autograd, pennylane, pennylane-sf, pennylane-qiskit```")
about = col3.beta_expander("About", True)
about.write("```cirq, cirq-core[contrib], texlive-latex-base, latexmk```")

## Tag cloud
# Create some sample text
text = 'Quantum, games, AI, robots, pokemon, lab, python, qiskit, pennylane, fractals, fun'

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()
