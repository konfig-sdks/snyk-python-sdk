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

from snyk_python_sdk.pydantic.apps_install_group_app404_response_errors import AppsInstallGroupApp404ResponseErrors
from snyk_python_sdk.pydantic.apps_install_group_app404_response_jsonapi import AppsInstallGroupApp404ResponseJsonapi

class AppsInstallGroupApp404Response(BaseModel):
    errors: AppsInstallGroupApp404ResponseErrors = Field(alias='errors')

    jsonapi: AppsInstallGroupApp404ResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True
