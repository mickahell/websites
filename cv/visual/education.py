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
        # Init var
        diploma = elem["diploma"]
        title = elem["title"]
        level = elem["level"] + " - " if elem["level"] is not None else ""
        date_begin = elem["date_begin"]
        date_end = elem["date_end"]
        country_city = (
            " - " + elem["country"] + " " + elem["city"]
            if elem["country"] and elem["city"] is not None
            else ""
        )
        school = elem["school"]

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
                st.write("#### " + diploma)
                st.write("**Specialty** : " + title)
                st.write("**Level** : " + level + date_begin + "  &#8594; " + date_end)
                st.write("**School/University** : " + school + country_city)
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
        # Init var
        title = elem["title"]
        type_cert = "Hackaton" if elem["diploma"] is not None else "Certification"
        cert_date = elem["date"]
        organization = elem["organization"]
        ref_id = elem["ref_id"]
        diploma_url = elem["diploma_url"]

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
                st.write("**Type** : " + type_cert + " - " + cert_date)
                st.write("**Organization** : " + organization)
                st.write("**Ref id** : [" + ref_id + "](" + diploma_url + ")")
        if i % 2 == 0:
            st.write("---")
