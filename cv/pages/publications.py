import streamlit as st
import json


def publi(json_data: json):
    """Show publications
    Arg:
      json: json of the page publications
    Return: nothing
    """
    st.write("## Publications")
    right_col, left_col = st.columns(2)
    line_container = st.container()
    for i, elem in enumerate(json_data["publications"]):
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
                st.write("**Author** : " + elem["author"])
                st.write("**Field** : " + elem["field"])
                st.write("**Type** : " + elem["type"] + " - **Langue** : " + elem["language"])
                st.write("**DOI** : [" + elem["doi"] + "](https://doi.org/" + elem["doi"] + ")" +
                         " - **Hal id** : [" + elem["hal_id"] + "](https://hal.archives-ouvertes.fr/" +
                         elem["hal_id"] + ")")
                st.write("[**Read it on Hal**](" + elem["hal_url"] + ")")
                st.write("**Publication date** : " + elem["publication_date"])
                with st.expander("Abstract :", False):
                    st.write(elem["abstract"])
        if i % 2 == 0:
            st.write("---")


def blog(json_data: json):
    """Show blogposts
  Arg: 
    json: json of the page blogposts
  Return: nothing
  """
    st.write("## Blog posts")
    right_col, left_col = st.columns(2)
    line_container = st.container()
    for i, elem in enumerate(json_data["blogposts"]):
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
                st.write("**Author** : " + elem["author"])
                st.write("**Field** : " + elem["field"])
                st.write("**Langue** : " + elem["language"])
                st.write("**DOI of the project** : [" + elem["doi"] + "](https://doi.org/" + elem["doi"] + ")")
                st.write("[**Read it**](" + elem["url"] + ")")
                st.write("**Publication date** : " + elem["publication_date"])
                with st.expander("Abstract :", False):
                    st.write(elem["abstract"])
        if i % 2 == 0:
            st.write("---")
