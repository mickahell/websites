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
    [Twitter](https://twitter.com/mickahell89700)  
    [Linkedin](https://www.linkedin.com/in/michaelrollin/)  
    ### Navigation
    [Experiences](#exp)  
    [Education](#education)  
    [Certifications](#certification)  
    [IT skills](#skills)  
    [Hobbies](#hobbies)  
    [Science Publications](#publi)
    """
)

content = """
## Curiculum vitae
### Experiences <a class="anchor" id="exp"></a>
- July 2018 to Today ; System Engineer - Orange by Altran - Sophia-Antipolis, France
Admin system responsible of the production servers for project Meta. Project about to getting and processing every metadata of the Orange TV.
  - Dockeurisation of the metadata processing system
  - Migration from a physical architecture to a virtual architecture in the cloud with Docker Swarm
  - Development of a new architecture un microservices
  - Processus automatisation with Ansible
  
- June 2017 to June 2019 ; Web Project Administrator - Erasmus Student Network France
Responsible of the IT strategic and of the IT prokect of the head NGO ESN France.
  - Responsible of the European project [Buddy System](https://buddysystem.eu/fr/the-project)
  - Development of plateforms : intranet, webshop, ...
  
- March 2017 to September 2017 ; Cybersecurity Engineer - Ekium, Lyon
Development of a cybersecurity architecture with a supervision system for a seawater desalination plant in Oman.

### Education <a class="anchor" id="education"></a>
- 2016 -- 2017 ; Master 2 - ESAIP Dijon IT project management
- 2016 ; Master 1 - LaSalle Cuernavaca (Mexico) Cibernética
- 2015 ; Licence 3 - Politechnika Varsovie (Poland) Electrical Engineering
- 2014 ; BTS St Joseph Dijon Electronics systems

### Certifications <a class="anchor" id="certification"></a>

### IT skills <a class="anchor" id="skills"></a>
_ **OS** : Ubuntu, CentOS, Windows Server 2008 / 2012 R2
_ **Coding** : Python, C++, QISkit, Pennylane
_ **Admin. services** : Docker, Swarm, Ansible, GitLab, Vmware
_ **Electronic** : MPLAB, PCAD, MATLAB
_ **English** : -- Toeic 795 / 990        **Spanish** : 

### Hobbies <a class="anchor" id="hobbies"></a>
### Science Publications <a class="anchor" id="publi"></a>
"""
st.markdown(content, unsafe_allow_html=True)
