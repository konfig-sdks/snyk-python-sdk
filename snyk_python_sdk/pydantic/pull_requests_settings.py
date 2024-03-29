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


class PullRequestsSettings(BaseModel):
    # Only fail when the issues found have a fix available.
    fail_only_for_issues_with_fix: typing.Optional[bool] = Field(None, alias='fail_only_for_issues_with_fix')

    # Fail if the project has any issues (\"all\"), or fail if a PR is introducing a new dependency with issues (\"only_new\"). If this value is unset, the setting is inherited from the org default.
    policy: typing.Optional[Literal["all", "only_new"]] = Field(None, alias='policy')

    # Only fail for issues greater than or equal to the specified severity. If this value is unset, the setting is inherited from the org default.
    severity_threshold: typing.Optional[Literal["low", "medium", "high", "critical"]] = Field(None, alias='severity_threshold')
    class Config:
        arbitrary_types_allowed = True
