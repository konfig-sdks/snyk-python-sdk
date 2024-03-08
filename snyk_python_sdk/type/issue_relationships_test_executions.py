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

from snyk_python_sdk.type.issue_relationships_test_executions_data import IssueRelationshipsTestExecutionsData

class RequiredIssueRelationshipsTestExecutions(TypedDict):
    data: IssueRelationshipsTestExecutionsData

class OptionalIssueRelationshipsTestExecutions(TypedDict, total=False):
    pass

class IssueRelationshipsTestExecutions(RequiredIssueRelationshipsTestExecutions, OptionalIssueRelationshipsTestExecutions):
    pass