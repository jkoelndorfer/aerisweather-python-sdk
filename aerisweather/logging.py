"""
aerisweather/logging
--------------------

Contains logging helper code.
"""

import logging


def getLogger(name: str) -> logging.Logger:
    """
    Small wrapper function around ``getLogger`` to ensure all loggers are
    appropriately namespaced under ``aerisweather``.

    :param name: the name of the logger to get
    :return: a logger of the given name, prefixed by ``aerisweather.``
    """
    return logging.getLogger(f"aerisweather.{name}")
