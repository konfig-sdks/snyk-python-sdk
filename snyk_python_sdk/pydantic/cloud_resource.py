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

from snyk_python_sdk.pydantic.environment import Environment
from snyk_python_sdk.pydantic.resource import Resource

class CloudResource(BaseModel):
    environment: Environment = Field(alias='environment')

    resource: typing.Optional[Resource] = Field(None, alias='resource')
    class Config:
        arbitrary_types_allowed = True