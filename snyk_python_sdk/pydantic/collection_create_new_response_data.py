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

from snyk_python_sdk.pydantic.collection_attributes import CollectionAttributes
from snyk_python_sdk.pydantic.collection_relationships import CollectionRelationships
from snyk_python_sdk.pydantic.types import Types

class CollectionCreateNewResponseData(BaseModel):
    attributes: CollectionAttributes = Field(alias='attributes')

    id: str = Field(alias='id')

    relationships: CollectionRelationships = Field(alias='relationships')

    type: typing.Optional[Types] = Field(None, alias='type')
    class Config:
        arbitrary_types_allowed = True