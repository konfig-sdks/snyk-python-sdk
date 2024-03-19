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

from snyk_python_sdk.type.issues_by_group_id500_response_errors import IssuesByGroupId500ResponseErrors
from snyk_python_sdk.type.issues_by_group_id500_response_jsonapi import IssuesByGroupId500ResponseJsonapi

class RequiredIssuesByGroupId500Response(TypedDict):
    errors: IssuesByGroupId500ResponseErrors

    jsonapi: IssuesByGroupId500ResponseJsonapi

class OptionalIssuesByGroupId500Response(TypedDict, total=False):
    pass

class IssuesByGroupId500Response(RequiredIssuesByGroupId500Response, OptionalIssuesByGroupId500Response):
    pass
