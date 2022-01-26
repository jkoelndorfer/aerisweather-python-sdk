"""
aerisweather/__version__.py
---------------------------

Contains the current version of the AerisWeather Python SDK.
"""

_module_name = __name__.split(".")[0]

try:
    from importlib.metadata import version as _v

    __version__ = _v(_module_name)
    del _v
except ImportError:
    from pkg_resources import get_distribution as _getdist

    __version__ = _getdist(_module_name).version
    del _getdist

del _module_name
