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

from snyk_python_sdk.type.access_token_ttl_seconds import AccessTokenTtlSeconds
from snyk_python_sdk.type.app_name import AppName
from snyk_python_sdk.type.redirect_uris import RedirectUris

class RequiredAppPatchRequestDataAttributes(TypedDict):
    pass

class OptionalAppPatchRequestDataAttributes(TypedDict, total=False):
    access_token_ttl_seconds: AccessTokenTtlSeconds

    name: AppName

    redirect_uris: RedirectUris

class AppPatchRequestDataAttributes(RequiredAppPatchRequestDataAttributes, OptionalAppPatchRequestDataAttributes):
    pass