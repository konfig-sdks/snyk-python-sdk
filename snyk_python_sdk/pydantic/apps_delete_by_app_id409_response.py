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

from snyk_python_sdk.pydantic.apps_delete_by_app_id409_response_errors import AppsDeleteByAppId409ResponseErrors
from snyk_python_sdk.pydantic.apps_delete_by_app_id409_response_jsonapi import AppsDeleteByAppId409ResponseJsonapi

class AppsDeleteByAppId409Response(BaseModel):
    errors: AppsDeleteByAppId409ResponseErrors = Field(alias='errors')

    jsonapi: AppsDeleteByAppId409ResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True