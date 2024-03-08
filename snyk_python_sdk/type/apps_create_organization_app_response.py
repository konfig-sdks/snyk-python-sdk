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

from snyk_python_sdk.type.apps_create_organization_app_response_errors import AppsCreateOrganizationAppResponseErrors
from snyk_python_sdk.type.apps_create_organization_app_response_jsonapi import AppsCreateOrganizationAppResponseJsonapi

class RequiredAppsCreateOrganizationAppResponse(TypedDict):
    errors: AppsCreateOrganizationAppResponseErrors

    jsonapi: AppsCreateOrganizationAppResponseJsonapi

class OptionalAppsCreateOrganizationAppResponse(TypedDict, total=False):
    pass

class AppsCreateOrganizationAppResponse(RequiredAppsCreateOrganizationAppResponse, OptionalAppsCreateOrganizationAppResponse):
    pass
