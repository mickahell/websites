## Build
- Qiskit lab : docker build . --file quantum_lab/jupyter/Dockerfile_qiskit --tag qiskit_lab:latest
- Page lab : docker build . --file quantum_lab/streamlit/Dockerfile --tag page_lab:latest
## Launch
- Qiskit lab : docker run -d --name qiskit_lab -v /opt/share:/opt/quantum_lab/data/share -p 9999:9999 qiskit_lab:latest  
- Page lab : docker run -d --name page_lab -p 8501:8501 -e LANG=C.UTF-8 page_lab:latest
