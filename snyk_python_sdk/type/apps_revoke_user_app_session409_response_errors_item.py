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

from snyk_python_sdk.type.apps_revoke_user_app_session409_response_errors_item_meta import AppsRevokeUserAppSession409ResponseErrorsItemMeta
from snyk_python_sdk.type.apps_revoke_user_app_session409_response_errors_item_source import AppsRevokeUserAppSession409ResponseErrorsItemSource

class RequiredAppsRevokeUserAppSession409ResponseErrorsItem(TypedDict):
    # A human-readable explanation specific to this occurrence of the problem.
    detail: str

    # The HTTP status code applicable to this problem, expressed as a string value.
    status: str

class OptionalAppsRevokeUserAppSession409ResponseErrorsItem(TypedDict, total=False):
    # A short, human-readable summary of the problem that SHOULD NOT change from occurrence to occurrence of the problem, except for purposes of localization.
    title: str

    # An application-specific error code, expressed as a string value.
    code: str

    # A unique identifier for this particular occurrence of the problem.
    id: str

    meta: AppsRevokeUserAppSession409ResponseErrorsItemMeta

    source: AppsRevokeUserAppSession409ResponseErrorsItemSource

class AppsRevokeUserAppSession409ResponseErrorsItem(RequiredAppsRevokeUserAppSession409ResponseErrorsItem, OptionalAppsRevokeUserAppSession409ResponseErrorsItem):
    pass
