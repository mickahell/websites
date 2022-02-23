import streamlit as st
import json


def publi(json: json):
    """Show publications
    Arg:
      json: json of the page publications
    Return: nothing
    """
    st.write("## Publications")
    for i in json["publications"]:
        st.write("### " + i["title"])
        st.write(i["author"])
        st.write(i["domaine"])
        st.write("Type of doc : " + i["type"] + " - Langue : " + i["language"])
        st.write("DOI : " + i["doi"] + "- Hal id : " + i["hal_id"])
        st.write("[Read it on Hal](" + i["hal_url"] + ")")
        st.write(i["publication_date"])
        with st.expander("Abstract :", False):
            st.write(i["abstract"])


def blog(json: json):
    """Show blogposts
  Arg: 
    json: json of the page blogposts
  Return: nothing
  """
    st.write("## Blog posts")
    for i in json["blogposts"]:
        st.write("### " + i["title"])
        st.write(i["author"])
        st.write(i["domaine"])
        st.write("Langue : " + i["language"])
        st.write("DOI of the project : " + i["doi"])
        st.write("[Read it](" + i["url"] + ")")
        st.write(i["publication_date"])
        with st.expander("Abstract :", False):
            st.write(i["abstract"])
