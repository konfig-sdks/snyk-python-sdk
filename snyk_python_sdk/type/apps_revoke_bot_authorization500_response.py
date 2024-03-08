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

from snyk_python_sdk.type.apps_revoke_bot_authorization500_response_errors import AppsRevokeBotAuthorization500ResponseErrors
from snyk_python_sdk.type.apps_revoke_bot_authorization500_response_jsonapi import AppsRevokeBotAuthorization500ResponseJsonapi

class RequiredAppsRevokeBotAuthorization500Response(TypedDict):
    errors: AppsRevokeBotAuthorization500ResponseErrors

    jsonapi: AppsRevokeBotAuthorization500ResponseJsonapi

class OptionalAppsRevokeBotAuthorization500Response(TypedDict, total=False):
    pass

class AppsRevokeBotAuthorization500Response(RequiredAppsRevokeBotAuthorization500Response, OptionalAppsRevokeBotAuthorization500Response):
    pass
