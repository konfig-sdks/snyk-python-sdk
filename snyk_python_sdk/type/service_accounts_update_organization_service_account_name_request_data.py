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

from snyk_python_sdk.type.service_accounts_update_organization_service_account_name_request_data_attributes import ServiceAccountsUpdateOrganizationServiceAccountNameRequestDataAttributes

class RequiredServiceAccountsUpdateOrganizationServiceAccountNameRequestData(TypedDict):
    attributes: ServiceAccountsUpdateOrganizationServiceAccountNameRequestDataAttributes

    # The ID of the service account. Must match the id in the url path.
    id: str

    # The Resource type.
    type: str

class OptionalServiceAccountsUpdateOrganizationServiceAccountNameRequestData(TypedDict, total=False):
    pass

class ServiceAccountsUpdateOrganizationServiceAccountNameRequestData(RequiredServiceAccountsUpdateOrganizationServiceAccountNameRequestData, OptionalServiceAccountsUpdateOrganizationServiceAccountNameRequestData):
    pass
