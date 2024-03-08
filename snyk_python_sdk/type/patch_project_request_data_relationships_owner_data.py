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


class RequiredPatchProjectRequestDataRelationshipsOwnerData(TypedDict):
    # The public ID of the user that owns the project
    id: typing.Optional[str]

    type: str

class OptionalPatchProjectRequestDataRelationshipsOwnerData(TypedDict, total=False):
    pass

class PatchProjectRequestDataRelationshipsOwnerData(RequiredPatchProjectRequestDataRelationshipsOwnerData, OptionalPatchProjectRequestDataRelationshipsOwnerData):
    pass