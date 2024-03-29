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

from snyk_python_sdk.pydantic.app_name import AppName
from snyk_python_sdk.pydantic.context import Context
from snyk_python_sdk.pydantic.scopes import Scopes

class PublicAppAttributes(BaseModel):
    # The oauth2 client id for the app.
    client_id: str = Field(alias='client_id')

    name: AppName = Field(alias='name')

    context: typing.Optional[Context] = Field(None, alias='context')

    scopes: typing.Optional[Scopes] = Field(None, alias='scopes')
    class Config:
        arbitrary_types_allowed = True
