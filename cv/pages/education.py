import streamlit as st
import json


def edu(json_data: json):
    """Show education
    Arg:
      json: json of the page education
    Return: nothing
    """
    st.write("## Education")
    right_col, left_col = st.columns(2)
    line_container = st.container()

    for i, elem in enumerate(json_data["education"]):
        if i % 2 == 0:
            line_container = st.container()
            right_col, empty, left_col = st.columns([10, 1, 10])
        if i % 2 == 0:
            sw_col = right_col
        else:
            sw_col = left_col
        with line_container:
            with sw_col:
                st.write("#### " + elem["diploma"])
                st.write("**Specialty** : " + elem["title"])
                level = elem["level"] + " - " if elem["level"] is not None else ""
                st.write("**Level** : " + level + elem["date_begin"] + "  &#8594; " + elem["date_end"])
                country_city = " - " + elem["country"] + " " + elem["city"] if elem["country"] and elem["city"] is not None else ""
                st.write("**School/University** : " + elem["school"] + country_city)
        if i % 2 == 0:
            st.write("---")


def cert(json_data: json):
    """Show certifications
  Arg: 
    json: json of the page certifications
  Return: nothing
  """
    st.write("## Certifications")
    right_col, left_col = st.columns(2)
    line_container = st.container()
    for i, elem in enumerate(json_data["certifications"]):
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
                type_cert = "Hackaton" if elem["diploma"] is not None else "Certification"
                st.write("**Type** : " + type_cert + " - " + elem["date"])
                st.write("**Organisation** : " + elem["organisme"])
                st.write("**Ref id** : [" + elem["ref_id"] + "](" + elem["diploma_url"] + ")")
        if i % 2 == 0:
            st.write("---")
