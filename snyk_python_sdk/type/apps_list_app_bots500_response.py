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

from snyk_python_sdk.type.apps_list_app_bots500_response_errors import AppsListAppBots500ResponseErrors
from snyk_python_sdk.type.apps_list_app_bots500_response_jsonapi import AppsListAppBots500ResponseJsonapi

class RequiredAppsListAppBots500Response(TypedDict):
    errors: AppsListAppBots500ResponseErrors

    jsonapi: AppsListAppBots500ResponseJsonapi

class OptionalAppsListAppBots500Response(TypedDict, total=False):
    pass

class AppsListAppBots500Response(RequiredAppsListAppBots500Response, OptionalAppsListAppBots500Response):
    pass
