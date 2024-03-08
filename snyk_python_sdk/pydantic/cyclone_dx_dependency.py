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

from snyk_python_sdk.pydantic.cyclone_dx_dependency_depends_on import CycloneDxDependencyDependsOn

class CycloneDxDependency(BaseModel):
    depends_on: typing.Optional[CycloneDxDependencyDependsOn] = Field(None, alias='dependsOn')

    ref: typing.Optional[str] = Field(None, alias='ref')
    class Config:
        arbitrary_types_allowed = True
