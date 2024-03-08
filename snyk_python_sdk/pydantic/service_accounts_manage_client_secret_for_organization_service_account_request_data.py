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
from pydantic import BaseModel, Field, RootModel

from snyk_python_sdk.pydantic.service_accounts_manage_client_secret_for_organization_service_account_request_data_attributes import ServiceAccountsManageClientSecretForOrganizationServiceAccountRequestDataAttributes

class ServiceAccountsManageClientSecretForOrganizationServiceAccountRequestData(BaseModel):
    attributes: ServiceAccountsManageClientSecretForOrganizationServiceAccountRequestDataAttributes = Field(alias='attributes')

    # The Resource type.
    type: Literal["service_account"] = Field(alias='type')
    class Config:
        arbitrary_types_allowed = True