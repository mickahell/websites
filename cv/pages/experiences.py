import streamlit as st
import json
import io
import requests


def exp(json_data: json, base_url: str):
    """Show experiences
    Arg:
      json: json of the page experiences
    Return: nothing
    """
    st.write("## Experiences")
    right_col, left_col = st.columns(2)
    line_container = st.container()

    for i, elem in enumerate(json_data["experiences"]):
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
                country_city = " - " + elem["country"] + " " + elem["city"] if elem["country"] and elem[
                    "city"] is not None else ""
                st.write("**Organisation** : " + elem["entreprise"] + country_city)
                date_end = elem["date_end"] if elem["date_end"] is not None else "today"
                st.write("**Period** : " + elem["date_begin"] + " &#8594; " + date_end)
                # Descriptions
                if elem["long_description_url"] is not None:
                    with st.expander(elem["short_description"]):
                        r = requests.get(base_url + elem["long_description_url"])
                        long_desc = io.StringIO(r.text)
                        st.write(long_desc.read())
                else:
                    st.write(elem["short_description"])

                # Technos
                list_tech = ""
                for tech in elem["technologies"]:
                    list_tech = tech + ", " + list_tech
                st.write("**Technologies used** : " + list_tech)
        if i % 2 == 0:
            st.write("---")
