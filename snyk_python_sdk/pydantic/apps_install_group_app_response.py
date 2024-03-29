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

from snyk_python_sdk.pydantic.app_install_with_client import AppInstallWithClient
from snyk_python_sdk.pydantic.json_api import JsonApi
from snyk_python_sdk.pydantic.paginated_links import PaginatedLinks

class AppsInstallGroupAppResponse(BaseModel):
    data: AppInstallWithClient = Field(alias='data')

    jsonapi: JsonApi = Field(alias='jsonapi')

    links: PaginatedLinks = Field(alias='links')
    class Config:
        arbitrary_types_allowed = True
