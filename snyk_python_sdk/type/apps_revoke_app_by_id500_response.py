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

from snyk_python_sdk.type.apps_revoke_app_by_id500_response_errors import AppsRevokeAppById500ResponseErrors
from snyk_python_sdk.type.apps_revoke_app_by_id500_response_jsonapi import AppsRevokeAppById500ResponseJsonapi

class RequiredAppsRevokeAppById500Response(TypedDict):
    errors: AppsRevokeAppById500ResponseErrors

    jsonapi: AppsRevokeAppById500ResponseJsonapi

class OptionalAppsRevokeAppById500Response(TypedDict, total=False):
    pass

class AppsRevokeAppById500Response(RequiredAppsRevokeAppById500Response, OptionalAppsRevokeAppById500Response):
    pass