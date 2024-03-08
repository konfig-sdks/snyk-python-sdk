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

from snyk_python_sdk.type.apps_create_organization_app409_response_errors import AppsCreateOrganizationApp409ResponseErrors
from snyk_python_sdk.type.apps_create_organization_app409_response_jsonapi import AppsCreateOrganizationApp409ResponseJsonapi

class RequiredAppsCreateOrganizationApp409Response(TypedDict):
    errors: AppsCreateOrganizationApp409ResponseErrors

    jsonapi: AppsCreateOrganizationApp409ResponseJsonapi

class OptionalAppsCreateOrganizationApp409Response(TypedDict, total=False):
    pass

class AppsCreateOrganizationApp409Response(RequiredAppsCreateOrganizationApp409Response, OptionalAppsCreateOrganizationApp409Response):
    pass
