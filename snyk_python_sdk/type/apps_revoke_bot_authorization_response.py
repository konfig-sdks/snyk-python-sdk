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

from snyk_python_sdk.type.apps_revoke_bot_authorization_response_errors import AppsRevokeBotAuthorizationResponseErrors
from snyk_python_sdk.type.apps_revoke_bot_authorization_response_jsonapi import AppsRevokeBotAuthorizationResponseJsonapi

class RequiredAppsRevokeBotAuthorizationResponse(TypedDict):
    errors: AppsRevokeBotAuthorizationResponseErrors

    jsonapi: AppsRevokeBotAuthorizationResponseJsonapi

class OptionalAppsRevokeBotAuthorizationResponse(TypedDict, total=False):
    pass

class AppsRevokeBotAuthorizationResponse(RequiredAppsRevokeBotAuthorizationResponse, OptionalAppsRevokeBotAuthorizationResponse):
    pass