import streamlit as st
import pandas as pd
import datetime
import io
import requests
import plotly.graph_objects as go


def info():
    page_name = "home"
    return page_name


def app():
    home_page = """
    <div align="center">
        Portail pour candidatures
    </div>
    </br>
    """
    st.markdown(home_page, unsafe_allow_html=True)



