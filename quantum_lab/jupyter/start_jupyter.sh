#!/bin/bash

cd /opt/quantum_lab/data/share

if [[ $LAB = "QISKIT" ]]
then
    port=9999
elif [[ $LAB = "PENNYLANE" ]]
then
    port=9998
elif [[ $LAB = "CIRQ" ]]
then
    port=9997
fi

jupyter notebook --allow-root --port=$port --no-browser --ip='*' --NotebookApp.token='' --NotebookApp.password=''
