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

from snyk_python_sdk.type.json_api import JsonApi
from snyk_python_sdk.type.links import Links
from snyk_python_sdk.type.service_accounts_create_for_organization_response_data import ServiceAccountsCreateForOrganizationResponseData

class RequiredServiceAccountsCreateForOrganizationResponse(TypedDict):
    data: ServiceAccountsCreateForOrganizationResponseData

    jsonapi: JsonApi

    links: Links

class OptionalServiceAccountsCreateForOrganizationResponse(TypedDict, total=False):
    pass

class ServiceAccountsCreateForOrganizationResponse(RequiredServiceAccountsCreateForOrganizationResponse, OptionalServiceAccountsCreateForOrganizationResponse):
    pass
