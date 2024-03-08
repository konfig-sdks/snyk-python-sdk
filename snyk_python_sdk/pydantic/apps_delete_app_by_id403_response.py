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

from snyk_python_sdk.pydantic.apps_delete_app_by_id403_response_errors import AppsDeleteAppById403ResponseErrors
from snyk_python_sdk.pydantic.apps_delete_app_by_id403_response_jsonapi import AppsDeleteAppById403ResponseJsonapi

class AppsDeleteAppById403Response(BaseModel):
    errors: AppsDeleteAppById403ResponseErrors = Field(alias='errors')

    jsonapi: AppsDeleteAppById403ResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True