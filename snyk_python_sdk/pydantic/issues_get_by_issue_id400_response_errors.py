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

from snyk_python_sdk.pydantic.issues_get_by_issue_id400_response_errors_item import IssuesGetByIssueId400ResponseErrorsItem

IssuesGetByIssueId400ResponseErrors = typing.List[IssuesGetByIssueId400ResponseErrorsItem]
