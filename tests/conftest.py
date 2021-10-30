"""
    Authored by dilshad on 24/10/2021

    PyTest uses this to detect test fixtures used by multiple test modules.
    https://docs.pytest.org/en/latest/fixture.html.
"""

import json
from typing import Any, List

import pytest

from example_project.example_module import ExampleClass


def load_test_json(fn="test_data/example_class_data.json", json_path="") -> Any:
    """Load test data.

    :return: Test data.
    :rtype: Any
    """

    with open(fn) as file:
        json_data = file.read()

    data = json.loads(json_data)
    if not json_path:
        return data
    for path in json_path.split("!"):
        data = data[path]
    return data


@pytest.fixture
def example_class() -> ExampleClass:
    """Return an ExampleClass for use with tests.

    :return: A example class.
    :rtype: ExampleClass
    """

    return ExampleClass()

@pytest.fixture
def example_data() -> List[int]:
    """Return an ExampleClass for use with tests.

    :return: A list of int.
    :rtype: List[int]
    """
    dat = load_test_json(json_path="example_class")
    return dat

