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

from snyk_python_sdk.type.create_collection_request_data import CreateCollectionRequestData

class RequiredCreateCollectionRequest(TypedDict):
    data: CreateCollectionRequestData

class OptionalCreateCollectionRequest(TypedDict, total=False):
    pass

class CreateCollectionRequest(RequiredCreateCollectionRequest, OptionalCreateCollectionRequest):
    pass