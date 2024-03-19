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

from snyk_python_sdk.type.apps_list_org_creations400_response_errors_item_meta import AppsListOrgCreations400ResponseErrorsItemMeta
from snyk_python_sdk.type.apps_list_org_creations400_response_errors_item_source import AppsListOrgCreations400ResponseErrorsItemSource

class RequiredAppsListOrgCreations400ResponseErrorsItem(TypedDict):
    # A human-readable explanation specific to this occurrence of the problem.
    detail: str

    # The HTTP status code applicable to this problem, expressed as a string value.
    status: str

class OptionalAppsListOrgCreations400ResponseErrorsItem(TypedDict, total=False):
    # A short, human-readable summary of the problem that SHOULD NOT change from occurrence to occurrence of the problem, except for purposes of localization.
    title: str

    # An application-specific error code, expressed as a string value.
    code: str

    # A unique identifier for this particular occurrence of the problem.
    id: str

    meta: AppsListOrgCreations400ResponseErrorsItemMeta

    source: AppsListOrgCreations400ResponseErrorsItemSource

class AppsListOrgCreations400ResponseErrorsItem(RequiredAppsListOrgCreations400ResponseErrorsItem, OptionalAppsListOrgCreations400ResponseErrorsItem):
    pass
