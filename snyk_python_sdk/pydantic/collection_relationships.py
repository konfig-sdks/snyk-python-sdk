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

from snyk_python_sdk.pydantic.collection_relationships_created_by_user import CollectionRelationshipsCreatedByUser
from snyk_python_sdk.pydantic.collection_relationships_org import CollectionRelationshipsOrg

class CollectionRelationships(BaseModel):
    created_by_user: CollectionRelationshipsCreatedByUser = Field(alias='created_by_user')

    org: CollectionRelationshipsOrg = Field(alias='org')
    class Config:
        arbitrary_types_allowed = True
