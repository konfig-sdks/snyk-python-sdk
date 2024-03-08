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

from snyk_python_sdk.type.app_name import AppName
from snyk_python_sdk.type.context import Context
from snyk_python_sdk.type.scopes import Scopes

class RequiredPublicAppAttributes(TypedDict):
    # The oauth2 client id for the app.
    client_id: str

    name: AppName

class OptionalPublicAppAttributes(TypedDict, total=False):
    context: Context

    scopes: Scopes

class PublicAppAttributes(RequiredPublicAppAttributes, OptionalPublicAppAttributes):
    pass