import sys
import streamlit as st
from streamlit import cli as stcli

st.set_page_config(page_title="Games", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

header = """
<div align="center">
    <h1>Games</h1>
</div>
<br /><br />
"""
st.markdown(header, unsafe_allow_html=True)

# Run Quantum Pokemon Fight
if st.checkbox('Quantum Pokemon Fight'):
    #sys.argv = ["streamlit", "run", "quantum_pokemon-fight/game.py"]
    #sys.argv = ["streamlit", "run", "test.py"]
    #sys.exit(stcli.main())

    import subprocess
    import os

    process = subprocess.Popen(["streamlit", "run", os.path.join('test.py')])

