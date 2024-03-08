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

from snyk_python_sdk.type.project_attributes import ProjectAttributes
from snyk_python_sdk.type.projects_get_by_project_id_response_data_meta import ProjectsGetByProjectIdResponseDataMeta
from snyk_python_sdk.type.projects_get_by_project_id_response_data_relationships import ProjectsGetByProjectIdResponseDataRelationships

class RequiredProjectsGetByProjectIdResponseData(TypedDict):
    attributes: ProjectAttributes

    # The Resource ID.
    id: str

    # The Resource type.
    type: str

class OptionalProjectsGetByProjectIdResponseData(TypedDict, total=False):
    meta: ProjectsGetByProjectIdResponseDataMeta

    relationships: ProjectsGetByProjectIdResponseDataRelationships

class ProjectsGetByProjectIdResponseData(RequiredProjectsGetByProjectIdResponseData, OptionalProjectsGetByProjectIdResponseData):
    pass