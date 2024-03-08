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

from snyk_python_sdk.type.image_attributes import ImageAttributes
from snyk_python_sdk.type.image_digest import ImageDigest
from snyk_python_sdk.type.image_relationships import ImageRelationships

class RequiredImage(TypedDict):
    attributes: ImageAttributes

    id: ImageDigest

    type: str

class OptionalImage(TypedDict, total=False):
    relationships: ImageRelationships

class Image(RequiredImage, OptionalImage):
    pass
