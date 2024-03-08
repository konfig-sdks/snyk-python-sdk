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

from snyk_python_sdk.type.image_target_ref_attributes import ImageTargetRefAttributes

class RequiredImageTargetRef(TypedDict):
    pass

class OptionalImageTargetRef(TypedDict, total=False):
    attributes: ImageTargetRefAttributes

    id: str

    type: str

class ImageTargetRef(RequiredImageTargetRef, OptionalImageTargetRef):
    pass
