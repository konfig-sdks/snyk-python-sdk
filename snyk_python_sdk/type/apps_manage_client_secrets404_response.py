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

from snyk_python_sdk.type.apps_manage_client_secrets404_response_errors import AppsManageClientSecrets404ResponseErrors
from snyk_python_sdk.type.apps_manage_client_secrets404_response_jsonapi import AppsManageClientSecrets404ResponseJsonapi

class RequiredAppsManageClientSecrets404Response(TypedDict):
    errors: AppsManageClientSecrets404ResponseErrors

    jsonapi: AppsManageClientSecrets404ResponseJsonapi

class OptionalAppsManageClientSecrets404Response(TypedDict, total=False):
    pass

class AppsManageClientSecrets404Response(RequiredAppsManageClientSecrets404Response, OptionalAppsManageClientSecrets404Response):
    pass
