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


class OrgAttributes(BaseModel):
    # Whether the organization is independent (that is, not part of a group).
    is_personal: bool = Field(alias='is_personal')

    # The display name of the organization.
    name: str = Field(alias='name')

    # The canonical (unique and URL-friendly) name of the organization.
    slug: str = Field(alias='slug')

    # Whether the organization permits access requests from users who are not members of the organization.
    access_requests_enabled: typing.Optional[bool] = Field(None, alias='access_requests_enabled')

    # The time the organization was created.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    # The Snyk ID of the group to which the organization belongs.
    group_id: typing.Optional[str] = Field(None, alias='group_id')

    # The time the organization was last modified.
    updated_at: typing.Optional[datetime] = Field(None, alias='updated_at')
    class Config:
        arbitrary_types_allowed = True
