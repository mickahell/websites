import streamlit as st
from datetime import datetime
import sys
from os import path

sys.path.append(path.abspath('posts/'))

import advocate
import welcome
import quantumlab
import qpokemonfight


def get_articles():
    POSTS = [
        advocate,
        welcome,
        quantumlab,
        qpokemonfight,
    ]
    return POSTS


def metadata(tags, date, lecture_time, key, title, extra):
    date_time = datetime.strptime(date, '%m/%Y')
    date_time = date_time.strftime("%b, %Y")

    str_tag = ""
    for i in tags:
        str_tag = str_tag + " #" + i

    meta = "<div style='color:grey'>" + date_time + " | " + lecture_time + " min read" + " | " + str_tag + "</div>"

    st.header(title, anchor=key)
    st.write(meta, unsafe_allow_html=True)
    st.write(extra)
