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

from snyk_python_sdk.pydantic.issues_get_by_id409_response_errors import IssuesGetById409ResponseErrors
from snyk_python_sdk.pydantic.issues_get_by_id409_response_jsonapi import IssuesGetById409ResponseJsonapi

class IssuesGetById409Response(BaseModel):
    errors: IssuesGetById409ResponseErrors = Field(alias='errors')

    jsonapi: IssuesGetById409ResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True