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

from snyk_python_sdk.type.common_issue_model_v_two_attributes_problems import CommonIssueModelVTwoAttributesProblems
from snyk_python_sdk.type.coordinate_v_two import CoordinateVTwo
from snyk_python_sdk.type.severity import Severity
from snyk_python_sdk.type.slots import Slots

class RequiredCommonIssueModelVTwoAttributes(TypedDict):
    pass

class OptionalCommonIssueModelVTwoAttributes(TypedDict, total=False):
    # A human-readable title for this issue.
    title: str

    # A description of the issue in Markdown format
    description: str

    coordinates: typing.List[CoordinateVTwo]

    created_at: datetime

    # The type from enumeration of the issue’s severity level. This is usually set from the issue’s producer, but can be overridden by policies.
    effective_severity_level: str

    problems: CommonIssueModelVTwoAttributesProblems

    # The severity level of the vulnerability: ‘low’, ‘medium’, ‘high’ or ‘critical’.
    severities: typing.List[Severity]

    slots: Slots

    # The issue type
    type: str

    # When the vulnerability information was last modified.
    updated_at: datetime

class CommonIssueModelVTwoAttributes(RequiredCommonIssueModelVTwoAttributes, OptionalCommonIssueModelVTwoAttributes):
    pass
