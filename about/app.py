import streamlit as st
import menu

st.set_page_config(page_title="About", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

menu.css()
menu.menu_app()

title = """
<div align="center">
    <h1>About here</h1>
</div>
<br /><br />
"""
st.markdown(title, unsafe_allow_html=True)

about = """
    This website is a platform for interactive computing, mainly Quantum computing but also classical.
    I'm using this space to make available what I'm developing/creating and vulgarize some subjects like Quantum science and game robots.  
    The place is still under development and definitely need lot of graphical improvement 
    but everything you can see here is totally made by me, often from scratch or by using some front and science framework.  
    
    #### Why the name Xtra Orbitals ?
    The __*Orbitals*__ particle of the name came from my passion from spacial and especially satellites and robots but also from the Quantum world : 
    an atom have electron orbiting around him. This electron can be used to calculate the ground state of this atom or of the entire molecule.  
    The __*Xtra*__ particle of the name came from my idea for the future of my ecosystem by adding more and more stuff not online web but also things for IOT.
    (Bonus :) The _*.xyz*_ is a reference to the main axes of a qubit.
"""
st.markdown(about)

whoami = """
    ## Who am I ?
    I'm **Michael Rollin**, I'm system engineer and Quantum enthusiast. I love IT and technology in general.  
    Since some years I'm trying to create strong robots who can beat human at playing games 
    by using not only algorithm but also decision making like Artificial Intelligence with different technologies like Quantum computing (real computer or simulator).  
    Also since May 2020, I'm doing research about Quantum computing so, this place is also a way to broadcast the tools I'm developing and the results of the research I'm doing.  
    
    Everything I'm coding is free and open source, so all of my researches, games and projects are fully available on my [GitHub](https://github.com/mickahell) profile.
    
    You can find me on my social network : 
    [![Linkedin](https://i.stack.imgur.com/gVE0j.png) Michael Rollin](https://www.linkedin.com/in/michaelrollin/)
    ![GitHub followers](https://img.shields.io/github/followers/mickahell?style=social) 
    ![Twitter Follow](https://img.shields.io/twitter/follow/mickahell89700?style=social) 
"""
st.markdown(whoami)

techno = """
    ## Technologies used
    The entire platform is structured as micro-services, each pages and apps are independents from each others.  
    List of all the technologies used for this platform :
    - Front : [Streamlit](https://streamlit.io/) & [ttyd](https://tsl0922.github.io/ttyd/)
    - Back : [Docker](https://www.docker.com/) & [NGINX](https://www.nginx.com/) & [GitHub Actions](https://github.com/features/actions)
    - Apps : [Qiskit](https://qiskit.org/) & [Pennylane](https://pennylane.ai/) & [Jupyter notebook](https://jupyter.org/)
    - Languages : Python & Bash & HTML/CSS
"""
st.markdown(techno)

