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

from snyk_python_sdk.type.issues_get_by_issue_id401_response_errors import IssuesGetByIssueId401ResponseErrors
from snyk_python_sdk.type.issues_get_by_issue_id401_response_jsonapi import IssuesGetByIssueId401ResponseJsonapi

class RequiredIssuesGetByIssueId401Response(TypedDict):
    errors: IssuesGetByIssueId401ResponseErrors

    jsonapi: IssuesGetByIssueId401ResponseJsonapi

class OptionalIssuesGetByIssueId401Response(TypedDict, total=False):
    pass

class IssuesGetByIssueId401Response(RequiredIssuesGetByIssueId401Response, OptionalIssuesGetByIssueId401Response):
    pass
