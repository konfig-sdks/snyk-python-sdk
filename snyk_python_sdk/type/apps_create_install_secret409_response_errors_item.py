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

from snyk_python_sdk.type.apps_create_install_secret409_response_errors_item_meta import AppsCreateInstallSecret409ResponseErrorsItemMeta
from snyk_python_sdk.type.apps_create_install_secret409_response_errors_item_source import AppsCreateInstallSecret409ResponseErrorsItemSource

class RequiredAppsCreateInstallSecret409ResponseErrorsItem(TypedDict):
    # A human-readable explanation specific to this occurrence of the problem.
    detail: str

    # The HTTP status code applicable to this problem, expressed as a string value.
    status: str

class OptionalAppsCreateInstallSecret409ResponseErrorsItem(TypedDict, total=False):
    # A short, human-readable summary of the problem that SHOULD NOT change from occurrence to occurrence of the problem, except for purposes of localization.
    title: str

    # An application-specific error code, expressed as a string value.
    code: str

    # A unique identifier for this particular occurrence of the problem.
    id: str

    meta: AppsCreateInstallSecret409ResponseErrorsItemMeta

    source: AppsCreateInstallSecret409ResponseErrorsItemSource

class AppsCreateInstallSecret409ResponseErrorsItem(RequiredAppsCreateInstallSecret409ResponseErrorsItem, OptionalAppsCreateInstallSecret409ResponseErrorsItem):
    pass
