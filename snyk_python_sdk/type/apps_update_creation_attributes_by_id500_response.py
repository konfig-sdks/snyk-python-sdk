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

from snyk_python_sdk.type.apps_update_creation_attributes_by_id500_response_errors import AppsUpdateCreationAttributesById500ResponseErrors
from snyk_python_sdk.type.apps_update_creation_attributes_by_id500_response_jsonapi import AppsUpdateCreationAttributesById500ResponseJsonapi

class RequiredAppsUpdateCreationAttributesById500Response(TypedDict):
    errors: AppsUpdateCreationAttributesById500ResponseErrors

    jsonapi: AppsUpdateCreationAttributesById500ResponseJsonapi

class OptionalAppsUpdateCreationAttributesById500Response(TypedDict, total=False):
    pass

class AppsUpdateCreationAttributesById500Response(RequiredAppsUpdateCreationAttributesById500Response, OptionalAppsUpdateCreationAttributesById500Response):
    pass