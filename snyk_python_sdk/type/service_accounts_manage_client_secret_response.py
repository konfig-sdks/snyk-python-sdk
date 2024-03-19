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
from snyk_python_sdk.type.service_accounts_manage_client_secret_response_data import ServiceAccountsManageClientSecretResponseData

class RequiredServiceAccountsManageClientSecretResponse(TypedDict):
    data: ServiceAccountsManageClientSecretResponseData

    jsonapi: JsonApi

class OptionalServiceAccountsManageClientSecretResponse(TypedDict, total=False):
    links: Links

class ServiceAccountsManageClientSecretResponse(RequiredServiceAccountsManageClientSecretResponse, OptionalServiceAccountsManageClientSecretResponse):
    pass
