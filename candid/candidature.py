import streamlit as st
import to_github
import unidecode


def info():
    page_name = "candidature"
    return page_name


def app():
    home_page = """
    <div align="center">
        Here is to write your candidature
    </div>
    </br>
    """
    st.markdown(home_page, unsafe_allow_html=True)

    job_position = {
        "wpa": "WPA",
        "president": "President"
    }

    st.write("""
    ### Syntax markdown
    - Gras : `__bla bla__`
    - Italique: `*bla bla*`
    - Saut de ligne: faire 2 espaces ou 2 sauts de ligne
    Plus d'info : https://www.markdownguide.org/basic-syntax/
    """)

    st.write("---")
    st.write("### Formulaire de candidature")

    with st.form("candidature", clear_on_submit=False):
        subject_select = st.radio("Position", list(job_position))
        subject = job_position[subject_select]
        name = st.text_input("Prénom Nom")
        asso = st.text_input("Ton asso")
        name_id = name.replace(" ", "")
        encode_name = unidecode.unidecode(name_id)

        header_txt = """
        ### """ + name + """ de """ + asso + """
        """ + "#### Poste : " + subject
        photo_url = st.text_input("Url de votre photo galaxy", placeholder="https://...")

        intro = st.text_area("Intro")
        block_intro = """
        ## Intro
        """ + intro

        known_esn = st.text_area("Comment j'ai connu ESN ?")
        block_known_esn = """
        ## Comment j'ai connu ESN ?
        """ + known_esn

        plain_content = "full" if len(intro) > 0 and len(known_esn) > 0 else ""
        content = block_intro + block_known_esn

        preview = st.form_submit_button("Preview")
        if preview:
            st.write(content, unsafe_allow_html=True)

        # Metadata profile
        full_content = header_txt + content
        profile_meta = [name, asso, subject, photo_url]

    if len(plain_content) > 0:
        if st.button("Submit"):
            to_github.candid2github(content=full_content, encode_name=encode_name, profile_meta=profile_meta)
            st.write("Thanks for submitting your candid ✌️")
