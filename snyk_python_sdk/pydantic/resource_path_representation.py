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

from snyk_python_sdk.pydantic.resource_path import ResourcePath

class ResourcePathRepresentation(BaseModel):
    resource_path_: ResourcePath = Field(alias='resource_path')
    class Config:
        arbitrary_types_allowed = True