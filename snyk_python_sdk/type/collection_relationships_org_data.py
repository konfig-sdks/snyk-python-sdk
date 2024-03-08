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


class RequiredCollectionRelationshipsOrgData(TypedDict):
    # ID of the org that this collection belongs to
    id: str

    type: str

class OptionalCollectionRelationshipsOrgData(TypedDict, total=False):
    pass

class CollectionRelationshipsOrgData(RequiredCollectionRelationshipsOrgData, OptionalCollectionRelationshipsOrgData):
    pass