import streamlit as st
import urllib.request
import json
from PIL import Image


@st.experimental_memo
def dl_json(base_url: str, page: str) -> json:
    """Get json from url
    Args:
        base_url: base of the url
        page: name of the page
    Return: json
    """
    json_url = base_url + page + ".json"
    with urllib.request.urlopen(json_url) as url:
        return_json = json.loads(url.read().decode())

    return return_json


@st.experimental_memo
def dl_img(img_url: str, dest: str) -> Image:
    """Get image from url
    Args:
        img_url: url of the image
        dest: dest to register the image
    Return: Image
    """
    urllib.request.urlretrieve(img_url, dest)
    return_img = Image.open(dest)

    return return_img
