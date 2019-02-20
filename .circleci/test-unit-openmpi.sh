#!/bin/bash

set -o nounset
set -o errexit
set -o xtrace

echo "[Running Tests]"
pytest --junitxml=test-reports/junit.xml mpirical/tests/test_tasks.py
pytest --junitxml=test-reports/junit.xml mpirical/tests/test_decorator.py
pytest --junitxml=test-reports/junit.xml mpirical/tests/test_serialization.py
pytest --junitxml=test-reports/junit.xml mpirical/tests/test_mpiruntask.py::test_mpirun_task_file_serial
pytest --junitxml=test-reports/junit.xml mpirical/tests/test_mpiruntask.py::test_mpirun_task_file_parallel
