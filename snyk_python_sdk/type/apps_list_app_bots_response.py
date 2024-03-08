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

from snyk_python_sdk.type.app_bot import AppBot
from snyk_python_sdk.type.json_api import JsonApi
from snyk_python_sdk.type.paginated_links import PaginatedLinks

class RequiredAppsListAppBotsResponse(TypedDict):
    data: typing.List[AppBot]

    jsonapi: JsonApi

    links: PaginatedLinks

class OptionalAppsListAppBotsResponse(TypedDict, total=False):
    pass

class AppsListAppBotsResponse(RequiredAppsListAppBotsResponse, OptionalAppsListAppBotsResponse):
    pass
