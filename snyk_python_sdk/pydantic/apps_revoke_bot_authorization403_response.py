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

from snyk_python_sdk.pydantic.apps_revoke_bot_authorization403_response_errors import AppsRevokeBotAuthorization403ResponseErrors
from snyk_python_sdk.pydantic.apps_revoke_bot_authorization403_response_jsonapi import AppsRevokeBotAuthorization403ResponseJsonapi

class AppsRevokeBotAuthorization403Response(BaseModel):
    errors: AppsRevokeBotAuthorization403ResponseErrors = Field(alias='errors')

    jsonapi: AppsRevokeBotAuthorization403ResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True
