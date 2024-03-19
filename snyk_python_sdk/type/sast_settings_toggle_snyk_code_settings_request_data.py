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

from snyk_python_sdk.type.sast_settings_toggle_snyk_code_settings_request_data_attributes import SastSettingsToggleSnykCodeSettingsRequestDataAttributes

class RequiredSastSettingsToggleSnykCodeSettingsRequestData(TypedDict):
    attributes: SastSettingsToggleSnykCodeSettingsRequestDataAttributes

    id: str

    type: str

class OptionalSastSettingsToggleSnykCodeSettingsRequestData(TypedDict, total=False):
    pass

class SastSettingsToggleSnykCodeSettingsRequestData(RequiredSastSettingsToggleSnykCodeSettingsRequestData, OptionalSastSettingsToggleSnykCodeSettingsRequestData):
    pass
