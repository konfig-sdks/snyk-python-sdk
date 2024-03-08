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


class Dependency(BaseModel):
    # The package name the issue was found in
    package_name: str = Field(alias='package_name')

    # The package version the issue was found in
    package_version: str = Field(alias='package_version')
    class Config:
        arbitrary_types_allowed = True
