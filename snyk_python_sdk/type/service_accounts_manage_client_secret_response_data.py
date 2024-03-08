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

from snyk_python_sdk.type.service_accounts_manage_client_secret_response_data_attributes import ServiceAccountsManageClientSecretResponseDataAttributes
from snyk_python_sdk.type.service_accounts_manage_client_secret_response_data_links import ServiceAccountsManageClientSecretResponseDataLinks

class RequiredServiceAccountsManageClientSecretResponseData(TypedDict):
    attributes: ServiceAccountsManageClientSecretResponseDataAttributes

    id: str

    type: str

class OptionalServiceAccountsManageClientSecretResponseData(TypedDict, total=False):
    links: ServiceAccountsManageClientSecretResponseDataLinks

class ServiceAccountsManageClientSecretResponseData(RequiredServiceAccountsManageClientSecretResponseData, OptionalServiceAccountsManageClientSecretResponseData):
    pass