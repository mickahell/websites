import streamlit as st


def app():
    header = """
    <div align="center">
        <h1>Online Quantum Lab</h1>
        Here an online version of my Docker images for <b>Quantum development</b> and <b>Quantum experiments</b>. 
        This platform is only for prototype, testing experiments and science <b>vulgarisation/demo</b>.
        <h2>Access</h2>
        <table>
            <tbody>
                <tr>
                    <td align="center"><a href="http://qiskit.xtraorbitals.xyz"><b>Qiskit</b></a></td>
                </tr>
            </tbody>
        </table>
    </div>
    """
    st.markdown(header, unsafe_allow_html=True)

    lib = """
    <br /><br />
    <h2>Libs available</h2>
    """
    st.markdown(lib, unsafe_allow_html=True)
    col0, col1, col2, col3 = st.columns(4)
    lib_commun = col0.expander("Common")
    lib_commun.write("```python3.8, networkx, numpy, matplotlib, notebook, pandas, scipy, tk```")
    libs_qiskit = col1.expander("Qiskit")
    libs_qiskit.write("```qiskit, qiskit[visualization], qiskit[nature], qiskit[finance], qiskit[optimization], qiskit[machine-learning]```")
    libs_qml = col2.expander("Pennylane / QML")
    libs_qml.write("```autograd, pennylane, pennylane-sf, pennylane-qiskit```")
    libs_cirq = col3.expander("Cirq")
    libs_cirq.write("```cirq, cirq-core[contrib], texlive-latex-base, latexmk```")

    body = """
    ## GitHub
    [![Docker Image CI](https://github.com/mickahell/quantum_lab/actions/workflows/docker-image.yml/badge.svg)](https://github.com/mickahell/quantum_lab/actions/workflows/docker-image.yml)
    [![Docker TAG CI](https://github.com/mickahell/quantum_lab/actions/workflows/docker-tag.yml/badge.svg)](https://github.com/mickahell/quantum_lab/actions/workflows/docker-tag.yml)
    [![GitHub release (latest by date)](https://img.shields.io/github/v/release/mickahell/quantum_lab)](https://github.com/mickahell/quantum_lab/releases)

    ## DockerHub
    [![Docker Pulls](https://img.shields.io/docker/pulls/mickahell/quantum_lab_qiskit?label=Quantum%20Lab%20Qiskit&style=for-the-badge)](https://hub.docker.com/r/mickahell/quantum_lab_qiskit)
    [![Docker Pulls](https://img.shields.io/docker/pulls/mickahell/quantum_lab_qiskit-full?label=Quantum%20Lab%20Qiskit-full&style=for-the-badge)](https://hub.docker.com/r/mickahell/quantum_lab_qiskit-full)
    [![Docker Pulls](https://img.shields.io/docker/pulls/mickahell/quantum_lab_qml?label=Quantum%20Lab%20QML&style=for-the-badge)](https://hub.docker.com/r/mickahell/quantum_lab_qml)
    [![Docker Pulls](https://img.shields.io/docker/pulls/mickahell/quantum_lab_qsharp?label=Quantum%20Lab%20Q%23&style=for-the-badge)](https://hub.docker.com/r/mickahell/quantum_lab_qsharp)
    [![Docker Pulls](https://img.shields.io/docker/pulls/mickahell/quantum_lab_myqlm?label=Quantum%20Lab%20myQLM&style=for-the-badge)](https://hub.docker.com/r/mickahell/quantum_lab_myqlm)
    [![Docker Pulls](https://img.shields.io/docker/pulls/mickahell/quantum_lab_simulaqron?label=Quantum%20Lab%20SimulaQron&style=for-the-badge)](https://hub.docker.com/r/mickahell/quantum_lab_simulaqron)

    [![Docker Pulls](https://img.shields.io/docker/pulls/mickahell/quantum_lab_cirq?label=Quantum%20Lab%20Cirq&style=for-the-badge)](https://hub.docker.com/r/mickahell/quantum_lab_cirq)

    ## Citation
    If you use my work, please cite as : <pre>Quantum Lab: Docker image for quantum laboratory, Michaël Rollin, 2021, DOI: <a href=https://doi.org/10.5281/zenodo.4664195>10.5281/zenodo.4664195</a></pre>
    """
    st.markdown(body, unsafe_allow_html=True)

    doi_col0, doi_col1 = st.columns([4, 1])
    doi = """
    [![DOI](https://zenodo.org/badge/343446026.svg)](https://zenodo.org/badge/latestdoi/343446026)  
    """
    doi_col1.markdown(doi)

    footer = """
    ### Bug / Feature
    If you have an idea of features do not hesitate and create an **[issue](https://github.com/mickahell/quantum_lab/issues/new)**.
    """
    st.markdown(footer, unsafe_allow_html=True)

    termofuse = """
    ## Term of use
    Anyone can use these quantum laboratories freely without any limitation, the ony limits are the one of the system. Max memory for a program is limit to 500MB. 
    It doesn't have the purpose to be as evolve as the <a href="https://quantum-computing.ibm.com/">IBM QC platform</a> or the <a href="https://quantumai.google/cirq">Google Cirq colab platform</a>.  
    These laboratories doesn't provide private access, means every notebook created will stay publicly available until someone delete it. If you don't want to share your work, feel free to delete your files. 
    Owner of the application is not be responsable of any data produice or loose and he doesn't own any of the data produice. Indeed all the data available in the laboratories are in the opensource field. 
    Anyone can import work and share it inside the application, if you want to share tutorial and keep them protect from deleting feel free to reach an issue on the [GitHUb repository](https://github.com/mickahell/websites/issues/new) or to send an email to my [GitHub email](https://github.com/mickahell).
    """
    st.markdown(termofuse, unsafe_allow_html=True)
