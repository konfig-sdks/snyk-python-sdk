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

from snyk_python_sdk.type.apps_list_org_creations409_response_errors import AppsListOrgCreations409ResponseErrors
from snyk_python_sdk.type.apps_list_org_creations409_response_jsonapi import AppsListOrgCreations409ResponseJsonapi

class RequiredAppsListOrgCreations409Response(TypedDict):
    errors: AppsListOrgCreations409ResponseErrors

    jsonapi: AppsListOrgCreations409ResponseJsonapi

class OptionalAppsListOrgCreations409Response(TypedDict, total=False):
    pass

class AppsListOrgCreations409Response(RequiredAppsListOrgCreations409Response, OptionalAppsListOrgCreations409Response):
    pass
