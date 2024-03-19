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

from snyk_python_sdk.type.environment_type_def import EnvironmentTypeDef

class RequiredEnvironment(TypedDict):
    # Internal ID for an environment.
    id: str

    name: str

    type: EnvironmentTypeDef

class OptionalEnvironment(TypedDict, total=False):
    # An optional native identifier for this environment. For example, a cloud account id.
    native_id: str

class Environment(RequiredEnvironment, OptionalEnvironment):
    pass
