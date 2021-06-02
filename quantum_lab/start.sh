#!/bin/bash

rm start_jupyter.sh

#openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout mykey.key -out mycert.pem

#jupyter notebook --allow-root --port=8888 --no-browser --ip='*' --NotebookApp.token='' --NotebookApp.password='' --certfile=mycert.pem --keyfile mykey.key

jupyter notebook --allow-root --port=8888 --no-browser --ip='*' --NotebookApp.token='' --NotebookApp.password=''
