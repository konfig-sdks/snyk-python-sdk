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


class RequiredAppsGetByClientId401ResponseJsonapi(TypedDict):
    # Version of the JSON API specification this server supports.
    version: str

class OptionalAppsGetByClientId401ResponseJsonapi(TypedDict, total=False):
    pass

class AppsGetByClientId401ResponseJsonapi(RequiredAppsGetByClientId401ResponseJsonapi, OptionalAppsGetByClientId401ResponseJsonapi):
    pass
