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


class RequiredProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationData(TypedDict):
    id: str

    # Type of the related resource
    type: str

class OptionalProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationData(TypedDict, total=False):
    pass

class ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationData(RequiredProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationData, OptionalProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationData):
    pass