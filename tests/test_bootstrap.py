"""
tests/test_bootstrap.py
-----------------------

Contains dummy tests whose purpose is to validate pytest
and code coverage are working correctly in the project.
"""

import aerisweather


def test_ok() -> None:
    assert aerisweather.__version__ is not None
