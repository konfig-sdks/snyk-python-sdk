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

from snyk_python_sdk.type.org_attributes import OrgAttributes
from snyk_python_sdk.type.org_relationships import OrgRelationships
from snyk_python_sdk.type.types import Types

class RequiredOrgWithRelationships(TypedDict):
    attributes: OrgAttributes

    # The Snyk ID of the organization.
    id: str

    type: Types

class OptionalOrgWithRelationships(TypedDict, total=False):
    relationships: OrgRelationships

class OrgWithRelationships(RequiredOrgWithRelationships, OptionalOrgWithRelationships):
    pass
