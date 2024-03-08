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

from snyk_python_sdk.pydantic.app_data import AppData
from snyk_python_sdk.pydantic.json_api import JsonApi
from snyk_python_sdk.pydantic.self_link import SelfLink

class AppsGetByClientIdResponse(BaseModel):
    data: typing.Optional[AppData] = Field(None, alias='items')

    jsonapi: typing.Optional[JsonApi] = Field(None, alias='jsonapi')

    links: typing.Optional[SelfLink] = Field(None, alias='links')
    class Config:
        arbitrary_types_allowed = True
