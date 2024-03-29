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

from snyk_python_sdk.type.apps_get_by_app_id401_response_errors import AppsGetByAppId401ResponseErrors
from snyk_python_sdk.type.apps_get_by_app_id401_response_jsonapi import AppsGetByAppId401ResponseJsonapi

class RequiredAppsGetByAppId401Response(TypedDict):
    errors: AppsGetByAppId401ResponseErrors

    jsonapi: AppsGetByAppId401ResponseJsonapi

class OptionalAppsGetByAppId401Response(TypedDict, total=False):
    pass

class AppsGetByAppId401Response(RequiredAppsGetByAppId401Response, OptionalAppsGetByAppId401Response):
    pass
