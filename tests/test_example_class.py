"""
    Authored by dilshad on 30/10/2021
    This is an example pytest for example project
"""

from typing import (List)
from example_project.example_module import ExampleClass
import pandas as pd

class TestExampleClass:
    """
        This is an example test class, with test fixtures defined in conftest
    """

    def test_description(self, example_class: ExampleClass, example_data: List[int]):
        """
            Test that summar() returns a valid summary for an array of ints
        """
        summary = example_class.summary(example_data)
        assert not summary.empty, "no summary produced"
