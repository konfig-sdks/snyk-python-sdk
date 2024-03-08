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

from snyk_python_sdk.type.apps_by_install_id401_response_errors_item_meta import AppsByInstallId401ResponseErrorsItemMeta
from snyk_python_sdk.type.apps_by_install_id401_response_errors_item_source import AppsByInstallId401ResponseErrorsItemSource

class RequiredAppsByInstallId401ResponseErrorsItem(TypedDict):
    # A human-readable explanation specific to this occurrence of the problem.
    detail: str

    # The HTTP status code applicable to this problem, expressed as a string value.
    status: str

class OptionalAppsByInstallId401ResponseErrorsItem(TypedDict, total=False):
    # A short, human-readable summary of the problem that SHOULD NOT change from occurrence to occurrence of the problem, except for purposes of localization.
    title: str

    # An application-specific error code, expressed as a string value.
    code: str

    # A unique identifier for this particular occurrence of the problem.
    id: str

    meta: AppsByInstallId401ResponseErrorsItemMeta

    source: AppsByInstallId401ResponseErrorsItemSource

class AppsByInstallId401ResponseErrorsItem(RequiredAppsByInstallId401ResponseErrorsItem, OptionalAppsByInstallId401ResponseErrorsItem):
    pass
