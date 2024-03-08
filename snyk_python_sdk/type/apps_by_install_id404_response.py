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

from snyk_python_sdk.type.apps_by_install_id404_response_errors import AppsByInstallId404ResponseErrors
from snyk_python_sdk.type.apps_by_install_id404_response_jsonapi import AppsByInstallId404ResponseJsonapi

class RequiredAppsByInstallId404Response(TypedDict):
    errors: AppsByInstallId404ResponseErrors

    jsonapi: AppsByInstallId404ResponseJsonapi

class OptionalAppsByInstallId404Response(TypedDict, total=False):
    pass

class AppsByInstallId404Response(RequiredAppsByInstallId404Response, OptionalAppsByInstallId404Response):
    pass