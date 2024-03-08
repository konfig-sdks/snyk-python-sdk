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

from snyk_python_sdk.type.apps_delete_app_by_id403_response_errors import AppsDeleteAppById403ResponseErrors
from snyk_python_sdk.type.apps_delete_app_by_id403_response_jsonapi import AppsDeleteAppById403ResponseJsonapi

class RequiredAppsDeleteAppById403Response(TypedDict):
    errors: AppsDeleteAppById403ResponseErrors

    jsonapi: AppsDeleteAppById403ResponseJsonapi

class OptionalAppsDeleteAppById403Response(TypedDict, total=False):
    pass

class AppsDeleteAppById403Response(RequiredAppsDeleteAppById403Response, OptionalAppsDeleteAppById403Response):
    pass