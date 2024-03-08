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

from snyk_python_sdk.type.apps_list_user_installed_apps401_response_errors import AppsListUserInstalledApps401ResponseErrors
from snyk_python_sdk.type.apps_list_user_installed_apps401_response_jsonapi import AppsListUserInstalledApps401ResponseJsonapi

class RequiredAppsListUserInstalledApps401Response(TypedDict):
    errors: AppsListUserInstalledApps401ResponseErrors

    jsonapi: AppsListUserInstalledApps401ResponseJsonapi

class OptionalAppsListUserInstalledApps401Response(TypedDict, total=False):
    pass

class AppsListUserInstalledApps401Response(RequiredAppsListUserInstalledApps401Response, OptionalAppsListUserInstalledApps401Response):
    pass
