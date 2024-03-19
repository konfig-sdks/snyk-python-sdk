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

from snyk_python_sdk.type.apps_revoke_group_app_install500_response_errors import AppsRevokeGroupAppInstall500ResponseErrors
from snyk_python_sdk.type.apps_revoke_group_app_install500_response_jsonapi import AppsRevokeGroupAppInstall500ResponseJsonapi

class RequiredAppsRevokeGroupAppInstall500Response(TypedDict):
    errors: AppsRevokeGroupAppInstall500ResponseErrors

    jsonapi: AppsRevokeGroupAppInstall500ResponseJsonapi

class OptionalAppsRevokeGroupAppInstall500Response(TypedDict, total=False):
    pass

class AppsRevokeGroupAppInstall500Response(RequiredAppsRevokeGroupAppInstall500Response, OptionalAppsRevokeGroupAppInstall500Response):
    pass
