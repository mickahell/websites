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

RUN apt-get update -yq
RUN pip3 install streamlit

ADD games/ /opt/games/

ADD games/start.sh .

# Go download my games
ADD https://github.com/mickahell/quantum_pokemon-fight/archive/refs/tags/3.1.tar.gz /opt/games/
RUN tar -xf /opt/games/3.1.tar.gz -C /opt/games/ && mv quantum_pokemon-fight-* quantum_pokemon-fight

## TODO add --> qNim

EXPOSE 8501

CMD ./start.sh
