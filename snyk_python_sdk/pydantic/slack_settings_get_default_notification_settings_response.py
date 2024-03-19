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

from snyk_python_sdk.pydantic.json_api import JsonApi
from snyk_python_sdk.pydantic.self_link import SelfLink
from snyk_python_sdk.pydantic.slack_default_settings_data import SlackDefaultSettingsData

class SlackSettingsGetDefaultNotificationSettingsResponse(BaseModel):
    data: typing.Optional[SlackDefaultSettingsData] = Field(None, alias='data')

    jsonapi: typing.Optional[JsonApi] = Field(None, alias='jsonapi')

    links: typing.Optional[SelfLink] = Field(None, alias='links')
    class Config:
        arbitrary_types_allowed = True
