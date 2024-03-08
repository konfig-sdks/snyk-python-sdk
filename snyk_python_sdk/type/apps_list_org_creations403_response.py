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

from snyk_python_sdk.type.apps_list_org_creations403_response_errors import AppsListOrgCreations403ResponseErrors
from snyk_python_sdk.type.apps_list_org_creations403_response_jsonapi import AppsListOrgCreations403ResponseJsonapi

class RequiredAppsListOrgCreations403Response(TypedDict):
    errors: AppsListOrgCreations403ResponseErrors

    jsonapi: AppsListOrgCreations403ResponseJsonapi

class OptionalAppsListOrgCreations403Response(TypedDict, total=False):
    pass

class AppsListOrgCreations403Response(RequiredAppsListOrgCreations403Response, OptionalAppsListOrgCreations403Response):
    pass