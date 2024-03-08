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

from snyk_python_sdk.pydantic.apps_revoke_user_app_session500_response_errors import AppsRevokeUserAppSession500ResponseErrors
from snyk_python_sdk.pydantic.apps_revoke_user_app_session500_response_jsonapi import AppsRevokeUserAppSession500ResponseJsonapi

class AppsRevokeUserAppSession500Response(BaseModel):
    errors: AppsRevokeUserAppSession500ResponseErrors = Field(alias='errors')

    jsonapi: AppsRevokeUserAppSession500ResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True