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
from pydantic import BaseModel, Field, RootModel


class GroupIacSettingsRequestAttributesCustomRules(BaseModel):
    # Whether the custom rules feature is enabled or not.
    is_enabled: typing.Optional[bool] = Field(None, alias='is_enabled')

    # The tag for an OCI artifact inside an OCI registry.
    oci_registry_tag: typing.Optional[str] = Field(None, alias='oci_registry_tag')

    # The URL to an OCI registry.
    oci_registry_url: typing.Optional[str] = Field(None, alias='oci_registry_url')
    class Config:
        arbitrary_types_allowed = True
