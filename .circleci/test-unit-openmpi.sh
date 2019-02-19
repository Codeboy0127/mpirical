#!/bin/bash

echo "[Running Tests]"
pytest --junitxml=test-reports/junit.xml mpirical/tests/test_tasks.py
pytest --junitxml=test-reports/junit.xml mpirical/tests/test_decorator.py
pytest --junitxml=test-reports/junit.xml mpirical/tests/test_serialization.py
pytest --junitxml=test-reports/junit.xml mpirical/tests/test_mpiruntask.py
