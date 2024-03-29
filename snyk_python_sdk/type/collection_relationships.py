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

from snyk_python_sdk.type.collection_relationships_created_by_user import CollectionRelationshipsCreatedByUser
from snyk_python_sdk.type.collection_relationships_org import CollectionRelationshipsOrg

class RequiredCollectionRelationships(TypedDict):
    created_by_user: CollectionRelationshipsCreatedByUser

    org: CollectionRelationshipsOrg

class OptionalCollectionRelationships(TypedDict, total=False):
    pass

class CollectionRelationships(RequiredCollectionRelationships, OptionalCollectionRelationships):
    pass
