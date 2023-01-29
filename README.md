# json-to-pydantic

JSON to [pydantic](https://docs.pydantic.dev/) generator

[![Screenshot](https://user-images.githubusercontent.com/653031/215356255-21155438-a910-4cd7-8eb1-106384dd2c77.png)](https://falkben.github.io/json-to-pydantic/)

Page at [falkben.github.io/json-to-pydantic/](https://falkben.github.io/json-to-pydantic/)

## About

Inspired by [@brokenloop's](https://github.com/brokenloop) [`jsontopydantic`](https://github.com/brokenloop/jsontopydantic), this project implements the same conversion (using [`datamodel-code-generator`](https://github.com/koxudaxi/datamodel-code-generator)), but does the conversion entirely in the browser, using [PyScript](https://pyscript.net/) & [Pyodide](https://pyodide.org/en/stable/).

## Developer Notes

### Install

1. Create virtual environment and activate:

    `python -m venv .venv && source .venv/bin/activate`

2. Install package

    `pip install -e . -r requirements.txt`

    Or with optional dev dependencies:

    `pip install -e ".[dev]" -r requirements.txt -r requirements_dev.txt`

### Dependencies

Dependencies are specified in `pyproject.toml` and managed with [pip-tools](https://github.com/jazzband/pip-tools/).

1. Install `pip-tools` (globally with [pipx](https://github.com/pypa/pipx) or in local virtual environment with pip)

2. Generate lock files:

    ```sh
    pip-compile pyproject.toml --quiet && \
    pip-compile --extra=dev --output-file=requirements_dev.txt pyproject.toml --quiet
    ```

To upgrade a dependency, pass the `--upgrade-package` flag along with the name of the package, or to upgrade all packages, pass the `--upgrade` flag to the command.

More information at: <https://github.com/jazzband/pip-tools/>
