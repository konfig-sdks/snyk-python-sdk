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


class RequiredAppsCreateOrganizationApp403ResponseJsonapi(TypedDict):
    # Version of the JSON API specification this server supports.
    version: str

class OptionalAppsCreateOrganizationApp403ResponseJsonapi(TypedDict, total=False):
    pass

class AppsCreateOrganizationApp403ResponseJsonapi(RequiredAppsCreateOrganizationApp403ResponseJsonapi, OptionalAppsCreateOrganizationApp403ResponseJsonapi):
    pass