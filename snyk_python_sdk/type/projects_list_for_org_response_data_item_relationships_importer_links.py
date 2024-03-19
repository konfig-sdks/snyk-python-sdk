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


class RequiredProjectsListForOrgResponseDataItemRelationshipsImporterLinks(TypedDict):
    pass

class OptionalProjectsListForOrgResponseDataItemRelationshipsImporterLinks(TypedDict, total=False):
    related: typing.Union[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

class ProjectsListForOrgResponseDataItemRelationshipsImporterLinks(RequiredProjectsListForOrgResponseDataItemRelationshipsImporterLinks, OptionalProjectsListForOrgResponseDataItemRelationshipsImporterLinks):
    pass
