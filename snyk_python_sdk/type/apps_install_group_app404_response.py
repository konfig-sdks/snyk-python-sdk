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

from snyk_python_sdk.type.apps_install_group_app404_response_errors import AppsInstallGroupApp404ResponseErrors
from snyk_python_sdk.type.apps_install_group_app404_response_jsonapi import AppsInstallGroupApp404ResponseJsonapi

class RequiredAppsInstallGroupApp404Response(TypedDict):
    errors: AppsInstallGroupApp404ResponseErrors

    jsonapi: AppsInstallGroupApp404ResponseJsonapi

class OptionalAppsInstallGroupApp404Response(TypedDict, total=False):
    pass

class AppsInstallGroupApp404Response(RequiredAppsInstallGroupApp404Response, OptionalAppsInstallGroupApp404Response):
    pass
