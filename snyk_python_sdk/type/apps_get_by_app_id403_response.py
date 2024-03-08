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

from snyk_python_sdk.type.apps_get_by_app_id403_response_errors import AppsGetByAppId403ResponseErrors
from snyk_python_sdk.type.apps_get_by_app_id403_response_jsonapi import AppsGetByAppId403ResponseJsonapi

class RequiredAppsGetByAppId403Response(TypedDict):
    errors: AppsGetByAppId403ResponseErrors

    jsonapi: AppsGetByAppId403ResponseJsonapi

class OptionalAppsGetByAppId403Response(TypedDict, total=False):
    pass

class AppsGetByAppId403Response(RequiredAppsGetByAppId403Response, OptionalAppsGetByAppId403Response):
    pass