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

from snyk_python_sdk.type.apps_delete_by_app_id401_response_errors import AppsDeleteByAppId401ResponseErrors
from snyk_python_sdk.type.apps_delete_by_app_id401_response_jsonapi import AppsDeleteByAppId401ResponseJsonapi

class RequiredAppsDeleteByAppId401Response(TypedDict):
    errors: AppsDeleteByAppId401ResponseErrors

    jsonapi: AppsDeleteByAppId401ResponseJsonapi

class OptionalAppsDeleteByAppId401Response(TypedDict, total=False):
    pass

class AppsDeleteByAppId401Response(RequiredAppsDeleteByAppId401Response, OptionalAppsDeleteByAppId401Response):
    pass
