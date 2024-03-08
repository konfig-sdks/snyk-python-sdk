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

from snyk_python_sdk.pydantic.apps_revoke_bot_authorization401_response_errors import AppsRevokeBotAuthorization401ResponseErrors
from snyk_python_sdk.pydantic.apps_revoke_bot_authorization401_response_jsonapi import AppsRevokeBotAuthorization401ResponseJsonapi

class AppsRevokeBotAuthorization401Response(BaseModel):
    errors: AppsRevokeBotAuthorization401ResponseErrors = Field(alias='errors')

    jsonapi: AppsRevokeBotAuthorization401ResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True