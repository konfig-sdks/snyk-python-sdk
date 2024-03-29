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


class RequiredAuditLogSearchItemsItem(TypedDict):
    created: datetime

    event: str

class OptionalAuditLogSearchItemsItem(TypedDict, total=False):
    content: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    group_id: str

    org_id: str

    project_id: str

class AuditLogSearchItemsItem(RequiredAuditLogSearchItemsItem, OptionalAuditLogSearchItemsItem):
    pass
