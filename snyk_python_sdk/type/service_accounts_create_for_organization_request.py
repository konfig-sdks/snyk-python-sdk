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

from snyk_python_sdk.type.service_accounts_create_for_organization_request_data import ServiceAccountsCreateForOrganizationRequestData

class RequiredServiceAccountsCreateForOrganizationRequest(TypedDict):
    data: ServiceAccountsCreateForOrganizationRequestData

class OptionalServiceAccountsCreateForOrganizationRequest(TypedDict, total=False):
    pass

class ServiceAccountsCreateForOrganizationRequest(RequiredServiceAccountsCreateForOrganizationRequest, OptionalServiceAccountsCreateForOrganizationRequest):
    pass
