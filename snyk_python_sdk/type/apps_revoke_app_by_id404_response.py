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

from snyk_python_sdk.type.apps_revoke_app_by_id404_response_errors import AppsRevokeAppById404ResponseErrors
from snyk_python_sdk.type.apps_revoke_app_by_id404_response_jsonapi import AppsRevokeAppById404ResponseJsonapi

class RequiredAppsRevokeAppById404Response(TypedDict):
    errors: AppsRevokeAppById404ResponseErrors

    jsonapi: AppsRevokeAppById404ResponseJsonapi

class OptionalAppsRevokeAppById404Response(TypedDict, total=False):
    pass

class AppsRevokeAppById404Response(RequiredAppsRevokeAppById404Response, OptionalAppsRevokeAppById404Response):
    pass
