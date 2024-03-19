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

from snyk_python_sdk.pydantic.link_property import LinkProperty

class PaginatedLinks(BaseModel):
    first: typing.Optional[LinkProperty] = Field(None, alias='first')

    last: typing.Optional[LinkProperty] = Field(None, alias='last')

    next: typing.Optional[LinkProperty] = Field(None, alias='next')

    prev: typing.Optional[LinkProperty] = Field(None, alias='prev')

    self_: typing.Optional[LinkProperty] = Field(None, alias='self')
    class Config:
        arbitrary_types_allowed = True
