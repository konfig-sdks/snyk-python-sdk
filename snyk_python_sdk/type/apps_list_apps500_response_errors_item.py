# coding: utf-8

"""
    Snyk API

    Missing description placeholder

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from snyk_python_sdk.type.apps_list_apps500_response_errors_item_meta import AppsListApps500ResponseErrorsItemMeta
from snyk_python_sdk.type.apps_list_apps500_response_errors_item_source import AppsListApps500ResponseErrorsItemSource

class RequiredAppsListApps500ResponseErrorsItem(TypedDict):
    # A human-readable explanation specific to this occurrence of the problem.
    detail: str

    # The HTTP status code applicable to this problem, expressed as a string value.
    status: str

class OptionalAppsListApps500ResponseErrorsItem(TypedDict, total=False):
    # A short, human-readable summary of the problem that SHOULD NOT change from occurrence to occurrence of the problem, except for purposes of localization.
    title: str

    # An application-specific error code, expressed as a string value.
    code: str

    # A unique identifier for this particular occurrence of the problem.
    id: str

    meta: AppsListApps500ResponseErrorsItemMeta

    source: AppsListApps500ResponseErrorsItemSource

class AppsListApps500ResponseErrorsItem(RequiredAppsListApps500ResponseErrorsItem, OptionalAppsListApps500ResponseErrorsItem):
    pass
