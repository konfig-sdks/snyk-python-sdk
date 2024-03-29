# coding: utf-8

"""
    Snyk API

    Snyk helps software-driven businesses develop fast and stay secure. Continuously find and fix vulnerabilities for npm, Maven, NuGet, RubyGems, PyPI and more.

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from snyk_python_sdk.type.service_accounts_update_organization_service_account_name_response_data_attributes import ServiceAccountsUpdateOrganizationServiceAccountNameResponseDataAttributes
from snyk_python_sdk.type.service_accounts_update_organization_service_account_name_response_data_links import ServiceAccountsUpdateOrganizationServiceAccountNameResponseDataLinks

class RequiredServiceAccountsUpdateOrganizationServiceAccountNameResponseData(TypedDict):
    attributes: ServiceAccountsUpdateOrganizationServiceAccountNameResponseDataAttributes

    id: str

    type: str

class OptionalServiceAccountsUpdateOrganizationServiceAccountNameResponseData(TypedDict, total=False):
    links: ServiceAccountsUpdateOrganizationServiceAccountNameResponseDataLinks

class ServiceAccountsUpdateOrganizationServiceAccountNameResponseData(RequiredServiceAccountsUpdateOrganizationServiceAccountNameResponseData, OptionalServiceAccountsUpdateOrganizationServiceAccountNameResponseData):
    pass
