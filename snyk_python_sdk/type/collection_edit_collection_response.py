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

from snyk_python_sdk.type.collection_edit_collection_response_data import CollectionEditCollectionResponseData
from snyk_python_sdk.type.json_api import JsonApi
from snyk_python_sdk.type.self_link import SelfLink

class RequiredCollectionEditCollectionResponse(TypedDict):
    pass

class OptionalCollectionEditCollectionResponse(TypedDict, total=False):
    data: CollectionEditCollectionResponseData

    jsonapi: JsonApi

    links: SelfLink

class CollectionEditCollectionResponse(RequiredCollectionEditCollectionResponse, OptionalCollectionEditCollectionResponse):
    pass