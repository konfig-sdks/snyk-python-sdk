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

from snyk_python_sdk.type.delete_projects_from_collection_request_data import DeleteProjectsFromCollectionRequestData

class RequiredDeleteProjectsFromCollectionRequest(TypedDict):
    data: DeleteProjectsFromCollectionRequestData

class OptionalDeleteProjectsFromCollectionRequest(TypedDict, total=False):
    pass

class DeleteProjectsFromCollectionRequest(RequiredDeleteProjectsFromCollectionRequest, OptionalDeleteProjectsFromCollectionRequest):
    pass