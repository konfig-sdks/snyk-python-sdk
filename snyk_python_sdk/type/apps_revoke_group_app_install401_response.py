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

from snyk_python_sdk.type.apps_revoke_group_app_install401_response_errors import AppsRevokeGroupAppInstall401ResponseErrors
from snyk_python_sdk.type.apps_revoke_group_app_install401_response_jsonapi import AppsRevokeGroupAppInstall401ResponseJsonapi

class RequiredAppsRevokeGroupAppInstall401Response(TypedDict):
    errors: AppsRevokeGroupAppInstall401ResponseErrors

    jsonapi: AppsRevokeGroupAppInstall401ResponseJsonapi

class OptionalAppsRevokeGroupAppInstall401Response(TypedDict, total=False):
    pass

class AppsRevokeGroupAppInstall401Response(RequiredAppsRevokeGroupAppInstall401Response, OptionalAppsRevokeGroupAppInstall401Response):
    pass
