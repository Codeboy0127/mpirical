#!/bin/bash

set -e
set -eo pipefail

echo; echo "===== UPDATE CONTAINER ====="; echo
apt-get update; apt-get install -y make

echo; echo "===== SETUP CONDA ====="; echo
conda config --set always_yes true --set changeps1 false --set quiet true
conda update --quiet conda
conda config --add channels conda-forge

echo; echo "===== CREATE ${ENV_NAME} ENVIRONMENT WITH PYTHON ${PYTHON}====="; echo
conda env create --name ${ENV_NAME} python=${PYTHON} --quiet

echo; echo "===== ACTIVATE ${ENV_NAME} ENVIRONMENT ====="; echo
source activate ${ENV_NAME}

echo; echo "===== UPDATE ${ENV_NAME} ENVIRONMENT ====="; echo
conda env update --file environment-dev.yml --quiet

echo; echo "===== UPDATE PIP ====="; echo
pip install pip --upgrade

echo; echo "===== INSTALL PACKAGE ====="; echo
pip install --no-deps --quiet -e .

echo; echo "===== CONDA LIST ${ENV_NAME} ====="; echo
conda list

echo; echo "===== PIP LIST ${ENV_NAME} ====="; echo
pip list
