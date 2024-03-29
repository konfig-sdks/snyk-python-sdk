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
from pydantic import BaseModel, Field, RootModel

from snyk_python_sdk.pydantic.audit_log_search_items import AuditLogSearchItems

class AuditLogSearch(BaseModel):
    items: typing.Optional[AuditLogSearchItems] = Field(None, alias='items')

    type: typing.Optional[str] = Field(None, alias='type')
    class Config:
        arbitrary_types_allowed = True
