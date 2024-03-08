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

from snyk_python_sdk.type.apps_list_apps403_response_errors import AppsListApps403ResponseErrors
from snyk_python_sdk.type.apps_list_apps403_response_jsonapi import AppsListApps403ResponseJsonapi

class RequiredAppsListApps403Response(TypedDict):
    errors: AppsListApps403ResponseErrors

    jsonapi: AppsListApps403ResponseJsonapi

class OptionalAppsListApps403Response(TypedDict, total=False):
    pass

class AppsListApps403Response(RequiredAppsListApps403Response, OptionalAppsListApps403Response):
    pass
