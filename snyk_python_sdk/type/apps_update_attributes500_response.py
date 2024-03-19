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

from snyk_python_sdk.type.apps_update_attributes500_response_errors import AppsUpdateAttributes500ResponseErrors
from snyk_python_sdk.type.apps_update_attributes500_response_jsonapi import AppsUpdateAttributes500ResponseJsonapi

class RequiredAppsUpdateAttributes500Response(TypedDict):
    errors: AppsUpdateAttributes500ResponseErrors

    jsonapi: AppsUpdateAttributes500ResponseJsonapi

class OptionalAppsUpdateAttributes500Response(TypedDict, total=False):
    pass

class AppsUpdateAttributes500Response(RequiredAppsUpdateAttributes500Response, OptionalAppsUpdateAttributes500Response):
    pass
