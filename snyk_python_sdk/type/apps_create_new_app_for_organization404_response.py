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

from snyk_python_sdk.type.apps_create_new_app_for_organization404_response_errors import AppsCreateNewAppForOrganization404ResponseErrors
from snyk_python_sdk.type.apps_create_new_app_for_organization404_response_jsonapi import AppsCreateNewAppForOrganization404ResponseJsonapi

class RequiredAppsCreateNewAppForOrganization404Response(TypedDict):
    errors: AppsCreateNewAppForOrganization404ResponseErrors

    jsonapi: AppsCreateNewAppForOrganization404ResponseJsonapi

class OptionalAppsCreateNewAppForOrganization404Response(TypedDict, total=False):
    pass

class AppsCreateNewAppForOrganization404Response(RequiredAppsCreateNewAppForOrganization404Response, OptionalAppsCreateNewAppForOrganization404Response):
    pass
