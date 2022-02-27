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
        # Init var
        title = elem["title"]
        author = elem["author"]
        field = elem["field"]
        doc_type = elem["type"]
        lang = elem["language"]
        doi = elem["doi"]
        paper_id = elem["paper_id"]
        journal_name = elem["journal_name"]
        journal_url = elem["journal_url"]
        publi_date = elem["publication_date"]
        abstract = elem["abstract"]

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
                st.write("**Author** : " + author)
                st.write("**Field** : " + field)
                st.write("**Type** : " + doc_type + " - **Langue** : " + lang)
                st.write("**DOI** : [" + doi + "](https://doi.org/" + doi + ")" + " - **Hal id** : [" + paper_id + "]("
                         + journal_url + paper_id + ")")
                st.write("[**Read it on " + journal_name + "**](" + journal_url + paper_id + ")")
                st.write("**Publication date** : " + publi_date)
                with st.expander("Abstract :", False):
                    st.write(abstract)
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
        # Init var
        title = elem["title"]
        author = elem["author"]
        field = elem["field"]
        lang = elem["language"]
        doi = elem["doi"]
        url = elem["url"]
        publi_date = elem["publication_date"]
        abstract = elem["abstract"]

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
                st.write("**Author** : " + author)
                st.write("**Field** : " + field)
                st.write("**Langue** : " + lang)
                st.write("**DOI of the project** : [" + doi + "](https://doi.org/" + doi + ")")
                st.write("[**Read it**](" + url + ")")
                st.write("**Publication date** : " + publi_date)
                with st.expander("Abstract :", False):
                    st.write(abstract)
        if i % 2 == 0:
            st.write("---")
