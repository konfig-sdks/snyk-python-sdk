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

from snyk_python_sdk.pydantic.types import Types

class SbomResource(BaseModel):
    id: str = Field(alias='id')

    type: Types = Field(alias='type')
    class Config:
        arbitrary_types_allowed = True
