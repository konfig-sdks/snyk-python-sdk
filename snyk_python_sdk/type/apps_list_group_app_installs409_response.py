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

from snyk_python_sdk.type.apps_list_group_app_installs409_response_errors import AppsListGroupAppInstalls409ResponseErrors
from snyk_python_sdk.type.apps_list_group_app_installs409_response_jsonapi import AppsListGroupAppInstalls409ResponseJsonapi

class RequiredAppsListGroupAppInstalls409Response(TypedDict):
    errors: AppsListGroupAppInstalls409ResponseErrors

    jsonapi: AppsListGroupAppInstalls409ResponseJsonapi

class OptionalAppsListGroupAppInstalls409Response(TypedDict, total=False):
    pass

class AppsListGroupAppInstalls409Response(RequiredAppsListGroupAppInstalls409Response, OptionalAppsListGroupAppInstalls409Response):
    pass
