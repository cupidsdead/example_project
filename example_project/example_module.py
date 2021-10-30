"""

Authored by dilshad on 24/10/2021

example_package.example_module.py

This is an example module with example class to highlight documentation
packaging etc

"""

import pandas as pd
from typing import List


class ExampleClass:
    """
    This is an example class.
    """

    def __init__(self):
        """
        empty init
        """
        pass

    def summary(self, input: List) -> pd.DataFrame:
        """
        Given a list of int, this function will produce a summary
        of stats such as avg, mean, mode etc.
        param: input: list of int
        return: pd.DataFrame
        """
        df = pd.DataFrame(input, columns=["val1"])
        print(df.describe())
        return df.describe()
