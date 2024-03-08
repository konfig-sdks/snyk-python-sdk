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

from snyk_python_sdk.pydantic.app_install_data_with_secret_attributes import AppInstallDataWithSecretAttributes
from snyk_python_sdk.pydantic.app_install_data_with_secret_relationships import AppInstallDataWithSecretRelationships
from snyk_python_sdk.pydantic.links import Links

class AppInstallDataWithSecret(BaseModel):
    attributes: AppInstallDataWithSecretAttributes = Field(alias='attributes')

    id: str = Field(alias='id')

    type: str = Field(alias='type')

    links: typing.Optional[Links] = Field(None, alias='links')

    relationships: typing.Optional[AppInstallDataWithSecretRelationships] = Field(None, alias='relationships')
    class Config:
        arbitrary_types_allowed = True
