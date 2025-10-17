#!/bin/bash

# Script to check if pyscript.toml is synchronized with requirements.txt
# This script runs the sync command and checks if any changes were made to pyscript.toml

set -euo pipefail

echo "Checking PyScript synchronization..."

# Store the current content of pyscript.toml
cp json_to_pydantic/static/pyscript.toml /tmp/pyscript_before.toml

# Run the sync script
python sync_pyscript_requirements.py

# Check if pyscript.toml was modified
if ! diff -q /tmp/pyscript_before.toml json_to_pydantic/static/pyscript.toml > /dev/null; then
    echo "✗ pyscript.toml was NOT synchronized with requirements.txt"
    echo "Changes detected in pyscript.toml:"
    diff /tmp/pyscript_before.toml json_to_pydantic/static/pyscript.toml || true
    echo ""
    echo "The sync script made changes, which means the files were out of sync."
    echo "Please commit these changes or ensure your local files are up to date."
    exit 1
else
    echo "✓ pyscript.toml is synchronized with requirements.txt"
    exit 0
fi
