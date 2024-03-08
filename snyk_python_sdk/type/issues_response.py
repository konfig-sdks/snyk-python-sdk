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

from snyk_python_sdk.type.common_issue_model import CommonIssueModel
from snyk_python_sdk.type.issues_meta import IssuesMeta
from snyk_python_sdk.type.json_api import JsonApi
from snyk_python_sdk.type.paginated_links import PaginatedLinks

class RequiredIssuesResponse(TypedDict):
    pass

class OptionalIssuesResponse(TypedDict, total=False):
    data: typing.List[CommonIssueModel]

    jsonapi: JsonApi

    links: PaginatedLinks

    meta: IssuesMeta

class IssuesResponse(RequiredIssuesResponse, OptionalIssuesResponse):
    pass