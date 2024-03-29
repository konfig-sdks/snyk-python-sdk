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

from snyk_python_sdk.type.audit_log_search import AuditLogSearch
from snyk_python_sdk.type.json_api import JsonApi
from snyk_python_sdk.type.links import Links

class RequiredAuditLogsSearchOrganizationAuditLogsResponse(TypedDict):
    data: AuditLogSearch

    jsonapi: JsonApi

class OptionalAuditLogsSearchOrganizationAuditLogsResponse(TypedDict, total=False):
    links: Links

class AuditLogsSearchOrganizationAuditLogsResponse(RequiredAuditLogsSearchOrganizationAuditLogsResponse, OptionalAuditLogsSearchOrganizationAuditLogsResponse):
    pass
