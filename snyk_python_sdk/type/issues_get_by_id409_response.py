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

from snyk_python_sdk.type.issues_get_by_id409_response_errors import IssuesGetById409ResponseErrors
from snyk_python_sdk.type.issues_get_by_id409_response_jsonapi import IssuesGetById409ResponseJsonapi

class RequiredIssuesGetById409Response(TypedDict):
    errors: IssuesGetById409ResponseErrors

    jsonapi: IssuesGetById409ResponseJsonapi

class OptionalIssuesGetById409Response(TypedDict, total=False):
    pass

class IssuesGetById409Response(RequiredIssuesGetById409Response, OptionalIssuesGetById409Response):
    pass
