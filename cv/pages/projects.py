import streamlit as st
import json


def projects(json_data: json):
    """Show projects
    Arg:
      json: json of the page projects
    Return: nothing
    """
    st.write("## Projects")
    right_col, left_col = st.columns(2)
    line_container = st.container()
    for i, elem in enumerate(json_data["projects"]):
        # Init var
        title = elem["title"]
        orga = elem["organization"]
        lang = elem["language"]
        opensource = elem["opensource"]
        doi = elem["doi"] if elem["doi"] is not None else None
        is_publish = "True" if elem["publish"] is not None else "Not yet"
        repo_url = elem["repo_url"]
        live_url = elem["live_url"] if elem["live_url"] is not None else None
        crea_date = elem["date"]
        description = elem["description"]

        # Design page
        if i % 2 == 0:
            line_container = st.container()
            right_col, empty, left_col = st.columns([10, 1, 10])
        if i % 2 == 0:
            sw_col = right_col
        else:
            sw_col = left_col
        with line_container:
            with sw_col:
                st.write("#### " + title)
                st.write("**Organization** : " + orga + " - **Langue** : " + lang)
                st.write("**Opensource** : " + str(opensource))
                st.write("**Release** : " + is_publish)
                if doi is not None:
                    st.write("**DOI** : [" + doi + "](https://doi.org/" + doi + ")")
                st.write("[**Repo access**](" + repo_url + ")")
                if live_url is not None:
                    st.write("[**Live platform**](" + live_url + ")")
                st.write("**Creation date** : " + crea_date)
                st.write(description)
        if i % 2 == 0:
            st.write("---")
