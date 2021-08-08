FROM mickahell/quantum_lab_qiskit:latest

# Var for labels
ARG GITHUB_ACTOR
ARG GITHUB_REPOSITORY
ARG GITHUB_REF

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Paris

LABEL org.opencontainers.image.title="Games" \
      org.opencontainers.image.authors=${GITHUB_ACTOR} \
      org.opencontainers.image.vendor=${GITHUB_REPOSITORY} \
      org.opencontainers.image.source="https://github.com/mickahell/websites" \
      org.opencontainers.image.url="https://github.com/mickahell/websites/tags" \
      org.opencontainers.image.description="Games" \
      org.opencontainers.image.os="Ubuntu Bionic" \
      org.opencontainers.image.version=${GITHUB_REF}

RUN apt-get update -yq && apt-get dist-upgrade -yq
RUN apt-get install build-essential cmake git libjson-c-dev libwebsockets-dev jq -y && \
    git clone https://github.com/tsl0922/ttyd.git && \
    cd ttyd && mkdir build && cd build && \
    cmake .. && \
    make && make install

ADD games/qpokemon-fight /opt/qpokemon/

ADD games/qpokemon-fight/start.sh .

# Go download my games
ADD https://github.com/mickahell/quantum_pokemon-fight/archive/refs/tags/3.6.tar.gz /opt/qpokemon/
RUN tar -xf /opt/qpokemon/3.6.tar.gz -C /opt/qpokemon/ && \
    mv /opt/qpokemon/quantum_pokemon-fight-* /opt/qpokemon/quantum_pokemon-fight

EXPOSE 7681
VOLUME /opt/qpokemon/quantum_pokemon-fight/stats

CMD ./start.sh
