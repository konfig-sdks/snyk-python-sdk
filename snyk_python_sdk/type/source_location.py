# coding: utf-8

"""
    Snyk API

    Snyk helps software-driven businesses develop fast and stay secure. Continuously find and fix vulnerabilities for npm, Maven, NuGet, RubyGems, PyPI and more.

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from snyk_python_sdk.type.region import Region

class RequiredSourceLocation(TypedDict):
    # A path to the file containing this issue, relative to the root of the project target, formatted using POSIX separators. 
    file: str

class OptionalSourceLocation(TypedDict, total=False):
    region: Region

class SourceLocation(RequiredSourceLocation, OptionalSourceLocation):
    pass
