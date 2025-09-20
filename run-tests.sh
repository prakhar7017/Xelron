#!/usr/bin/env bash
set -euo pipefail

# Install test dependencies
python3 -m pip install -r requirements.txt >/dev/null 2>&1 || true

# Run the test suite
python3 -m pytest -v tests/test_outputs.py
