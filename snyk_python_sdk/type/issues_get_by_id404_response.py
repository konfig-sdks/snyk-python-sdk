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

from snyk_python_sdk.type.issues_get_by_id404_response_errors import IssuesGetById404ResponseErrors
from snyk_python_sdk.type.issues_get_by_id404_response_jsonapi import IssuesGetById404ResponseJsonapi

class RequiredIssuesGetById404Response(TypedDict):
    errors: IssuesGetById404ResponseErrors

    jsonapi: IssuesGetById404ResponseJsonapi

class OptionalIssuesGetById404Response(TypedDict, total=False):
    pass

class IssuesGetById404Response(RequiredIssuesGetById404Response, OptionalIssuesGetById404Response):
    pass