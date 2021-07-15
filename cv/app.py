import streamlit as st

st.set_page_config(page_title="CV", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

hide_menu_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer::before {content:'Xtra Orbitals™️ | Since 2021 | ';}
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

col1, col2 = st.sidebar.beta_columns(2)
col1.image('data/IMG_1574.png')

st.sidebar.markdown(
    """
    # Michael Rollin  
    27 years old  
    [email](mailto:michael.rollin@orange.fr)  
    [GitHub](https://github.com/mickahell)  
    [Twitter]()  
    [Linkedin]()  
    ### Navigation
    [Link](#hobbies)
    """
)

"""
## Curiculum vitae
### Experiences
### Education
### Certifications
### IT skills
### Hobbies
### Science Publications
"""
