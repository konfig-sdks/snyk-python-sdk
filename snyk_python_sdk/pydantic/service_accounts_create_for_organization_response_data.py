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

from snyk_python_sdk.pydantic.service_accounts_create_for_organization_response_data_attributes import ServiceAccountsCreateForOrganizationResponseDataAttributes
from snyk_python_sdk.pydantic.service_accounts_create_for_organization_response_data_links import ServiceAccountsCreateForOrganizationResponseDataLinks

class ServiceAccountsCreateForOrganizationResponseData(BaseModel):
    attributes: ServiceAccountsCreateForOrganizationResponseDataAttributes = Field(alias='attributes')

    id: str = Field(alias='id')

    type: str = Field(alias='type')

    links: typing.Optional[ServiceAccountsCreateForOrganizationResponseDataLinks] = Field(None, alias='links')
    class Config:
        arbitrary_types_allowed = True