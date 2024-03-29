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

from snyk_python_sdk.pydantic.types import Types
from snyk_python_sdk.pydantic.update_collection_request_data_attributes import UpdateCollectionRequestDataAttributes

class UpdateCollectionRequestData(BaseModel):
    attributes: UpdateCollectionRequestDataAttributes = Field(alias='attributes')

    type: Types = Field(alias='type')

    id: typing.Optional[str] = Field(None, alias='id')
    class Config:
        arbitrary_types_allowed = True
