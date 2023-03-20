FROM mickahell/quantum_lab_qiskit:latest

# Var for labels
ARG GITHUB_ACTOR
ARG GITHUB_REPOSITORY
ARG GITHUB_REF

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Paris

LABEL org.opencontainers.image.title="Games" \
      org.opencontainers.image.vendor=${GITHUB_REPOSITORY} \
      org.opencontainers.image.source="https://github.com/mickahell/websites" \
      org.opencontainers.image.url="https://github.com/mickahell/websites/tags" \
      org.opencontainers.image.description="Games" \
      org.opencontainers.image.version=${GITHUB_REF}

RUN apt-get update -yq && apt-get dist-upgrade -yq
RUN apt-get install build-essential cmake git libjson-c-dev libwebsockets-dev jq -y && \
    git clone https://github.com/tsl0922/ttyd.git && \
    cd ttyd && mkdir build && cd build && \
    cmake .. && \
    make && make install
    
RUN pip3 install qiskit_optimization fire

ADD games/qnim-game /opt/qnim/

ADD games/qnim-game/start.sh .

# Go download my games
ADD https://github.com/mickahell/quantum_Nim-game/archive/refs/tags/2.2.tar.gz /opt/qnim/
RUN tar -xf /opt/qnim/2.2.tar.gz -C /opt/qnim/ && \
    mv /opt/qnim/quantum_Nim-game-* /opt/qnim/quantum_nim-game

EXPOSE 7681

CMD ./start.sh
