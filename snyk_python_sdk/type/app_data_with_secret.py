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

from snyk_python_sdk.type.app_resource_attributes_with_secret import AppResourceAttributesWithSecret

class RequiredAppDataWithSecret(TypedDict):
    attributes: AppResourceAttributesWithSecret

    id: str

    type: str

class OptionalAppDataWithSecret(TypedDict, total=False):
    pass

class AppDataWithSecret(RequiredAppDataWithSecret, OptionalAppDataWithSecret):
    pass