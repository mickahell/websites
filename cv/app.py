import streamlit as st
from PIL import Image
import urllib.request
from pages import experiences
from pages import education
from pages import publications
import function
import common

st.set_page_config(page_title="CV", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

common.css()

# Init var
base_url = "https://raw.githubusercontent.com/mickahell/mickahell/main/cv/json/english/"
index_page = "index"

# Download json
# to put in cache
# Calcul index
index = function.dl_json(base_url, index_page)
db = index["index"]
# Calcul entire pages
info = function.dl_json(base_url, db["info"]["key"])
exp = function.dl_json(base_url, db["experiences"]["key"])
edu = function.dl_json(base_url, db["education"]["key"])
publi = function.dl_json(base_url, db["publications"]["key"])
projects = function.dl_json(base_url, db["projects"]["key"])
# Profile pic
urllib.request.urlretrieve(info["info"]["photo_url"], "data/profile.png")
photo_profile = Image.open("data/profile.png")

# Debug
print(info["info"]["socials"])

# Profile
profile = info["info"]
socials = info["info"]["socials"]
with st.sidebar:
    # Personal info
    st.image(photo_profile, output_format='PNG', use_column_width=True)
    st.title(profile["first_name"] + " " + profile["last_name"])
    st.write("### " + profile["title"])
    st.write("Country : " + profile["country"])
    st.write(":email: : " + profile["email"])
    st.write(":link: : " + profile["website"])

    # Socials
    github_md = "[![GitHub](https://raw.githubusercontent.com/mickahell/mickahell/main/resources/github.png)](" + \
                socials["github_url"] + ")"
    linkedin_md = "[![Linkedin](https://raw.githubusercontent.com/mickahell/mickahell/main/resources/linkedin.png)](" + \
                  socials["linkedin_url"] + ")"
    scholar_md = "[![Scholar](https://raw.githubusercontent.com/mickahell/mickahell/main/resources/scholar.png)](" + \
                  socials["scholar_url"] + ")"
    st.write(github_md + " " + linkedin_md + " " + scholar_md)

    # Skills
    st.write("## Skills")
    for i in profile["skills"]:
        with st.expander(i["category"], False):
            for y in i["list"]:
                st.write("▶ " + y)
    # Languages
    st.write("## Languages")
    for i in profile["languages"]:
        if "native" in i["level"]:
            st.write(i["name"] + " : " + i["level"])
        else:
            level = ""
            grade = " - " + i["diploma"] if i["diploma"] is not None else ""
            for u in i["level"]:
                level = level + "⭑"
            st.write(i["name"] + " : " + level + grade)

    # Hobbies
    st.write("## Hobbies")
    for i in profile["hobbies"]:
        st.write(i)


# Experiences
with st.container():
    experiences.exp(json=exp, base_url=base_url)

# Education
with st.container():
    education.edu(json=edu)
with st.container():
    education.cert(json=edu)

# Publications
with st.container():
    publications.publi(json=publi)
with st.container():
    publications.blog(json=publi)

# Projects

