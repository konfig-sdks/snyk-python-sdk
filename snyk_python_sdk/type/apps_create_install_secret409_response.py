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

from snyk_python_sdk.type.apps_create_install_secret409_response_errors import AppsCreateInstallSecret409ResponseErrors
from snyk_python_sdk.type.apps_create_install_secret409_response_jsonapi import AppsCreateInstallSecret409ResponseJsonapi

class RequiredAppsCreateInstallSecret409Response(TypedDict):
    errors: AppsCreateInstallSecret409ResponseErrors

    jsonapi: AppsCreateInstallSecret409ResponseJsonapi

class OptionalAppsCreateInstallSecret409Response(TypedDict, total=False):
    pass

class AppsCreateInstallSecret409Response(RequiredAppsCreateInstallSecret409Response, OptionalAppsCreateInstallSecret409Response):
    pass
