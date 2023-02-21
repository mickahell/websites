FROM ubuntu:22.04

# Var for labels
ARG GITHUB_ACTOR
ARG GITHUB_REPOSITORY
ARG GITHUB_REF

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Paris

LABEL org.opencontainers.image.title="About" \
      org.opencontainers.image.authors=${GITHUB_ACTOR} \
      org.opencontainers.image.vendor=${GITHUB_REPOSITORY} \
      org.opencontainers.image.source="https://github.com/mickahell/websites/about" \
      org.opencontainers.image.url="https://github.com/mickahell/websites/tags" \
      org.opencontainers.image.description="xtra Orbitals" \
      org.opencontainers.image.os="Ubuntu Focal" \
      org.opencontainers.image.version=${GITHUB_REF}

RUN apt-get update -yq \
&& apt-get install python3-pip -y

RUN pip3 install streamlit==1.16.0

ADD about/ /opt/about/
ADD common/common.py /opt/about/

ADD about/start.sh .

EXPOSE 8501

CMD ./start.sh
