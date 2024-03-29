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

from snyk_python_sdk.type.apps_list_app_bots401_response_errors import AppsListAppBots401ResponseErrors
from snyk_python_sdk.type.apps_list_app_bots401_response_jsonapi import AppsListAppBots401ResponseJsonapi

class RequiredAppsListAppBots401Response(TypedDict):
    errors: AppsListAppBots401ResponseErrors

    jsonapi: AppsListAppBots401ResponseJsonapi

class OptionalAppsListAppBots401Response(TypedDict, total=False):
    pass

class AppsListAppBots401Response(RequiredAppsListAppBots401Response, OptionalAppsListAppBots401Response):
    pass
