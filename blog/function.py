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


def author():
    col0, col1 = st.columns([1, 10])
    col0.image('posts/ressources/IMG_1574.png', output_format='PNG', use_column_width=True)
    col1.write("""
    __Michaël Rollin__ : <div style='color:grey'>System engineer & Qiskit Advocate</div>
                        I create quantum autom processes and tools for IT engineering.  
                        <img src='https://raw.githubusercontent.com/AkashGutha/Qiskit-Snippets/master/assets/qiskit.gif' width="32"/>
                        [![GitHub](https://raw.githubusercontent.com/mickahell/xtraorbitals.xyz/main/blog/posts/ressources/github.png)](https://github.com/mickahell)
                        [![LinkedIn](https://raw.githubusercontent.com/mickahell/xtraorbitals.xyz/main/blog/posts/ressources/linkedin.png)](https://www.linkedin.com/in/michaelrollin/)
                        [![Twitter](https://raw.githubusercontent.com/mickahell/xtraorbitals.xyz/main/blog/posts/ressources/twitter.png)](https://twitter.com/mickahell89700)
    """, unsafe_allow_html=True)
