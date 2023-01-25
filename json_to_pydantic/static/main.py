import asyncio
import json

import micropip


def convert_to_schema(input_text: str, all_optional: bool, snake_case_field: bool):
    from datamodel_code_generator.parser.jsonschema import JsonSchemaParser
    from genson import SchemaBuilder

    builder = SchemaBuilder()
    input = json.loads(input_text)
    builder.add_object(input)
    schema = builder.to_schema()
    if all_optional:
        schema["required"] = []

    parser = JsonSchemaParser(
        source=json.dumps(schema),
        base_class="pydantic.BaseModel",
        snake_case_field=snake_case_field,
    )

    return parser.parse()


async def convert():

    from js import document

    # todo: set button to disabled and show loading spinner

    input_text = document.querySelector("#json-ta").value

    all_optional = document.querySelector("#all_optional_checkbox").checked

    snake_case_field = document.querySelector("#snake_case_field_checkbox").checked

    try:
        model = convert_to_schema(input_text, all_optional, snake_case_field)
    except Exception as e:
        print(e)
        return None

    document.querySelector("#pydantic-ta").value = model

    return model


async def load_deps():
    # install without deps using micropip to avoid several deps
    await micropip.install(
        "https://files.pythonhosted.org/packages/af/e9/10c8eb73138bcb6b124e2fc2df7ec8b163f8710d947d9e685b22db215010/datamodel_code_generator-0.16.1-py3-none-any.whl",
        deps=False,
    )


async def setup():
    await load_deps()
    await convert()


asyncio.create_task(setup())
