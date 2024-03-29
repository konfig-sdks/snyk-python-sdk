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

from snyk_python_sdk.type.apps_create_organization_app403_response_errors import AppsCreateOrganizationApp403ResponseErrors
from snyk_python_sdk.type.apps_create_organization_app403_response_jsonapi import AppsCreateOrganizationApp403ResponseJsonapi

class RequiredAppsCreateOrganizationApp403Response(TypedDict):
    errors: AppsCreateOrganizationApp403ResponseErrors

    jsonapi: AppsCreateOrganizationApp403ResponseJsonapi

class OptionalAppsCreateOrganizationApp403Response(TypedDict, total=False):
    pass

class AppsCreateOrganizationApp403Response(RequiredAppsCreateOrganizationApp403Response, OptionalAppsCreateOrganizationApp403Response):
    pass
