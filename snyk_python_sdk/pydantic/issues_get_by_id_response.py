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

from snyk_python_sdk.pydantic.issues_get_by_id_response_errors import IssuesGetByIdResponseErrors
from snyk_python_sdk.pydantic.issues_get_by_id_response_jsonapi import IssuesGetByIdResponseJsonapi

class IssuesGetByIdResponse(BaseModel):
    errors: IssuesGetByIdResponseErrors = Field(alias='errors')

    jsonapi: IssuesGetByIdResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True
