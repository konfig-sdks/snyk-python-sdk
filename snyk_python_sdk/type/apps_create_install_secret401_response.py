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

from snyk_python_sdk.type.apps_create_install_secret401_response_errors import AppsCreateInstallSecret401ResponseErrors
from snyk_python_sdk.type.apps_create_install_secret401_response_jsonapi import AppsCreateInstallSecret401ResponseJsonapi

class RequiredAppsCreateInstallSecret401Response(TypedDict):
    errors: AppsCreateInstallSecret401ResponseErrors

    jsonapi: AppsCreateInstallSecret401ResponseJsonapi

class OptionalAppsCreateInstallSecret401Response(TypedDict, total=False):
    pass

class AppsCreateInstallSecret401Response(RequiredAppsCreateInstallSecret401Response, OptionalAppsCreateInstallSecret401Response):
    pass
