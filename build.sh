#!/bin/bash

set -euo pipefail

python -m pip install --upgrade build

# genson
rm -rf /tmp/GenSON
git clone --depth 1 --branch v1.2.2 git@github.com:wolverdude/GenSON.git /tmp/GenSON
python -m build /tmp/GenSON
cp /tmp/GenSON/dist/*.whl json_to_pydantic/static/wheels

# Other packages have pre-build wheels on pypi so we use those instead
