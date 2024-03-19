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

from snyk_python_sdk.type.apps_update_attributes404_response_errors import AppsUpdateAttributes404ResponseErrors
from snyk_python_sdk.type.apps_update_attributes404_response_jsonapi import AppsUpdateAttributes404ResponseJsonapi

class RequiredAppsUpdateAttributes404Response(TypedDict):
    errors: AppsUpdateAttributes404ResponseErrors

    jsonapi: AppsUpdateAttributes404ResponseJsonapi

class OptionalAppsUpdateAttributes404Response(TypedDict, total=False):
    pass

class AppsUpdateAttributes404Response(RequiredAppsUpdateAttributes404Response, OptionalAppsUpdateAttributes404Response):
    pass
