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

from snyk_python_sdk.type.links import Links
from snyk_python_sdk.type.public_app_data_attributes import PublicAppDataAttributes

class RequiredPublicAppData(TypedDict):
    id: str

    type: str

class OptionalPublicAppData(TypedDict, total=False):
    attributes: PublicAppDataAttributes

    links: Links

class PublicAppData(RequiredPublicAppData, OptionalPublicAppData):
    pass