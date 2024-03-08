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

from snyk_python_sdk.type.json_api import JsonApi
from snyk_python_sdk.type.sbom_resource import SbomResource

class RequiredSbomResponse(TypedDict):
    data: SbomResource

    jsonapi: JsonApi

class OptionalSbomResponse(TypedDict, total=False):
    pass

class SbomResponse(RequiredSbomResponse, OptionalSbomResponse):
    pass
