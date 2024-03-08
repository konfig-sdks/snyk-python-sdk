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

from snyk_python_sdk.type.apps_update_creation_attributes_by_id401_response_errors import AppsUpdateCreationAttributesById401ResponseErrors
from snyk_python_sdk.type.apps_update_creation_attributes_by_id401_response_jsonapi import AppsUpdateCreationAttributesById401ResponseJsonapi

class RequiredAppsUpdateCreationAttributesById401Response(TypedDict):
    errors: AppsUpdateCreationAttributesById401ResponseErrors

    jsonapi: AppsUpdateCreationAttributesById401ResponseJsonapi

class OptionalAppsUpdateCreationAttributesById401Response(TypedDict, total=False):
    pass

class AppsUpdateCreationAttributesById401Response(RequiredAppsUpdateCreationAttributesById401Response, OptionalAppsUpdateCreationAttributesById401Response):
    pass