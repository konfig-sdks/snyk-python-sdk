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

from snyk_python_sdk.pydantic.severity_threshold import SeverityThreshold

class SettingsAttributes(BaseModel):
    severity_threshold: SeverityThreshold = Field(alias='severity_threshold')

    target_channel_id: str = Field(alias='target_channel_id')
    class Config:
        arbitrary_types_allowed = True
