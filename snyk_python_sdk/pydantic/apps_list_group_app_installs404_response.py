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

from snyk_python_sdk.pydantic.apps_list_group_app_installs404_response_errors import AppsListGroupAppInstalls404ResponseErrors
from snyk_python_sdk.pydantic.apps_list_group_app_installs404_response_jsonapi import AppsListGroupAppInstalls404ResponseJsonapi

class AppsListGroupAppInstalls404Response(BaseModel):
    errors: AppsListGroupAppInstalls404ResponseErrors = Field(alias='errors')

    jsonapi: AppsListGroupAppInstalls404ResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True