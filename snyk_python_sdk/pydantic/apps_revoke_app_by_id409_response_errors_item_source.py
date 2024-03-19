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


class AppsRevokeAppById409ResponseErrorsItemSource(BaseModel):
    # A string indicating which URI query parameter caused the error.
    parameter: typing.Optional[str] = Field(None, alias='parameter')

    # A JSON Pointer [RFC6901] to the associated entity in the request document.
    pointer: typing.Optional[str] = Field(None, alias='pointer')
    class Config:
        arbitrary_types_allowed = True
