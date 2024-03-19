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

from snyk_python_sdk.type.latest_dependency_total import LatestDependencyTotal
from snyk_python_sdk.type.latest_issue_counts import LatestIssueCounts

class RequiredProjectsListForOrgResponseDataItemMeta(TypedDict):
    pass

class OptionalProjectsListForOrgResponseDataItemMeta(TypedDict, total=False):
    # The date that the project was last uploaded and monitored using cli.
    cli_monitored_at: typing.Optional[datetime]

    latest_dependency_total: LatestDependencyTotal

    latest_issue_counts: LatestIssueCounts

class ProjectsListForOrgResponseDataItemMeta(RequiredProjectsListForOrgResponseDataItemMeta, OptionalProjectsListForOrgResponseDataItemMeta):
    pass
