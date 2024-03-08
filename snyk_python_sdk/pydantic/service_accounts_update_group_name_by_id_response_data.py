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

from snyk_python_sdk.pydantic.service_accounts_update_group_name_by_id_response_data_attributes import ServiceAccountsUpdateGroupNameByIdResponseDataAttributes
from snyk_python_sdk.pydantic.service_accounts_update_group_name_by_id_response_data_links import ServiceAccountsUpdateGroupNameByIdResponseDataLinks

class ServiceAccountsUpdateGroupNameByIdResponseData(BaseModel):
    attributes: ServiceAccountsUpdateGroupNameByIdResponseDataAttributes = Field(alias='attributes')

    id: str = Field(alias='id')

    type: str = Field(alias='type')

    links: typing.Optional[ServiceAccountsUpdateGroupNameByIdResponseDataLinks] = Field(None, alias='links')
    class Config:
        arbitrary_types_allowed = True