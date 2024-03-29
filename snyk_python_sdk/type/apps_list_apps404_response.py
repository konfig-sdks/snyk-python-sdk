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

from snyk_python_sdk.type.apps_list_apps404_response_errors import AppsListApps404ResponseErrors
from snyk_python_sdk.type.apps_list_apps404_response_jsonapi import AppsListApps404ResponseJsonapi

class RequiredAppsListApps404Response(TypedDict):
    errors: AppsListApps404ResponseErrors

    jsonapi: AppsListApps404ResponseJsonapi

class OptionalAppsListApps404Response(TypedDict, total=False):
    pass

class AppsListApps404Response(RequiredAppsListApps404Response, OptionalAppsListApps404Response):
    pass
