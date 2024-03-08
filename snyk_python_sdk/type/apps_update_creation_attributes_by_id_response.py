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

from snyk_python_sdk.type.app_data import AppData
from snyk_python_sdk.type.json_api import JsonApi
from snyk_python_sdk.type.self_link import SelfLink

class RequiredAppsUpdateCreationAttributesByIdResponse(TypedDict):
    pass

class OptionalAppsUpdateCreationAttributesByIdResponse(TypedDict, total=False):
    items: AppData

    jsonapi: JsonApi

    links: SelfLink

class AppsUpdateCreationAttributesByIdResponse(RequiredAppsUpdateCreationAttributesByIdResponse, OptionalAppsUpdateCreationAttributesByIdResponse):
    pass
