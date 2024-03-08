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

from snyk_python_sdk.type.app_bot_relationships_app import AppBotRelationshipsApp

class RequiredAppBotRelationships(TypedDict):
    app: AppBotRelationshipsApp

class OptionalAppBotRelationships(TypedDict, total=False):
    pass

class AppBotRelationships(RequiredAppBotRelationships, OptionalAppBotRelationships):
    pass
