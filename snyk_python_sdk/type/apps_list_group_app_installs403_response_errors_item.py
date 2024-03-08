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

from snyk_python_sdk.type.apps_list_group_app_installs403_response_errors_item_meta import AppsListGroupAppInstalls403ResponseErrorsItemMeta
from snyk_python_sdk.type.apps_list_group_app_installs403_response_errors_item_source import AppsListGroupAppInstalls403ResponseErrorsItemSource

class RequiredAppsListGroupAppInstalls403ResponseErrorsItem(TypedDict):
    # A human-readable explanation specific to this occurrence of the problem.
    detail: str

    # The HTTP status code applicable to this problem, expressed as a string value.
    status: str

class OptionalAppsListGroupAppInstalls403ResponseErrorsItem(TypedDict, total=False):
    # A short, human-readable summary of the problem that SHOULD NOT change from occurrence to occurrence of the problem, except for purposes of localization.
    title: str

    # An application-specific error code, expressed as a string value.
    code: str

    # A unique identifier for this particular occurrence of the problem.
    id: str

    meta: AppsListGroupAppInstalls403ResponseErrorsItemMeta

    source: AppsListGroupAppInstalls403ResponseErrorsItemSource

class AppsListGroupAppInstalls403ResponseErrorsItem(RequiredAppsListGroupAppInstalls403ResponseErrorsItem, OptionalAppsListGroupAppInstalls403ResponseErrorsItem):
    pass
