#!/bin/bash

set -o nounset
set -o errexit
set -o xtrace

echo "[Building documentation]"
cd docs
make html
