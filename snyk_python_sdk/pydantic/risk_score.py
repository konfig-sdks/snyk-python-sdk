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


class RiskScore(BaseModel):
    # Risk scoring model used to calculate the score value
    model: str = Field(alias='model')

    # Risk score value, which may be used for overall prioritization
    value: int = Field(alias='value')

    updated_at: typing.Optional[datetime] = Field(None, alias='updated_at')
    class Config:
        arbitrary_types_allowed = True
