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


class RequiredAppsGetByClientId400ResponseJsonapi(TypedDict):
    # Version of the JSON API specification this server supports.
    version: str

class OptionalAppsGetByClientId400ResponseJsonapi(TypedDict, total=False):
    pass

class AppsGetByClientId400ResponseJsonapi(RequiredAppsGetByClientId400ResponseJsonapi, OptionalAppsGetByClientId400ResponseJsonapi):
    pass
