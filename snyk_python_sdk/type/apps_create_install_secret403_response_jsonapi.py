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


class RequiredAppsCreateInstallSecret403ResponseJsonapi(TypedDict):
    # Version of the JSON API specification this server supports.
    version: str

class OptionalAppsCreateInstallSecret403ResponseJsonapi(TypedDict, total=False):
    pass

class AppsCreateInstallSecret403ResponseJsonapi(RequiredAppsCreateInstallSecret403ResponseJsonapi, OptionalAppsCreateInstallSecret403ResponseJsonapi):
    pass
