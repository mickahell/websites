## Build
- Jupyter : docker build . --file quantum_lab/jupyter/Dockerfile_qiskit --tag jupyter_lab:latest
- Streamlit : docker build . --file quantum_lab/streamlit/Dockerfile --tag page_lab:latest
## Launch
- Jupyter : docker run -d -v /opt/share:/opt/quantum_lab/data/share -p 9999:9999 qiskit_lab:latest  
- Streamlit : docker run -d -p 8501:8501 -e LANG=C.UTF-8 page_lab:latest
