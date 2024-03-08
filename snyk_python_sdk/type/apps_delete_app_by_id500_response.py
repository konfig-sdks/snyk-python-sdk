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

from snyk_python_sdk.type.apps_delete_app_by_id500_response_errors import AppsDeleteAppById500ResponseErrors
from snyk_python_sdk.type.apps_delete_app_by_id500_response_jsonapi import AppsDeleteAppById500ResponseJsonapi

class RequiredAppsDeleteAppById500Response(TypedDict):
    errors: AppsDeleteAppById500ResponseErrors

    jsonapi: AppsDeleteAppById500ResponseJsonapi

class OptionalAppsDeleteAppById500Response(TypedDict, total=False):
    pass

class AppsDeleteAppById500Response(RequiredAppsDeleteAppById500Response, OptionalAppsDeleteAppById500Response):
    pass
