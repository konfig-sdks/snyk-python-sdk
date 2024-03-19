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

from snyk_python_sdk.pydantic.apps_create_new_app_for_organization409_response_errors import AppsCreateNewAppForOrganization409ResponseErrors
from snyk_python_sdk.pydantic.apps_create_new_app_for_organization409_response_jsonapi import AppsCreateNewAppForOrganization409ResponseJsonapi

class AppsCreateNewAppForOrganization409Response(BaseModel):
    errors: AppsCreateNewAppForOrganization409ResponseErrors = Field(alias='errors')

    jsonapi: AppsCreateNewAppForOrganization409ResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True
