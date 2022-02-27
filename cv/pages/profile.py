import streamlit as st
import json
from PIL import Image


def profile(json_data: json, _photo_profile: Image):
    """Show profile
    Arg:
      json: json of the page profile
    Return: nothing
    """
    # Init var
    profile_json = json_data["profile"]
    socials = json_data["profile"]["socials"]
    first_name = profile_json["first_name"]
    last_name = profile_json["last_name"]
    title = profile_json["title"]
    country = profile_json["country"]
    email = profile_json["email"]
    website = profile_json["website"]
    github_md = (
        "[![GitHub](https://raw.githubusercontent.com/mickahell/mickahell/main/resources/github.png)]("
        + socials["github_url"]
        + ")"
    )
    linkedin_md = (
        "[![Linkedin](https://raw.githubusercontent.com/mickahell/mickahell/main/resources/linkedin.png"
        ")](" + socials["linkedin_url"] + ")"
    )
    scholar_md = (
        "[![Scholar](https://raw.githubusercontent.com/mickahell/mickahell/main/resources/scholar.png)]("
        + socials["scholar_url"]
        + ")"
    )
    skills = profile_json["skills"]
    langs = profile_json["languages"]
    hobbies = profile_json["hobbies"]

    # Design page
    with st.sidebar:
        # Personal info
        st.image(_photo_profile, output_format="PNG", use_column_width=True)
        st.title(first_name + " " + last_name)
        st.write("### " + title)
        st.write("Country : " + country)
        st.write(":email: : " + email)
        st.write(":link: : " + website)

        # Socials
        st.write(github_md + " " + linkedin_md + " " + scholar_md)

        # Skills
        st.write("## Skills")
        for i in skills:
            with st.expander(i["category"], False):
                for y in i["list"]:
                    st.write("▶ " + y)
        # Languages
        st.write("## Languages")
        for i in langs:
            if "native" in i["level"]:
                st.write(i["name"] + " : " + i["level"])
            else:
                level = ""
                grade = " - " + i["diploma"] if i["diploma"] is not None else ""
                for _ in i["level"]:
                    level = level + "⭑"
                st.write(i["name"] + " : " + level + grade)

        # Hobbies
        st.write("## Hobbies")
        for i in hobbies:
            st.write(i)
