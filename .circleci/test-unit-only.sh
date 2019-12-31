#!/bin/bash

set -o nounset
set -o errexit
set -o xtrace

echo "[Running Tests]"
pytest --verbose mpirical/tests/
