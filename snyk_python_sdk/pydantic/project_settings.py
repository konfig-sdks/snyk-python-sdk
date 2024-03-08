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
from pydantic import BaseModel, Field, RootModel

from snyk_python_sdk.pydantic.auto_dependency_upgrade_settings import AutoDependencyUpgradeSettings
from snyk_python_sdk.pydantic.auto_remediation_prs_settings import AutoRemediationPRsSettings
from snyk_python_sdk.pydantic.manual_remediation_prs_settings import ManualRemediationPRsSettings
from snyk_python_sdk.pydantic.pull_request_assignment_settings import PullRequestAssignmentSettings
from snyk_python_sdk.pydantic.pull_requests_settings import PullRequestsSettings
from snyk_python_sdk.pydantic.recurring_tests_settings import RecurringTestsSettings

class ProjectSettings(BaseModel):
    pull_requests: PullRequestsSettings = Field(alias='pull_requests')

    recurring_tests: RecurringTestsSettings = Field(alias='recurring_tests')

    auto_dependency_upgrade: typing.Optional[AutoDependencyUpgradeSettings] = Field(None, alias='auto_dependency_upgrade')

    auto_remediation_prs: typing.Optional[AutoRemediationPRsSettings] = Field(None, alias='auto_remediation_prs')

    manual_remediation_prs: typing.Optional[ManualRemediationPRsSettings] = Field(None, alias='manual_remediation_prs')

    pull_request_assignment: typing.Optional[PullRequestAssignmentSettings] = Field(None, alias='pull_request_assignment')
    class Config:
        arbitrary_types_allowed = True