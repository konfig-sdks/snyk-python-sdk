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

from snyk_python_sdk.type.projects_list_for_org_response_data_item_relationships_importer_data import ProjectsListForOrgResponseDataItemRelationshipsImporterData
from snyk_python_sdk.type.projects_list_for_org_response_data_item_relationships_importer_links import ProjectsListForOrgResponseDataItemRelationshipsImporterLinks
from snyk_python_sdk.type.projects_list_for_org_response_data_item_relationships_importer_meta import ProjectsListForOrgResponseDataItemRelationshipsImporterMeta

class RequiredProjectsListForOrgResponseDataItemRelationshipsImporter(TypedDict):
    data: ProjectsListForOrgResponseDataItemRelationshipsImporterData

    links: ProjectsListForOrgResponseDataItemRelationshipsImporterLinks

class OptionalProjectsListForOrgResponseDataItemRelationshipsImporter(TypedDict, total=False):
    meta: ProjectsListForOrgResponseDataItemRelationshipsImporterMeta

class ProjectsListForOrgResponseDataItemRelationshipsImporter(RequiredProjectsListForOrgResponseDataItemRelationshipsImporter, OptionalProjectsListForOrgResponseDataItemRelationshipsImporter):
    pass