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

from snyk_python_sdk.type.image_relationships_image_target_refs import ImageRelationshipsImageTargetRefs

class RequiredImageRelationships(TypedDict):
    pass

class OptionalImageRelationships(TypedDict, total=False):
    image_target_refs: ImageRelationshipsImageTargetRefs

class ImageRelationships(RequiredImageRelationships, OptionalImageRelationships):
    pass