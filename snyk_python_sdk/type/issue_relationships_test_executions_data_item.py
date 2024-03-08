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

from snyk_python_sdk.type.test_execution_type import TestExecutionType

class RequiredIssueRelationshipsTestExecutionsDataItem(TypedDict):
    id: str

    type: TestExecutionType

class OptionalIssueRelationshipsTestExecutionsDataItem(TypedDict, total=False):
    pass

class IssueRelationshipsTestExecutionsDataItem(RequiredIssueRelationshipsTestExecutionsDataItem, OptionalIssueRelationshipsTestExecutionsDataItem):
    pass
