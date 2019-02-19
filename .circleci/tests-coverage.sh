#!/bin/bash

echo "[Running Tests with Coverage]"
pytest --junitxml=test-reports/junit.xml --cov=./ mpirical/tests/

echo

echo "[Uploading Coverage]"
codecov