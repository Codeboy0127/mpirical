#!/bin/bash

set -e
set -eo pipefail

apt-get update; apt-get install -y make
conda config --set always_yes true --set changeps1 false --set quiet true
conda update -q conda
conda config --add channels conda-forge
conda env create --name ${ENV_NAME} python=${PYTHON} --quiet
conda env list
source activate ${ENV_NAME}
conda env update --file environment-dev.yml --quiet
pip install pip --upgrade
pip install --no-deps --quiet -e .
conda list --name ${ENV_NAME}
