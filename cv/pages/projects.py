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
        if i % 2 == 0:
            line_container = st.container()
            right_col, empty, left_col = st.columns([10, 1, 10])
        if i % 2 == 0:
            sw_col = right_col
        else:
            sw_col = left_col
        with line_container:
            with sw_col:
                st.write("#### " + elem["title"])
                st.write("**Organisation** : " + elem["organisation"] + " - **Langue** : " + elem["language"])
                st.write("**Opensource** : " + str(elem["opensource"]))
                publish = "True" if elem["publish"] is not None else "Not yet"
                st.write("**Release** : " + publish)
                if elem["doi"] is not None:
                    st.write("**DOI** : [" + elem["doi"] + "](https://doi.org/" + elem["doi"] + ")")
                st.write("[**Repo access**](" + elem["repo_url"] + ")")
                if elem["live_url"] is not None:
                    st.write("[**Live platform**](" + elem["live_url"] + ")")
                st.write("**Creation date** : " + elem["date"])
                st.write(elem["description"])
        if i % 2 == 0:
            st.write("---")
