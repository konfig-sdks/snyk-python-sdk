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

from snyk_python_sdk.pydantic.projects_get_by_project_id_response_data_relationships_importer_data import ProjectsGetByProjectIdResponseDataRelationshipsImporterData
from snyk_python_sdk.pydantic.projects_get_by_project_id_response_data_relationships_importer_links import ProjectsGetByProjectIdResponseDataRelationshipsImporterLinks
from snyk_python_sdk.pydantic.projects_get_by_project_id_response_data_relationships_importer_meta import ProjectsGetByProjectIdResponseDataRelationshipsImporterMeta

class ProjectsGetByProjectIdResponseDataRelationshipsImporter(BaseModel):
    data: ProjectsGetByProjectIdResponseDataRelationshipsImporterData = Field(alias='data')

    links: ProjectsGetByProjectIdResponseDataRelationshipsImporterLinks = Field(alias='links')

    meta: typing.Optional[ProjectsGetByProjectIdResponseDataRelationshipsImporterMeta] = Field(None, alias='meta')
    class Config:
        arbitrary_types_allowed = True