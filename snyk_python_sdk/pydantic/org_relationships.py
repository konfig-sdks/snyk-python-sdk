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

from snyk_python_sdk.pydantic.member_role_relationship import MemberRoleRelationship

class OrgRelationships(BaseModel):
    member_role: typing.Optional[MemberRoleRelationship] = Field(None, alias='member_role')
    class Config:
        arbitrary_types_allowed = True