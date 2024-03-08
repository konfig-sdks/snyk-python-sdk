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

from snyk_python_sdk.type.projects_get_by_project_id_response_data_relationships_importer_data import ProjectsGetByProjectIdResponseDataRelationshipsImporterData
from snyk_python_sdk.type.projects_get_by_project_id_response_data_relationships_importer_links import ProjectsGetByProjectIdResponseDataRelationshipsImporterLinks
from snyk_python_sdk.type.projects_get_by_project_id_response_data_relationships_importer_meta import ProjectsGetByProjectIdResponseDataRelationshipsImporterMeta

class RequiredProjectsGetByProjectIdResponseDataRelationshipsImporter(TypedDict):
    data: ProjectsGetByProjectIdResponseDataRelationshipsImporterData

    links: ProjectsGetByProjectIdResponseDataRelationshipsImporterLinks

class OptionalProjectsGetByProjectIdResponseDataRelationshipsImporter(TypedDict, total=False):
    meta: ProjectsGetByProjectIdResponseDataRelationshipsImporterMeta

class ProjectsGetByProjectIdResponseDataRelationshipsImporter(RequiredProjectsGetByProjectIdResponseDataRelationshipsImporter, OptionalProjectsGetByProjectIdResponseDataRelationshipsImporter):
    pass
