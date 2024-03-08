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

from snyk_python_sdk.type.org_invitation_attributes import OrgInvitationAttributes
from snyk_python_sdk.type.org_invitation_relationships import OrgInvitationRelationships

class RequiredOrgInvitation(TypedDict):
    attributes: OrgInvitationAttributes

    id: str

    type: str

class OptionalOrgInvitation(TypedDict, total=False):
    relationships: OrgInvitationRelationships

class OrgInvitation(RequiredOrgInvitation, OptionalOrgInvitation):
    pass
