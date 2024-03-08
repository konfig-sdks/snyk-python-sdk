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

from snyk_python_sdk.pydantic.project_attributes import ProjectAttributes
from snyk_python_sdk.pydantic.projects_get_by_project_id_response_data_meta import ProjectsGetByProjectIdResponseDataMeta
from snyk_python_sdk.pydantic.projects_get_by_project_id_response_data_relationships import ProjectsGetByProjectIdResponseDataRelationships

class ProjectsGetByProjectIdResponseData(BaseModel):
    attributes: ProjectAttributes = Field(alias='attributes')

    # The Resource ID.
    id: str = Field(alias='id')

    # The Resource type.
    type: str = Field(alias='type')

    meta: typing.Optional[ProjectsGetByProjectIdResponseDataMeta] = Field(None, alias='meta')

    relationships: typing.Optional[ProjectsGetByProjectIdResponseDataRelationships] = Field(None, alias='relationships')
    class Config:
        arbitrary_types_allowed = True