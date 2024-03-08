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

from snyk_python_sdk.type.service_accounts_create_for_organization_request_data_attributes import ServiceAccountsCreateForOrganizationRequestDataAttributes

class RequiredServiceAccountsCreateForOrganizationRequestData(TypedDict):
    attributes: ServiceAccountsCreateForOrganizationRequestDataAttributes

class OptionalServiceAccountsCreateForOrganizationRequestData(TypedDict, total=False):
    # The Resource type.
    type: str

class ServiceAccountsCreateForOrganizationRequestData(RequiredServiceAccountsCreateForOrganizationRequestData, OptionalServiceAccountsCreateForOrganizationRequestData):
    pass