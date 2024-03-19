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

from snyk_python_sdk.type.apps_revoke_user_app_session403_response_errors import AppsRevokeUserAppSession403ResponseErrors
from snyk_python_sdk.type.apps_revoke_user_app_session403_response_jsonapi import AppsRevokeUserAppSession403ResponseJsonapi

class RequiredAppsRevokeUserAppSession403Response(TypedDict):
    errors: AppsRevokeUserAppSession403ResponseErrors

    jsonapi: AppsRevokeUserAppSession403ResponseJsonapi

class OptionalAppsRevokeUserAppSession403Response(TypedDict, total=False):
    pass

class AppsRevokeUserAppSession403Response(RequiredAppsRevokeUserAppSession403Response, OptionalAppsRevokeUserAppSession403Response):
    pass
