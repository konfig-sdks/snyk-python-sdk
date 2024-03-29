# coding: utf-8

"""
    Snyk API

    Snyk helps software-driven businesses develop fast and stay secure. Continuously find and fix vulnerabilities for npm, Maven, NuGet, RubyGems, PyPI and more.

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from snyk_python_sdk.pydantic.projects_update_by_project_id_response_data_relationships_importer import ProjectsUpdateByProjectIdResponseDataRelationshipsImporter
from snyk_python_sdk.pydantic.projects_update_by_project_id_response_data_relationships_organization import ProjectsUpdateByProjectIdResponseDataRelationshipsOrganization
from snyk_python_sdk.pydantic.projects_update_by_project_id_response_data_relationships_owner import ProjectsUpdateByProjectIdResponseDataRelationshipsOwner

class ProjectsUpdateByProjectIdResponseDataRelationships(BaseModel):
    organization: ProjectsUpdateByProjectIdResponseDataRelationshipsOrganization = Field(alias='organization')

    target: typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(alias='target')

    importer: typing.Optional[ProjectsUpdateByProjectIdResponseDataRelationshipsImporter] = Field(None, alias='importer')

    owner: typing.Optional[ProjectsUpdateByProjectIdResponseDataRelationshipsOwner] = Field(None, alias='owner')
    class Config:
        arbitrary_types_allowed = True
