#!/bin/bash

cd /opt/quantum_lab/data/share/

LANGUAGE="" LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 jupyter notebook --allow-root --port=9999 --no-browser --ip='*' --NotebookApp.token=''
