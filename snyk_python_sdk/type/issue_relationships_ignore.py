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

from snyk_python_sdk.type.issue_relationships_ignore_data import IssueRelationshipsIgnoreData

class RequiredIssueRelationshipsIgnore(TypedDict):
    data: IssueRelationshipsIgnoreData

class OptionalIssueRelationshipsIgnore(TypedDict, total=False):
    pass

class IssueRelationshipsIgnore(RequiredIssueRelationshipsIgnore, OptionalIssueRelationshipsIgnore):
    pass