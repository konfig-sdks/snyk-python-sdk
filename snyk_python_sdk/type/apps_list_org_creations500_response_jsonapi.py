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


class RequiredAppsListOrgCreations500ResponseJsonapi(TypedDict):
    # Version of the JSON API specification this server supports.
    version: str

class OptionalAppsListOrgCreations500ResponseJsonapi(TypedDict, total=False):
    pass

class AppsListOrgCreations500ResponseJsonapi(RequiredAppsListOrgCreations500ResponseJsonapi, OptionalAppsListOrgCreations500ResponseJsonapi):
    pass
