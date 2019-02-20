#!/bin/bash

set -o nounset
set -o errexit
set -o xtrace

echo "[Running Tests]"
pytest --nompiunstable mpirical/tests/
pytest --mpiunstable mpirical/tests/
