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

from snyk_python_sdk.pydantic.projects_update_by_project_id_response_data_relationships_organization_data import ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationData
from snyk_python_sdk.pydantic.projects_update_by_project_id_response_data_relationships_organization_links import ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationLinks
from snyk_python_sdk.pydantic.projects_update_by_project_id_response_data_relationships_organization_meta import ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationMeta

class ProjectsUpdateByProjectIdResponseDataRelationshipsOrganization(BaseModel):
    data: ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationData = Field(alias='data')

    links: ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationLinks = Field(alias='links')

    meta: typing.Optional[ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationMeta] = Field(None, alias='meta')
    class Config:
        arbitrary_types_allowed = True