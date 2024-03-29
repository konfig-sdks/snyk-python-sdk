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

from snyk_python_sdk.type.image_digest import ImageDigest
from snyk_python_sdk.type.image_name import ImageName
from snyk_python_sdk.type.platform import Platform

class RequiredImageAttributes(TypedDict):
    layers: typing.List[ImageDigest]

    platform: Platform

class OptionalImageAttributes(TypedDict, total=False):
    names: typing.List[ImageName]

class ImageAttributes(RequiredImageAttributes, OptionalImageAttributes):
    pass
