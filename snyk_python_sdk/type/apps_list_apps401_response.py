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

from snyk_python_sdk.type.apps_list_apps401_response_errors import AppsListApps401ResponseErrors
from snyk_python_sdk.type.apps_list_apps401_response_jsonapi import AppsListApps401ResponseJsonapi

class RequiredAppsListApps401Response(TypedDict):
    errors: AppsListApps401ResponseErrors

    jsonapi: AppsListApps401ResponseJsonapi

class OptionalAppsListApps401Response(TypedDict, total=False):
    pass

class AppsListApps401Response(RequiredAppsListApps401Response, OptionalAppsListApps401Response):
    pass
