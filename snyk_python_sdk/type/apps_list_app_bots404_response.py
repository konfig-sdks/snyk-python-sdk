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

from snyk_python_sdk.type.apps_list_app_bots404_response_errors import AppsListAppBots404ResponseErrors
from snyk_python_sdk.type.apps_list_app_bots404_response_jsonapi import AppsListAppBots404ResponseJsonapi

class RequiredAppsListAppBots404Response(TypedDict):
    errors: AppsListAppBots404ResponseErrors

    jsonapi: AppsListAppBots404ResponseJsonapi

class OptionalAppsListAppBots404Response(TypedDict, total=False):
    pass

class AppsListAppBots404Response(RequiredAppsListAppBots404Response, OptionalAppsListAppBots404Response):
    pass
