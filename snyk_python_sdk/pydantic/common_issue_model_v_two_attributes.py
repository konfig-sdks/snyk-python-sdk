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
from pydantic import BaseModel, Field, RootModel

from snyk_python_sdk.pydantic.common_issue_model_v_two_attributes_problems import CommonIssueModelVTwoAttributesProblems
from snyk_python_sdk.pydantic.coordinate_v_two import CoordinateVTwo
from snyk_python_sdk.pydantic.severity import Severity
from snyk_python_sdk.pydantic.slots import Slots

class CommonIssueModelVTwoAttributes(BaseModel):
    # A human-readable title for this issue.
    title: typing.Optional[str] = Field(None, alias='title')

    # A description of the issue in Markdown format
    description: typing.Optional[str] = Field(None, alias='description')

    coordinates: typing.Optional[typing.List[CoordinateVTwo]] = Field(None, alias='coordinates')

    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    # The type from enumeration of the issue’s severity level. This is usually set from the issue’s producer, but can be overridden by policies.
    effective_severity_level: typing.Optional[Literal["info", "low", "medium", "high", "critical"]] = Field(None, alias='effective_severity_level')

    problems: typing.Optional[CommonIssueModelVTwoAttributesProblems] = Field(None, alias='problems')

    # The severity level of the vulnerability: ‘low’, ‘medium’, ‘high’ or ‘critical’.
    severities: typing.Optional[typing.List[Severity]] = Field(None, alias='severities')

    slots: typing.Optional[Slots] = Field(None, alias='slots')

    # The issue type
    type: typing.Optional[str] = Field(None, alias='type')

    # When the vulnerability information was last modified.
    updated_at: typing.Optional[datetime] = Field(None, alias='updated_at')
    class Config:
        arbitrary_types_allowed = True
