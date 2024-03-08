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

from snyk_python_sdk.type.apps_revoke_group_app_install409_response_errors import AppsRevokeGroupAppInstall409ResponseErrors
from snyk_python_sdk.type.apps_revoke_group_app_install409_response_jsonapi import AppsRevokeGroupAppInstall409ResponseJsonapi

class RequiredAppsRevokeGroupAppInstall409Response(TypedDict):
    errors: AppsRevokeGroupAppInstall409ResponseErrors

    jsonapi: AppsRevokeGroupAppInstall409ResponseJsonapi

class OptionalAppsRevokeGroupAppInstall409Response(TypedDict, total=False):
    pass

class AppsRevokeGroupAppInstall409Response(RequiredAppsRevokeGroupAppInstall409Response, OptionalAppsRevokeGroupAppInstall409Response):
    pass