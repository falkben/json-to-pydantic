#!/usr/bin/env python3

"""Script which synchronizes the requirements.txt file with the pyscript.toml file"""

import toml


def main() -> int:
    with open("json_to_pydantic/static/pyscript.toml", "r") as f:
        pyscript_config = toml.load(f)

    with open("requirements.txt", "r") as f:
        requirements = [
            line.strip()
            for line in f.read().splitlines()
            if line.strip() and not line.strip().startswith("#")
        ]

    pyscript_config["packages"] = requirements

    with open("json_to_pydantic/static/pyscript.toml", "w") as f:
        toml.dump(pyscript_config, f)
    print("Synchronized requirements.txt with pyscript.toml")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
