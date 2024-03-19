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

from snyk_python_sdk.pydantic.projects_list_for_org_response_data_item_relationships_importer_data import ProjectsListForOrgResponseDataItemRelationshipsImporterData
from snyk_python_sdk.pydantic.projects_list_for_org_response_data_item_relationships_importer_links import ProjectsListForOrgResponseDataItemRelationshipsImporterLinks
from snyk_python_sdk.pydantic.projects_list_for_org_response_data_item_relationships_importer_meta import ProjectsListForOrgResponseDataItemRelationshipsImporterMeta

class ProjectsListForOrgResponseDataItemRelationshipsImporter(BaseModel):
    data: ProjectsListForOrgResponseDataItemRelationshipsImporterData = Field(alias='data')

    links: ProjectsListForOrgResponseDataItemRelationshipsImporterLinks = Field(alias='links')

    meta: typing.Optional[ProjectsListForOrgResponseDataItemRelationshipsImporterMeta] = Field(None, alias='meta')
    class Config:
        arbitrary_types_allowed = True
