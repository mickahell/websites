import streamlit as st
import io
import requests


def exp(json: json, base_url: str):
  """Show experiences
  Arg: 
    json: json of the page experiences
  Return: nothing
  """
  st.write("## Experiences")
  for i in json["experiences"]:
    st.write("### " + i["title"])
    country_city = " - " + i["country"] + " " + i["city"] if i["country"] and i["city"] is not None else ""
    st.write("### " + i["entreprise"] + country_city)
    date_end = i["date_end"] if i["date_end"] is not None else "today"
    st.write("### " + i["date_begin"] + " -> " + date_end)
    # Descriptions
    with st.expander(i["short_description"]):
      r = requests.get(base_url + i["long_description_url"])
      long_desc = io.StringIO(r.text)
      st.write("long_desc")
    
    # Technos
    for tech in i["technologies"]:
      list_tech = list_tech + ", " + tech
    st.write("**Technologies used** : " + list_tech)
