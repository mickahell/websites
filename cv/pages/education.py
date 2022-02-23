import streamlit as st
import json


def edu(json: json):
    """Show education
    Arg:
      json: json of the page education
    Return: nothing
    """
    st.write("## Education")
    for i in json["education"]:
        st.write("### " + i["diploma"])
        level = i["level"] + " - " if i["level"] is not None else ""
        st.write(level + i["date_begin"] + "  -> " + i["date_end"])
        st.write(i["school"])
        country_city = " - " + i["country"] + " " + i["city"] if i["country"] and i["city"] is not None else ""


def cert(json: json):
    """Show certifications
  Arg: 
    json: json of the page certifications
  Return: nothing
  """
    st.write("## Certifications")
    for i in json["certifications"]:
        st.write("### " + i["title"])
        type_cert = "Hackaton" if i["diploma"] is not None else "Certification"
        st.write(type_cert + " - " + i["date"])
        st.write(i["organisme"])
        st.write("Ref id : [" + i["ref_id"] + "](" + i["diploma_url"] + ")")
