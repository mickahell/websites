import streamlit as st
import sys
from os import path

sys.path.append(path.abspath('gallery/'))

import statevector


def app():
    st.title('Welcome in the Quantum Fractals Museum')
    st.write("""Every picture you'll see here are generate from experiments, mathematically, randomly, quantumly, etc  
             All of them are uniq and fully free & opensource""")

    with st.expander("Disclaimer", True):
        st.write(""":warning: 
            The museum is still under development, the first experiments/gallery are available but 
            are still subject to change and evolve. If you encounter some trouble, just refresh the page !  
            Also some bugs can appear in the creation mode. Also, the processes can take some minutes to run correctly.  
            The form study for the platform is still open, the goal is to reach at least 200 answer, 
            it takes less than 30 secs to fill it.   
            --> [![](https://img.shields.io/badge/Form-Access-orange)](https://docs.google.com/forms/d/e/1FAIpQLSf-qSPuL8VQSi0BHwCzIBxck16gHNwUUBtCI7zDNVS7PLZYIg/viewform)
            """"")

    statevector.app()
