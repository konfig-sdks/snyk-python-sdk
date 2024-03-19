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

from snyk_python_sdk.type.apps_revoke_group_app_install403_response_errors import AppsRevokeGroupAppInstall403ResponseErrors
from snyk_python_sdk.type.apps_revoke_group_app_install403_response_jsonapi import AppsRevokeGroupAppInstall403ResponseJsonapi

class RequiredAppsRevokeGroupAppInstall403Response(TypedDict):
    errors: AppsRevokeGroupAppInstall403ResponseErrors

    jsonapi: AppsRevokeGroupAppInstall403ResponseJsonapi

class OptionalAppsRevokeGroupAppInstall403Response(TypedDict, total=False):
    pass

class AppsRevokeGroupAppInstall403Response(RequiredAppsRevokeGroupAppInstall403Response, OptionalAppsRevokeGroupAppInstall403Response):
    pass
