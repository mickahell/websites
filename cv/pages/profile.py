import streamlit as st
import json
from PIL import Image


def profile(json_data: json, _photo_profile: Image):
    profile_json = json_data["info"]
    socials = json_data["info"]["socials"]
    with st.sidebar:
        # Personal info
        st.image(_photo_profile, output_format='PNG', use_column_width=True)
        st.title(profile_json["first_name"] + " " + profile_json["last_name"])
        st.write("### " + profile_json["title"])
        st.write("Country : " + profile_json["country"])
        st.write(":email: : " + profile_json["email"])
        st.write(":link: : " + profile_json["website"])

        # Socials
        github_md = "[![GitHub](https://raw.githubusercontent.com/mickahell/mickahell/main/resources/github.png)](" + \
                    socials["github_url"] + ")"
        linkedin_md = "[![Linkedin](https://raw.githubusercontent.com/mickahell/mickahell/main/resources/linkedin.png" \
                      ")](" + socials["linkedin_url"] + ")"
        scholar_md = "[![Scholar](https://raw.githubusercontent.com/mickahell/mickahell/main/resources/scholar.png)](" \
                     + socials["scholar_url"] + ")"
        st.write(github_md + " " + linkedin_md + " " + scholar_md)

        # Skills
        st.write("## Skills")
        for i in profile_json["skills"]:
            with st.expander(i["category"], False):
                for y in i["list"]:
                    st.write("▶ " + y)
        # Languages
        st.write("## Languages")
        for i in profile_json["languages"]:
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
        for i in profile_json["hobbies"]:
            st.write(i)
