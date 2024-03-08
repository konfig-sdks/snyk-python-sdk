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


class AppInstallWithClientAttributes(BaseModel):
    client_id: str = Field(alias='client_id')

    client_secret: str = Field(alias='client_secret')
    class Config:
        arbitrary_types_allowed = True
