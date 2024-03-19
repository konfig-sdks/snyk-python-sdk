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


class RequiredGroupIacSettingsRequestAttributesCustomRules(TypedDict):
    pass

class OptionalGroupIacSettingsRequestAttributesCustomRules(TypedDict, total=False):
    # Whether the custom rules feature is enabled or not.
    is_enabled: bool

    # The tag for an OCI artifact inside an OCI registry.
    oci_registry_tag: str

    # The URL to an OCI registry.
    oci_registry_url: str

class GroupIacSettingsRequestAttributesCustomRules(RequiredGroupIacSettingsRequestAttributesCustomRules, OptionalGroupIacSettingsRequestAttributesCustomRules):
    pass
