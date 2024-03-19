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

from snyk_python_sdk.pydantic.links import Links
from snyk_python_sdk.pydantic.public_app_attributes import PublicAppAttributes

class PublicApp(BaseModel):
    id: str = Field(alias='id')

    type: str = Field(alias='type')

    attributes: typing.Optional[PublicAppAttributes] = Field(None, alias='attributes')

    links: typing.Optional[Links] = Field(None, alias='links')
    class Config:
        arbitrary_types_allowed = True
