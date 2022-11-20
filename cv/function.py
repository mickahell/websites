import streamlit as st
import urllib.request
import json
import os
from PIL import Image


@st.experimental_memo
def dl_json(base_url: str, page: str) -> json:
    """Get json from url
    Args:
        base_url: base of the url
        page: name of the page
    Return: json
    """
    # Local only
    #ssl._create_default_https_context = ssl._create_unverified_context

    json_url = base_url + page + ".json"
    with urllib.request.urlopen(json_url) as url:
        return_json = json.loads(url.read().decode())

    return return_json


@st.experimental_memo
def dl_img(img_url: str, dest: str, force: bool = False) -> Image:
    """Get image from url
    Args:
        img_url: url of the image
        dest: dest to register the image
        force: force dl image
    Return: Image
    """
    # Local only
    #ssl._create_default_https_context = ssl._create_unverified_context

    current_dir = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(str("{}/".format(current_dir) + dest)) or force:
        urllib.request.urlretrieve(img_url, "{}/".format(current_dir) + dest)
    return_img = Image.open(str("{}/".format(current_dir) + dest))

    return return_img
