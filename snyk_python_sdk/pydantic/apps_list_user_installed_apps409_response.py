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

from snyk_python_sdk.pydantic.apps_list_user_installed_apps409_response_errors import AppsListUserInstalledApps409ResponseErrors
from snyk_python_sdk.pydantic.apps_list_user_installed_apps409_response_jsonapi import AppsListUserInstalledApps409ResponseJsonapi

class AppsListUserInstalledApps409Response(BaseModel):
    errors: AppsListUserInstalledApps409ResponseErrors = Field(alias='errors')

    jsonapi: AppsListUserInstalledApps409ResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True
