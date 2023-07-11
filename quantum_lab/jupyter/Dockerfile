ARG LAB_ENV
#ARG LAB_ENV=qiskit-full
#ARG LAB_ENV=qml
#ARG LAB_ENV=cirq

FROM mickahell/quantum_lab_${LAB_ENV}:latest

ARG LAB_ENV

# Var for labels
ARG GITHUB_ACTOR
ARG GITHUB_REPOSITORY
ARG GITHUB_REF

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Paris
ENV LAB=${LAB_ENV}

LABEL org.opencontainers.image.title="Online ${LAB_ENV} Lab" \
      org.opencontainers.image.authors=${GITHUB_ACTOR} \
      org.opencontainers.image.vendor=${GITHUB_REPOSITORY} \
      org.opencontainers.image.source="https://github.com/mickahell/websites" \
      org.opencontainers.image.url="https://github.com/mickahell/websites/tags" \
      org.opencontainers.image.description="Online Quantum Lab for ${LAB_ENV} env" \
      org.opencontainers.image.os="Ubuntu Bionic" \
      org.opencontainers.image.version=${GITHUB_REF}

RUN apt-get update -yq && apt-get dist-upgrade -yq
RUN pip install jupyterthemes

# Jupyter conf
#RUN jt -t onedork -T -N
COPY quantum_lab/jupyter/jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py
COPY quantum_lab/jupyter/custom.js /root/.jupyter/custom/custom.js
#COPY quantum_lab/jupyter/custom.css /root/.jupyter/custom/custom.css
#COPY quantum_lab/jupyter/${LAB_ENV}_logo.png /root/.jupyter/custom/logo.png

ADD quantum_lab/jupyter/start_jupyter.sh /opt/quantum_lab/

EXPOSE 9999

# Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

CMD /opt/quantum_lab/start_jupyter.sh
