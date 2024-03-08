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

from snyk_python_sdk.pydantic.apps_create_install_secret401_response_errors import AppsCreateInstallSecret401ResponseErrors
from snyk_python_sdk.pydantic.apps_create_install_secret401_response_jsonapi import AppsCreateInstallSecret401ResponseJsonapi

class AppsCreateInstallSecret401Response(BaseModel):
    errors: AppsCreateInstallSecret401ResponseErrors = Field(alias='errors')

    jsonapi: AppsCreateInstallSecret401ResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True
