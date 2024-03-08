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

from snyk_python_sdk.pydantic.apps_manage_client_secrets404_response_errors import AppsManageClientSecrets404ResponseErrors
from snyk_python_sdk.pydantic.apps_manage_client_secrets404_response_jsonapi import AppsManageClientSecrets404ResponseJsonapi

class AppsManageClientSecrets404Response(BaseModel):
    errors: AppsManageClientSecrets404ResponseErrors = Field(alias='errors')

    jsonapi: AppsManageClientSecrets404ResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True
