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


class RequiredProjectsUpdateByProjectIdResponseDataRelationshipsImporterData(TypedDict):
    id: str

    # Type of the related resource
    type: str

class OptionalProjectsUpdateByProjectIdResponseDataRelationshipsImporterData(TypedDict, total=False):
    pass

class ProjectsUpdateByProjectIdResponseDataRelationshipsImporterData(RequiredProjectsUpdateByProjectIdResponseDataRelationshipsImporterData, OptionalProjectsUpdateByProjectIdResponseDataRelationshipsImporterData):
    pass
