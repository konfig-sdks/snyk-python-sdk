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

from snyk_python_sdk.type.service_account_attributes import ServiceAccountAttributes
from snyk_python_sdk.type.service_account_links import ServiceAccountLinks

class RequiredServiceAccount(TypedDict):
    attributes: ServiceAccountAttributes

    id: str

    type: str

class OptionalServiceAccount(TypedDict, total=False):
    links: ServiceAccountLinks

class ServiceAccount(RequiredServiceAccount, OptionalServiceAccount):
    pass
