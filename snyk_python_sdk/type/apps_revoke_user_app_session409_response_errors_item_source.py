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


class RequiredAppsRevokeUserAppSession409ResponseErrorsItemSource(TypedDict):
    pass

class OptionalAppsRevokeUserAppSession409ResponseErrorsItemSource(TypedDict, total=False):
    # A string indicating which URI query parameter caused the error.
    parameter: str

    # A JSON Pointer [RFC6901] to the associated entity in the request document.
    pointer: str

class AppsRevokeUserAppSession409ResponseErrorsItemSource(RequiredAppsRevokeUserAppSession409ResponseErrorsItemSource, OptionalAppsRevokeUserAppSession409ResponseErrorsItemSource):
    pass
