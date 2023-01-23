import json


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

    model = convert_to_schema(input_text, all_optional, snake_case_field)

    document.querySelector("#pydantic-ta").value = model

    return model
