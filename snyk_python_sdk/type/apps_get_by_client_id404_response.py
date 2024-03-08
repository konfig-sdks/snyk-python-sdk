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

from snyk_python_sdk.type.apps_get_by_client_id404_response_errors import AppsGetByClientId404ResponseErrors
from snyk_python_sdk.type.apps_get_by_client_id404_response_jsonapi import AppsGetByClientId404ResponseJsonapi

class RequiredAppsGetByClientId404Response(TypedDict):
    errors: AppsGetByClientId404ResponseErrors

    jsonapi: AppsGetByClientId404ResponseJsonapi

class OptionalAppsGetByClientId404Response(TypedDict, total=False):
    pass

class AppsGetByClientId404Response(RequiredAppsGetByClientId404Response, OptionalAppsGetByClientId404Response):
    pass
