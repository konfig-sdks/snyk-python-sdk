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


class SlackChannelAttributes(BaseModel):
    # Name of the Slack Channel
    name: typing.Optional[str] = Field(None, alias='name')

    # Channel type
    type: typing.Optional[Literal["public", "private", "direct_message", "multiparty_direct_message"]] = Field(None, alias='type')
    class Config:
        arbitrary_types_allowed = True
