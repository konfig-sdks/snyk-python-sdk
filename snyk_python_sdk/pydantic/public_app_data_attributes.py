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
from pydantic import BaseModel, Field, RootModel

from snyk_python_sdk.pydantic.public_app_data_attributes_scopes import PublicAppDataAttributesScopes

class PublicAppDataAttributes(BaseModel):
    client_id: str = Field(alias='client_id')

    # New name of the app to display to users during authorization flow.
    name: str = Field(alias='name')

    # Allow installing the app to a org/group or to a user, default tenant.
    context: typing.Optional[Literal["tenant", "user"]] = Field(None, alias='context')

    scopes: typing.Optional[PublicAppDataAttributesScopes] = Field(None, alias='scopes')
    class Config:
        arbitrary_types_allowed = True
