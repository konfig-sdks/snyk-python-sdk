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

from snyk_python_sdk.type.apps_install_snyk_app_to_org401_response_errors import AppsInstallSnykAppToOrg401ResponseErrors
from snyk_python_sdk.type.apps_install_snyk_app_to_org401_response_jsonapi import AppsInstallSnykAppToOrg401ResponseJsonapi

class RequiredAppsInstallSnykAppToOrg401Response(TypedDict):
    errors: AppsInstallSnykAppToOrg401ResponseErrors

    jsonapi: AppsInstallSnykAppToOrg401ResponseJsonapi

class OptionalAppsInstallSnykAppToOrg401Response(TypedDict, total=False):
    pass

class AppsInstallSnykAppToOrg401Response(RequiredAppsInstallSnykAppToOrg401Response, OptionalAppsInstallSnykAppToOrg401Response):
    pass
