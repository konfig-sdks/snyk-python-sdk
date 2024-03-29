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

from snyk_python_sdk.type.service_accounts_list_group_service_accounts_response_data_item_attributes import ServiceAccountsListGroupServiceAccountsResponseDataItemAttributes
from snyk_python_sdk.type.service_accounts_list_group_service_accounts_response_data_item_links import ServiceAccountsListGroupServiceAccountsResponseDataItemLinks

class RequiredServiceAccountsListGroupServiceAccountsResponseDataItem(TypedDict):
    attributes: ServiceAccountsListGroupServiceAccountsResponseDataItemAttributes

    id: str

    type: str

class OptionalServiceAccountsListGroupServiceAccountsResponseDataItem(TypedDict, total=False):
    links: ServiceAccountsListGroupServiceAccountsResponseDataItemLinks

class ServiceAccountsListGroupServiceAccountsResponseDataItem(RequiredServiceAccountsListGroupServiceAccountsResponseDataItem, OptionalServiceAccountsListGroupServiceAccountsResponseDataItem):
    pass
