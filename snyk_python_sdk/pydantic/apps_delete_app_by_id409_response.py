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

from snyk_python_sdk.pydantic.apps_delete_app_by_id409_response_errors import AppsDeleteAppById409ResponseErrors
from snyk_python_sdk.pydantic.apps_delete_app_by_id409_response_jsonapi import AppsDeleteAppById409ResponseJsonapi

class AppsDeleteAppById409Response(BaseModel):
    errors: AppsDeleteAppById409ResponseErrors = Field(alias='errors')

    jsonapi: AppsDeleteAppById409ResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True