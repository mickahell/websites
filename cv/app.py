import streamlit as st

st.set_page_config(page_title="CV", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

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
