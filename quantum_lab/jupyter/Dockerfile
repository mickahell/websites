FROM mickahell/quantum_lab_qiskit:latest

# Var for labels
ARG GITHUB_ACTOR
ARG GITHUB_REPOSITORY
ARG GITHUB_REF

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Paris
ENV LAB=qiskit
ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8

LABEL org.opencontainers.image.title="Online qiskit Lab" \
      org.opencontainers.image.authors=${GITHUB_ACTOR} \
      org.opencontainers.image.vendor=${GITHUB_REPOSITORY} \
      org.opencontainers.image.source="https://github.com/mickahell/websites" \
      org.opencontainers.image.url="https://github.com/mickahell/websites/tags" \
      org.opencontainers.image.description="Online Quantum Lab for qiskit env" \
      org.opencontainers.image.version=${GITHUB_REF}

RUN apt-get update -yq && apt-get dist-upgrade -yq

# Jupyter conf
COPY quantum_lab/jupyter/jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py

ADD quantum_lab/jupyter/start_jupyter.sh /opt/quantum_lab/

EXPOSE 9999

# Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

CMD /opt/quantum_lab/start_jupyter.sh
