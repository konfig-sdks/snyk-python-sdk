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

from snyk_python_sdk.type.apps_get_by_app_id400_response_errors import AppsGetByAppId400ResponseErrors
from snyk_python_sdk.type.apps_get_by_app_id400_response_jsonapi import AppsGetByAppId400ResponseJsonapi

class RequiredAppsGetByAppId400Response(TypedDict):
    errors: AppsGetByAppId400ResponseErrors

    jsonapi: AppsGetByAppId400ResponseJsonapi

class OptionalAppsGetByAppId400Response(TypedDict, total=False):
    pass

class AppsGetByAppId400Response(RequiredAppsGetByAppId400Response, OptionalAppsGetByAppId400Response):
    pass
