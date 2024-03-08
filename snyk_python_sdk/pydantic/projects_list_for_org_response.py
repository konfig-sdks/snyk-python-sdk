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

from snyk_python_sdk.pydantic.json_api import JsonApi
from snyk_python_sdk.pydantic.links import Links
from snyk_python_sdk.pydantic.projects_list_for_org_response_data import ProjectsListForOrgResponseData
from snyk_python_sdk.pydantic.projects_list_for_org_response_meta import ProjectsListForOrgResponseMeta

class ProjectsListForOrgResponse(BaseModel):
    jsonapi: JsonApi = Field(alias='jsonapi')

    links: Links = Field(alias='links')

    data: typing.Optional[ProjectsListForOrgResponseData] = Field(None, alias='data')

    meta: typing.Optional[ProjectsListForOrgResponseMeta] = Field(None, alias='meta')
    class Config:
        arbitrary_types_allowed = True
