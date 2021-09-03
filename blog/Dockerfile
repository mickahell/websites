FROM ubuntu:20.04

# Var for labels
ARG GITHUB_ACTOR
ARG GITHUB_REPOSITORY
ARG GITHUB_REF

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Paris

LABEL org.opencontainers.image.title="Blog" \
      org.opencontainers.image.authors=${GITHUB_ACTOR} \
      org.opencontainers.image.vendor=${GITHUB_REPOSITORY} \
      org.opencontainers.image.source="https://github.com/mickahell/xtraorbitals.xyz/blog" \
      org.opencontainers.image.url="https://github.com/mickahell/websites/tags" \
      org.opencontainers.image.description="xtra Orbitals" \
      org.opencontainers.image.os="Ubuntu Bionic" \
      org.opencontainers.image.version=${GITHUB_REF}

RUN apt-get update -yq

ADD blog/ /opt/blog/
ADD menu.py /opt/blog/

ADD blog/start.sh .

RUN pip install /opt/blog/requirements.txt

EXPOSE 8501

CMD ./start.sh
