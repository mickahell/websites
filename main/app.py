import streamlit as st
import streamlit.components.v1 as components
import requests
from requests.structures import CaseInsensitiveDict
from common import common


def isrunning(url):
    status = requests.get(url)
    if status.status_code == 200:
        return [url, "ok"]
    else:
        return [url, "ko"]


st.set_page_config(page_title="Xtra Orbitals", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

common.css()
common.menu_main()

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

blog_posts = """
    ## Latest blog posts
"""
st.markdown(blog_posts)
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
r = requests.get('https://raw.githubusercontent.com/mickahell/xtraorbitals.xyz/main/blog/articles_db.json',
                 headers=headers)
articles_db = r.json()

art0, art1, art2 = st.columns(3)
artcol = [art0, art1, art2]
compteur = 0
for i in articles_db:
    if int(i['id']) < 3:
        with artcol[compteur]:
            with st.expander(i["title"], True):
                str_tag = ""
                for u in i["tag"]:
                    str_tag = str_tag + " #" + u
                meta = "<div style='color:grey'>" + i["date"] + " | " + str_tag + "</div>"
                button = "<form action=" + i['link'] + "><input type='submit' value='See >' /></form>"
                st.write(meta, unsafe_allow_html=True)
                st.write(i["preview"] + "<br /><br />" + button, unsafe_allow_html=True)
    compteur += 1

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
status_blog = isrunning("https://blog.xtraorbitals.xyz/")
status_museum = isrunning("https://beta-museum.xtraorbitals.xyz/")

for i in (
        status_qiskit, status_penny, status_cirq, status_qpokemon, status_qnim, status_games, status_about, status_lab):
    if i[1] != "ok":
        msg = i[0], ":warning: : is down !"
        st.write(msg)

# Versions
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
              Museum: 4: Building
              auto-fractal: 4: Building
            section qMaths
</div>
""", height=600, scrolling=False)

# Author
common.author()
