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


class RequiredAppsListAppBots500ResponseJsonapi(TypedDict):
    # Version of the JSON API specification this server supports.
    version: str

class OptionalAppsListAppBots500ResponseJsonapi(TypedDict, total=False):
    pass

class AppsListAppBots500ResponseJsonapi(RequiredAppsListAppBots500ResponseJsonapi, OptionalAppsListAppBots500ResponseJsonapi):
    pass
