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

from snyk_python_sdk.pydantic.severity_threshold import SeverityThreshold

class ProjectSettingsPatchRequestDataAttributes(BaseModel):
    # Current status of the project settings.
    is_active: typing.Optional[bool] = Field(None, alias='is_active')

    severity_threshold: typing.Optional[SeverityThreshold] = Field(None, alias='severity_threshold')

    target_channel_id: typing.Optional[str] = Field(None, alias='target_channel_id')
    class Config:
        arbitrary_types_allowed = True
