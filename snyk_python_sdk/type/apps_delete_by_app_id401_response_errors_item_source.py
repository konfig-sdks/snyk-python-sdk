# coding: utf-8

"""
    Snyk API

    Missing description placeholder

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredAppsDeleteByAppId401ResponseErrorsItemSource(TypedDict):
    pass

class OptionalAppsDeleteByAppId401ResponseErrorsItemSource(TypedDict, total=False):
    # A string indicating which URI query parameter caused the error.
    parameter: str

    # A JSON Pointer [RFC6901] to the associated entity in the request document.
    pointer: str

class AppsDeleteByAppId401ResponseErrorsItemSource(RequiredAppsDeleteByAppId401ResponseErrorsItemSource, OptionalAppsDeleteByAppId401ResponseErrorsItemSource):
    pass
