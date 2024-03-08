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

from snyk_python_sdk.type.relationship import Relationship

class RequiredOrgInvitationRelationships(TypedDict):
    pass

class OptionalOrgInvitationRelationships(TypedDict, total=False):
    org: Relationship

class OrgInvitationRelationships(RequiredOrgInvitationRelationships, OptionalOrgInvitationRelationships):
    pass
