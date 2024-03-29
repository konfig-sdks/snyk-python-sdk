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

from snyk_python_sdk.type.access_token_ttl_seconds import AccessTokenTtlSeconds
from snyk_python_sdk.type.app_name import AppName
from snyk_python_sdk.type.context import Context
from snyk_python_sdk.type.redirect_uris import RedirectUris
from snyk_python_sdk.type.scopes import Scopes

class RequiredAppPostRequestDataAttributes(TypedDict):
    context: Context

    name: AppName

    redirect_uris: RedirectUris

    scopes: Scopes

class OptionalAppPostRequestDataAttributes(TypedDict, total=False):
    access_token_ttl_seconds: AccessTokenTtlSeconds

class AppPostRequestDataAttributes(RequiredAppPostRequestDataAttributes, OptionalAppPostRequestDataAttributes):
    pass
