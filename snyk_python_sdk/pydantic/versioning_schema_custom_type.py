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


class VersioningSchemaCustomType(BaseModel):
    # The regular expression used to describe the format of tags. Keep in mind that backslashes in the expression need to be escaped due to being encompassed in a JSON string. 
    expression: str = Field(alias='expression')

    type: Literal["custom"] = Field(alias='type')

    # A customizable string that can be set for a custom versioning schema to describe its meaning. This label has no function. 
    label: typing.Optional[str] = Field(None, alias='label')
    class Config:
        arbitrary_types_allowed = True
