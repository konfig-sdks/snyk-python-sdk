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

from snyk_python_sdk.type.apps_delete_app_by_id409_response_errors import AppsDeleteAppById409ResponseErrors
from snyk_python_sdk.type.apps_delete_app_by_id409_response_jsonapi import AppsDeleteAppById409ResponseJsonapi

class RequiredAppsDeleteAppById409Response(TypedDict):
    errors: AppsDeleteAppById409ResponseErrors

    jsonapi: AppsDeleteAppById409ResponseJsonapi

class OptionalAppsDeleteAppById409Response(TypedDict, total=False):
    pass

class AppsDeleteAppById409Response(RequiredAppsDeleteAppById409Response, OptionalAppsDeleteAppById409Response):
    pass
