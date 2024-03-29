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

from snyk_python_sdk.type.apps_revoke_user_app_session500_response_errors import AppsRevokeUserAppSession500ResponseErrors
from snyk_python_sdk.type.apps_revoke_user_app_session500_response_jsonapi import AppsRevokeUserAppSession500ResponseJsonapi

class RequiredAppsRevokeUserAppSession500Response(TypedDict):
    errors: AppsRevokeUserAppSession500ResponseErrors

    jsonapi: AppsRevokeUserAppSession500ResponseJsonapi

class OptionalAppsRevokeUserAppSession500Response(TypedDict, total=False):
    pass

class AppsRevokeUserAppSession500Response(RequiredAppsRevokeUserAppSession500Response, OptionalAppsRevokeUserAppSession500Response):
    pass
