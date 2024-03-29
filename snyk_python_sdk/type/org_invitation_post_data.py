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

from snyk_python_sdk.type.org_invitation_post_attributes import OrgInvitationPostAttributes
from snyk_python_sdk.type.org_invitation_post_data_relationships import OrgInvitationPostDataRelationships

class RequiredOrgInvitationPostData(TypedDict):
    attributes: OrgInvitationPostAttributes

    type: str

class OptionalOrgInvitationPostData(TypedDict, total=False):
    relationships: OrgInvitationPostDataRelationships

class OrgInvitationPostData(RequiredOrgInvitationPostData, OptionalOrgInvitationPostData):
    pass
