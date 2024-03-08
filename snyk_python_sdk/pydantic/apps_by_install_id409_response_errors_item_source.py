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


class AppsByInstallId409ResponseErrorsItemSource(BaseModel):
    # A string indicating which URI query parameter caused the error.
    parameter: typing.Optional[str] = Field(None, alias='parameter')

    # A JSON Pointer [RFC6901] to the associated entity in the request document.
    pointer: typing.Optional[str] = Field(None, alias='pointer')
    class Config:
        arbitrary_types_allowed = True
