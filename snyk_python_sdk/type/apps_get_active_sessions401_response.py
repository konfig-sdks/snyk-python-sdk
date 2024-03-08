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

from snyk_python_sdk.type.apps_get_active_sessions401_response_errors import AppsGetActiveSessions401ResponseErrors
from snyk_python_sdk.type.apps_get_active_sessions401_response_jsonapi import AppsGetActiveSessions401ResponseJsonapi

class RequiredAppsGetActiveSessions401Response(TypedDict):
    errors: AppsGetActiveSessions401ResponseErrors

    jsonapi: AppsGetActiveSessions401ResponseJsonapi

class OptionalAppsGetActiveSessions401Response(TypedDict, total=False):
    pass

class AppsGetActiveSessions401Response(RequiredAppsGetActiveSessions401Response, OptionalAppsGetActiveSessions401Response):
    pass
