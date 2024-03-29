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


class Package(BaseModel):
    # The version of the package
    version: str = Field(alias='version')

    # The package’s name
    name: str = Field(alias='name')

    # The package type or protocol
    type: str = Field(alias='type')

    # The purl of the package
    url: str = Field(alias='url')

    # A name prefix, such as a maven group id or docker image owner
    namespace: typing.Optional[str] = Field(None, alias='namespace')
    class Config:
        arbitrary_types_allowed = True
