import streamlit as st


def app():
    article = st.beta_expander("Article on Full-Stack Quantum Computation", expanded=True)
    article_view = """
    <iframe
        title="Quantum Lab article"
        width="100%"
        height="7200"
        src="https://fullstackquantumcomputation.tech/blog/post-quantum-lab/">
    </iframe>
    """
    article.write(article_view, unsafe_allow_html=True)
    st.write("<h3>See on <a href='https://fullstackquantumcomputation.tech/blog/post-quantum-lab/'><b>Full-Stack Quantum Computation</b></a></h3>", unsafe_allow_html=True)
