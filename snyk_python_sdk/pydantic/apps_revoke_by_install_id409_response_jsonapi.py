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


class AppsRevokeByInstallId409ResponseJsonapi(BaseModel):
    # Version of the JSON API specification this server supports.
    version: str = Field(alias='version')
    class Config:
        arbitrary_types_allowed = True
