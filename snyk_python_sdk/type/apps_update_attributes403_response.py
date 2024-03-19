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

from snyk_python_sdk.type.apps_update_attributes403_response_errors import AppsUpdateAttributes403ResponseErrors
from snyk_python_sdk.type.apps_update_attributes403_response_jsonapi import AppsUpdateAttributes403ResponseJsonapi

class RequiredAppsUpdateAttributes403Response(TypedDict):
    errors: AppsUpdateAttributes403ResponseErrors

    jsonapi: AppsUpdateAttributes403ResponseJsonapi

class OptionalAppsUpdateAttributes403Response(TypedDict, total=False):
    pass

class AppsUpdateAttributes403Response(RequiredAppsUpdateAttributes403Response, OptionalAppsUpdateAttributes403Response):
    pass
