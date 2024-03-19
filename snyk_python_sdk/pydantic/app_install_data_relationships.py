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

from snyk_python_sdk.pydantic.app_install_data_relationships_app import AppInstallDataRelationshipsApp

class AppInstallDataRelationships(BaseModel):
    app: typing.Optional[AppInstallDataRelationshipsApp] = Field(None, alias='app')
    class Config:
        arbitrary_types_allowed = True
