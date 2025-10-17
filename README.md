# json-to-pydantic

JSON to [pydantic](https://docs.pydantic.dev/) generator

[![Screenshot](https://user-images.githubusercontent.com/653031/215360300-c3674889-bb8c-40e7-adfb-9e384fb61a7f.png)](https://falkben.github.io/json-to-pydantic/)

Page at [falkben.github.io/json-to-pydantic/](https://falkben.github.io/json-to-pydantic/)

## About

Inspired by [@brokenloop's](https://github.com/brokenloop) [`jsontopydantic`](https://github.com/brokenloop/jsontopydantic), this project implements the same conversion (using [`datamodel-code-generator`](https://github.com/koxudaxi/datamodel-code-generator)), but does the conversion entirely in the browser, using [PyScript](https://pyscript.net/) & [Pyodide](https://pyodide.org/en/stable/).

## Developer Notes

### Install

1. Create virtual environment and activate:

    `uv venv -p 3.13 && source .venv/bin/activate`

2. Install package

    `uv pip install -e . -r requirements.txt`

    Or with optional dev dependencies:

    `uv pip install -e ".[dev]" -r requirements.txt -r requirements_dev.txt`

### Dependencies

Dependencies are specified in `pyproject.toml` and managed with [pip-tools](https://github.com/jazzband/pip-tools/).

Generate lock files and sync pyscript dependencies:

```sh
uv pip compile pyproject.toml --quiet --output-file=requirements.txt && \
uv pip compile --extra=dev --output-file=requirements_dev.txt pyproject.toml --constraint requirements.txt --quiet && \
python sync_pyscript_requirements.py
```

### CI Checks

The CI pipeline includes a check to ensure that `pyscript.toml` stays synchronized with `requirements.txt`. If you update dependencies, make sure to run the sync command above. The CI will fail if the PyScript configuration is out of sync.

You can manually check synchronization status with:

```sh
bash check_pyscript_sync.sh
```
