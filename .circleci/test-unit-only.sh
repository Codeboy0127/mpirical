#!/bin/bash

set -o nounset
set -o errexit
set -o xtrace

echo "[Running Tests]"
pytest --junitxml=test-reports/junit.xml mpirical/tests/
