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

from snyk_python_sdk.type.app_install_data import AppInstallData
from snyk_python_sdk.type.json_api import JsonApi
from snyk_python_sdk.type.paginated_links import PaginatedLinks

class RequiredAppsListUserInstalledAppsResponse(TypedDict):
    data: typing.List[AppInstallData]

    jsonapi: JsonApi

    links: PaginatedLinks

class OptionalAppsListUserInstalledAppsResponse(TypedDict, total=False):
    pass

class AppsListUserInstalledAppsResponse(RequiredAppsListUserInstalledAppsResponse, OptionalAppsListUserInstalledAppsResponse):
    pass
