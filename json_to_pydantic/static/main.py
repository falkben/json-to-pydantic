import json

from datamodel_code_generator.parser.jsonschema import JsonSchemaParser
from genson import SchemaBuilder


def convert_to_schema(input_text: str, all_optional: bool, snake_case_field: bool):
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


def convert(_event):
    from pyscript import document

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


if __name__ == "__main__":
    convert(None)
