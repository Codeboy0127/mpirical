#!/bin/bash

echo "[Running Tests]"
pytest --junitxml=test-reports/junit.xml mpirical/tests/
