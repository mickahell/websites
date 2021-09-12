import streamlit as st
from datetime import datetime


def metadata(tags, date, lecture_time, key, title, extra):
    date_time = datetime.strptime(date, '%m/%Y')
    date_time = date_time.strftime("%b, %Y")

    meta = "<div style='color:grey'>" + date_time + " | " + lecture_time + " min read" + "</div>"

    st.header(title, anchor=key)
    st.write(meta, unsafe_allow_html=True)
    st.write(extra)
