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

from snyk_python_sdk.type.issue_relationships_organization_data import IssueRelationshipsOrganizationData

class RequiredIssueRelationshipsOrganization(TypedDict):
    data: IssueRelationshipsOrganizationData

class OptionalIssueRelationshipsOrganization(TypedDict, total=False):
    pass

class IssueRelationshipsOrganization(RequiredIssueRelationshipsOrganization, OptionalIssueRelationshipsOrganization):
    pass
