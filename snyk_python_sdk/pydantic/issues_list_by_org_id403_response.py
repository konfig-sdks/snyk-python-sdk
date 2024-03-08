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

from snyk_python_sdk.pydantic.issues_list_by_org_id403_response_errors import IssuesListByOrgId403ResponseErrors
from snyk_python_sdk.pydantic.issues_list_by_org_id403_response_jsonapi import IssuesListByOrgId403ResponseJsonapi

class IssuesListByOrgId403Response(BaseModel):
    errors: IssuesListByOrgId403ResponseErrors = Field(alias='errors')

    jsonapi: IssuesListByOrgId403ResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True
