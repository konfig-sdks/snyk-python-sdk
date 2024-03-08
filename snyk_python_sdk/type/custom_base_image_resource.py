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

from snyk_python_sdk.type.custom_base_image_attributes import CustomBaseImageAttributes

class RequiredCustomBaseImageResource(TypedDict):
    attributes: CustomBaseImageAttributes

    id: str

    type: str

class OptionalCustomBaseImageResource(TypedDict, total=False):
    pass

class CustomBaseImageResource(RequiredCustomBaseImageResource, OptionalCustomBaseImageResource):
    pass
