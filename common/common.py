import streamlit as st


def css():
    css = """
        <style>
            #MainMenu {visibility: hidden;}
            footer::before {content:'Xtra Orbitals™️ | Since 2021 | ';}

            .header {
                background: #555;
                color: #f1f1f1; 
                position: fixed;
                overflow: hidden;
                background-color: #333;
                top: 34px;
                left: 190px;}

            .header a {
                float: left;
                color: #f2f2f2;
                text-align: center;
                padding: 10px 16px;
                text-decoration: none;
                font-size: 15px;}

            .header a:hover {
                background-color: #ddd;
                color: black;}

            .logo a {
                color: black;
                position: fixed;
                top: 10px;}

            .logo img {
                width: 100px;
                opacity: 0.7;}

            .logo img:hover {
            opacity: 1;}
        </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def menu_app():
    # Menu
    menu = """
        <div class="logo">
            <a href="https://xtraorbitals.xyz">
                <img src="https://raw.githubusercontent.com/mickahell/xtraorbitals.xyz/main/logo.png"/>
            </a>
        </div>
        <div class="header">
            <a href="https://xtraorbitals.xyz"><b>Home</b></a>
        </div>
    """
    st.markdown(menu, unsafe_allow_html=True)


def menu_main():
    st.sidebar.write("# Menu")
    st.sidebar.write("## Apps")
    with st.sidebar.expander("", True):
        st.write("""
            ▶︎ 🧪 **[Lab](https://quantum-lab.xtraorbitals.xyz)**  
            ▶︎ 🕹 **[Games](https://games.xtraorbitals.xyz)**  
            ▶︎ 🎭 **[Beta Museum](https://beta-museum.xtraorbitals.xyz)**
            """)
    st.sidebar.write("""▶︎ 🗞 **[Blog](https://blog.xtraorbitals.xyz)**""")
    st.sidebar.write("""▶︎ 📑 **[Resume](https://cv.xtraorbitals.xyz)**""")
    st.sidebar.write("""▶︎ **[About](https://about.xtraorbitals.xyz)**""")


def author():
    col0, col1 = st.columns([1, 10])
    col0.image('https://raw.githubusercontent.com/mickahell/mickahell/main/resources/profile.png', output_format='PNG', use_column_width=True)
    col1.write("""
    __Michaël Rollin__ : <div style='color:grey'>System engineer & Qiskit Advocate</div>
                        I create quantum autom processes and tools for IT engineering.  
                        <img src='https://raw.githubusercontent.com/AkashGutha/Qiskit-Snippets/master/assets/qiskit.gif' width="32"/>
                        [![GitHub](https://raw.githubusercontent.com/mickahell/mickahell/main/resources/github.png)](https://github.com/mickahell)
                        [![LinkedIn](https://raw.githubusercontent.com/mickahell/mickahell/main/resources/linkedin.png)](https://www.linkedin.com/in/michaelrollin/)
                        [![Twitter](https://raw.githubusercontent.com/mickahell/mickahell/main/resources/twitter.png)](https://twitter.com/mickahell89700)
    """, unsafe_allow_html=True)
