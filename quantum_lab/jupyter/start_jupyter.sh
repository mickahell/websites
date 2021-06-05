#!/bin/bash

cd /opt/quantum_lab/data/share

jupyter notebook --allow-root --port=9999 --no-browser --ip='*' --NotebookApp.token='' --NotebookApp.password=''
