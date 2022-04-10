"""
tests/test_logging
------------------

Tests functionality in the aerisweather.logging module.
"""

import logging

from aerisweather.logging import getLogger


class TestGetLogger:
    """
    Tests the functionality of the getLogger function.
    """

    def test_returns_logger(self) -> None:
        """
        Tests that getLogger returns a logging.Logger.
        """
        log = getLogger("test")

        assert isinstance(log, logging.Logger)

    def test_logger_namespaced_under_aerisweather(self) -> None:
        """
        Tests that getLogger's logger is namespaced under aerisweather.
        """
        log = getLogger("test")

        assert log.name.startswith("aerisweather.")
