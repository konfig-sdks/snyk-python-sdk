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

from snyk_python_sdk.type.coordinate import Coordinate
from snyk_python_sdk.type.model_class import ModelClass
from snyk_python_sdk.type.problem import Problem
from snyk_python_sdk.type.resolution import Resolution
from snyk_python_sdk.type.risk import Risk
from snyk_python_sdk.type.type_def import TypeDef

class RequiredIssueAttributes(TypedDict):
    # A human-readable title for this issue.
    title: str

    # The creation time of this issue.
    created_at: datetime

    # The computed effective severity of this issue. This is either the highest level from all included severities, or an overridden value set via group level policy. 
    effective_severity_level: str

    # A flag indicating if the issue is being ignored. Derived from the issue's ignore, which provides more details.
    ignored: bool

    # An opaque key used for uniquely identifying this issue across test runs, within a project.
    key: str

    # The issue's status. Derived from the issue's resolution, which provides more details.
    status: str

    type: TypeDef

    # The time when this issue was last modified.
    updated_at: datetime

class OptionalIssueAttributes(TypedDict, total=False):
    # A markdown-formatted optional description of this issue. Links are not permitted.
    description: str

    # A list of details for weakness data, policy, etc that are the class of this issue's source.
    classes: typing.List[ModelClass]

    # Where the issue originated, specific to issue type. Details on what code, package, etc introduced the issue. An issue may be caused by more than one coordinate. 
    coordinates: typing.List[Coordinate]

    # A list of details for vulnerability data, policy, etc that are the source of this issue.
    problems: typing.List[Problem]

    resolution: Resolution

    risk: Risk

    # An opaque identifier for corelating across test runs.
    tool: str

class IssueAttributes(RequiredIssueAttributes, OptionalIssueAttributes):
    pass
