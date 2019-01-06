#!/bin/bash

set -e
set -eo pipefail

echo; echo "===== UPDATE CONTAINER ====="; echo
apt-get update; apt-get install -y make

echo; echo "===== SETUP CONDA ====="; echo
conda config --set always_yes true --set changeps1 false --set quiet true
conda update --quiet conda
conda config --add channels conda-forge

echo; echo "===== CREATE ${ENV_NAME} ENVIRONMENT WITH PYTHON${PYTHON} ====="; echo
conda create --name ${ENV_NAME} python=${PYTHON} --quiet

echo; echo "===== ACTIVATE ${ENV_NAME} ENVIRONMENT ====="; echo
source activate ${ENV_NAME}

echo; echo "===== ${ENV_NAME} ENVIRONMENT PYTHON VERSION ====="; echo
python --version

echo; echo "===== INSTALL MPICH ====="; echo
conda install mpich
which mpicc
which gcc

echo; echo "===== INSTALL DEVELOPMENT REQUIREMENTS ====="; echo
pip install -r requirements/development.txt

echo; echo "===== INSTALL CODECOV ====="; echo
conda install codecov

echo; echo "===== INSTALL PACKAGE ====="; echo
pip install --no-deps --quiet -e .

echo; echo "===== CONDA LIST ${ENV_NAME} ====="; echo
conda list
