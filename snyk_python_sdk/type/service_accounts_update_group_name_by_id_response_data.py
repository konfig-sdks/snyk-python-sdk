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

from snyk_python_sdk.type.service_accounts_update_group_name_by_id_response_data_attributes import ServiceAccountsUpdateGroupNameByIdResponseDataAttributes
from snyk_python_sdk.type.service_accounts_update_group_name_by_id_response_data_links import ServiceAccountsUpdateGroupNameByIdResponseDataLinks

class RequiredServiceAccountsUpdateGroupNameByIdResponseData(TypedDict):
    attributes: ServiceAccountsUpdateGroupNameByIdResponseDataAttributes

    id: str

    type: str

class OptionalServiceAccountsUpdateGroupNameByIdResponseData(TypedDict, total=False):
    links: ServiceAccountsUpdateGroupNameByIdResponseDataLinks

class ServiceAccountsUpdateGroupNameByIdResponseData(RequiredServiceAccountsUpdateGroupNameByIdResponseData, OptionalServiceAccountsUpdateGroupNameByIdResponseData):
    pass