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

from snyk_python_sdk.type.apps_list_org_apps404_response_errors import AppsListOrgApps404ResponseErrors
from snyk_python_sdk.type.apps_list_org_apps404_response_jsonapi import AppsListOrgApps404ResponseJsonapi

class RequiredAppsListOrgApps404Response(TypedDict):
    errors: AppsListOrgApps404ResponseErrors

    jsonapi: AppsListOrgApps404ResponseJsonapi

class OptionalAppsListOrgApps404Response(TypedDict, total=False):
    pass

class AppsListOrgApps404Response(RequiredAppsListOrgApps404Response, OptionalAppsListOrgApps404Response):
    pass
