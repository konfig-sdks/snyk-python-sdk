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

from snyk_python_sdk.type.apps_list_org_creations401_response_errors import AppsListOrgCreations401ResponseErrors
from snyk_python_sdk.type.apps_list_org_creations401_response_jsonapi import AppsListOrgCreations401ResponseJsonapi

class RequiredAppsListOrgCreations401Response(TypedDict):
    errors: AppsListOrgCreations401ResponseErrors

    jsonapi: AppsListOrgCreations401ResponseJsonapi

class OptionalAppsListOrgCreations401Response(TypedDict, total=False):
    pass

class AppsListOrgCreations401Response(RequiredAppsListOrgCreations401Response, OptionalAppsListOrgCreations401Response):
    pass