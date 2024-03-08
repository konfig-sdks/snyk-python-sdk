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


class PublicTargetAttributes(BaseModel):
    # The human readable name that represents this target. These are generated based on the provided properties, and the source. 
    display_name: str = Field(alias='display_name')

    # If the target is private, or publicly accessible
    is_private: bool = Field(alias='is_private')

    # The URL for the resource.
    url: typing.Optional[str] = Field(alias='url')

    # The creation date of the target
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')
    class Config:
        arbitrary_types_allowed = True