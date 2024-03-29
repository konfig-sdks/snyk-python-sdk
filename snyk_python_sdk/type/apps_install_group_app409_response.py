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

from snyk_python_sdk.type.apps_install_group_app409_response_errors import AppsInstallGroupApp409ResponseErrors
from snyk_python_sdk.type.apps_install_group_app409_response_jsonapi import AppsInstallGroupApp409ResponseJsonapi

class RequiredAppsInstallGroupApp409Response(TypedDict):
    errors: AppsInstallGroupApp409ResponseErrors

    jsonapi: AppsInstallGroupApp409ResponseJsonapi

class OptionalAppsInstallGroupApp409Response(TypedDict, total=False):
    pass

class AppsInstallGroupApp409Response(RequiredAppsInstallGroupApp409Response, OptionalAppsInstallGroupApp409Response):
    pass
