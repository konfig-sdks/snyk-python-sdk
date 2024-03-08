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


class RequiredPublicTargetAttributes(TypedDict):
    # The human readable name that represents this target. These are generated based on the provided properties, and the source. 
    display_name: str

    # If the target is private, or publicly accessible
    is_private: bool

    # The URL for the resource.
    url: typing.Optional[str]

class OptionalPublicTargetAttributes(TypedDict, total=False):
    # The creation date of the target
    created_at: datetime

class PublicTargetAttributes(RequiredPublicTargetAttributes, OptionalPublicTargetAttributes):
    pass