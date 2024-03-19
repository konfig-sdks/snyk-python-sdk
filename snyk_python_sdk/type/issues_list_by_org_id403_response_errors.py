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

from snyk_python_sdk.type.issues_list_by_org_id403_response_errors_item import IssuesListByOrgId403ResponseErrorsItem

IssuesListByOrgId403ResponseErrors = typing.List[IssuesListByOrgId403ResponseErrorsItem]
