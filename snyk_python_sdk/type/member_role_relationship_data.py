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

from snyk_python_sdk.type.org_role_attributes import OrgRoleAttributes
from snyk_python_sdk.type.types import Types

class RequiredMemberRoleRelationshipData(TypedDict):
    # The Snyk ID of the organization role.
    id: str

    type: Types

class OptionalMemberRoleRelationshipData(TypedDict, total=False):
    attributes: OrgRoleAttributes

class MemberRoleRelationshipData(RequiredMemberRoleRelationshipData, OptionalMemberRoleRelationshipData):
    pass
