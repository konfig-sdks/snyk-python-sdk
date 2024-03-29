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

from snyk_python_sdk.type.json_api import JsonApi
from snyk_python_sdk.type.paginated_links import PaginatedLinks
from snyk_python_sdk.type.session_data import SessionData

class RequiredAppsGetActiveSessionsResponse(TypedDict):
    data: typing.List[SessionData]

    jsonapi: JsonApi

class OptionalAppsGetActiveSessionsResponse(TypedDict, total=False):
    links: PaginatedLinks

class AppsGetActiveSessionsResponse(RequiredAppsGetActiveSessionsResponse, OptionalAppsGetActiveSessionsResponse):
    pass
