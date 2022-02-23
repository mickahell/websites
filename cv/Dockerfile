FROM ubuntu:20.04

# Var for labels
ARG GITHUB_ACTOR
ARG GITHUB_REPOSITORY
ARG GITHUB_REF

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Paris

LABEL org.opencontainers.image.title="Curriculum Vitae" \
      org.opencontainers.image.authors=${GITHUB_ACTOR} \
      org.opencontainers.image.vendor=${GITHUB_REPOSITORY} \
      org.opencontainers.image.source="https://github.com/mickahell/websites" \
      org.opencontainers.image.url="https://github.com/mickahell/websites/tags" \
      org.opencontainers.image.description="Curriculum Vitae" \
      org.opencontainers.image.os="Ubuntu Focal" \
      org.opencontainers.image.version=${GITHUB_REF}

RUN apt-get update -yq \
&& apt-get install python3-pip -y

ADD cv/ /opt/cv/

ADD cv/start.sh .

RUN pip3 install --upgrade pip setuptools
RUN pip3 install -r /opt/cv/requirements.txt

EXPOSE 8501

CMD ./start.sh
