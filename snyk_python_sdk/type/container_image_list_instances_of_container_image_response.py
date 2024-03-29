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

from snyk_python_sdk.type.image import Image
from snyk_python_sdk.type.json_api import JsonApi
from snyk_python_sdk.type.paginated_links import PaginatedLinks

class RequiredContainerImageListInstancesOfContainerImageResponse(TypedDict):
    pass

class OptionalContainerImageListInstancesOfContainerImageResponse(TypedDict, total=False):
    data: typing.List[Image]

    jsonapi: JsonApi

    links: PaginatedLinks

class ContainerImageListInstancesOfContainerImageResponse(RequiredContainerImageListInstancesOfContainerImageResponse, OptionalContainerImageListInstancesOfContainerImageResponse):
    pass
