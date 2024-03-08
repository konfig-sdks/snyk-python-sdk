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

from snyk_python_sdk.type.apps_create_organization_app404_response_errors import AppsCreateOrganizationApp404ResponseErrors
from snyk_python_sdk.type.apps_create_organization_app404_response_jsonapi import AppsCreateOrganizationApp404ResponseJsonapi

class RequiredAppsCreateOrganizationApp404Response(TypedDict):
    errors: AppsCreateOrganizationApp404ResponseErrors

    jsonapi: AppsCreateOrganizationApp404ResponseJsonapi

class OptionalAppsCreateOrganizationApp404Response(TypedDict, total=False):
    pass

class AppsCreateOrganizationApp404Response(RequiredAppsCreateOrganizationApp404Response, OptionalAppsCreateOrganizationApp404Response):
    pass