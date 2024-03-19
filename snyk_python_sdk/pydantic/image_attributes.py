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

from snyk_python_sdk.pydantic.image_digest import ImageDigest
from snyk_python_sdk.pydantic.image_name import ImageName
from snyk_python_sdk.pydantic.platform import Platform

class ImageAttributes(BaseModel):
    layers: typing.List[ImageDigest] = Field(alias='layers')

    platform: Platform = Field(alias='platform')

    names: typing.Optional[typing.List[ImageName]] = Field(None, alias='names')
    class Config:
        arbitrary_types_allowed = True
