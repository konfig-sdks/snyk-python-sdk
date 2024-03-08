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

from snyk_python_sdk.type.org_attributes import OrgAttributes
from snyk_python_sdk.type.org_relationships import OrgRelationships
from snyk_python_sdk.type.types import Types

class RequiredOrgsUpdateDetailsResponseData(TypedDict):
    id: str

    type: Types

class OptionalOrgsUpdateDetailsResponseData(TypedDict, total=False):
    attributes: OrgAttributes

    relationships: OrgRelationships

class OrgsUpdateDetailsResponseData(RequiredOrgsUpdateDetailsResponseData, OptionalOrgsUpdateDetailsResponseData):
    pass
