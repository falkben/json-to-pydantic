from pathlib import Path
from tempfile import TemporaryDirectory

from pyscript import Element


async def convert():

    from datamodel_code_generator import InputFileType, generate

    input = Element("json-ta").value

    with TemporaryDirectory() as temporary_directory_name:
        temporary_directory = Path(temporary_directory_name)
        output = Path(temporary_directory / "model.py")
        generate(
            input,
            input_file_type=InputFileType.JsonSchema,
            input_filename="example.json",
            output=output,
            disable_timestamp=True,
        )
        model = output.read_text()

    model = "\n".join(model.splitlines()[3:])

    Element("pydantic-ta").write(model)
    return model
