#!/bin/bash

set -o nounset
set -o errexit
set -o xtrace

echo "[Running Tests with Coverage]"
pytest --verbose --junitxml=test-reports/junit.xml --cov=./ mpirical/tests/

echo

echo "[Uploading Coverage]"
codecov