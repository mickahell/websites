import streamlit as st
from PIL import Image
import urllib.request
import function
import common

# import profile
# import exp
# import education
# import hobbies
# import extra

st.set_page_config(page_title="CV", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

common.css()

title = """
<div align="center">
    <h1>CV</h1>
</div>
<br /><br />
"""
st.markdown(title, unsafe_allow_html=True)

# Init var
base_url = "https://raw.githubusercontent.com/mickahell/mickahell/main/cv/json/"
data_page = ["index", "info", "experiences", "education", "publications", "projects"]

# Download json
## to put in cache
index = function.dl_json(base_url, data_page[0])
info = function.dl_json(base_url, data_page[1])
exp = function.dl_json(base_url, data_page[2])
edu = function.dl_json(base_url, data_page[3])
publi = function.dl_json(base_url, data_page[4])
projects = function.dl_json(base_url, data_page[5])
urllib.request.urlretrieve(info["info"]["photo_url"], "data/profile.png")
photo_profile = Image.open("data/profile.png")

# Calcul index
print(info["info"]["socials"][0])

# Profile
profile = info["info"]
socials = info["info"]["socials"][0]
with st.sidebar:
    # Personal info
    st.image(photo_profile, output_format='PNG', use_column_width=True)
    st.title(profile["first_name"] + " " + profile["last_name"])
    st.write("### " + profile["title"])
    st.write("Country : " + profile["country"])
    st.write("📧 : " + profile["email"])
    st.write("🔗 : " + profile["website"])

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

# Education

# Publications

# Projects
