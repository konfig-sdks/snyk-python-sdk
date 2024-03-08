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


class RequiredPullRequestsSettings(TypedDict):
    pass

class OptionalPullRequestsSettings(TypedDict, total=False):
    # Only fail when the issues found have a fix available.
    fail_only_for_issues_with_fix: bool

    # Fail if the project has any issues (\"all\"), or fail if a PR is introducing a new dependency with issues (\"only_new\"). If this value is unset, the setting is inherited from the org default.
    policy: str

    # Only fail for issues greater than or equal to the specified severity. If this value is unset, the setting is inherited from the org default.
    severity_threshold: str

class PullRequestsSettings(RequiredPullRequestsSettings, OptionalPullRequestsSettings):
    pass
