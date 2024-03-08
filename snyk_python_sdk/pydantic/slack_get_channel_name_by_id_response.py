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

from snyk_python_sdk.pydantic.json_api import JsonApi
from snyk_python_sdk.pydantic.self_link import SelfLink
from snyk_python_sdk.pydantic.slack_channel import SlackChannel

class SlackGetChannelNameByIdResponse(BaseModel):
    data: SlackChannel = Field(alias='data')

    jsonapi: JsonApi = Field(alias='jsonapi')

    links: SelfLink = Field(alias='links')
    class Config:
        arbitrary_types_allowed = True
