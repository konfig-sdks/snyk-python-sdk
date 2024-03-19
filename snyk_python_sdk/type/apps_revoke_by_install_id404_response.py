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

from snyk_python_sdk.type.apps_revoke_by_install_id404_response_errors import AppsRevokeByInstallId404ResponseErrors
from snyk_python_sdk.type.apps_revoke_by_install_id404_response_jsonapi import AppsRevokeByInstallId404ResponseJsonapi

class RequiredAppsRevokeByInstallId404Response(TypedDict):
    errors: AppsRevokeByInstallId404ResponseErrors

    jsonapi: AppsRevokeByInstallId404ResponseJsonapi

class OptionalAppsRevokeByInstallId404Response(TypedDict, total=False):
    pass

class AppsRevokeByInstallId404Response(RequiredAppsRevokeByInstallId404Response, OptionalAppsRevokeByInstallId404Response):
    pass
