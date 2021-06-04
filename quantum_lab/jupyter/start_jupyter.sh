#!/bin/bash

#openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout mykey.key -out mycert.pem

#jupyter notebook --allow-root --port=8888 --no-browser --ip='*' --NotebookApp.token='' --NotebookApp.password='' --certfile=mycert.pem --keyfile mykey.key

cd /opt/quantum_lab/data/share

jupyter notebook --allow-root --port=9999 --no-browser --ip='*' --NotebookApp.token='' --NotebookApp.password=''
