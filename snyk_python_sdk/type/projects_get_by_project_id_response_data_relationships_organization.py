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

from snyk_python_sdk.type.projects_get_by_project_id_response_data_relationships_organization_data import ProjectsGetByProjectIdResponseDataRelationshipsOrganizationData
from snyk_python_sdk.type.projects_get_by_project_id_response_data_relationships_organization_links import ProjectsGetByProjectIdResponseDataRelationshipsOrganizationLinks
from snyk_python_sdk.type.projects_get_by_project_id_response_data_relationships_organization_meta import ProjectsGetByProjectIdResponseDataRelationshipsOrganizationMeta

class RequiredProjectsGetByProjectIdResponseDataRelationshipsOrganization(TypedDict):
    data: ProjectsGetByProjectIdResponseDataRelationshipsOrganizationData

    links: ProjectsGetByProjectIdResponseDataRelationshipsOrganizationLinks

class OptionalProjectsGetByProjectIdResponseDataRelationshipsOrganization(TypedDict, total=False):
    meta: ProjectsGetByProjectIdResponseDataRelationshipsOrganizationMeta

class ProjectsGetByProjectIdResponseDataRelationshipsOrganization(RequiredProjectsGetByProjectIdResponseDataRelationshipsOrganization, OptionalProjectsGetByProjectIdResponseDataRelationshipsOrganization):
    pass
