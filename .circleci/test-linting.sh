#!/bin/bash

set -o nounset
set -o errexit
set -o xtrace

echo "[Check linting]"
flake8
