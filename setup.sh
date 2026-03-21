#!/usr/bin/env bash
set -e

python3 -m venv .venv
.venv/bin/pip install PyQt6  # use the venv's pip directly, no activation needed

echo "Done. Run 'source .venv/bin/activate' to activate the venv."