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


class RequiredAppsListApps409ResponseJsonapi(TypedDict):
    # Version of the JSON API specification this server supports.
    version: str

class OptionalAppsListApps409ResponseJsonapi(TypedDict, total=False):
    pass

class AppsListApps409ResponseJsonapi(RequiredAppsListApps409ResponseJsonapi, OptionalAppsListApps409ResponseJsonapi):
    pass