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


class RequiredPublicTargetRelationshipsOrganizationData(TypedDict):
    id: str

    # Content type.
    type: str

class OptionalPublicTargetRelationshipsOrganizationData(TypedDict, total=False):
    pass

class PublicTargetRelationshipsOrganizationData(RequiredPublicTargetRelationshipsOrganizationData, OptionalPublicTargetRelationshipsOrganizationData):
    pass