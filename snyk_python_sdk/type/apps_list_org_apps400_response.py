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

from snyk_python_sdk.type.apps_list_org_apps400_response_errors import AppsListOrgApps400ResponseErrors
from snyk_python_sdk.type.apps_list_org_apps400_response_jsonapi import AppsListOrgApps400ResponseJsonapi

class RequiredAppsListOrgApps400Response(TypedDict):
    errors: AppsListOrgApps400ResponseErrors

    jsonapi: AppsListOrgApps400ResponseJsonapi

class OptionalAppsListOrgApps400Response(TypedDict, total=False):
    pass

class AppsListOrgApps400Response(RequiredAppsListOrgApps400Response, OptionalAppsListOrgApps400Response):
    pass
