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


class RequiredAppsListGroupAppInstalls404ResponseErrorsItemSource(TypedDict):
    pass

class OptionalAppsListGroupAppInstalls404ResponseErrorsItemSource(TypedDict, total=False):
    # A string indicating which URI query parameter caused the error.
    parameter: str

    # A JSON Pointer [RFC6901] to the associated entity in the request document.
    pointer: str

class AppsListGroupAppInstalls404ResponseErrorsItemSource(RequiredAppsListGroupAppInstalls404ResponseErrorsItemSource, OptionalAppsListGroupAppInstalls404ResponseErrorsItemSource):
    pass
