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

from snyk_python_sdk.type.apps_install_snyk_app_to_org400_response_errors import AppsInstallSnykAppToOrg400ResponseErrors
from snyk_python_sdk.type.apps_install_snyk_app_to_org400_response_jsonapi import AppsInstallSnykAppToOrg400ResponseJsonapi

class RequiredAppsInstallSnykAppToOrg400Response(TypedDict):
    errors: AppsInstallSnykAppToOrg400ResponseErrors

    jsonapi: AppsInstallSnykAppToOrg400ResponseJsonapi

class OptionalAppsInstallSnykAppToOrg400Response(TypedDict, total=False):
    pass

class AppsInstallSnykAppToOrg400Response(RequiredAppsInstallSnykAppToOrg400Response, OptionalAppsInstallSnykAppToOrg400Response):
    pass
