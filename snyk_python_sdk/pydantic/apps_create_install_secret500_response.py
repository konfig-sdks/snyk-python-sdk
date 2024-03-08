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

from snyk_python_sdk.pydantic.apps_create_install_secret500_response_errors import AppsCreateInstallSecret500ResponseErrors
from snyk_python_sdk.pydantic.apps_create_install_secret500_response_jsonapi import AppsCreateInstallSecret500ResponseJsonapi

class AppsCreateInstallSecret500Response(BaseModel):
    errors: AppsCreateInstallSecret500ResponseErrors = Field(alias='errors')

    jsonapi: AppsCreateInstallSecret500ResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True
