import streamlit as st

st.set_page_config(page_title="Quantum Lab", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

header = """
<div align="center">
    <h1>Quantum Lab</h1>
    Here an online version of my Docker images for <b>Quantum development</b> and <b>Quantum experiments</b>. 
    This platform is only for prototype, testing experiments and science <b>vulgarisation/demo</b>.
    <h2>Access</h2>
    <table>
        <tbody>
            <tr>
                <td align="center"><a href="https://qiskit.xtraorbitals.xyz"><b>Qiskit</b></a></td>
                <td align="center"><a href="https://qml.xtraorbitals.xyz"><b>Pennylane</b></a></td>
                <td align="center"><a href="https://cirq.xtraorbitals.xyz"><b>Cirq</b></a></td>
            </tr>
        </tbody>
    </table>
</div>
<br /><br />
"""
st.markdown(header, unsafe_allow_html=True)

article = st.beta_expander("Article on Full-Stack Quantum Computation")
article_view = """
<iframe id="inlineFrameExample"
    title="Inline Frame Example"
    width="100%"
    height="500"
    src="https://fullstackquantumcomputation.tech/blog/post-quantum-lab/">
</iframe>
"""
article.write(article_view, unsafe_allow_html=True)

lib = """
<br /><br />
<h2>Libs available</h2>
"""
st.markdown(lib, unsafe_allow_html=True)
col0, col1, col2, col3 = st.beta_columns(4)
lib_commun = col0.beta_expander("Common")
lib_commun.write("```networkx, numpy, matplotlib, notebook, pandas, scipy, tk```")
libs_qiskit = col1.beta_expander("Qiskit")
libs_qiskit.write("```qiskit, qiskit[visualization], qiskit-nature```")
libs_qml = col2.beta_expander("Pennylane / QML")
libs_qml.write("```autograd, pennylane, pennylane-sf, pennylane-qiskit```")
libs_cirq = col3.beta_expander("Cirq")
libs_cirq.write("```cirq, cirq-core[contrib], texlive-latex-base, latexmk```")

body = """
## GitHub
[![Docker Image CI](https://github.com/mickahell/quantum_lab/actions/workflows/docker-image.yml/badge.svg)](https://github.com/mickahell/quantum_lab/actions/workflows/docker-image.yml)
[![Docker TAG CI](https://github.com/mickahell/quantum_lab/actions/workflows/docker-tag.yml/badge.svg)](https://github.com/mickahell/quantum_lab/actions/workflows/docker-tag.yml)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/mickahell/quantum_lab)](https://github.com/mickahell/quantum_lab/releases)

## DockerHub
[![Docker Pulls](https://img.shields.io/docker/pulls/mickahell/quantum_lab_qiskit?label=Quantum%20Lab%20Qiskit&style=for-the-badge)](https://hub.docker.com/r/mickahell/quantum_lab_qiskit)
[![Docker Pulls](https://img.shields.io/docker/pulls/mickahell/quantum_lab_qml?label=Quantum%20Lab%20QML&style=for-the-badge)](https://hub.docker.com/r/mickahell/quantum_lab_qml)
[![Docker Pulls](https://img.shields.io/docker/pulls/mickahell/quantum_lab_qsharp?label=Quantum%20Lab%20Q%23&style=for-the-badge)](https://hub.docker.com/r/mickahell/quantum_lab_qsharp)
[![Docker Pulls](https://img.shields.io/docker/pulls/mickahell/quantum_lab_myqlm?label=Quantum%20Lab%20myQLM&style=for-the-badge)](https://hub.docker.com/r/mickahell/quantum_lab_myqlm)
[![Docker Pulls](https://img.shields.io/docker/pulls/mickahell/quantum_lab_simulaqron?label=Quantum%20Lab%20SimulaQron&style=for-the-badge)](https://hub.docker.com/r/mickahell/quantum_lab_simulaqron)

[![Docker Pulls](https://img.shields.io/docker/pulls/mickahell/quantum_lab_cirq?label=Quantum%20Lab%20Cirq&style=for-the-badge)](https://hub.docker.com/r/mickahell/quantum_lab_cirq)

## Citation
If you use my work, please cite as : <pre>Quantum Lab: Docker image for quantum laboratory, Michaël Rollin, 2021, DOI: <a href=https://doi.org/10.5281/zenodo.4664195>10.5281/zenodo.4664195</a></pre>
"""
st.markdown(body, unsafe_allow_html=True)

doi_col0, doi_col1 = st.beta_columns([4, 1])
doi = """
[![DOI](https://zenodo.org/badge/343446026.svg)](https://zenodo.org/badge/latestdoi/343446026)  
"""
doi_col1.markdown(doi)

footer = """
### Bug / Feature
If you have an idea of features do not hesitate and create an **[issue](https://github.com/mickahell/quantum_lab/issues/new)**.
"""
st.markdown(footer, unsafe_allow_html=True)
