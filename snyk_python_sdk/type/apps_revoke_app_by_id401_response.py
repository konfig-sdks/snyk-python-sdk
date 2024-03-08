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

from snyk_python_sdk.type.apps_revoke_app_by_id401_response_errors import AppsRevokeAppById401ResponseErrors
from snyk_python_sdk.type.apps_revoke_app_by_id401_response_jsonapi import AppsRevokeAppById401ResponseJsonapi

class RequiredAppsRevokeAppById401Response(TypedDict):
    errors: AppsRevokeAppById401ResponseErrors

    jsonapi: AppsRevokeAppById401ResponseJsonapi

class OptionalAppsRevokeAppById401Response(TypedDict, total=False):
    pass

class AppsRevokeAppById401Response(RequiredAppsRevokeAppById401Response, OptionalAppsRevokeAppById401Response):
    pass