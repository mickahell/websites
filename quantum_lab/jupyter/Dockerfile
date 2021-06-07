ARG quantum_env
#ARG quantum_env=qiskit
#ARG quantum_env=qml
#ARG quantum_env=cirq

FROM mickahell/quantum_lab_${quantum_env}:latest

# Var for labels
ARG GITHUB_ACTOR
ARG GITHUB_REPOSITORY
ARG GITHUB_REF

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Paris
ENV LAB=QISKIT

LABEL org.opencontainers.image.title="Online ${quantum_env} Lab" \
      org.opencontainers.image.authors=${GITHUB_ACTOR} \
      org.opencontainers.image.vendor=${GITHUB_REPOSITORY} \
      org.opencontainers.image.source="https://github.com/mickahell/websites" \
      org.opencontainers.image.url="https://github.com/mickahell/websites/tags" \
      org.opencontainers.image.description="Online Quantum Lab for ${quantum_env} env" \
      org.opencontainers.image.os="Ubuntu Bionic" \
      org.opencontainers.image.version=${GITHUB_REF}

RUN apt-get update -yq
RUN pip3 install jupyterthemes

# Jupyter conf
RUN jt -t onedork -T -N
COPY quantum_lab/jupyter/jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py
COPY quantum_lab/jupyter/custom.js /root/.jupyter/custom/custom.js

ADD quantum_lab/jupyter/start_jupyter.sh /opt/quantum_lab/

EXPOSE 9999

# Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

CMD /opt/quantum_lab/start_jupyter.sh
