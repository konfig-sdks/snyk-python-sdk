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


class RequiredProjectsListForOrgResponseDataItemRelationshipsOrganizationLinks(TypedDict):
    pass

class OptionalProjectsListForOrgResponseDataItemRelationshipsOrganizationLinks(TypedDict, total=False):
    related: typing.Union[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

class ProjectsListForOrgResponseDataItemRelationshipsOrganizationLinks(RequiredProjectsListForOrgResponseDataItemRelationshipsOrganizationLinks, OptionalProjectsListForOrgResponseDataItemRelationshipsOrganizationLinks):
    pass
