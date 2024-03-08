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

from snyk_python_sdk.pydantic.apps_create_organization_app500_response_errors import AppsCreateOrganizationApp500ResponseErrors
from snyk_python_sdk.pydantic.apps_create_organization_app500_response_jsonapi import AppsCreateOrganizationApp500ResponseJsonapi

class AppsCreateOrganizationApp500Response(BaseModel):
    errors: AppsCreateOrganizationApp500ResponseErrors = Field(alias='errors')

    jsonapi: AppsCreateOrganizationApp500ResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True
