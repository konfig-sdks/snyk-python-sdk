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

from snyk_python_sdk.type.apps_revoke_app_by_id403_response_errors import AppsRevokeAppById403ResponseErrors
from snyk_python_sdk.type.apps_revoke_app_by_id403_response_jsonapi import AppsRevokeAppById403ResponseJsonapi

class RequiredAppsRevokeAppById403Response(TypedDict):
    errors: AppsRevokeAppById403ResponseErrors

    jsonapi: AppsRevokeAppById403ResponseJsonapi

class OptionalAppsRevokeAppById403Response(TypedDict, total=False):
    pass

class AppsRevokeAppById403Response(RequiredAppsRevokeAppById403Response, OptionalAppsRevokeAppById403Response):
    pass