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


class RequiredAppsInstallSnykAppToOrg403ResponseJsonapi(TypedDict):
    # Version of the JSON API specification this server supports.
    version: str

class OptionalAppsInstallSnykAppToOrg403ResponseJsonapi(TypedDict, total=False):
    pass

class AppsInstallSnykAppToOrg403ResponseJsonapi(RequiredAppsInstallSnykAppToOrg403ResponseJsonapi, OptionalAppsInstallSnykAppToOrg403ResponseJsonapi):
    pass
