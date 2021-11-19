"""

Explicit imports:
    profit.fit
    profit.run
    profit.sur
    profit.ui
    profit.uq
"""

from . import main
from . import pre
from . import config

from . import util

# Retrieving package version at runtime
# https://pypi.org/project/setuptools-scm/
try:
    from setuptools_scm import get_version as version
    __version__ = version(root='..', relative_to=__file__)
    del version
except ModuleNotFoundError:
    try:
        from importlib.metadata import version, PackageNotFoundError
    except ModuleNotFoundError:  # required for python3.7
        from importlib_metadata import version, PackageNotFoundError

    try:
        __version__ = version("profit")
    except PackageNotFoundError:
        # package is not installed
        __version__ = "?"

    del version, PackageNotFoundError  # clean up namespace
