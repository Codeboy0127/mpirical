#!/bin/bash

set -o nounset
set -o errexit
set -o xtrace

echo "[Running Tests]"
pytest -m 'not mpiunstable' mpirical/tests/
pytest -m mpiunstable mpirical/tests/
