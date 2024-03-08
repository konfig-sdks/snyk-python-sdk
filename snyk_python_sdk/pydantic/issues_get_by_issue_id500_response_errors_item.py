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

from snyk_python_sdk.pydantic.issues_get_by_issue_id500_response_errors_item_meta import IssuesGetByIssueId500ResponseErrorsItemMeta
from snyk_python_sdk.pydantic.issues_get_by_issue_id500_response_errors_item_source import IssuesGetByIssueId500ResponseErrorsItemSource

class IssuesGetByIssueId500ResponseErrorsItem(BaseModel):
    # A human-readable explanation specific to this occurrence of the problem.
    detail: str = Field(alias='detail')

    # The HTTP status code applicable to this problem, expressed as a string value.
    status: str = Field(alias='status')

    # A short, human-readable summary of the problem that SHOULD NOT change from occurrence to occurrence of the problem, except for purposes of localization.
    title: typing.Optional[str] = Field(None, alias='title')

    # An application-specific error code, expressed as a string value.
    code: typing.Optional[str] = Field(None, alias='code')

    # A unique identifier for this particular occurrence of the problem.
    id: typing.Optional[str] = Field(None, alias='id')

    meta: typing.Optional[IssuesGetByIssueId500ResponseErrorsItemMeta] = Field(None, alias='meta')

    source: typing.Optional[IssuesGetByIssueId500ResponseErrorsItemSource] = Field(None, alias='source')
    class Config:
        arbitrary_types_allowed = True
