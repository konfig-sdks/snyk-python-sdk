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

from snyk_python_sdk.pydantic.apps_create_new_app_for_organization500_response_errors import AppsCreateNewAppForOrganization500ResponseErrors
from snyk_python_sdk.pydantic.apps_create_new_app_for_organization500_response_jsonapi import AppsCreateNewAppForOrganization500ResponseJsonapi

class AppsCreateNewAppForOrganization500Response(BaseModel):
    errors: AppsCreateNewAppForOrganization500ResponseErrors = Field(alias='errors')

    jsonapi: AppsCreateNewAppForOrganization500ResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True
