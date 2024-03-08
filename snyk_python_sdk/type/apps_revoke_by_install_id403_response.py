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

from snyk_python_sdk.type.apps_revoke_by_install_id403_response_errors import AppsRevokeByInstallId403ResponseErrors
from snyk_python_sdk.type.apps_revoke_by_install_id403_response_jsonapi import AppsRevokeByInstallId403ResponseJsonapi

class RequiredAppsRevokeByInstallId403Response(TypedDict):
    errors: AppsRevokeByInstallId403ResponseErrors

    jsonapi: AppsRevokeByInstallId403ResponseJsonapi

class OptionalAppsRevokeByInstallId403Response(TypedDict, total=False):
    pass

class AppsRevokeByInstallId403Response(RequiredAppsRevokeByInstallId403Response, OptionalAppsRevokeByInstallId403Response):
    pass
