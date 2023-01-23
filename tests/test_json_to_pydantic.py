"""Tests for `json_to_pydantic` package."""

from json_to_pydantic.static import main


def test_json_to_pydantic_import():
    import json_to_pydantic  # noqa: F401


def test_convert():
    simple = """{
  "a": "b",
  "c": 123
}"""
    result = main.convert_to_schema(simple, False, False)
    print(result)
