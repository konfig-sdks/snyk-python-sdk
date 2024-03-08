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

from snyk_python_sdk.type.apps_install_snyk_app_to_org_request_data import AppsInstallSnykAppToOrgRequestData
from snyk_python_sdk.type.apps_install_snyk_app_to_org_request_relationships import AppsInstallSnykAppToOrgRequestRelationships

class RequiredAppsInstallSnykAppToOrgRequest(TypedDict):
    data: AppsInstallSnykAppToOrgRequestData

    relationships: AppsInstallSnykAppToOrgRequestRelationships

class OptionalAppsInstallSnykAppToOrgRequest(TypedDict, total=False):
    pass

class AppsInstallSnykAppToOrgRequest(RequiredAppsInstallSnykAppToOrgRequest, OptionalAppsInstallSnykAppToOrgRequest):
    pass