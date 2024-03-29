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

from snyk_python_sdk.type.remedy_metadata import RemedyMetadata

class RequiredRemedy(TypedDict):
    type: str

class OptionalRemedy(TypedDict, total=False):
    # A markdown-formatted optional description of this remedy. Links are not permitted.
    description: str

    # An optional identifier for correlating remedies between coordinates or across issues. They are scoped to a single Project and test run. Remedies with the same correlation_id must have the same contents. 
    correlation_id: str

    meta: RemedyMetadata

class Remedy(RequiredRemedy, OptionalRemedy):
    pass
