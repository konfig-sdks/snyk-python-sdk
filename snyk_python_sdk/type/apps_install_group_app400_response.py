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

from snyk_python_sdk.type.apps_install_group_app400_response_errors import AppsInstallGroupApp400ResponseErrors
from snyk_python_sdk.type.apps_install_group_app400_response_jsonapi import AppsInstallGroupApp400ResponseJsonapi

class RequiredAppsInstallGroupApp400Response(TypedDict):
    errors: AppsInstallGroupApp400ResponseErrors

    jsonapi: AppsInstallGroupApp400ResponseJsonapi

class OptionalAppsInstallGroupApp400Response(TypedDict, total=False):
    pass

class AppsInstallGroupApp400Response(RequiredAppsInstallGroupApp400Response, OptionalAppsInstallGroupApp400Response):
    pass
