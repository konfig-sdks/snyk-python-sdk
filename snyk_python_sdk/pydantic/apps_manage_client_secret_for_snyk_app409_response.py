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

from snyk_python_sdk.pydantic.apps_manage_client_secret_for_snyk_app409_response_errors import AppsManageClientSecretForSnykApp409ResponseErrors
from snyk_python_sdk.pydantic.apps_manage_client_secret_for_snyk_app409_response_jsonapi import AppsManageClientSecretForSnykApp409ResponseJsonapi

class AppsManageClientSecretForSnykApp409Response(BaseModel):
    errors: AppsManageClientSecretForSnykApp409ResponseErrors = Field(alias='errors')

    jsonapi: AppsManageClientSecretForSnykApp409ResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True