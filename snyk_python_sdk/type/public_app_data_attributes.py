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

from snyk_python_sdk.type.public_app_data_attributes_scopes import PublicAppDataAttributesScopes

class RequiredPublicAppDataAttributes(TypedDict):
    client_id: str

    # New name of the app to display to users during authorization flow.
    name: str

class OptionalPublicAppDataAttributes(TypedDict, total=False):
    # Allow installing the app to a org/group or to a user, default tenant.
    context: str

    scopes: PublicAppDataAttributesScopes

class PublicAppDataAttributes(RequiredPublicAppDataAttributes, OptionalPublicAppDataAttributes):
    pass
