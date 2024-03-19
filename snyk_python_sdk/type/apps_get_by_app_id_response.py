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

from snyk_python_sdk.type.app_data import AppData
from snyk_python_sdk.type.json_api import JsonApi
from snyk_python_sdk.type.self_link import SelfLink

class RequiredAppsGetByAppIdResponse(TypedDict):
    pass

class OptionalAppsGetByAppIdResponse(TypedDict, total=False):
    items: AppData

    jsonapi: JsonApi

    links: SelfLink

class AppsGetByAppIdResponse(RequiredAppsGetByAppIdResponse, OptionalAppsGetByAppIdResponse):
    pass
