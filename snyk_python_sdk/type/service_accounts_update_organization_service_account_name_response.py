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

from snyk_python_sdk.type.json_api import JsonApi
from snyk_python_sdk.type.links import Links
from snyk_python_sdk.type.service_accounts_update_organization_service_account_name_response_data import ServiceAccountsUpdateOrganizationServiceAccountNameResponseData

class RequiredServiceAccountsUpdateOrganizationServiceAccountNameResponse(TypedDict):
    data: ServiceAccountsUpdateOrganizationServiceAccountNameResponseData

    jsonapi: JsonApi

    links: Links

class OptionalServiceAccountsUpdateOrganizationServiceAccountNameResponse(TypedDict, total=False):
    pass

class ServiceAccountsUpdateOrganizationServiceAccountNameResponse(RequiredServiceAccountsUpdateOrganizationServiceAccountNameResponse, OptionalServiceAccountsUpdateOrganizationServiceAccountNameResponse):
    pass