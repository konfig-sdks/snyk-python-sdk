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

from snyk_python_sdk.type.apps_manage_client_secrets500_response_errors import AppsManageClientSecrets500ResponseErrors
from snyk_python_sdk.type.apps_manage_client_secrets500_response_jsonapi import AppsManageClientSecrets500ResponseJsonapi

class RequiredAppsManageClientSecrets500Response(TypedDict):
    errors: AppsManageClientSecrets500ResponseErrors

    jsonapi: AppsManageClientSecrets500ResponseJsonapi

class OptionalAppsManageClientSecrets500Response(TypedDict, total=False):
    pass

class AppsManageClientSecrets500Response(RequiredAppsManageClientSecrets500Response, OptionalAppsManageClientSecrets500Response):
    pass
