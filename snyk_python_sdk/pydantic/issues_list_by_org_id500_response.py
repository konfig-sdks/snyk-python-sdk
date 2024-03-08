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

from snyk_python_sdk.pydantic.issues_list_by_org_id500_response_errors import IssuesListByOrgId500ResponseErrors
from snyk_python_sdk.pydantic.issues_list_by_org_id500_response_jsonapi import IssuesListByOrgId500ResponseJsonapi

class IssuesListByOrgId500Response(BaseModel):
    errors: IssuesListByOrgId500ResponseErrors = Field(alias='errors')

    jsonapi: IssuesListByOrgId500ResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True
