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


class CommonIssueModelAttributesProblemsItem(BaseModel):
    id: str = Field(alias='id')

    source: str = Field(alias='source')

    # When this problem was disclosed to the public.
    disclosed_at: typing.Optional[datetime] = Field(None, alias='disclosed_at')

    # When this problem was first discovered.
    discovered_at: typing.Optional[datetime] = Field(None, alias='discovered_at')

    # When this problem was last updated.
    updated_at: typing.Optional[datetime] = Field(None, alias='updated_at')

    # An optional URL for this problem.
    url: typing.Optional[str] = Field(None, alias='url')
    class Config:
        arbitrary_types_allowed = True
