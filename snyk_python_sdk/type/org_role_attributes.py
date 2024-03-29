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


class RequiredOrgRoleAttributes(TypedDict):
    pass

class OptionalOrgRoleAttributes(TypedDict, total=False):
    # The display name of the organization role.
    name: str

class OrgRoleAttributes(RequiredOrgRoleAttributes, OptionalOrgRoleAttributes):
    pass
