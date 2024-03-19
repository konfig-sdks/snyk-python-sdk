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

from snyk_python_sdk.type.collection_attributes import CollectionAttributes
from snyk_python_sdk.type.collection_meta import CollectionMeta
from snyk_python_sdk.type.collection_relationships import CollectionRelationships
from snyk_python_sdk.type.types import Types

class RequiredCollectionResponse(TypedDict):
    attributes: CollectionAttributes

    id: str

    meta: CollectionMeta

    relationships: CollectionRelationships

    type: Types

class OptionalCollectionResponse(TypedDict, total=False):
    pass

class CollectionResponse(RequiredCollectionResponse, OptionalCollectionResponse):
    pass
