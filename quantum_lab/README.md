## Build
- Qiskit lab    : docker build . --build-arg LAB_ENV=qiskit --file quantum_lab/jupyter/Dockerfile --tag qiskit_lab:latest
- Pennylane lab : docker build . --build-arg LAB_ENV=qml --file quantum_lab/jupyter/Dockerfile --tag qml_lab:latest
- Cirq lab      : docker build . --build-arg LAB_ENV=cirq --file quantum_lab/jupyter/Dockerfile --tag cirq_lab:latest
- Page lab      : docker build . --file quantum_lab/streamlit/Dockerfile --tag page_lab:latest
## Launch
- Qiskit lab    : docker run -d --name qiskit_lab -v /opt/share/quantum_lab:/opt/quantum_lab/data/share -p 9999:9999 qiskit_lab:latest  
- Pennylane lab : docker run -d --name qml_lab -v /opt/share/quantum_lab:/opt/quantum_lab/data/share -p 9998:9999 qml_lab:latest
- Cirq lab      : docker run -d --name cirq_lab -v /opt/share/quantum_lab:/opt/quantum_lab/data/share -p 9997:9999 cirq_lab:latest
- Page lab      : docker run -d --name page_lab -p 8501:8501 -e LANG=C.UTF-8 page_lab:latest
