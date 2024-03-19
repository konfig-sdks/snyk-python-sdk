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

from snyk_python_sdk.type.apps_revoke_by_install_id500_response_errors import AppsRevokeByInstallId500ResponseErrors
from snyk_python_sdk.type.apps_revoke_by_install_id500_response_jsonapi import AppsRevokeByInstallId500ResponseJsonapi

class RequiredAppsRevokeByInstallId500Response(TypedDict):
    errors: AppsRevokeByInstallId500ResponseErrors

    jsonapi: AppsRevokeByInstallId500ResponseJsonapi

class OptionalAppsRevokeByInstallId500Response(TypedDict, total=False):
    pass

class AppsRevokeByInstallId500Response(RequiredAppsRevokeByInstallId500Response, OptionalAppsRevokeByInstallId500Response):
    pass
