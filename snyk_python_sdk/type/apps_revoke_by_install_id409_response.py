# coding: utf-8

"""
    Snyk API

    Missing description placeholder

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from snyk_python_sdk.type.apps_revoke_by_install_id409_response_errors import AppsRevokeByInstallId409ResponseErrors
from snyk_python_sdk.type.apps_revoke_by_install_id409_response_jsonapi import AppsRevokeByInstallId409ResponseJsonapi

class RequiredAppsRevokeByInstallId409Response(TypedDict):
    errors: AppsRevokeByInstallId409ResponseErrors

    jsonapi: AppsRevokeByInstallId409ResponseJsonapi

class OptionalAppsRevokeByInstallId409Response(TypedDict, total=False):
    pass

class AppsRevokeByInstallId409Response(RequiredAppsRevokeByInstallId409Response, OptionalAppsRevokeByInstallId409Response):
    pass
