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

from snyk_python_sdk.pydantic.platform import Platform

class ImageTargetRefAttributes(BaseModel):
    platform: typing.Optional[Platform] = Field(None, alias='platform')

    target_id: typing.Optional[str] = Field(None, alias='target_id')

    target_reference: typing.Optional[str] = Field(None, alias='target_reference')
    class Config:
        arbitrary_types_allowed = True
